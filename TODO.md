# TODO

Parked work, roughly in the order it is likely to be picked up. Nothing
here is a commitment; it is a list of things known to be missing so that
they stop being rediscovered.

Finished work lives in [DONE.md](DONE.md), which is worth a look before
starting anything here: several of its entries record something that
was tried and measured and did not work, and those are the ones most
likely to be thought of again. An entry moves there only when nothing
about it is outstanding — one that was half done, however large the
half, stays here with the rest of it.

[balancing_notes.md](balancing_notes.md) is the third file, for a
question that has been measured hard but not decided. Read it before
reopening anything it covers: the numbers are expensive to produce and
the dead ends are the expensive part to rediscover.

## The spell list

The damaging spells are done: bolts, lances, and the three area families
(bursts, blasts, fields), across four damage types. What is missing:

- **Non-damaging crowd control and area denial.** *Done, as the wards:
  fog, darkness, briars, sleet, hallowed ground, silence.* What is still
  missing from the category is anything that blocks movement outright —
  a wall — and anything that keeps a named kind of creature out.
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
- **The game has no top, and the level clock has consumers past
  fifteen.** Nothing declares a level cap. `sim/balance.py` measures at
  1, 5, 10 and 15 and the prose talks about "level fifteen" as though
  it were the end, but that is habit rather than a rule, and
  `disciplines.levels_per_master` is `8` — a count, so a second Master
  arrives at sixteen. Something has to be decided, and the two answers
  are different games:
  - **Cap it.** Say sixteen or twenty in `advancement.md`, and the
    second Master is either the last thing you buy or unreachable.
    Cheap, honest, and it gives `experience.md`'s thresholds an end to
    aim at. It also makes the panel's top level the actual top level,
    which is what every gate currently assumes without saying so.
  - **Open it up.** Levels past fifteen need something to spend a
    budget on, and today they have less than nothing: about a fifth of
    a level 15 budget already buys nothing measurable — see
    [balancing_notes.md](balancing_notes.md). A sixteenth level under
    the present menu is mostly a ceiling raise and a power. Options
    worth measuring are a fourth discipline grade above Master, a
    second attribute track, or letting a Master grade open a second
    power pool — all of which are new material rather than a bigger
    number.
  Settle the economy first either way. Deciding the cap while a level
  at the top is worth a fifth less than it says decides it against a
  number that is known to be wrong.
- **Experience is drafted and threat is not in it yet.** `experience.md`
  awards points for milestones the adventure names, one experience point
  to one advancement point, with level derived from the career total.
  Threat is meant to become a fourth milestone -- an award keyed off a
  creature's `challenge_level` -- so that earning is a hybrid rather
  than either thing alone. It is deliberately not there yet: nothing has
  measured `challenge_level`, and the creature loader below is the
  prerequisite. When it lands, this should be one more entry in the
  award list and nothing else in the document should have to move. If it
  does have to move, the shape was wrong.
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
  axis has to come first**, and the weapon-block entry below is where
  the candidates for one are.
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
  in play. That is a pre-payment on the weapon-block entry below rather
  than a fix:
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

  **Then the caster was allowed to give ground, and the single-target
  gap entry -- now in `DONE.md` -- is mostly answered.** Holding the range rather than standing still
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

- **Constitution now also speeds recovery and shortens a wound**, on
  top of the free mastery hit points. Untested by the simulator in both
  cases: the breather and rest percentages move by only a few points and
  the day model cannot see the difference, and how long a character
  stays wounded is a between-session question the fight model has no
  view of at all. The arithmetic is what it is — a wound that keeps a
  constitution 10 character down for six nights keeps a constitution 18
  character down for two.
- **The advancement point economy is oversupplied.** *Measured at
  length; see [balancing_notes.md](balancing_notes.md), which supersedes
  what this entry used to say.* The short form: unspent points were the
  small half. Counting the reservoir bought past the point where it
  measurably stops paying, dead points run 7% of the budget at level 5,
  14% at level 10 and 20% at level 15. Every tracked skill is at its
  ceiling from level 5 onward, so points do not constrain the combat
  sheet at all. A supply cut to 13 or 14 a level and a reservoir cap
  near saturation both measure well; mastery hit points do not work as
  a sink and neither does raising prices. What is still open is the
  sink for what is left, and whether points should constrain combat at
  all.

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

- **A median over builds is only as good as the panel.** Adding three
  priests to test the armour grant took the median build's weapon
  spread from `0.180` to `0.238` and duly failed a gate calibrated at
  `0.20` -- with no rule changed. Three builds differing in one number
  are one build voting three times, and every panel-wide statistic
  reads that as three opinions. The two extra priests were moved out of
  `ARCHETYPES` into `ARMOUR_PANEL` for that reason and the figure went
  back to `0.180`.
  Worth knowing before adding an archetype for any other reason: the
  gates that take a spread or a median over the panel assume its builds
  are distinct, and nothing checks that they are.

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
- **`best_difficulty` scans sixty difficulties and stops at none of
  them.** Expected cost looks monotonic in difficulty, and if it is,
  the scan can break rather than continue. That is an assumption about
  every future power as well as the present ones, so it wants deciding
  rather than assuming.
- **Four of the six Master signatures do nothing** in the model: Read
  the Blow, Command the Room, School Mastery, Granted Domain.
- **The Social discipline is unmeasured**, because nothing in the model
  represents a fight that talking could change.
