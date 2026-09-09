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

import os
import zlib
from concurrent.futures import ProcessPoolExecutor

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

    def map(self, fn, items):
        items = list(items)
        # One worker, or one item, is not worth a process for.
        if self.jobs <= 1 or len(items) < 2:
            return [fn(self.M, item) for item in items]
        if self._ex is None:
            self._ex = ProcessPoolExecutor(
                max_workers=self.jobs, initializer=_init_worker,
                initargs=(self._source, self._overrides))
        return list(self._ex.map(_run, [(fn, item) for item in items]))

    def close(self):
        if self._ex is not None:
            self._ex.shutdown()
            self._ex = None

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
        return False
