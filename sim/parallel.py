# parallel.py -- running independent measurements at the same time.
#
# The simulator's work divides into pieces that say nothing to each
# other. One archetype shopping for its kit does not care what the next
# one bought; one duel does not care how the duel before it went. A
# profile of `balance.py --check` puts 56% of the time in gear shopping
# and 41% in duels, and both of those are piles of independent pieces,
# so both are worth spreading across the cores a modern machine has and
# a serial run leaves idle.
#
# Two rules hold this together, and the second matters more than the
# speed does.
#
# **A worker builds its own `Mechanics`.** It is not handed one. The
# object carries caches that are large, and a sweep mutates `M.rules`
# in memory, so a worker is given the SOURCE and the list of overrides
# and rebuilds from those -- which is also what makes it impossible for
# a worker to be looking at a different ruleset from the one that sent
# it the work.
#
# **`--jobs` may change the speed and must never change an answer.** A
# measuring tool that reports different numbers depending on how many
# cores it was given is not measuring anything. Gear shopping is pure
# arithmetic over the d20's faces and has no randomness in it at all,
# so it is exactly identical either way. Duels are Monte Carlo, and
# they are made safe by seeding each duel from its own name rather than
# drawing from one stream in whatever order the work happened to
# finish -- see `duel_seed`.
"""Spreading independent measurements across cores."""

import hashlib
import json
import os
import time
import zlib
from concurrent.futures import ProcessPoolExecutor, as_completed

# Eight rather than everything. The machines this runs on have sixteen
# cores and are also running an editor, a browser and whatever else;
# taking every core makes the rest of the desktop unpleasant and buys
# little, because the last few workers are competing with the first few
# for memory bandwidth. Raise it with --jobs when the machine is idle.
DEFAULT_JOBS = 8

# Worker-side state. One `Mechanics` per process, built once by the
# initializer and read by every task that process handles.
_M = None


def resolve_jobs(requested=None):
    """How many workers to use.

    An explicit --jobs wins; then ICO_SIM_JOBS, so a slow machine can
    set it once rather than on every command; then the default, capped
    at the number of cores actually present so that a four-core laptop
    does not run eight."""
    if requested is not None:
        return max(1, int(requested))
    env = os.environ.get("ICO_SIM_JOBS")
    if env:
        return max(1, int(env))
    return max(1, min(DEFAULT_JOBS, os.cpu_count() or 1))


def duel_seed(base, *parts):
    """A seed belonging to one duel rather than to its position in a
    queue.

    Every duel seeds itself from its own name -- the base seed, the
    level, and the two builds -- so the result is the same whether it
    ran first, last, or beside fifteen others. That is what lets duels
    be handed out to workers at all.

    It is also worth having on its own. Drawing every duel from one
    stream in sequence meant the ORDER was part of the answer: adding
    an archetype, or measuring one more level, re-rolled every pairing
    after it, and `sim/README.md` has had to warn people about that for
    as long as the gates have existed. It cannot happen now.

    `zlib.crc32` rather than `hash`, because `hash` is randomised per
    process and would make every worker disagree with every other."""
    name = "|".join([str(base)] + [str(p) for p in parts])
    return zlib.crc32(name.encode("utf-8"))


def _init_worker(source, overrides):
    global _M
    import model as m
    _M = m.Mechanics(source)
    for parts, value in overrides:
        m.override(_M, parts, value)


def _run(payload):
    fn, item = payload
    return fn(_M, item)


def mechanics_stamp(M):
    """What ruleset a checkpoint was taken against.

    Resuming a run against different numbers would mix two rulesets into
    one report and the report would not say so, which is worse than
    losing the work."""
    body = json.dumps(M.rules, sort_keys=True, default=str)
    over = json.dumps([[list(parts), value] for parts, value in M.overrides],
                      default=str)
    return hashlib.sha256((body + over).encode("utf-8")).hexdigest()[:16]


def _tuples(value):
    """JSON has no tuples and every checkpointable result here is one.

    A result comes back from `json.load` as a list and callers key
    dictionaries on it, so it has to go back to being hashable. Anything
    stored in a checkpoint has to survive this, which is the price of
    the file being readable by a person halfway through a run."""
    if isinstance(value, list):
        return tuple(_tuples(v) for v in value)
    return value


class Checkpoint:
    """Results already in hand, and how far the run has got.

    Written atomically on a timer rather than after every task: a write
    of a few thousand results costs single-figure milliseconds, so at
    any sane interval the cost is far below the noise of the measurement
    -- pick the interval for how much work you are willing to lose.

    The file is meant to be read while the run is going. `done` out of
    `total`, the rate, an estimate of what is left, and the name of the
    last task to land, so a run that is stuck says what it is stuck on.
    """

    def __init__(self, path, stamp, interval=30.0):
        self.path = path
        self.stamp = stamp
        self.interval = interval
        self.results = {}
        self.total = 0
        self.done = 0
        self.resumed = 0
        self.last = ""
        self.started = time.time()
        self._written = 0.0

    @classmethod
    def load(cls, path, stamp, interval=30.0):
        """An existing checkpoint, or an empty one. A checkpoint taken
        against other numbers is refused rather than merged."""
        ck = cls(path, stamp, interval)
        if not path or not os.path.exists(path):
            return ck
        with open(path, "r", encoding="utf-8") as fh:
            saved = json.load(fh)
        if saved.get("stamp") != stamp:
            raise ValueError(
                "%s was taken against a different ruleset (%s, not %s).\n"
                "  Delete it to start again, or point --checkpoint "
                "somewhere else." % (path, saved.get("stamp"), stamp))
        ck.results = {k: _tuples(v) for k, v in saved.get("results", {}).items()}
        return ck

    def begin(self, total, already):
        self.total += total
        self.done += already
        self.resumed += already

    def get(self, key):
        return self.results.get(key)

    def put(self, key, value):
        self.results[key] = value
        self.done += 1
        self.last = key
        self.flush()

    def flush(self, force=False):
        now = time.time()
        if not force and now - self._written < self.interval:
            return
        self._written = now
        if not self.path:
            return
        elapsed = now - self.started
        fresh = self.done - self.resumed
        rate = fresh / elapsed if elapsed > 0 and fresh else 0.0
        left = self.total - self.done
        payload = {
            "stamp": self.stamp,
            "done": self.done,
            "total": self.total,
            "resumed": self.resumed,
            "elapsed_seconds": round(elapsed, 1),
            "per_second": round(rate, 3),
            "seconds_left": round(left / rate, 1) if rate else None,
            "last_finished": self.last,
            "results": self.results,
        }
        tmp = self.path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=1, default=str)
        os.replace(tmp, self.path)


class Pool:
    """A handle on however many workers this run is allowed.

    Tasks are plain top-level functions taking `(M, item)`, so the same
    function runs unchanged in a worker or in this process -- which is
    what makes `--jobs 1` a real serial fallback rather than a second
    code path that can drift from the first."""

    def __init__(self, M, jobs=None):
        self.M = M
        self.jobs = resolve_jobs(jobs)
        self._source = str(M.path)
        self._overrides = list(getattr(M, "overrides", ()))
        self._ex = None

    def map(self, fn, items, checkpoint=None, label="", keys=None):
        """Run `fn` over `items`, in input order however they finish.

        `checkpoint`, when given, is consulted before anything is
        submitted and written to as each result lands. A run that died
        halfway resumes from it, and because every random measurement
        here is seeded from its own name, the resumed run produces the
        same numbers as one that never stopped -- which is the whole
        reason a checkpoint is worth having rather than a way to get a
        subtly different answer quickly.

        Results are collected as they COMPLETE rather than in the order
        they were submitted. `ProcessPoolExecutor.map` yields in order,
        so one slow task at the front hides every fast one behind it,
        and nothing can be checkpointed or reported until the slow one
        lands. The answer is unaffected: `out` is filled by index."""
        items = list(items)
        # A caller with big task tuples gives short keys instead, so the
        # checkpoint stays readable and does not carry a copy of every
        # archetype's attributes in its index.
        keys = (["%s|%s" % (label, k) for k in keys] if keys is not None
                else ["%s|%r" % (label, item) for item in items])
        out = [None] * len(items)

        todo = []
        for i, item in enumerate(items):
            hit = None if checkpoint is None else checkpoint.get(keys[i])
            if hit is not None:
                out[i] = hit
            else:
                todo.append((i, item))
        if checkpoint is not None:
            checkpoint.begin(len(items), len(items) - len(todo))

        def landed(i, value):
            out[i] = value
            if checkpoint is not None:
                checkpoint.put(keys[i], value)

        # One worker, or one item, is not worth a process for.
        if self.jobs <= 1 or len(todo) < 2:
            for i, item in todo:
                landed(i, fn(self.M, item))
            if checkpoint is not None:
                checkpoint.flush(force=True)
            return out

        if self._ex is None:
            self._ex = ProcessPoolExecutor(
                max_workers=self.jobs, initializer=_init_worker,
                initargs=(self._source, self._overrides))
        futures = {self._ex.submit(_run, (fn, item)): i for i, item in todo}
        for future in as_completed(futures):
            landed(futures[future], future.result())
        if checkpoint is not None:
            checkpoint.flush(force=True)
        return out

    def close(self):
        if self._ex is not None:
            self._ex.shutdown()
            self._ex = None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False
