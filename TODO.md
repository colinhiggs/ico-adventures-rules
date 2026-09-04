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
- **Curing and restorative.** *Done: Mend, Cure Wounds, Cleanse,
  Restoration, and now Staunch.*
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

- **Reviving and raising the dead.** *Done, as Staunch and Raise the
  Dead.* Raise the Dead is the only spell in the game whose cost is not
  refunded by a night's sleep, and the only one with an explicit
  exemption from healing. If a second such spell is ever wanted, that
  exemption needs to become a general rule rather than a note on one
  entry.
- **Poison** is named in the skill list as something Fortitude resists
  and exists nowhere else. It wants to be a condition.
- **Level 1 fights are too short.** *Fixed, by granting ten mastery hit
  points free at character creation rather than by raising what a
  character may buy — see the design note in `character-creation.md`.*
  What is left of it is one pairing: two level 1 casters against each
  other still run past the twelve-round ceiling, because their damage
  with an empty reservoir is so small that more hit points simply
  lengthen the stalemate. That is the free-floor entry below rather
  than a hit point problem.
- **The dagger and the hand axe are dead weapons.** The staff is alive
  now that it has reach, and it took the dagger's job: same damage,
  better block, longer reach, and equally free to cast around, so a
  caster has no reason to carry a knife instead. The hand axe wants to
  be throwable, which needs ranged weapons to exist first — it is
  otherwise a short sword with worse accuracy, worse block and no
  quickness.
- **The caster's single-target gap.** *Closed by giving spells a damage
  rate from casting skill.* Against the best conventional martial build
  a caster now contributes 1.5x to 1.8x less across levels 5 to 15,
  where it was three to five times; the priest sits mid-table at every
  level and casters still clear a crowd in about half the rounds a
  fighter needs. Contribution spread with the paragon set aside is 2.2x,
  2.5x and 2.4x at levels 5, 10 and 15 -- at or inside the gate.
- **The paragon's lead is much reduced and not gone.** Measured with
  the Master limit and the weapon changes together, its contribution
  spread runs 1.7x, 2.3x, 3.1x, 2.9x and 2.8x at levels 1, 5, 8, 10 and
  15 against a 2.5x target. The trajectory of the whole effort, at
  level 15: 5.5x before any of it, 3.7x after spells took damage from
  casting skill, 3.3x after Untouchable was kept out of plate, 2.8x
  with the Master limit and the weapon table on top.

  The two changes pull in opposite directions at level 8 and the same
  direction above it. The Master limit takes level 15 down (827 to 732)
  and pushes level 8 up (from 2.6x to 3.1x), because at level 8 the
  second Master was a purchase the build should never have made -- it
  cost 33 stamina and 9 points of offence for half a point of damage
  taken, and forbidding it makes the character better. Above level 8
  the compounding it prevents is real.

  What is left at level 8 is not signature stacking. It is an ordinary
  single-Master build with good attributes out-contributing the
  duellist, which is a question about attribute spreads and stances
  rather than about disciplines or weapons.

- **A caster's free floor was out of band at both ends.** *Fixed, by
  giving spells a damage rate from spellcasting skill the way weapons
  have one from attack skill — see the design note in `damage.md`.*
  Casters now keep 39% to 62% of their damage with an empty reservoir
  across every level, inside the 35-85% band throughout. What is left is
  the same complaint about two HYBRID builds: the paragon at level 8 and
  the spellblade at level 15 keep 86% and 92%, because their floor is a
  great axe rather than a spell. That is a statement about those builds,
  not about the magic rules.
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
