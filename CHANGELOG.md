# Changelog

What changed between versions of the Ico rules, and what an adventure
built against an earlier one has to do about it. The three tiers and
what they oblige are defined in `VERSIONING.md`.

Every MAJOR entry must name its renames and removals old-to-new. That
list is the whole reason this file exists: without it, "revisit your
adventure" is a search, and with it, it is a substitution.

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
