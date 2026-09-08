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
- **A `harm` domain, if enough spells ever want one.** Cause Wounds is
  tagged healing and death, the way Staunch already is: domains are
  tags rather than categories and one match is enough for access, so
  the reversed spell needed no domain of its own. A harm domain is
  still arguable, and the question is what it would mean. Read widely
  it is most of the damaging spells, which makes it a second name for
  war and worth nothing. Read narrowly it is direct injury to the life
  force, or the intent to cause pain rather than merely damage, which
  is a distinct thing worth having a god of -- and currently has one
  spell in it. A neutral `life` domain covering both directions was
  the other candidate and was dropped as too near a duplicate of
  healing. The list is open, so none of this costs anything to leave
  until there are spells enough to settle it.

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
- **The dagger and the hand axe are dead weapons.** *Partly answered:
  both are throwable now that `ranged-weapons.md` exists, so the hand
  axe is no longer a short sword with worse everything.* The staff is
  still alive and still holding the dagger's job — same damage, better
  block, longer reach, equally free to cast around — so a caster who
  never throws anything has no reason to carry a knife instead. Whether
  a throw at the dagger's range is worth the hand is still unmeasured:
  duels have distance now, but nothing in the model picks up a ranged
  weapon or throws anything, so the gear chooser cannot price a throw.
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

  Constitution has since been given free mastery hit points, faster
  recovery and quicker healing, and that closed most of it.

- **The strength double-dip is real, worth about ten per cent, and
  should be left alone.** Block skill and melee attack do share an
  attribute, so strength raises offence and defence together. Measured
  across the pairings anybody would actually choose, though, the gap is
  small — at level 15, strength-and-block 100%, constitution-and-dodge
  97%, constitution-and-block 95%, dexterity-and-dodge 91%, a spread of
  1.10x. At level 8 it is 1.11x.

  Three repairs were measured and every one is worse:

  - **Block governed by constitution** widens the spread to 1.56x and
    1.59x. It does not remove the double-dip, it moves it onto the
    attribute that now also grants hit points, recovery and healing.
  - **Block governed by dexterity** gives the tightest spread of raw
    pairings but drops the count of builds that prefer to block from
    four in ten to two: every defensive option would run on one
    attribute, and blocking stops being a real choice.
  - **Finesse extended to medium weapons** keeps all four blockers and
    reads 1.06x at level 15, but 1.20x at level 8 — better at one end
    and worse at the other.

  A ten per cent premium for a coherent build is not a defect. The gate
  that is actually failing fails on the paragon against the spellblade,
  which is a different quarrel entirely.

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
- **The reach rules are measured now, and they are too strong.** The
  duel loop has positions, and with them the 2.0.0 rules take about a
  quarter off every fight where one side outreaches the other — enough
  to put five more pairings under the round-length floor. A pairing with
  equal reaches does not move at all, which is what says the effect is
  the reach rules rather than the rewrite. That measurement is an upper
  bound rather than an estimate: the model gives the free attack away
  for nothing because Riposte and Deflect are not modelled, and fights
  on open ground so the tight-space penalty never applies, so both of
  the counterweights the rules were given are invisible to it. What to
  do about it is a design question and not a modelling one — the honest
  options are to make the free attack cost something the model can see,
  to narrow when it triggers, or to accept shorter fights between
  mismatched weapons and move `TARGET_ROUNDS`.
- **The tight-space penalty still has no home in the simulator, by
  construction.** Duels have distance now, but distance is not walls.
  Every fight the model runs is on open ground, which is an
  `ASSUMPTIONS` entry rather than an oversight, so one of the two
  counterweights to the reach buff remains unmeasurable — and the other,
  the reaction, is unmeasurable for a different reason: nothing spends
  reactions here. A
  positional model would need walls before this means anything, and
  walls are a much larger thing than distance.
- **The area spells now say how far away they can be put.** *Done:
  `blast`, `burst`, `field` and `ward` carry `range: 10`, the same
  figure a bolt and a lance already had, and the prose says once that
  an area spell is placed rather than centred on the caster.* What it
  changed is smaller than it looks and worth recording: a caster
  clearing six goblins already did it in one round to one and a half,
  so opening at ten squares instead of two did not make it faster --
  it made it **free**. The evoker, the priest and the spellblade now
  finish untouched, where the spellblade in particular was losing
  `9%` of its hit points. The crowd gate never bound on any of them,
  so nothing moved in `--check`; the contribution spread is measured
  from duels, and nothing in a duel opens at range yet.
- **The long-range rule lives in two documents.** `spell-properties`
  owns `long_range_multiplier` and `ranged-weapons` owns
  `long_range_penalty`, and each interpolates the other's half. Nothing
  can drift, because neither value is written twice, but the rule reads
  as though it belongs to whichever page you happened to open. Both
  constants want one home — `movement` already owns the squares they
  are counted in. Moving either one removes a mechanics key, which is a
  MAJOR bump, so it waits for the next one.
- **Ranged weapons are unmeasured.** *Statted in
  `ranged-weapons.md`: sling, shortbow, longbow, both crossbows, the
  javelin, and throwing ranges on the dagger and hand axe.* Not one of
  those numbers has been through `sim/`, because the simulator has no
  positions and so has no way to represent the thing an archer is
  buying. They are a first pass, priced by eye against the melee table.
  The entry below on positions is now the blocker for this one.

## Simulator gaps

- **No creature loader.** A bestiary entry is deliberately shaped like
  the simulator's `Character` -- six attributes, ranked skills,
  disciplines, the two hit point pools, stamina and spirit, a stance,
  and weapon and armour keyed into the equipment tables -- so that
  asking whether a creature is a fair fight at a given level is a
  measurement against the archetype panel rather than a guess. Nothing
  yet reads one. The missing piece is a short function that builds a
  `Character` from `mechanics.json`'s entry for a creature, plus a
  balance report that pits the bestiary against the archetypes the way
  the archetypes are currently pitted against each other. Until it
  exists, `challenge_level` in a stat block is an author's estimate and
  should be read as one.
- **Natural weapons have nowhere to live.** The goblin carries a weapon
  off the equipment table. A wolf's bite is not in `weapons.md` and
  should not be, because that table is also the shop. Creatures
  probably want an inline `weapon:` map using the same keys as a table
  entry, which the loader above would have to accept alongside a bare
  table key.
- **Positions reach duels and the crowd loop; nothing yet picks up a
  ranged weapon.** Duels have distance and so do skirmishes -- one
  number per creature, an opening at the hero's own range, ground to
  give and ground to cross, the band answered out of the reaction, and
  a limit on how many bodies can stand where they can hit you. What is
  missing is anything that would use it: no build shoots, throws, or
  opens a fight at spell range, because the spells a caster actually
  picks against a crowd declare no range (see the rules gap above).
  Until that is filled and ranged weapons reach the combat loop, the
  crowd numbers are the same numbers a positionless model produced,
  and the machinery is groundwork rather than measurement.
- **The simulator was thirteen minutes and is now under three.**
  *Done, and recorded here because the next person to profile it should
  know where the easy wins have already gone.* Values and the figures
  derived from them are cached on the `Mechanics` instance; a blow is
  split into the part the margin changes and the part it does not; a
  combatant is copied by hand rather than by `deepcopy`; `duel` asks
  what each side will do and what a round of it is worth off one search
  rather than two; and the spell search no longer rebuilds a spell's
  definition seven million times a level. Every one of those was
  checked by dumping duels, skirmishes, contributions and offence
  figures on a fixed seed and diffing -- byte-identical, every time.
  Two lessons worth keeping. Guesses about where the time goes were
  wrong twice: sharing the duel planning was estimated at a third and
  measured at five per cent, because planning happens once a duel and
  the trials happen three thousand times. And this machine varies by
  twenty-five per cent between batches, so a timing is only worth
  quoting when the two versions were run back to back.
- **`best_difficulty` scans sixty difficulties and stops at none of
  them.** Expected cost looks monotonic in difficulty, and if it is,
  the scan can break rather than continue. That is an assumption about
  every future power as well as the present ones, so it wants deciding
  rather than assuming.
- **Four of the six Master signatures do nothing** in the model: Read
  the Blow, Command the Room, School Mastery, Granted Domain.
- **The Social discipline is unmeasured**, because nothing in the model
  represents a fight that talking could change.
