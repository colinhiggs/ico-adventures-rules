# TODO

Parked work, roughly in the order it is likely to be picked up. Nothing
here is a commitment; it is a list of things known to be missing so that
they stop being rediscovered.

## The spell list

The damaging spells are done: bolts, lances, and the three area families
(bursts, blasts, fields), across four damage types. What is missing:

- **Non-damaging crowd control and area denial.** *Done, as the wards:
  fog, darkness, briars, sleet, hallowed ground, silence.* What is still
  missing from the category is anything that blocks movement outright —
  a wall — and anything that keeps a named kind of creature out.
- **Curing and restorative.** *In progress.*
- **Protection.** *Done, as the guards: Bulwark, Stoneskin, Elemental
  Guard, Mantle of Warding, Deathward.* Still missing: anything that
  protects a place rather than a person, and anything that turns an
  effect back on its caster.
- **Support and buff.** *Done, as the blessings, plus Rally and Hold the
  Line for the commander.* Still missing: anything that buffs a whole
  party by magic rather than by shouting, which was left out on purpose
  until there is a reason to want both.
- **Domain spells for spiritual casters.** The domains exist
  (`war`, `nature`, `healing`, `magic`) and only shape which spell a
  Granted Domain makes cheap. A druid needs nature spells that are not
  simply elemental damage with a leaf on them: weather, plants, animals,
  terrain.
- **Divination, movement and utility.** Not urgent, and mostly outside
  what the simulator can say anything about.

## Rules gaps found while doing the above

- **Reviving and raising the dead.** Dying is settled now — see
  `dying.md` — so a spell that pulls somebody back from death's door
  faster, or back from death itself, finally has rules to sit on. The
  death domain has one spell and this is the obvious second.
- **Poison** is named in the skill list as something Fortitude resists
  and exists nowhere else. It wants to be a condition.
- **Level 1 fights are too short.** Measured, not suspected: duels at
  level 1 average barely above the three-round floor before any
  particular rule is blamed. A question about hit points and damage at
  the bottom of the curve.
- **The hand axe and the staff are still dead weapons.** Both are
  dominated by arithmetic rather than by structure: the short sword
  beats the hand axe on accuracy, block and quickness for one point of
  damage, and the dagger beats the staff for a caster because it is
  quick and so equally free to cast around. The staff does now have its
  narrative job back, and its one real edge — the best block value on
  the table — pays only a caster who blocks. A repricing job on the
  weapon table.
- **The caster's single-target gap.** A caster contributes three to five
  times less than a martial build on the contribution gate. Part of that
  is the metric, which counts neither crowds nor range; part of it is
  real. It has survived every change made so far.
- **Every domain now has at least one spell**, but they are very
  unevenly served: war and healing are deep, forge and luck have a
  single spell each. A god granting three thin domains grants a thin
  priest, which is a content problem rather than a rules one.
- **A caster's free floor catches up with its paid output.** Minor
  spells scale with casting skill and have no minimum cost, so at level
  15 the priest keeps 96% of its damage with an empty reservoir, and at
  level 1 only 30% -- outside the band at both ends and in opposite
  directions. The reservoir matters too much early and not at all late.
- **Nothing grants an extra action, deliberately**, and at some point
  somebody will want a Haste. The reasoning against is written up in the
  blessings design note; it is a decision, not an oversight.
- **Ranged weapons are not statted at all.**

## Simulator gaps

- **No positions.** Reach and quickness are modelled first-order in
  duels and not at all in the crowd loop, and a caster duels toe to toe
  with spells that reach ten squares. This is the single largest source
  of doubt in every number the report prints.
- **Four of the six Master signatures do nothing** in the model: Read
  the Blow, Command the Room, School Mastery, Granted Domain.
- **The Social discipline is unmeasured**, because nothing in the model
  represents a fight that talking could change.
