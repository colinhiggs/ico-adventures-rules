# Changelog

What changed between versions of the Ico rules, and what an adventure
built against an earlier one has to do about it. The three tiers and
what they oblige are defined in `VERSIONING.md`.

Every MAJOR entry must name its renames and removals old-to-new. That
list is the whole reason this file exists: without it, "revisit your
adventure" is a search, and with it, it is a substitution.

## 1.0.2

No mechanic value changed. An adventure written against 1.0.0 or 1.0.1
needs to do nothing.

`sim/balance.py` and `sim/sweep.py` take `--path`, naming the ruleset
to measure the same way `tools/build.py` does. Without it they read the
`build/` beside themselves, which is right almost always, since the
simulator ships inside the ruleset it measures; with it they can
measure a ruleset that is not this one — an older pinned version
against the current one, or a tag worked out into a temporary clone to
find when a gate started failing. `sweep.py` now prints the file it
read, as `balance.py` already did.

## 1.0.1

No mechanic value changed. An adventure written against 1.0.0 needs to
do nothing.

`SHARING.md` is new: who may write to which part of this repository,
now that the projects built on these rules hold it as a git submodule
and write to it. The short of it is that `rules/bestiary/` is open to
anyone — writing an adventure creates monsters — and that a change
moving a mechanic value comes from here, because the value is measured
against the whole system rather than against the encounter that
noticed it. It also covers where a new creature belongs, how to add
one, and the submodule habits that keep two writers apart.

`README.md` gained a pointer to it.

Worth knowing on the toolset side, though it is not part of this
version: `tools/test_rules.py` now takes `--path`, so a project holding
the rules and the toolset as sibling submodules can run the ruleset's
suite where it lies instead of only building it.

## 1.0.0

The first tagged version. Nothing to compare it against — this entry
records what an adventure written today can rely on.

The ruleset is complete enough to play: character creation, the six
attributes and six disciplines, the two hit point pools, combat with the
block and dodge stances, skills, powers and advancement, the equipment
tables, and magic — schools, domains, spell preparation, and a spell
list of forty-three spells built on eight shared chassis, covering the
damaging families, the guards, blessings and wards, and the restorative
and revival spells.

Two things an adventure should know are deliberately unfinished:

- **The bestiary has one creature in it.** The stat block format is
  settled (`rules/bestiary/`, `kind: creature`) and the goblin
  demonstrates it, but the bestiary is expected to grow largely from
  the adventures that need creatures.
- **`challenge_level` in a stat block is an author's estimate.** The
  simulator cannot yet load a creature and measure it against the
  archetype panel, so that number has not been checked by anything.
  See `TODO.md`.

Ranged weapons are not statted at all, and there are no positions in the
simulator, so anything an adventure does at a distance is unmeasured.
