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
- **Casting in Harness asks for Magical, and a war-priest has the
  same problem.** The power forgives part of armour's skill penalty on
  the casting roll and lets a size `M` weapon stop occupying a hand,
  and it requires Martial and Magical both at Adept. A Spiritual caster
  in mail meets exactly the same collision, rolls exactly the same
  `spellcasting` skill, and cannot take it. That is a gap rather than a
  decision. It was left because widening the requirement would be the
  first time two disciplines were treated as interchangeable in a
  prerequisite, and that is a precedent to set deliberately rather than
  in passing -- the honest options are a second power for the
  Spiritual side, a requirement reading "Magical or Spiritual", or a
  general notion of a casting discipline that both belong to. The
  third is the tidiest and the largest.
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
  never throws anything has no reason to carry a knife instead.
  Measured against the gear chooser's own objective, the two are not
  equally dead and the gate names them as though they were. The dagger
  reaches 94% of the best weapon for the level 10 duellist and beats
  the short sword there, on quickness against the panel's reaching foe;
  it is simply never first. The hand axe is bottom or next-to-bottom in
  every build at every level — too small for reach, not quick, less
  block than the short sword, and its one extra damage point is worth
  less than quickness. It is the only weapon in the table that buys
  nothing at all.
  *The throw is now measured, and it is not the answer.* The model
  prices one — Attack (ranged) off dexterity, the weapon's own accuracy
  and damage, a shield's block against it but not a weapon's — and it
  comes to zero for two independent reasons, neither of which is about
  daggers.
  The first is that **a range of six squares or less buys no rounds at
  all**. The standard foe strides five and is given the first move, so
  the shortest range that buys even one round of acting before contact
  is `7`, at every level. The hand axe throws `3`, the dagger and the
  javelin `4`, the sling `6`. All four are under it. That is the
  conservatism in `rounds_at` biting unevenly — it costs a caster
  holding a bolt one round in three and costs anything short its whole
  capability — and it is the line to revisit if a throw is ever meant
  to count. Revisiting it moves every caster's numbers, so it is a
  decision rather than a tidy-up.
  The second is that **nobody has the skill**. `attack_ranged` is a
  Martial skill that `TRACKED_SKILLS` does not list, so no build spends
  a point on it and every throw is thrown at bare dexterity. It gets
  worse with level, not better: `2.91` at level 1 and `1.15` at level
  10, as the targeting difficulty climbs past an arm that never trains.
  Trained to the rank of the melee attack it competes with, the same
  throw is worth `9.10` at level 10 against the swing's `11.95` — about
  three quarters of a melee attack, which is roughly what a thrown
  weapon should be. So the throw is a real capability in the rules and
  a dead one in the measurement, and the two fixes for that have very
  different blast radii.
- **The weapon table has one live axis, and it is the damage rating.**
  Across twelve build-by-level cells the ranking under the chooser's
  objective *is* the damage-rating ranking, with one exception (the
  level 10 duellist and paragon, where quickness lifts the dagger past
  the short sword). The other columns are dominated, unreachable or
  unpriced:
  - *Accuracy* is worth `0.87` of a damage point, measured, and no
    weapon carries more than `+2`. It cannot reorder anything.
  - *Weapon `block_ap`* is nearly dead content. A shield overrides it
    entirely and shields cost 5–40gp, so only a blocker who declines a
    shield ever collects one. The staff's `7` and the short sword's `6`
    are the best block values in the game — better than a great
    shield's `5` — and almost nobody is in a position to be paid them.
  - *Armour taxes small weapons harder.* Against ap 4 the tax is 41.9%
    of the dagger's raw damage and 25.4% of the great axe's.
    `max_reduction_fraction` stops plate making light weapons useless,
    which is what it is for, but it makes the tax regressive: a point of
    damage rating is worth more to a weapon that already has plenty.
    That is the engine concentrating the table at the top.
  - *`reduction_ignored` cannot differentiate anything.* `damage_curve`
    carries a comment promising it to axes and no axe has the key.
    Measured, one point of ignored reduction is exactly one point of
    damage rating at every armour value from ap 2 to ap 8 — `12`
    damage with `1` ignored and `11` damage with `2` agree to three
    decimals throughout. The two differ only where the cap binds, which
    is small weapons against plate, and there it is worth `+1.3%`.
    Tried as a design axis it made things worse: axes ignoring `1`
    widened the duellist's spread from 1.16x to 1.22x and pushed the
    dagger from 95% to 89%.
- **Reach is unpriced, and it is what the two-handers are bought for.**
  Ablate the reach bonus on the size L weapons and the paragon's great
  axe falls from first to fifth and the berserker's from first to
  second. The `-2` defence penalty pays for the damage almost exactly:
  `+20.7%` offence against `+22.3%` incoming. Reach rides free on top of
  a trade that has already been settled. The design note in
  `weapons.md` has this backwards — it says the penalty is what buys
  the reach.
  The penalty cannot be raised to cover it. A sweep over levels 1 to 15
  says `-2` is already the best value the game has: `-1`, `-3` and `-4`
  each put four measurements out of band against `-2`'s three, and `-3`
  shortens the fastest fight from 2.5 rounds to 2.3 when four of the
  nine current gate failures are already fights ending too fast. The
  penalty's other end is the round-count gate, so it cannot be spent
  here.
  Giving reach its own home was the obvious answer and it does not
  work. *Tried and measured, six ways, all worse than today.* There is
  no spear or polearm in the table even though `reach.md` and
  `turn-order.md` both talk about them — a polearm holding a band, a
  spear in a shield wall — so the weapon the rules describe has never
  existed and reach was attached to the two biggest damage weapons
  instead. Adding it back costs more than it pays. Counting the way the
  gate counts, weapons never chosen at any of levels 1, 5, 10 and 15:

  | configuration | never chosen | count |
  | --- | --- | --- |
  | today | dagger, hand_axe | **2** |
  | spear `7` added, two-handers keep reach | dagger, hand_axe, sword | 3 |
  | spear added, reach off the two-handers | dagger, short_sword, sword, two_handed_sword | 4 |
  | ...plus a polearm at `10` | + polearm | 5 |
  | ...plus a polearm at `11` | dagger, great_axe, short_sword, sword, two_handed_sword | 5 |
  | the penalty follows reach, + spear | hand_axe, short_sword, spear, staff, two_handed_sword | 5 |
  | the penalty follows reach, + spear + polearm | + polearm | 6 |

  Each failure says something.
  *The spear itself is fine.* At `7` damage, size M, one hand, reach
  `1`, it is bought by the duellist, paragon, commander and spellblade
  from level 10 on. What it kills is the **sword**, because reach is
  worth about one point of damage and the spear is exactly one point
  cheaper. At `6` the spear is dead instead. The whole window is one
  damage point wide.
  *Taking reach off the two-handers kills them.* Without it the `-2`
  is a bad trade — the wash above loses to a battle axe that gets `9`
  damage at size M for no penalty at all — and the sentinel, the only
  build that ever told the twins apart, abandons both for the battle
  axe.
  *Making the penalty follow reach rather than size is the worst of
  the six*, even though it is what `weapons.md`'s prose asserts. It
  hands the great axe `12` damage for no penalty whatever, and casters
  drop the **staff for a dagger** — which costs the staff the one job
  it exists to do. The prose is wrong about what the penalty buys; the
  penalty is still in the right place.

  So the real blocker is the entry above: the damage rating is the only
  live axis and eight weapons already sit about one per rung (from `5`
  to `12` when this was written; `6` to `10` since the ratings were
  compressed, which makes the crowding worse rather than better). A ninth weapon has to stand on a rung, and whatever was
  standing there dies. Moving reach about changes which rung a weapon
  effectively occupies; it does not make a new one. **A second live
  axis has to come first**, and the entry below is where the candidates
  for one are.
- **The damage ratings were compressed, and it made the block axis
  necessary rather than optional.** *Done.* The ratings looked like a
  little over two to one and were nearer four to one where it counts:
  armour is subtracted from every blow and `damage.md`'s cap holds the
  subtraction to half the raw figure, so a small weapon loses a share
  and a large one loses a fixed amount. Against ap `4` the bare ratings
  at the two ends arrived as `2` and `8`. They now arrive as `3` and
  `6`. Ratings went `5,5,6,7,8,9,12,12` to `6,6,6,7,8,8,10,10`.
  It bought a lot. Round-count failures went from seven to four,
  because the biggest weapons had been ending duels before anybody
  spent anything, and the spellblade's empty-reservoir gate came into
  band as a side effect. Six tables were measured; this one has the
  flattest weapon usage of any of them, four weapons within `11` and
  `9` picks across four levels.
  Two things it did not buy, both worth knowing.
  *Accuracy cannot compress a table.* It was the obvious lever and it
  is the wrong one: a point of accuracy is worth `0.71`-`0.87` of a
  damage point to a small weapon and `1.05`-`1.32` to a large one,
  because its extra hits are worth whatever that weapon deals. Adding
  it to the small end was measured and made an extra pairing end too
  fast. It is an identity axis, not a compression lever.
  *Dead weapons went from two to four* -- battle axe, hand axe, short
  sword and two-handed sword. That is the trade that was accepted going
  in, and mostly it is ties rather than rot: a squeezed table has more
  weapons than rungs. But two of the four are **dominated** rather than
  tied, which is a different thing and is not acceptable on its own
  terms: the battle axe and the sword now share a rating and the sword
  has a point of accuracy on it, and the two-handed sword remains the
  great axe's exact twin.
  There is no room left to fix that with damage, which is the point:
  compressing the ratings removed the slack that was hiding the fact
  that **block is dead**. An axe trades block for damage and a sword
  the other way round, and that trade cannot be priced while a 15gp
  shield erases the weapon's block value entirely. The entry below is
  no longer a nice-to-have.
- **The dead-weapon gate measured the wrong thing.** *Replaced by three
  that measure the right ones.* It fired when a weapon was never
  chosen, which under a compressed table is the normal condition rather
  than a defect: equivalent weapons tie, the chooser takes one, and the
  other reads as dead for ever. Reading the scores instead of the
  winner says the table was in much better shape than the gate implied
  -- the four weapons it called dead sit at `1.000`, `0.96`, `0.95` and
  `0.92` of being somebody's first choice, and the two-handed sword was
  "dead" only because it ties the great axe exactly.
  What replaced it: how much the weapon decides about the character
  (median build's best-to-worst gap, `<= 20%`), the same inside one
  class (`<= 30%`), and whether any weapon is beaten on every axis and
  wins on none. Both spread gates fail on the pre-compression table
  (`28%` and `38%`) and pass on this one (`18%` and `26%`), which is
  what makes them gates rather than thresholds fitted to today.
  One reduction was tried and abandoned, recorded so it is not tried
  again: asking whether a weapon is *somebody's* near-miss saturates.
  With ten varied builds nearly every weapon is one, and it scored the
  old wide table `0.959` against the narrow one's `0.921` -- backwards.
- **The battle axe was the one real mistake in the weapon table.**
  *Formally fixed; really still waiting on block.* It shared the
  sword's rating, cost and size while the sword had a point of accuracy
  and two of block on it, so there was nothing it won on. It is now
  cheaper (`12gp` against `20gp`, which is where history puts an axe
  beside a sword) and blocks for `4` rather than `3`. The domination
  gate passes and every weapon-table gate now passes with it.
  What did **not** happen is the interesting part, and it is worth
  keeping: the axe's measured utility did not move by a thousandth --
  `0.945`, `0.965`, `0.954`, `0.957` across the four levels, before and
  after, identical. Neither half of the change reaches the measure.
  The price does not bind at a purse of 150gp upwards, and the block
  point is worth nothing because a build that blocks nearly always
  carries a shield and a shield replaces the weapon's value outright.
  So the axe is no longer a mistake on paper and is still not a choice
  in play. That is a pre-payment on the entry below rather than a fix:
  the moment a weapon's block value means something, this weapon
  already has the numbers to be the axe-shaped answer to the sword.
- **Weapon block is the most promising dead axis, and there are two
  different ideas here.** They were briefly conflated in conversation
  and are worth keeping apart, because one is a repair and the other is
  new design.
  *A block value nobody can collect.* `damage.md` has you block with
  the shield **or** the weapon, so a shield erases whatever the weapon
  was worth. The staff's `7` and the short sword's `6` are the two best
  block values in the game — better than a great shield's `5` — and
  only a blocker who declines a shield ever sees one, which no build
  with a spare 15gp does. Letting the two add, or otherwise making the
  weapon's value collectible, would give small weapons a defensive axis
  that is currently decoration. It is a change to `damage.md` and not
  to the weapon table.
  *Blocking at reach, for somebody else.* The stronger idea. A long
  weapon can physically get between a blow and the person standing next
  to you, and a short one cannot, so a reaching weapon could spend its
  reaction to block for an **ally** within its reach. That is a second
  axis that belongs to reach specifically, it is paid for out of the
  same one reaction `reach.md` already spends on the band — so a spear
  is still choosing between holding the line, striking the approach and
  covering its neighbour — and it is the mechanical statement of the
  design note that is already in `reach.md`: *a spear in a shield wall
  is the oldest good idea in warfare.* A shield wall is exactly a row
  of people defending their neighbour.
  It also explains why every measurement above undervalues reach. A
  rule that only pays when somebody is standing beside you is worth
  precisely nothing in a duel and nothing in `contributions`, and those
  are the only two things `sim/` can see — see the simulator gap on
  parties below. So this one cannot be settled by measuring it as the
  weapon table is measured today; it would have to be argued at the
  table, or the simulator would have to grow a second friendly body.
- **The great axe and the two-handed sword are the same weapon.**
  Identical offence at every level, tied at exactly 100.0% for every
  dodging build. They differ only in block value (`2` against `4`) and
  5gp, and weapon block value only reaches a blocker carrying no
  shield, so only the sentinel tells them apart. The eight-row table
  has seven weapons in it, and the dead-weapon gate does not see this
  one because both of them get bought.
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

- **Casters are the weakest thing in the game, and armour no longer
  hides it.** `armour.hampers_spellcasting` charges the skill penalty
  off the casting roll as well as the dodge, which is what stopped
  every caster in the panel buying full plate at every level. The
  choice was made knowing the price, and the price is that the
  contribution spread gets **worse**: `2.9x` to `3.4x` at level 10, the
  evoker falling from `170` to `145`, and a new failure at level 5
  where there was none. The gate was already failing and this is the
  same failure louder, not a new kind of one.

  **The guards are not the answer, and this entry used to say they
  were.** The reasoning was that a robed caster's protection ought to
  come from Bulwark and Stoneskin rather than from a breastplate, and
  that `MAX_SELF_GUARD_RATIO` was the cap holding them back. Measured,
  none of that is a lever:

  - `MAX_SELF_GUARD_RATIO` is a **gate threshold, not a knob**. It caps
    how good a self-cast guard is allowed to be, and no build reaches
    it -- the ratios sit at `0.84` to `0.94` against a cap of `1.00`.
    Raising it permits something that is not happening.
  - Making the guards themselves stronger barely helps. Sweeping
    `protection_per_step` from `1` to `6` (and Bulwark's from `2` to
    `12`) takes the evoker's self-cast ratio from `0.93` to `1.13` and
    moves the contribution spread by **nothing at all**: `3.34x` at
    every strength, the evoker pinned at `147`. Stoneskin flattens at
    `0.93` however strong it gets, because extra armour runs into
    `damage.max_reduction_fraction`.
  - The reason it moves nothing is that **`contributions` never casts a
    guard**. It is offence times `total_hp / taken`, and no guard is
    applied anywhere in it. The metric that reports casters as weak
    cannot see protection at all.
  - Even crediting a self-cast guard at full value, which the metric
    does not, the evoker goes `147` to `164` and needs `197` to pass
    the `2.5x` gate. The whole guard family is worth about a third of
    the gap.

  **Probed on the damage side, and it is half offence and half
  survival.** At level 10 the paragon is `1.99x` ahead on offence plus
  control and `1.68x` ahead on survival, and `1.99 x 1.68` is the whole
  of the `3.34x`. The survival half is the armour rule above doing
  exactly what it was meant to do: the evoker takes `8.71` a round in
  partial leather where the paragon takes `5.19` in a breastplate.

  What the sweeps say, all measured at levels 1, 5, 10 and 15:

  - **`damage.damage_per_casting_skill_step` `3` to `1` fixes it**, and
    by a distance. Contribution spread `1.91x` to `2.25x` at every
    level, caster free floors a healthy `54%` to `71%`, and
    `--check` goes from **fourteen failures to six** -- the lowest this
    ruleset has measured since duels had no positions. The six left are
    the paragon being too strong and the dead weapons, both older than
    this question.
  - **But it overpays, and the reason is worth knowing.** At step `3`
    a caster's skill is ALREADY at per-blow parity: casting skill `16`
    gives `5` damage, and a duellist's attack skill `16` gives `2` from
    skill plus about `4` from margin. Step `1` makes it `16`, about
    `2.7x` what the fighter gets. It works because it pays for the
    survival half of the gap out of the offence half, not because the
    rate was wrong.
  - `lance.damage_per_step` `1` to `2` fixes the spread on its own
    (`2.49x` at level 10) and is far more targeted, but it lifts only
    the paid spell and not the free one, so caster floors fall out of
    the `35-85%` band at levels 1 and 5 (`33%`, `29%`). `--check`
    stays at fourteen failures, just different ones.
  - `casting 2` plus `lance 2` passes the spread everywhere and keeps
    floors at `36-43%`, but that is two keys to buy what one nearly
    does, and it sits against the floor bound.

  So the decision is not "which number", it is whether a caster's
  survival deficit should be repaid in damage. If it should, step `1`
  is the change and the design note in `damage.md` needs to say why
  the rate is steeper than parity. If it should not, the missing
  piece is defensive and the guards cannot supply it -- see above --
  so it would have to be something new.

  **Armour is a second measured dead end, alongside the guards.** The
  evoker was forced into every entry in the table at level 10 and the
  one it already picks is the best of them: `partial_leather` at
  `147`, against `137` in leather, `132` in a breastplate and `100` in
  full plate. Every one of those is LEGAL -- `casting_survives_the_kit`
  passes even full plate at this level -- so the caster is optimising
  and not trapped. Survival spans only `8.03` to `10.39` across the
  whole ladder, because `max_reduction_fraction` caps what any armour
  can do, while offence falls from `16.86` to `9.59`. The best figure
  reachable by re-equipping is the `147` it has, against `197` needed.

  **The steeper rate is also what makes armour unaffordable, which is
  the argument against step `1` that the sweeps do not show.** Casting
  skill feeds damage at one point per step, so a point of armour skill
  penalty costs a caster `1/step` of damage against a warrior's
  `1/8`. At step `3` that is `0.33` a point; at step `1` it is `1.00`,
  eight times what the warrior pays. Measured on the ladder: wearing a
  breastplate costs the evoker `10%` of its contribution at step `3`
  and `19%` at step `1`. Step `1` does not repair the fragility, it
  deepens it and pays compensation in damage -- and it overshoots, the
  evoker reaching `245` and the binding build becoming the generalist
  at `233`.

  **What the design note already says decides the rate.** Its argument
  is structural: a blow turns margin into damage and a spell never
  does, so the caster's one route is steeper to stand in for the
  warrior's two. Measured at level 10 that is duellist `16` attack
  bonus giving `2` from skill plus about `4` from margin, against
  evoker `16` casting bonus giving `5`. Step `3` IS that argument's
  answer, and the caster is fractionally behind it. Step `1` gives
  `16` against `6` and leaves the note defending a rate it did not
  derive.

  **`contributions` now opens at range, and the gap survives it.** The
  metric measured a caster standing in contact for the whole fight,
  which is the one situation its design says to avoid, and it did so
  after the model had gained everything needed to do better -- duels
  have distance and every spell declares a range. It now credits the
  rounds a build acts before the foe arrives, at the spell's worth
  rather than the build's best turn, so no martial figure moves. The
  standard foe closes five squares from reach one, and the count is
  deliberately mean -- the caster never gives ground and is assumed to
  act second -- so a range-10 caster gets **one** free round, not two.

  What that is worth, and it is not nothing: the level 5 spread goes
  `2.84x` to `2.49x` and PASSES, level 10 goes `3.34x` to `3.00x`,
  level 15 `2.86x`, and `--check` goes from fourteen failures to
  **thirteen**. The evoker gains `147` to `164` at level 10 -- the
  same figure crediting a guard at full value was worth, arrived at
  honestly.

  But it does not close the gap, and that is the useful part of the
  result. Measured on top of it, at levels 1, 5 and 10:

  - **distance alone: thirteen failures**, level 10 spread `3.00x`.
  - **distance plus `damage_per_casting_skill_step` `2`: nine
    failures**, spread `2.6x` -- still failing, by a tenth. No floor
    failures at all, the spellblade's `86%` included.
  - **distance plus `lance.damage_per_step` `2`: fourteen failures**,
    and worse than the baseline in kind: caster floors break at both
    ends, `33%` and `29%` at level 1 and `34%` at level 5, exactly as
    the sweep above warned.

  So the metric was genuinely blind and is less so, the level 5 gate
  was failing for a reason that was not the rules, and **the level 10
  question is unchanged**. Nothing here should be read as choosing a
  number: the closest combination still overpays against the design
  note's own argument and still misses. The decision above is still
  the decision.

  **Then the caster was allowed to give ground, and the entry above is
  now mostly answered.** Holding the range rather than standing still
  for it is what `_crowd_advance` already has a hero do, against a
  budget as deep as the range; applying the same rule here takes a
  caster from one free round to three, and two for the generalist,
  whose plate costs it a stride. Nothing else changed, and no mechanic
  moved.

      level      standing still     giving ground
      1          1.57x              1.64x
      5          2.49x              1.99x
      10         3.00x  evoker      2.63x  spellblade
      15         2.86x              2.41x  -- passes

  **The evoker reaches `197.7` at level 10 against the `196.6` it
  needed.** The build this entry is named after is no longer the
  weakest thing in the game at any level, and it got there without a
  number moving -- it was being measured standing in contact for a
  fight it would have spent backing away.

  What is left of the level 10 failure is the **spellblade** at `187`,
  and that is the hybrid entry below rather than this one: a build
  that cannot wear plate without switching off half of itself, whose
  cost is already written down there. The caster question and the
  hybrid question were the same failure and are now two, which is the
  useful part.

  **The ground budget is the assumption to watch, and it was not
  chosen for its answer.** Measured at level 10: no ground `3.00x`,
  half `2.76x`, the range `2.63x`, double `2.40x` -- which passes.
  It is set at the range because that is where the crowd loop sets it,
  and taking the wider one to clear a gate would be exactly the move
  the top of this file says not to make. The **spellblade came out incoherent** and no
  longer does: the gear chooser used to keep it in full plate, because
  its melee dominates damage-times-survival, and it then could not land
  a field at level 5. A build with ranks in spellcasting now refuses
  kit that stops it landing the spell it would cast unarmoured -- a
  legality filter rather than a scoring term, because pricing the
  second capability needs a weight nobody can derive. It wears light
  armour and keeps its axe at levels 5 and 10, and picks up a staff at
  15.

  What that cost is worth writing down. The spellblade loses about a
  sixth of its contribution -- `151` to `127` at level 5, `196` to
  `161` at level 10, `245` to `213` at 15 -- because plate was worth
  eight points off every blow and light armour is worth three. Four
  round-length failures appeared, of which three are the spellblade
  dying faster, and all four sit between `2.96` and `3.00` rounds
  against a floor of `3.00`. That is the honest shape of a hybrid that
  cannot wear plate, and the alternative was a build that had quietly
  stopped being a caster while still being scored as one.

  What is still open underneath it: the spell never beats the axe in
  ANY kit, including one carrying no penalty at all -- best spell
  `15.7` against a one-handed power at `12.1`, and the axe
  configuration wins on score even so. The constraint stops the build
  buying its way out of being a caster; it does not make casting worth
  doing. That is the contribution spread again, and per the
  measurements above it is the spell's damage that wants looking at,
  not its protection.

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
  so nothing moved in `--check`. The contribution spread did not move
  either, and the reason given here was wrong: it is not measured from
  duels. `contributions` is analytic -- `attack_expectation` times
  `expected_offence` -- and the duel loop feeds only `TARGET_ROUNDS`.
  So giving duels an opening distance could never have moved it. What
  moved it was giving `contributions` one; see the caster entry above.
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
  those numbers has been through `sim/`. They are a first pass, priced
  by eye against the melee table.
  The blocker used to be that the simulator had no positions and so no
  way to represent what an archer is buying. That is no longer true:
  positions landed with the caster-gap work, and *throwing* landed
  after it — a throw is priced as a shot and counted among the openings
  a build can take. What is still missing is narrower again: nothing
  sells a bow. `gear_options` offers weapons off `weapons.md` only, so
  no build can buy a shortbow, and none of the six shooting weapons has
  been through `sim/` even now.
  Two of the numbers can be read against the melee table already, and
  they do not look well. The shortest range that buys a build a single
  round before contact is `7` squares, so the sling's `6` and the
  javelin's `4` buy nothing whatever a build does with them; the
  shortbow's `10` buys two rounds and the longbow's `18` buys six.
  Whether that spread is the right shape is exactly what measuring
  would settle.

## Simulator gaps

- **Nobody ever has an ally.** Every measurement in `sim/` is one
  body against one body, or one body against a crowd of enemies. There
  is no second friendly creature anywhere in the model, so any rule
  whose whole point is what it does for the person standing next to you
  is worth exactly zero here and cannot be told apart from a rule that
  does nothing.
  That is not a small blind spot. It is why the reach entry in the
  rules gaps above cannot get an answer: the most promising thing to
  hang on a long weapon — blocking a blow aimed at an ally — would
  measure as worthless in a duel and worthless in `contributions`,
  which between them are everything the simulator can see. Flanking,
  the shield wall `reach.md`'s design note invokes, Rally and Hold the
  Line, the into-melee penalty on shooting past a friend, and the whole
  question of whether the spellblade's flanking role is worth anything
  are all in the same position.
  What it would take is a second hero on the friendly side of `duel` --
  a pair against a foe worth two of them -- rather than a whole party
  simulator. That is enough to price "this helps the person beside me"
  against "this helps me", which is the comparison every one of those
  rules is asking for.
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
  bow.** Duels have distance and so do skirmishes -- one number per
  creature, an opening at the hero's own range, ground to give and
  ground to cross, the band answered out of the reaction, and a limit
  on how many bodies can stand where they can hit you. Builds open at
  spell range and can throw what they are holding. What is still
  missing is anything that shoots: `gear_options` sells melee weapons
  only, so no build buys a bow or a sling, and the crowd numbers are
  still the numbers a positionless model produced because the spells a
  caster actually picks against a crowd declare no range (see the rules
  gap above).
- **The simulator was thirteen minutes, then under three, and is
  now under two.**
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
  *Then parallelised, and it is now a hundred seconds.* A profile put
  56% of `--check` in gear shopping and 41% in duels, and both are
  piles of pieces that say nothing to each other, so both go to a pool
  of workers. Eight of them take `--check` from `4m36s` to `1m43s` on
  a sixteen-core machine; sixteen workers reach `1m36s`, which is why
  the default is eight rather than everything. `--jobs` sets it and
  `ICO_SIM_JOBS` sets it for a machine.
  The property to protect is that `--jobs` changes the speed and never
  a number, and `sim/README.md` carries the two-line diff that checks
  it. Shopping is safe for free, being arithmetic over the die's faces
  rather than rolls of it. Duels are Monte Carlo and are safe because
  each one now seeds itself from its own name rather than drawing from
  one stream in sequence -- which also retires the oldest wart in this
  file, that the ORDER of the duels was part of the answer and adding
  an archetype re-rolled every pairing after it. It cost a one-off
  renumbering when it landed: the count stayed at nine, but
  `L10 duellist vs berserker` left the failing set and
  `L1 berserker vs commander` joined it, both of them pairings sitting
  within a tenth of the three-round bound.
- **`best_difficulty` scans sixty difficulties and stops at none of
  them.** Expected cost looks monotonic in difficulty, and if it is,
  the scan can break rather than continue. That is an assumption about
  every future power as well as the present ones, so it wants deciding
  rather than assuming.
- **Four of the six Master signatures do nothing** in the model: Read
  the Blow, Command the Room, School Mastery, Granted Domain.
- **The Social discipline is unmeasured**, because nothing in the model
  represents a fight that talking could change.
