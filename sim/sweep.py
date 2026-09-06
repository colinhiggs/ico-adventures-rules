# sweep.py -- what happens to the game if this number were different?
#
# balance.py answers "is the current ruleset balanced". This answers the
# question you ask next: "which value should it be, and what does that
# cost me somewhere else". It overrides mechanics IN MEMORY ONLY -- no
# rule file is touched, so a sweep is always safe to run.
#
#   # one mechanic, several values
#   python3 sim/sweep.py -m character-creation.max_starting_mastery_hp=15,20,25
#
#   # two mechanics at once: every combination, as a grid
#   python3 sim/sweep.py -m damage.damage_per_attack_skill_step=3,4,6 \
#                        -m advancement.free_mastery_hp_per_level=2,3,4
#
#   # nested keys work too
#   python3 sim/sweep.py -m discipline-powers.power_attack.damage_per_step=1,2
#
# The column that matters for matching two curves against each other is
# DRIFT: mean rounds at the top level divided by mean rounds at the
# bottom. 1.0 means a fight takes the same number of rounds at level 15
# as at level 1 -- damage and hit points growing in step. Above 1.0 the
# game grinds as it advances; below 1.0 it gets swingier.

import argparse
import itertools
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import balance as b
import model as m


def parse_mechanic(spec):
    """'rule.key=1,2,3' or 'rule.nested.key=1,2' -> (path, [values])."""
    if "=" not in spec:
        raise SystemExit("--mechanic needs rule.key=v1,v2 (got %r)" % spec)
    path, raw = spec.split("=", 1)
    parts = path.split(".")
    if len(parts) < 2:
        raise SystemExit(
            "%r needs at least a rule id and a key, e.g. "
            "damage.margin_to_damage_fraction" % path)
    values = []
    for token in raw.split(","):
        token = token.strip()
        values.append(float(token) if "." in token else int(token))
    return parts, values


def apply_override(M, parts, value):
    rule_id, keys = parts[0], parts[1:]
    if rule_id not in M.rules:
        raise SystemExit("no rule '%s' in mechanics.json" % rule_id)
    cur = M.rules[rule_id]
    for k in keys[:-1]:
        if k not in cur:
            raise SystemExit("'%s' has no key '%s'" % (rule_id, k))
        cur = cur[k]
    if keys[-1] not in cur:
        raise SystemExit(
            "'%s' has no mechanic '%s' (have: %s)"
            % (".".join(parts[:-1]), keys[-1], ", ".join(sorted(cur))))
    cur[keys[-1]] = value


def measure_level(M, level, trials):
    chars = b.build_all(level, M)
    names = list(chars)
    rounds = []
    for i, a in enumerate(names):
        for c in names[i + 1:]:
            r, _, _ = m.duel(chars[a], chars[c], M, trials=trials)
            rounds.append(r)
    contrib = b.contributions(chars, level, M)
    return {
        "fastest": min(rounds),
        "mean": sum(rounds) / len(rounds),
        "slowest": max(rounds),
        "spread": max(contrib.values()) / max(0.01, min(contrib.values())),
        "hp": max(c.total_hp for c in chars.values()),
    }


def evaluate(M, levels, trials):
    per_level = [measure_level(M, level, trials) for level in levels]
    out_of_band = 0
    for r in per_level:
        if r["fastest"] < b.TARGET_ROUNDS[0] or r["slowest"] > b.TARGET_ROUNDS[1]:
            out_of_band += 1
        if r["spread"] > b.MAX_CONTRIBUTION_SPREAD:
            out_of_band += 1
    return {
        "fastest": min(r["fastest"] for r in per_level),
        "slowest": max(r["slowest"] for r in per_level),
        "spread": max(r["spread"] for r in per_level),
        "drift": per_level[-1]["mean"] / max(0.01, per_level[0]["mean"]),
        "hp": per_level[-1]["hp"],
        "out_of_band": out_of_band,
        "per_level": per_level,
    }


def main():
    ap = argparse.ArgumentParser(
        description="Sweep one or two mechanics and report the effect.")
    ap.add_argument("-m", "--mechanic", action="append", required=True,
                    help="rule.key=v1,v2,v3 (repeat for a 2-D grid)")
    ap.add_argument("--levels", default="1,5,10,15")
    ap.add_argument("--trials", type=int, default=800)
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--verbose", action="store_true",
                    help="also print every level of every combination")
    ap.add_argument("--path", default=None,
                    help="Ruleset directory to sweep (or a mechanics.json), "
                         "instead of this checkout's own build/.")
    args = ap.parse_args()

    if len(args.mechanic) > 2:
        raise SystemExit("at most two mechanics at a time; the grid gets "
                         "unreadable beyond that")

    levels = [int(x) for x in args.levels.split(",")]
    specs = [parse_mechanic(s) for s in args.mechanic]
    labels = [".".join(p[-1:]) for p, _ in specs]

    print("Sweeping %s over levels %s (%d trials/duel)"
          % (" x ".join(".".join(p) for p, _ in specs),
             ",".join(str(x) for x in levels), args.trials))
    print("source: %s" % m.resolve_mechanics_path(args.path))
    print("target: %.0f-%.0f rounds, spread <= %.1fx, drift near 1.0\n"
          % (b.TARGET_ROUNDS[0], b.TARGET_ROUNDS[1], b.MAX_CONTRIBUTION_SPREAD))

    head = "%-10s %-10s %-8s %-8s %-8s %-7s %-6s %s" % (
        labels[0], labels[1] if len(labels) > 1 else "",
        "fastest", "slowest", "spread", "drift", "hp", "verdict")
    print(head)
    print("-" * len(head))

    best = None
    for combo in itertools.product(*[values for _, values in specs]):
        random.seed(args.seed)
        M = m.Mechanics(args.path)
        for (parts, _), value in zip(specs, combo):
            apply_override(M, parts, value)
        r = evaluate(M, levels, args.trials)
        verdict = "ok" if r["out_of_band"] == 0 else "%d out of band" % r["out_of_band"]
        print("%-10s %-10s %-8.1f %-8.1f %-8.1fx %-7.2f %-6d %s"
              % (combo[0], combo[1] if len(combo) > 1 else "",
                 r["fastest"], r["slowest"], r["spread"], r["drift"],
                 r["hp"], verdict))
        if args.verbose:
            for level, pl in zip(levels, r["per_level"]):
                print("             L%-3d      %-8.1f %-8.1f %-8.1fx %-7s %d"
                      % (level, pl["fastest"], pl["slowest"], pl["spread"],
                         "", pl["hp"]))
        score = (r["out_of_band"], abs(r["drift"] - 1.0))
        if best is None or score < best[0]:
            best = (score, combo, r)

    if best:
        combo, r = best[1], best[2]
        print("\nBest: %s"
              % ", ".join("%s=%s" % (".".join(p), v)
                          for (p, _), v in zip(specs, combo)))
        print("  %.1f-%.1f rounds, spread %.1fx, drift %.2f, %s"
              % (r["fastest"], r["slowest"], r["spread"], r["drift"],
                 "all levels in band" if r["out_of_band"] == 0
                 else "%d measurement(s) out of band" % r["out_of_band"]))


if __name__ == "__main__":
    main()
