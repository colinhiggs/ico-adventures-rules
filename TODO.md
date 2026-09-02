# TODO

Parked work, roughly in the order it is likely to be picked up. Nothing
here is a commitment; it is a list of things known to be missing so that
they stop being rediscovered.

## The spell list

The damaging spells are done: bolts, lances, and the three area families
(bursts, blasts, fields), across four damage types. What is missing:

- **Non-damaging crowd control and area denial.** The `field` chassis
  was written expecting most fields to be these — fog, tangling ground,
  silence, darkness — denying ground by what they do rather than by what
  they deal. The diffuse spread rate exists for exactly this and is
  currently used only by the damaging fields.
- **Curing and restorative.** *In progress.*
- **Protection.** Wards, shields, resistance to a damage type, cover
  against a school.
- **Support and buff.** Raising an ally's skills, damage, movement or
  defence for a duration.
- **Domain spells for spiritual casters.** The domains exist
  (`war`, `nature`, `healing`, `magic`) and only shape which spell a
  Granted Domain makes cheap. A druid needs nature spells that are not
  simply elemental damage with a leaf on them: weather, plants, animals,
  terrain.
- **Divination, movement and utility.** Not urgent, and mostly outside
  what the simulator can say anything about.

## Rules gaps found while doing the above

- **Dying, unconsciousness and death.** Nothing in the rules says what
  happens at zero core hit points. Anything reviving, stabilising or
  raising the dead needs this first.
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
