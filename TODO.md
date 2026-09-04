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
- **The paragon's lead is not the paragon.** Investigated properly and
  it is neither its disciplines nor its weapon: a duellist given the
  paragon's attributes and told to dodge scores exactly what the paragon
  scores, 478 at level 8 and 732 at level 15, to the point. Athletic
  Adept is worth literally nothing to a blocker — 404 before and 404
  after — because Redouble needs the dodge stance and a blocker's
  targeting difficulty comes from a skill Athletic does not touch.

  Both stances are healthy. Four builds of ten prefer to block, and the
  duellist at dexterity 12 is better blocking (617) than dodging (536),
  while the paragon at dexterity 16 is better dodging (732) than
  blocking (606). Neither is right in general, which is what the design
  note says it wants.

  What the investigation actually turned up is about ATTRIBUTES, and it
  is the more useful finding. Measured from a common 76-point base with
  four points to place, at levels 8 and 15:

      +4 strength, blocking     464   725
      +4 dexterity, dodging     440   656
      +4 strength, dodging      385   630
      +4 constitution, blocking 353   520
      +4 constitution, dodging  343   529

  Two things fall out. **Strength is the best attribute a martial build
  can buy**, because block skill is governed by strength and melee
  attack is too, so one attribute raises offence and defence together
  where dexterity raises only defence. And **constitution is the worst
  by a distance**, because core hit points are a small slice of a total
  pool that mastery hit points dominate, so the attribute that buys them
  buys very little.

  It also means the strongest build is not in the roster at all: a
  strength-heavy blocker beats the paragon on a like-for-like base, so
  the contribution spread is understated rather than overstated.

  Moving block to constitution was measured and does fix the
  double-dip — the spread of the five options narrows from 1.39x to
  1.24x at level 15 — but it makes blocking worse than dodging across
  the board, which risks a stance choice currently in good health. It
  is a real design decision and is not taken.

  Constitution has since been given free mastery hit points per level
  instead, which takes it from three quarters of the best attribute to
  about nine tenths without touching the stances. **Strength blocking
  is still the best four points in the game**, because block skill and
  melee attack share an attribute. That double-dip is the last thing
  standing, and the only repairs for it are moving block off strength
  or giving dexterity a second job of its own.

- **Constitution now also speeds recovery and shortens a wound**, on
  top of the free mastery hit points. Untested by the simulator in both
  cases: the breather and rest percentages move by only a few points and
  the day model cannot see the difference, and how long a character
  stays wounded is a between-session question the fight model has no
  view of at all. The arithmetic is what it is — a wound that keeps a
  constitution 10 character down for six nights keeps a constitution 18
  character down for two.
- **High level builds cannot spend their points.** At level 15 every
  archetype has 8 to 38 points it is unable to place, because the
  mastery hit point ceiling and the power source ceiling both bind. The
  power source ceiling is the strange one: raising it converts those
  points into stamina or spirit and the extra buys nothing whatever,
  because a senior character already has more reservoir than a fight
  can spend. The advancement menu needs another sink, not a bigger one.

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
