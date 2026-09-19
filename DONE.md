# Done

Work that is finished, moved out of `TODO.md` so that the list of what
is left stays readable. Nothing here needs doing.

It is kept, rather than deleted with the commit that finished it,
because most of these entries are not announcements that something was
done — they are the reasoning that got there, the measurements taken on
the way, and in several cases a record of what was tried and did not
work. That last kind is the most valuable and the easiest to lose: an
idea that looks obvious will be had again by somebody, and the note
saying it was measured and found wanting is what stops it being built
twice.

Entries keep the headings they had in `TODO.md`, and an entry that
still has something outstanding stayed there rather than coming here,
however much of it was finished.

The **Now:** line an entry carried while it was in flight does not come
with it: that line was always about the present, and the present has
moved on. Whatever it held that is still worth having gets written into
the body of the entry before it moves.

## The spell list

- **Curing and restorative.** *Done: Mend, Cure Wounds, Cleanse,
  Restoration, and now Staunch.*

## Rules gaps found while doing the above

- **Reviving and raising the dead.** *Done, as Staunch and Raise the
  Dead.* Raise the Dead is the only spell in the game whose cost is not
  refunded by a night's sleep, and the only one with an explicit
  exemption from healing. If a second such spell is ever wanted, that
  exemption needs to become a general rule rather than a note on one
  entry.
- **Casting in Harness asked for Magical, and a war-priest had the
  same problem.** *Closed, by the third option -- the tidiest and the
  largest.* `discipline-list` now names a **casting discipline**: one
  whose skill group contains `spellcasting`, which is Magical and
  Spiritual. Nothing declares the membership separately, so a
  discipline given `spellcasting` becomes one by that fact and there is
  no second list to drift. The power asks for `[martial, casting]`.
  A god also grants its priests between `0` and `3` points of relief
  from armour on the casting roll, as part of its package alongside its
  domains -- so a war god's priest wears mail because of who they serve
  rather than because they trained for it, and the two stack for
  somebody who did both.
  Three things measured that are worth keeping.
  *The grant is monotonic but coarse.* At `0` the priest wears partial
  leather, at `2` studded leather, at `3` a chain shirt and later a
  breastplate. A grant of `1` is indistinguishable from none, because
  the relief is on the casting roll only and the dodge still pays, so
  one point of armour buys one point of dodge penalty and the chooser
  declines. The usable span is really `0`, `2`, `3`.
  *`4` would do nothing.* The heaviest armour a priest will take is a
  breastplate at `-3`, so `3` cancels it outright and a fourth point
  has nothing left to forgive.
  *It does not fix the level 1 skirmisher pairing, whatever it looked
  like at first.* Across the whole `0` to `3` span that duel moves from
  `2.988` rounds to `3.001` against a bound of `3.000` -- thirteen
  thousandths, with only the top of the span clearing, and by one
  thousandth. The gate now passes and should not be trusted to stay
  passing; what is actually short there is the skirmisher's level 1
  damage.
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
  shield erases the weapon's block value entirely. The weapon-block
  entry in `TODO.md` is no longer a nice-to-have.
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
  moved it was giving `contributions` one; see the caster entry in
  `TODO.md`.

## Simulator gaps

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

## The advancement point economy

**Status: measured, not decided.** Opened because `TODO.md` carried
"high level builds cannot spend their points — 8 to 38 spare at level
15". That turned out to be the small half of the problem.

### What is actually wrong

Three findings, in the order they change the picture.

**1. From level 5, points do not determine the combat sheet — ceilings
do.** Every tracked skill on every archetype sits exactly at its
ceiling at levels 5, 8, 10 and 15 (47 of 47 skill slots across the
panel). At level 1 it is 39 of 47. Mastery hit points and the power
source are at their ceilings too. So a character's combat capability is
a function of their level and their discipline choices, and the budget
is not a constraint on it at all.

This contradicts what `skills.md` says it is doing. Its design note
argues that specialisation is expressed in the *price* rather than the
ceiling — *"keeping pace everywhere costs them everything. The
trade-off is then a budget decision the player makes each level."*
Measured, there is no budget decision: the ceiling arrives first, for
the specialist and the generalist alike.

**2. The budget is calibrated, not loose.** Sweeping
`advancement.points_per_level`:

| points/level | drift |
|---|---|
| 15 | 1.04 |
| 12 | 1.18 |
| 10 | 1.53 |

Cutting it makes fights *longer*, because characters stop reaching
their skill ceilings and offence falls faster than defence. The current
15 is sized so that the most expensive build — the generalist, paying
two a rank everywhere — just reaches its ceilings.

**3. The surplus is the specialisation discount, refunded in a currency
with nothing to buy.** A specialist pays one a rank for the same
ceilings the generalist pays two for. Both arrive at the same sheet.
The difference comes back as spare points. At level 15 the generalist
ends with 5 unspent and the berserker with 38.

So the price difference produces no difference in the character. It
only produces change.

### The reservoir is the real waste, and it is three times the surplus

Unspent points were never the whole of it. Every build also empties its
leftovers into the power source, and that reservoir is inert well below
what it buys.

Expected offence against reservoir size at level 15:

```
berserker  10:16.79  20:18.24  30:24.43  40:25.53  60:27.02  80:27.02  151:27.02  300:27.02
paragon    10:16.75  20:19.15  30:27.83  40:28.23  60:31.36  80:31.36  151:31.36  300:31.36
evoker     10:12.75  20:13.60  30:17.85  40:17.85  60:17.85  80:17.85  151:17.85  300:17.85
```

Identical from 60 upward for a martial and from 30 upward for a caster.
Builds carry 147 to 153. The cause is structural:
`using-powers.max_cost_of_a_successful_power` is `10`, and the model
spends at most a quarter of the reservoir on one power, so above
roughly 40 to 60 there is nothing left to spend it on.

It is not a within-one-fight artefact. Across a whole adventuring day
(five encounters, breather recovery), a level 15 berserker holds 100%
of fresh offence at stamina 40, 60, 100 and 151 alike. Only at 25 does
it sag, to 0.68 by the last fight.

The sweep agrees from the other end. `max_power_source_bought_per_level`
at 3, 6 and 10 produces *identical* output — 2.3-9.8 rounds, spread
2.3, drift 1.04, 125 hp, 4 out of band at every setting. Not close:
the same numbers.

Dead points, counting both the unspent and the reservoir bought past
each build's own saturation point:

| level | dead in the reservoir | unspent | total | share of budget |
|---|---|---|---|---|
| 5 | 69 | 9 | 78 of 1100 | 7% |
| 10 | 215 | 44 | 259 of 1850 | 14% |
| 15 | 351 | 167 | 518 of 2600 | 20% |

Per build at level 15 — "enough" is the smallest reservoir giving
identical expected offence:

```
build           has  enough  src pts  needed   dead  unspent
berserker       151      45       45      10     35       38
commander       149      45       45      11     34        6
duellist        149      45       45      11     34       17
evoker          151      30       45       5     40        8
generalist      149      25       45       4     41        5
paragon         147      45       45      11     34       18
priest          153      35       45       6     39        8
sentinel        151      45       45      10     35       38
skirmisher      102      45       30      11     19        0
spellblade      147      25       45       5     40       29
```

Everybody buys 45 points of reservoir and needs 4 to 11.

`advancement.md` already says this in prose — *"a senior character
already has far more stamina or spirit than a fight can spend"* — and
the rules still sell it.

### Four changes proposed, and what they measured

Proposed: 10 points per level; one point buys one mastery hit point,
max two per level; one point buys two of a power source, max two per
level; `using-powers.base_cost` from 10 to 12.

Run as a ladder so each change could be seen on its own. Every row is
600 trials per duel over levels 1, 5, 10, 15.

| variant | drift | spread | hp | out of band | gates |
|---|---|---|---|---|---|
| A baseline | 1.04 | 2.3 | 125 | 4 | 3 |
| B change 1 only | 1.53 | 2.3 | 125 | 2 | 12 |
| C 1+2 | 1.67 | 3.1 | 139 | 5 | 16 |
| D 1+2+3 | 1.66 | 3.0 | 139 | 4 | 19 |
| E all four | 1.73 | 3.1 | 139 | 4 | 23 |
| F 1+3+4, no mastery change | 1.52 | 2.3 | 125 | 2 | 19 |
| G as E but mastery capped at 1/level | 1.59 | 2.9 | 125 | 4 | 25 |

**Why it fails: the cut starves the powers economy.** Nine of E's
twenty-three failures are one gate — *"keeps 86-92% of its damage with
an empty reservoir (band 35-85%)"*. Builds pass it from the wrong side:
an empty reservoir barely differs from a full one because the reservoir
is nearly empty either way. Reservoir at level 10, against a power
costing about 10 a round:

```
build        baseline   10 pts/level   full package
berserker         106             19             20
duellist          104             14             14
spellblade        102             12             14
```

One power a fight, then bare weapon. The rest follows — casters "can
neither land nor afford any field", and under E the spellblade takes
8.1 rounds and 67% of its hit points to clear six goblins, against a
target of four rounds and a quarter of them. Under F, which leaves
mastery hit points alone, the same build takes 11.9 rounds and 90%.

Change 1 does nearly all of it alone. Change 3 is inert next to it: D
is byte-identical to C, because change 1 has already zeroed reservoir
spending, so repricing it changes nothing still being bought.

### What worked

Same harness, aimed at the reservoir cap rather than its price, and at
a shallower supply cut.

| points/level | reservoir cap | drift | spread | out of band | gates | dead @L10 | dead @L15 |
|---|---|---|---|---|---|---|---|
| 15 (today) | 3 | 1.04 | 2.3 | 4 | 3 | 11% | 19% |
| 15 | 1 | 1.21 | 2.3 | 2 | 2 | 11% | 19% |
| 14 | 3 | 1.05 | 2.3 | 4 | 3 | 7% | 15% |
| 14 | 1 | 1.21 | 2.3 | 2 | 3 | 7% | 15% |
| 13 | 3 | 1.08 | 2.2 | 3 | 5 | 3% | 10% |
| **13** | **1** | 1.21 | 2.2 | **1** | 4 | 3% | 10% |
| 12 | 3 | 1.18 | 2.6 | 4 | 7 | 1% | 5% |
| 12 | 1 | 1.26 | 2.6 | 2 | 6 | 1% | 5% |

*(the dead-point columns here use one 45-point saturation threshold for
every build, so they compare with each other rather than with the
per-build table above, which is the more accurate one)*

**The knee is between 13 and 12.** At 12 the contribution spread reaches
2.6 and breaks its own gate at 2.5. 13 is the last defensible rung.

The best combination measured is **13 points a level with the reservoir
capped at 1 point a level**: one out-of-band measurement against
today's four, the tightest spread at 2.2, and dead points halved. It
costs one extra gate failure and 0.17 of drift.

**14 points a level costs nothing at all** — drift 1.05, the same three
failures as today — and still takes dead points from 19% to 15%. It
just does not buy much.

Two caveats on that recommendation, both softening it:

- The two failures that appear under any supply cut are the level 5
  spellblade field and the weapon-spread gate. Both look like existing
  softness that a tighter budget exposes rather than causes.
- The drift cost is overstated by a simulator bug — see below.

Capping the reservoir also removes the level 10 berserker-versus-paragon
failure, but for a reason that is not about the economy. All three
standing failures are *fights too short*; cutting the berserker's
stamina cuts its damage. That failure returns the moment the berserker
is fixed properly.

### Dead ends

Recorded so they are not built twice.

- **Mastery hit points as a sink for martial builds.** Does not work in
  any form tested. It buys hit points, hit points lengthen fights, and
  the drift and spread follow (hp 125 to 139, spread 2.3 to 3.1).
  Tightening its cap made it worse rather than better: variant G was
  the worst of the seven at 25 failures. Sweeping
  `max_mastery_hp_bought_per_level` alone gives drift 1.04 / 1.33 /
  2.01 at 1 / 3 / 6, with hit points 125 / 153 / 195. It also silently
  doubles the cost of the *starting* mastery reserve, because
  `character-creation.md` says further mastery hit points are "spent at
  the same prices" — at one hit point per point, the 25-point starting
  ceiling costs 25 of a 30-point pool, and skill ceilings reached at
  level 1 collapse from 39 of 47 to 9 of 47.
- **Raising `using-powers.base_cost`.** Too small, and it shrinks
  exactly where the problem grows: the best damage power costs +0.65
  stamina a round more at level 1 and +0.15 at level 15.
- **Raising prices generally.** Where a ceiling binds, a higher price
  buys the same ranks for more points — the same character, a smaller
  number. It only bites below level 5, which is the one place the game
  has already had to repair once.
- **Raising `skills.cap_per_level` from 1 to 2.** Absorbs the surplus
  completely at every level and takes drift from 1.04 to 1.10,
  re-inflating the curve the constitution work in `advancement.md`
  flattened.
- **Buying a third discipline.** Makes the surplus *worse*, because a
  grade cheapens the ranks you were already buying by more than the
  grade costs. Berserker at level 15 goes from 38 unspent to 44 with a
  third Initiate and 45 with an Adept. Only Master, at a 40-point
  spend, pulls it down — to 25.

### There is no spectrum to balance

Asked because the obvious repair to a dead sink is a *competing* sink:
make damage buyable so that hit points become worth buying, and let a
player sit anywhere between a tank and a striker. Before designing
that, it is worth knowing whether the choice exists at all today.

`sim/balance.py --spectrum` answers it. `build_character` takes an
`aggression` dial from 0 to 1 which splits the discretionary budget
between the attack skills and the power source at one end and mastery
hit points and the defensive skills at the other. It defaults to
`None`, which is the cascade this model has always used, so no existing
number moves — `--check` returns the same three failures at the same
round counts.

Contribution across the dial:

```
level 1                0%      25%      50%      75%     100%   spread
berserker              65       90       90       90       90    1.38x
sentinel               89      116      116      116      116    1.31x
generalist             53       70       57       57       57    1.32x
commander              84       97       97       97       97    1.15x

level 5      every build flat, except spellblade 139 -> 118
level 10     every build flat, except evoker and priest, both falling
level 15     every build identical to the point, 1.00x throughout
```

**The game has a real spectrum at level 1 and has lost it by level 5.**
At level 1 the budget is tight enough that emphasis matters, six of ten
builds do best at a quarter to offence, and the generalist is the shape
you would want everywhere — 53 at the defensive end, 70 in the middle,
57 at the aggressive end, so both ends are worse than the middle.

At level 15 the dial is not merely flat, it is inert: a berserker built
at 0 and at 1 is the *same character*, every rank, 109 mastery hit
points and 151 stamina both ways. The budget affords both ends at once,
so there is nothing to choose.

**Where the dial does move the sheet, the flatness is two dead ends and
not a balance.** At level 5 the berserker's fortitude runs 8 down to 1
across the dial and its reservoir 40 up to 61, and contribution does not
move at all. Testing each separately:

```
L5  fortitude   0 / 4 / 8 / 12   ->  182 / 182 / 182 / 182
L5  stamina    20 / 30 / 40 / 61 ->  156 / 182 / 182 / 182
L10 fortitude   0 / 4 / 8 / 12   ->  306 / 306 / 306 / 306
L10 stamina    20 / 30 / 40 / 61 ->  237 / 281 / 281 / 306
```

The marginal point at level 5 and beyond goes either to a skill worth
nothing or to a reservoir already past saturation. That is the same
finding as the dead points above, seen from the other side: it is not
that a character has points left over, it is that *the marginal point
buys nothing*.

One caveat on fortitude's zero. Contribution is
`(offence + control) x survival` against the standard foe, and
fortitude resists poison, disease and duress rather than blows. Its
score of nothing here is partly a limit of the measurement and not
proof that the skill is idle in play — but it does mean the defensive
end of this dial is thinner than it looks, because dodge and block fill
first and fortitude is what the marginal point actually reaches.

### K, put through the dial

K is 13 points a level with the power source capped at 1 point a level
— the combination that measured best on the gates. Run through the
spectrum, it does something the gate numbers gave no sign of.

Builds whose contribution moves at all across the dial, out of ten:

| level | today | K |
|---|---|---|
| 1 | 7 | 6 |
| 5 | 1 | **6** |
| 10 | 2 | **4** |
| 15 | 0 | **1** |

At level 5 the panel goes from one build with a live choice to six. The
generalist spreads 1.50x and the skirmisher 1.49x, where both were flat
before. At level 10 the skirmisher spreads 2.38x. At level 15 the
skirmisher is the only build that moves at all, and it is also the only
build with headroom left.

**Less headroom means the dial bites harder, not less.** That is worth
stating because it is easy to get backwards: cutting the budget and
cutting the ceilings both reduce headroom, and while headroom is still
positive that makes the choice *sharper*. It is only once headroom goes
negative that the dial dies. K reduces headroom everywhere, which
revives levels 5 and 10 and leaves 15 as dead as it was.

The cost is at level 1, where the budget is the chargen pool and does
not move, so all K does there is take two points off the reservoir's
ceiling. Spreads shrink a little and the skirmisher stops moving.

### Why every curve plateaus at a quarter

Almost every row that moves has the same shape: it rises from 0% to 25%
and then goes flat. That is not a property of the game, it is the shape
of the two lists. For a berserker at level 15 under K:

```
to place 192    offence 33    defence 74    spot 45    capacity 152
```

A quarter of 192 is 48, which already overfills an offence side worth
33. Everything above 25% spills back to the other end and changes
nothing.

**The offence side is the shallow one.** It is one attack skill's ranks
plus the reservoir, and the reservoir is the shallowest thing in the
game. That is the single number a competing-sink design has to move: not
the balance between the ends, but the depth of the offensive one.

`sim/balance.py --headroom` reports this and takes about a twentieth of
a second, because it needs no duels and no shopping. Run it before the
sweep rather than after: it says whether there is a choice to measure,
and the sweep only says how the choice came out.

### The party as the unit, and what it says so far

**Status: engine built and measured. Enough diagnostics to start
rebalancing on; the assumptions are named as they arise and three of
them have already been wrong.**

Three of the four roles worth designing for are invisible to a solo
metric: `(offence + control) x survival` scores tanking as a longer
fight, gives support nobody to support, and has no varied context for
flexibility. `sim/model.py` now has `party_encounter`, N heroes against
a crowd, and `balance.py --party` scores each build into each slot of a
reference party.

The measure is marginal, because a support build scores nothing alone:
what the party gets through with this build in a slot, minus what it
gets through with somebody else there. Two somebodies, answering two
questions -- a replacement-level stand-in (is this build worth having?)
and the purpose-built role-holder (what is it FOR?).

#### What 280 trials says at level 5

**Measured before the front rank closed, so the table below is void and
kept only as the record of what the geometry was worth.** See "the
assumption that was wrong" underneath it.

Noise floor 0.10. The intact reference party clears 3.52 of 5.

| role-holder | worth over a stand-in | after the line closes |
|---|---|---|
| striker | +0.61 | +0.64 |
| line | +0.32 | **+0.70** |
| caster | +0.21 | +0.36 |
| healer | +0.16 | **+0.39** |

```
against the role-holders     line   striker    caster    healer   spread
berserker                   +0.29     +0.19     +0.43     +0.37    0.24
priest                      +0.23     +0.00     +0.12     +0.22    0.23
paragon                     +0.22     +0.10     +0.37     +0.38    0.28
skirmisher                  -0.01     -0.18     -0.24     -0.25    0.23
commander                   -0.04     -0.29     -0.45     -0.48    0.44
evoker                      -0.38     -0.57     +0.10     +0.15    0.72
generalist                  -0.44     -0.83     -0.73     -0.58    0.39
```

**Healing is not specialised**, and that part does not depend on any of
the numbers above. `mend` is a minor spell any caster can take, and the
spread of healing across every caster in the panel is 6.0 to 7.0 hit
points a round -- arithmetic over the d20's faces, with no sampling in
it, so no number of trials and no change of geometry will move it. The
Spiritual discipline and the healing domain buy essentially nothing over
any caster with a minor cure.

What that is NOT evidence for, and was briefly claimed to be, is that a
healer is worth little to a party. The pre-closing table had the healer
at a quarter of a striker's worth; with the line closing it is +0.39
against the striker's +0.64, level with the caster. The healer looked
worthless in fights that were too easy because nobody needed healing,
which is a fact about the engine and not about the rules.

The test that actually asks whether a healer role exists is the healer
against **another caster** in the healer's slot, not against a
replacement-level stand-in: +0.39 over a stand-in includes everything
that is worth having about being a caster at all. Pre-closing, the
evoker -- a pure damage caster -- scored +0.15 in the healer's slot,
meaning it filled that slot BETTER than the purpose-built healer. That
is the direct evidence, it needs re-measuring under the corrected
geometry, and it is the number to look at first.

**Three builds beat every specialist in every slot** -- berserker,
paragon, priest -- and all three are flat, spreads 0.23 to 0.28. The
best builds in the game are generalists who outperform specialists at
the specialists' own jobs. That is the party-level form of everything
above: when a budget can max every ceiling, being good at one thing buys
nothing. Only the evoker is genuinely specialised, spread 0.72.

#### The assumption that was wrong, and what fixing it cost

*Fixed: the front rank now walks in. Everything above it measured
before that, and the whole build-by-slot table wants re-running.*

The party opened at its longest acting range, which is the casters', and
nobody closed. At level 5 against goblins that is 10 squares against a
mook move of 4: **three rounds of a 5.6-round fight in which the two
casters shoot and the two melee heroes cannot reach anything.** The
line-holder acts in 22% of rounds and the striker in 46%.

So the engine *overstated* casting rather than understating it, which is
the opposite of what the first reading of the caster column suggested.

Closing the line costs the party a great deal: the intact reference
party falls from 3.52 encounters to 2.77, because it engages sooner and
loses the volley. Harder fights make everybody in a slot matter more, so
every role-holder is worth more than it was and the ordering changes --
the line-holder goes from third to first. The lesson is more general
than the fix: **a geometry that makes fights easy compresses every
difference between builds**, and this report had been measuring a party
three rounds' grace away from the fight it was supposed to be in.

What closing does not fix is the line-holder's own participation, which
stays at about 21% of rounds. Its idle rounds were never mostly the
approach: it stands at the front and dies in 41% of encounters, and
closing sooner means being hit sooner.

Three more assumptions are in `party_encounter`'s docstring and all
three are load-bearing: the party holds a line and the back rank is
reached only once the front falls; a mook hits whoever it is likeliest
to hurt; the triage rule for when to heal.

#### Reactions, Guard, and the table as it now stands

*Everything above this line was measured before the model played
reactions at all. Both tables above are superseded and are kept only as
the record of what each fix was worth.*

Four things landed after the geometry fix, each of them moving the
table. Two were corrections to the model, one implemented rules it had
never played, and one was a rule change.

**1. Mook targeting was backwards.** It picked the lowest targeting
difficulty, and the code called that "whoever it is likeliest to hurt"
and the conservative choice. Armour in these rules *lowers* targeting
difficulty and pays back in reduction, so that rule means "hit the one
in plate" — the single target a competent enemy would leave alone. The
tank was taking 2.82 a blow and the casters 3.79, and the tank was
drawing every one of them. It also handed a defensive build its whole
job for free: it protected the party by wearing armour rather than by
doing anything. Targeting now goes by expected damage.

**2. The reference line-holder was a worse build than the panel's own
sentinel** — `strength` 14 against 16, 158 contribution against 186.
Two attribute points were the entire gap. An awareness grade and a
martial grade were each tried and left *every number identical*,
because the block skill is already at its ceiling and already focused.
The only lever that moved anything was the one track the per-level
ceilings do not touch, which is the advancement-economy finding above
arriving from a third direction.

**3. The reaction economy.** `turn-order.md` gives everybody one
reaction a round and its design note says that is what makes Riposte,
Deflect and Guard choices rather than free extras. The model had only
ever spent it on reach, and its own assumption list admitted the cost:
with the two powers it competes with unimplemented, the reach answer
was free. All three now compete for the one reaction in the party path.
Over a whole run they fire at roughly 8.3 Ripostes, 2.4 reach answers
and 1.1 Deflects per trial, and the party gains **+0.31 encounters** —
the size of the hole the model had.

**4. Guard costs the reaction.** `turn-order.md` had always claimed it
did; Guard's own entry never said so, so the rule the design note
described was written nowhere a player or a program could find it.
`costs_the_reaction` is now on Guard, Riposte, Deflect and Anticipate,
the simulator reads it the way `opens_for` reads discipline and grade,
and `reaction_kit` lists the reactions a build holds that it cannot
price rather than dropping them from the score. MINOR when a release is
next cut: four names added, no value moved.

Guard itself is worth about +0.2 to the party and about +0.2 to the
line-holder's worth. At 120 trials that is two standard deviations —
suggestive, not settled.

##### The triage rule outweighed the mechanic

This is the expensive lesson of the entry. The first Guard run gave
line +1.41 and striker +0.89, which would have been the most decisive
thing ever measured here. It was an artefact of the triage test: it
asked whether the guardian could survive **one blow** before committing
to a round of them, so a hurt guardian would step in front of six. The
party it wrecked worst was the one with a replacement-level body in the
line, and because every worth in the table is a difference against that
party, crippling it inflated the line-holder's worth.

Changing the test to "survive the round you are committing to" — one
line — moved the headline by **0.55, about five times the noise**,
while Guard itself moves it by 0.2, about two. *The modelling choice
around the mechanic outweighed the mechanic by more than double.*
Before any number in this section is quoted, that is the thing to
remember about all of them.

##### The back rank was the best place to tank from

Guard let anybody cover anybody, and the line assumption made the back
rank unreachable. Together they handed a melee build in a back-rank
slot both halves of the deal: untargetable, and still free to volunteer
for blows. Measured against banning cross-rank guarding outright, same
seeds:

| party | as built | cross-rank banned | artefact |
|---|---|---|---|
| skirmisher in caster | 3.83 | 3.01 | +0.82 |
| paragon in caster | 4.23 | 3.63 | +0.61 |
| sentinel in healer | 3.67 | 3.19 | +0.48 |
| paragon in healer | 4.22 | 4.06 | +0.16 |
| healer in healer | 3.31 | 3.31 | +0.00 |
| paragon in line | 3.17 | 3.17 | +0.00 |

Both controls sit at exactly zero — the reference healer has no martial
discipline and so no Guard, and the paragon in the line is already in
the front rank. The evoker, the one build in the panel with no martial
discipline at all, was likewise the one whose back-rank columns did not
move between tables while commander, duellist, sentinel and skirmisher
swung between 0.4 and 0.9.

The fix is not the ban. Guard says you *place yourself* between an ally
and what is coming, so covering the rank in front puts you in it for
the round: reachable like anybody else standing there, and no longer
treating that rank as cover for your own weapon. The corrected parties
land between the two columns, which is what that should look like.

##### The table, at 120 trials

Noise floor: one estimate 0.05, a difference 0.08. Nothing below about
0.15 is a real difference. The intact reference party clears 3.39 of 5.

| role-holder | before reactions | + reactions | + Guard |
|---|---|---|---|
| line | +0.76 | +0.64 | **+0.93** |
| striker | +0.42 | +0.36 | +0.60 |
| caster | +0.22 | +0.08 | +0.28 |
| healer | +0.24 | +0.17 | **+0.03** |
| *intact party* | *2.83* | *3.14* | *3.39* |

```
against the role-holders     line   striker    caster    healer   spread
berserker                   +0.75     +0.15     +0.58     +0.69     0.60
priest                      +0.23     +0.01     +0.08     +0.15     0.22
paragon                     -0.34     +0.09     +0.39     +0.53     0.87
skirmisher                  -0.15     +0.05     +0.37     +0.43     0.58
sentinel                    -0.22     -0.07     +0.18     +0.22     0.44
duellist                    -0.28     -0.07     +0.09     +0.15     0.42
commander                   -0.24     +0.01     +0.06     +0.13     0.37
spellblade                  -0.20     -0.31     -0.18     -0.15     0.16
evoker                      -1.18     -0.31     -0.04     +0.05     1.24
generalist                  -1.15     -0.96     -0.54     -0.44     0.70
```

##### What the table says that the design should hear

**Making the model more faithful made the builds more alike.** Mean
spread in the table above, across the three runs: 0.699 before
reactions, 0.661 with the artefact in, **0.560** corrected. Down a
fifth, and the wrong way for a design whose goal is competing sinks.

The reason is legible in the mechanics. **Guard is martial *initiate*.**
Nine of the ten panel builds have it, and so does the replacement-level
stand-in. A power everybody owns cannot distinguish anybody; it raises
the floor. If Guard is meant to make tanking a *role*, it is at the
wrong grade — and that is the same shape as the two findings above,
where ceilings bound everything a point could buy and only an uncapped
attribute moved anything.

**The reference healer is worth +0.03 — nothing at all.** This is not
the back-rank artefact; the stand-in in that chair never guards,
because the survive-the-round rule rejects a guardian that soft. It is
a real consequence of the reaction economy: Guard, Riposte and Deflect
prevent or repay damage as it happens, and healing it back afterwards
is the worse deal. Support-as-healing has been outcompeted by
support-as-interposition. It also means eight of ten builds name
"healer" as their best slot for no reason except that the healer
reference is the weakest thing to beat, so the `best` column currently
measures reference quality and not build role.

**The paragon has gone flat**: +0.59, +0.69, +0.66, +0.56 against
stand-ins, spread 0.13 — the flattest row measured here. Good
everywhere, which is the "high and flat" failure the report's own
docstring names.

**Commander and duellist remain identical** across four tables and all
eight cells. Their combat sheets differ in one skill their shared
stance never reads. `rally` and `hold_the_line` are still unpriced, so
the commander still pays five points for nothing — and the excuse the
code carried for that ("there are no allies") expired when the party
engine arrived.

##### Two things found and deliberately not changed

- **The two paths read `reach.md` differently.** It answers an opponent
  "standing in your band" who then moves towards you, so the swing
  lands as they *arrive* inside the short weapon's reach. The party
  path does that; `_crowd_advance` in the solo path answers *entry* to
  the band instead. They agree whenever a mook covers the whole band in
  one move, which is most of the time. Changing the solo path moves
  every duel number and every gate with them, so it is recorded here
  rather than done.
- **There is no polearm.** `turn-order.md` pictures "a fighter holding
  a polearm choosing between their reach and their Riposte every round
  of the fight". The only reach-2 weapons are `great_axe`, `staff` and
  `two_handed_sword`, all two-handed, so that fighter cannot exist and
  a shield user never faces the choice at all. The reference
  line-holder carries a sword, reach 1 — the shortest weapon in its own
  party — and so has no band to defend.

#### The baseline the rebalancing starts from

*Two changes land here, and they landed in the same run, so nothing
below is cleanly attributable to either until the control run named at
the end says otherwise.*

**Guard moved from Initiate to Adept.** At Initiate nine of the ten
panel builds had it and so did the replacement-level stand-in that every
worth in the table is a difference against. At Adept six have it and the
stand-in does not. Guard now sits at exactly Riposte's grade, which is
where the two things one reaction must choose between belong.

**The free mastery hit point now arrives with the level that grants
it.** `advancement.md` lists it under *what a level gives*, beside the
points; the points arrived as `chargen + (level - 1) x per_level` and
the hit points multiplied by `level`. So a first-level character
collected a level's grant it had not gained, and every character after
it carried one extra level's worth for ever — 2 to 4 hit points, all of
it the constitution bonus, which is up to a tenth of a level 1 build.

Every archetype now starts at exactly 35 mastery hit points: the free
ten plus the twenty-five buy cap, with constitution no longer reaching
level one at all.

The free ten themselves were never in question. `char.mhp = free_mhp +
bought_mhp`, nothing is deducted for them, and `character-creation.md`
says nobody pays for them. That was checked on a live build before
anything was touched.

##### The level 1 calibration was made against hit points that were not there

Gates, read as numbers and not as a count — three failures became four:

| pairing | before | after |
|---|---|---|
| L1 berserker vs skirmisher | 2.9 | 2.9 |
| **L1 skirmisher vs priest** | **passing** | **2.6 FAIL** |
| L5 berserker vs spellblade | 2.3 | 2.3 |
| L10 berserker vs paragon | 2.8 | 2.7 |

The three that already failed did not move. The new one is not a
knife-edge pairing tipping over: this file's own guidance records the
level 1 priest duel as passing by a thousandth of a round, and it is now
2.6 — it fell by four tenths.

That is the finding rather than the damage. `character-creation.md`'s
design note records first-level fights being measurably too short, a
third of pairings under the floor, and the free ten as the fix. **That
calibration was made against a level 1 character holding three hit
points the rules never gave it.** The lever the note already names is
`max_starting_mastery_hp`, and the note also says what raising it costs:
it raises the price of surviving and the bill lands on whoever has least
to spare — a level 1 wizard paying in power source.

##### The table, at 60 trials

Noise: one estimate 0.08, a difference 0.11. Nothing below about 0.21 is
a real difference. Intact reference party 3.21 of 5.

| role-holder | Guard initiate, no mhp fix | this baseline |
|---|---|---|
| line | +0.93 | +0.83 |
| striker | +0.60 | +0.46 |
| caster | +0.28 | +0.14 |
| healer | +0.03 | **+0.00** |
| *intact party* | *3.39* | *3.21* |

```
against the role-holders     line   striker    caster    healer   spread
berserker                   +0.84     +0.20     +0.72     +0.70     0.64
priest                      +0.41     +0.04     -0.07     +0.13     0.47
spellblade                  +0.07     -0.21     -0.10     -0.25     0.31
sentinel                    -0.08     -0.08     +0.04     +0.12     0.21
duellist                    -0.13     +0.01     +0.05     +0.14     0.27
commander                   -0.18     +0.11     +0.03     +0.14     0.32
paragon                     -0.25     +0.16     +0.55     +0.72     0.97
skirmisher                  -0.30     -0.03     -0.30     -0.29     0.27
generalist                  -1.01     -0.76     -0.69     -0.49     0.52
evoker                      -1.24     -0.27     +0.00     +0.11     1.35
```

##### There is no healer role

The party clears 3.21 with the purpose-built healer in the chair and
3.21 with a replacement-level body in it. Not "small": zero.

This is not the back-rank guarding artefact — the stand-in never guards,
because the survive-the-round rule rejects a guardian that soft. It is
the reaction economy doing what healing used to: Guard, Riposte and
Deflect prevent or repay damage as it happens, and healing it back
afterwards is the worse trade. Support-as-healing has been outcompeted
by support-as-interposition, and the arithmetic finding above — `mend`
available to every caster at 6.0 to 7.0 hit points a round — says the
Spiritual discipline was never buying much of it anyway.

It also means the `best` column is unreadable. Seven builds name
"healer" for no reason except that the healer reference is the weakest
thing to beat.

##### Moving Guard did not restore differentiation

Mean spread in the table above, across the runs:

| | mean spread |
|---|---|
| before reactions | 0.699 |
| Guard at Initiate | 0.560 |
| Guard at Adept | 0.533 |

No improvement, and the comparison flatters the last row: spread is a
*range* across four noisy cells, so noise biases it upward, and this run
has more noise (60 trials) than the one above it (120). A real fall
would show up damped.

So **the diagnosis was incomplete.** "A power everybody owns cannot
differentiate anybody" is true, and removing Guard from four builds and
from the stand-in did not restore the spread, so Guard's grade was not
what was holding it down. Whatever is flattening these builds is
upstream of any one power.

The one clear response to the grade change: **the skirmisher lost Guard
and collapsed in the back-rank slots**, caster +0.37 to -0.30 and healer
+0.43 to -0.29, both far past the threshold. A build that had been
earning its keep by back-rank tanking cannot any more.

##### What still stands, five tables in

- **The berserker is the best tank in the game.** +0.84 over the
  purpose-built line-holder and +1.67 over a stand-in there, its own
  best slot. A dodge-stance 18-strength damage build beats the defensive
  specialist at defence. Nothing currently expresses a tank role.
- **The evoker is the only genuine specialist**, spread 1.35, and the
  only build for which position matters: -1.24 in the line and actually
  worse than a replacement body there. That is the shape the design
  wants, and one build in ten has it.
- **The paragon is flat**: +0.58, +0.62, +0.69, +0.73 against stand-ins,
  spread 0.15. Good everywhere, for nothing.
- **Commander and duellist have separated at last** — by 0.05 and 0.10,
  under the 0.21 threshold, so still unresolved after five tables.
  `rally` and `hold_the_line` remain unpriced.

##### The control run: Guard's grade moves exactly one build

Guard's grade and the mastery hit point fix were confounded in
everything above, so the grade was run on its own: same seed, same
trials, same fix, Guard back at Initiate, built as a separate ruleset so
that one value is the only difference.

**Nine of the ten rows came back bit-identical**, and so did the intact
party and all four stand-in baselines. One row moved:

| skirmisher | line | striker | caster | healer | spread |
|---|---|---|---|---|---|
| Guard at Initiate | -0.16 | +0.09 | **+0.50** | **+0.37** | 0.67 |
| Guard at Adept | -0.30 | -0.03 | **-0.30** | **-0.29** | 0.27 |

So the whole effect of the grade is one build, and the direction is
against the change. Mean spread, now measured at matched noise:

| | mean spread |
|---|---|
| Guard at Initiate | 0.573 |
| Guard at Adept | 0.534 |

Moving Guard to Adept *reduced* differentiation. The earlier 0.560
against 0.533 was the confounded pair and understated it.

**Almost nobody uses Guard.** Nine builds had it at Initiate and only
one behaved differently without it, so generalist, priest and the
stand-in were carrying a power they never declared. The triage rule is
why: a guardian must be tough enough to survive the round it commits to
*and* be standing beside somebody softer, and most builds are never
both. The reference line-holder and striker are Adept either way, which
is why the reference party did not move at all.

And the one build that did use it was using it for something the design
wants. Since a guardian joins the rank it covers, a skirmisher in a
back-rank slot steps up, tanks, and pays the exposure — a mobile
high-dodge build with a real reason to be somewhere. Spread 0.67, best
slot the caster's. Moving Guard to Adept deleted the only role Guard was
creating.

The diagnosis that prompted the move — *a power everybody owns cannot
differentiate anybody* — was the wrong half of the problem. The trouble
is not that everybody owns Guard; it is that almost nobody can use it.
Raising the grade addressed ownership and left use untouched.

#### What the numbers cost

One estimate at 24 trials carries a standard deviation of 0.12, so a
difference carries 0.17 and nothing below about 0.35 is resolved. 280
trials brings that to 0.10 and takes 117 minutes across twelve workers.
Two separate claims were made from single 24-trial estimates -- +0.48
and +0.06 for the same quantity, whose true value is +0.25 -- before
anybody measured the variance. Measure the variance first.

#### Still to do here

- **Match the references for quality.** This has gone from a footnote
  to the dominant effect: the healer reference is worth +0.03 and the
  line-holder +0.93, so the `best` column is reading which reference is
  weakest and calling it a build's role. Nothing in the first table
  means much until the four are level.
- **Price the ally buffs.** `rally`, `hold_the_line` and
  `call_the_shot` all carry an ally bonus and none is called, which is
  why commander and duellist keep measuring as the same build.
  `blessing_spells` is likewise uncalled, so support is still measured
  as healing and interposition only.
- **Let the crowd play around the guard.** A mook picks by expected
  damage and the blow is redirected afterwards, which is what the power
  says happens — but an enemy that picked the best *unguarded* target
  would take much of Guard's value back. This is also what would make
  `extra_allies_per_step` worth anything: while the crowd concentrates
  every blow on one target, a second ally under the same shield insures
  against something that does not happen, so Guard is measured at base
  difficulty only.
- **Re-measure the evoker in the healer's slot** — a pure damage caster
  against the purpose-built healer is the direct test of whether a
  healer role exists, and it is now +0.05, which is to say there is not
  one.
- **Guard's grade: measured, and Adept is the worse of the two.** It
  moves exactly one build, costs that build the only role Guard was
  creating, and lowers mean spread from 0.573 to 0.534. The open
  question is not the grade but why nine builds hold a power only one of
  them ever declares — which is a question about the triage rule and
  about what Guard asks of a guardian, not about what it costs to buy.
- **Re-calibrate level 1 hit points.** The free ten were sized against
  a character holding three more than the rules gave it, and with that
  corrected a second level 1 duel falls under the three-round floor.
  `max_starting_mastery_hp` is the lever `character-creation.md` names.

### Making power damage carry the scaling

**Status: measured, not decided.** Opened because plain damage does not
scale at all and something has to.

### The finding underneath everything else here

A duel's plain swings are flat across fifteen levels. Attack skill and
targeting difficulty rise together, so the margin a blow lands with does
not grow: measured, the margin contributes **4.8 damage at level 1, at
level 5 and at level 15**, and the whole of a plain swing goes from 7.4
to 7.7 over fourteen levels. Every point of damage progression in this
game comes from powers.

That makes the power curve the single lever that decides whether a
high-level fight takes as long as a low-level one, and it is why
`margin_to_damage_fraction` is not the lever it looks like: it scales
every level by the same factor and moves no ratio at all.

### What the scaling has to be

For fights to hold their length, total damage must grow as total hit
points do. Plain damage is flat and core hit points are flat, so the
whole of both curves lands on the power term:

| level | total hp | plain | power now | power needs |
|---|---|---|---|---|
| 1 | 31 | 7.4 | 2.3 | 2.3 |
| 5 | 51 | 7.2 | 6.8 | 8.9 |
| 10 | 76 | 7.7 | 8.5 | 16.2 |
| 15 | 101 | 7.7 | 11.1 | 24.1 |

**10.5x, not 4.5x.** Worth stating plainly because the obvious target --
*make power damage scale like mastery hit points* -- is already true:
power damage grows 4.8x against mastery's 4.5x, and fights still stretch
from 3.2 rounds to 5.4. Matching mastery does not pay for the flat
terms.

### Why no linear knob can do it

Damage is `steps x damage_per_step` and steps grow linearly with skill.
Every knob on that expression is a *multiplier*: doubling what a step is
worth doubles first level and fifteenth alike, so the ratio between them
never moves however hard anything is turned. Measured against the
stamina budget, the linear form delivers 3.4x against the 10.5x wanted.
A ratio only moves if the shape changes.

### The quadratic, measured

`damage = steps^2 / divisor` -- steps buy a *pitch* and the damage is the
pitch squared. Implemented behind one optional mechanic,
`using-powers.damage_pitch_divisor`, so dropping the key restores linear
exactly.

It does what it was built for. Power damage grows **14.1x** (2.3 to
32.5) and duel length goes from 3.2/3.7/4.7/5.4 rounds to
**3.2/3.1/3.0/2.6**. It is self-limiting without a cap, because expected
damage is the curve times the chance of making the roll, so pushing
further multiplies a bigger number by a smaller chance and the product
peaks at a finite difficulty that rises with skill. And it delivers the
two regimes a high-level character wants for free: at level 15 a 3-step
use is worth 2.25 damage and costs 4.4 (about ten a day), a 13-step use
is worth 27.5 and costs 10 (about four a day).

### What it costs, and why it was not adopted

Nine gate failures, and five are the same one. **Powers end up carrying
85% of a level 15 character's damage**, so an empty reservoir leaves it
a quarter of its output against a band that wants 35 to 85%.

| divisor | L1 dmg/kept/rnds | L5 | L10 | L15 |
|---|---|---|---|---|
| /4 | 9.8 / 86% / 3.2 | 16.3 / 56% / 3.1 | 25.3 / 30% / 3.0 | 38.3 / 22% / 2.6 |
| /6 | 9.8 / 86% / 3.2 | 14.0 / 66% / 3.7 | 18.8 / 52% / 4.0 | 25.8 / 33% / 3.9 |
| /9 | 9.8 / 86% / 3.2 | 14.0 / 66% / 3.7 | 16.4 / 67% / 4.6 | 20.7 / 59% / 4.9 |
| /12 | 9.8 / 86% / 3.2 | 14.0 / 66% / 3.7 | 16.1 / 68% / 4.7 | 18.1 / 67% / 5.6 |

The flatter the fight-length curve, the more of a character's damage
lives in its reservoir. That is not a defect of the quadratic; it is
what *"powers carry all the scaling"* means once plain damage is flat,
and any design that puts the whole curve on powers meets it.

Two side effects, both real:

- **Accuracy becomes paramount.** Squaring the payoff puts far more
  behind the hit roll, so whoever rolls highest compounds. The
  contribution spread blew out to 3.0x with the skirmisher on top, and
  the berserker abandoned its great axe for a *staff* at level 10 --
  under a quadratic the axe's `-2` unwieldy penalty costs more than its
  `+4` damage gains, because the roll now gates a much larger prize.
  The weapon-spread gate failed at 40%.
- **It is harder arithmetic at a table.** Players find a linear step
  count easier than a squared one, and this is used on every attack.

Neither is fatal. Both are the reason a design that reaches the same
place with two linear terms is worth trying first -- see the entry
below. The implementation is kept: `step_damage` is one function behind
one optional key, so this can be re-measured at any divisor by adding
the key back.

### The multiplicative alternative, measured

Two linear terms that multiply reach the same place as one curved one,
with arithmetic a table can do. **How hard** a power is pushed stays
linear in the steps declared; **how often** it can be thrown becomes the
second term. Their product is the scaling.

#### Why the second lever was dead

It was not dormant, it was *coupled to the first*. The minimum a power
can cost is `difficulty // minimum_cost_divisor` -- a fraction of how
hard you pushed -- so a character whose skill has doubled declares a
harder version of the same power and pays a proportionally larger
minimum. Measured across fifteen levels, cost per use rises 4.4 to 8.1
while the pool rises 18 to 46, and the two very nearly cancel:

| level | pool | cost | uses a day | rounds powered | steps |
|---|---|---|---|---|---|
| 1 | 18 | 4.4 | 4.1 | 20% | 3 |
| 5 | 26 | 5.0 | 5.1 | 26% | 5 |
| 10 | 36 | 6.5 | 5.5 | 28% | 8 |
| 15 | 46 | 8.1 | 5.6 | 28% | 10 |

**Effect 3.3x times frequency 1.4x is 4.6x**, against the 10.5x wanted.
Pushing effect up raises cost, which cuts frequency: the two levers were
fighting each other through the difficulty declaration.

#### Decoupling them

`using-powers.minimum_cost_flat`, optional, replaces the fraction with a
number that does not know the difficulty at all. Then pool growth
reaches the player as uses. Implemented as one function, `minimum_cost`,
which every one of the model's fifteen floor sites now goes through;
without the key it is the divisor exactly as before.

| combination | L1 | L5 | L10 | L15 | product |
|---|---|---|---|---|---|
| as now | 3st/20%/c4.4 | 5st/26%/c5.0 | 8st/28%/c6.5 | 10st/28%/c8.1 | 4.6x |
| flat 2, pool 4, base 12 | 4st/22%/c4.6 | 5st/39%/c4.6 | 8st/61%/c4.6 | 10st/83%/c4.6 | **9.5x** |

Effect 2.5x times frequency 3.8x. The higher `base_cost` is what holds
level 1 to a fifth of its rounds while the pool carries level 15 to four
fifths -- few uses early, many late, which is what was wanted.

#### It does not hit the quadratic's wall

This is the result that separates the two designs. Damage kept with an
empty reservoir runs **62% to 66% at every level**, comfortably inside
the 35-85% band, where the quadratic put five builds at 22-31%. Keeping
the effect linear keeps plain swings a real share of output. Four gate
failures against the quadratic's nine, and both reservoir failures are
single builds one or six points outside the band rather than a
collapse.

#### What it breaks, and what that says about the ladder

> **Corrected.** Most of this subsection turned out to be an artefact of
> the crowd planner scoring whole kills — see *The simulator fault that
> nearly became the headline* below. Re-measured with that fixed, the
> day does not fall apart: the same design clears `3.29` at level 5 and
> `4.26` at level 10 rather than `1.15` and `1.91`. The creature
> asymmetry is also smaller than it reads here, because the two columns
> compared were not carrying the same reservoir knobs. The numbers below
> are left as they were taken; *Re-measuring the multiplicative design
> on the ladder* is the one to read.

The party day falls apart in the middle:

| level | fight length | cleared of 5 |
|---|---|---|
| 1 | 4.1 | 2.75 |
| 5 | 10.8 | **1.15** |
| 10 | 10.7 | **1.91** |
| 15 | 8.9 | 3.30 |

Not because characters got weaker. **A flat minimum is worth far more to
a creature than to a character**, because creatures declare high
difficulties out of small pools and were the ones the proportional floor
was pricing out:

| who | pool | cost d/3 -> flat | uses a day | gain |
|---|---|---|---|---|
| hobgoblin | 20 | 4.4 -> 4.6 | 4.5 -> 4.3 | 1.0x |
| gnoll | 34 | 8.1 -> 4.6 | 4.2 -> 7.4 | 1.8x |
| hill giant | 48 | 9.1 -> 4.6 | 5.3 -> 10.4 | 2.0x |
| striker L5 | 32 | 5.8 -> 4.6 | 5.6 -> 7.0 | 1.2x |
| striker L10 | 52 | 5.5 -> 4.2 | 9.5 -> 12.4 | 1.3x |

The gnoll and the giant double their power uses while the party gains a
fifth. Levels 5 and 10 collapsed because the day is made of those.

Two things a rework of powers into a ladder of difficulties would have
to settle, both visible in these numbers:

- **The difficulty range is too narrow to carry two levers.** Steps run
  only 4 to 10 across fifteen levels, most of that capped by what a roll
  can reach, so effect manages 2.5x and frequency is left doing 3.8x of
  the work. A wider ladder -- more rungs, further apart, with real
  differences of effect between them -- is what would let the first
  lever pull its weight.
- **Frequency saturates and cannot be pushed past it.** Nobody powers
  more than every round, so the whole lever is `1 / (level 1
  frequency)`. Holding level 1 *down* is what makes the design work,
  which is a happy accident of wanting that anyway.
- **Creatures need their own rung.** Built from the same parts but with
  pools a fraction of a character's, they take any change to the cost
  rule disproportionately. Either their power budgets scale with threat,
  or the cost rule needs a term that knows how large a reservoir it is
  spending from.

#### Where the three designs stand

| | scaling | arithmetic | weight on the hit roll | reservoir dependence |
|---|---|---|---|---|
| linear | 4.6x | easiest | normal | fine |
| multiplicative | 9.5x | linear | normal | fine, 62-66% kept |
| quadratic | 14.1x | squared | extreme | fails, 22-31% kept |

Both alternatives are one optional mechanic away from the committed
rules -- `damage_pitch_divisor` and `minimum_cost_flat` -- and neither
key is in the ruleset. `step_damage` and `minimum_cost` are in the model
and fall back to the current behaviour exactly when the keys are absent,
so either can be re-measured by adding one line to `using-powers.md`.

## What this asks of any competing-sink design

Two rules fall out, and the second is the one that is easy to miss.

- **A lever gated by level is not a sink.** Attack ranks and power
  steps both scale with level on their own, so no amount of budget buys
  more of them. Only a lever gated by *points spent* can absorb points.
- **Competing sinks need depth that outruns the budget.** If both ends
  can be afforded at once, the player is handed both and never chooses,
  which is what happens here from level 5. It is not enough for the two
  ends to be balanced against each other; the budget has to be unable
  to reach both.

The reservoir fails the second rule badly today: its useful ceiling is
30 at levels 1, 5 and 10 and 50 at level 15, while the budget goes from
50 points to 260.

### Still open

- **The sink.** Even at 13 points a level, about 10% of a level 15
  budget is dead. Whatever absorbs it cannot be hit points. The trap is
  that any sink the simulator can see raises what the simulator
  measures, and a sink it cannot see will not move these numbers at
  all — the honest candidates are non-combat, and those already exist
  as thirty untracked skills and languages that nothing in `sim/`
  models.
- **Whether points should constrain combat at all.** Today they do not,
  from level 5. That may be a good design — it means combat power
  cannot be min-maxed out of a budget — but it is not what
  `skills.md` and `advancement.md` say. Either the ceilings should stop
  binding, or the design notes should stop claiming a trade-off that
  does not happen.
- **The interaction with `experience.md`.** The draft there prices a
  level at `advancement.points_per_level` rather than declaring its own
  number, so a move to 13 or 14 carries through with no edit. That is
  the intended behaviour and is worth confirming rather than assuming
  if the value moves.

### Why cost does not fall with skill, and where the lever is

`using-powers` prices a power at `base_cost + difficulty - skill_roll`,
which is exactly the mechanism a design wants if higher-level characters
are to do more with a reservoir that grows slowly: roll better, pay
less. It does not work, and the reason is the minimum.

No power may cost less than `difficulty // minimum_cost_divisor`. That
floor is set by the difficulty you declared and **knows nothing about
your skill**, so once the formula sinks beneath it, every further point
of skill buys nothing at all.

| build | level | declared | skill | floor | formula | paid |
|---|---|---|---|---|---|---|
| duellist | 1 | 12 | 7 | 4 | 4.5 | 4.5 |
| duellist | 5 | 20 | 11 | 6 | 8.5 | 8.5 |
| duellist | 10 | 20 | 16 | 6 | 3.5 | **6.0 floor** |
| duellist | 15 | 20 | 21 | 6 | -1.5 | **6.0 floor** |
| evoker | 15 | 30 | 21 | 10 | 8.5 | **10.0 floor** |

Martial builds reach the floor by level 10 and casters by level 15.
After that the price of a power is a function of the difficulty declared
and of nothing else.

Two facts sit beside it. Declared difficulty is nearly flat with level
— 12 to 20 for the martial builds across fifteen levels, 25 to 30 for
the casters — so characters do not push harder as they improve, they
succeed more often at the same push. And spend per fight is flat at
about 10 from level 1 to level 15 while the reservoir goes from 21 to
145, which is the same fact seen from the other end.

So the lever for *"cost comes down as skill goes up"* is
`minimum_cost_divisor`, or a floor that is relative to skill rather than
to declared difficulty. It is not `base_cost`, which is already being
cancelled out.

### One simulator fault found on the way

Both belong in `TODO.md` under simulator gaps if they are not fixed
alongside whatever is decided here.

- **`max_cost_of_a_successful_power` was not modelled. Fixed, and it
  changed nothing.** `using-powers` says a successful power never costs
  more than 10; the model computed `base_cost + difficulty - roll` with
  a floor and no ceiling, so above a declared difficulty of 32 the floor
  overtook the cap and billed a successful power for reaching further.
  The cap is in now. Every number this file records was unmoved by it,
  gates included, because **nothing in the panel ever declares a
  difficulty above 30** — the fault was real and dormant. Worth having
  because it is correct, and worth knowing it is not what was hiding
  anything.
- **The spend priority is fixed, and becomes load-bearing under a tight
  budget.** `build_character` reserves mastery hit points, then buys
  skills to their caps, then dumps whatever is left into the power
  source. That was a fair model of a player while points were
  abundant. Under a cut budget it buys no reservoir at all, which a
  player would not do. Reallocating would move the failures rather than
  remove them — at 190 points with skills wanting 123 and mastery
  wanting 53 there is no allocation that also funds a reservoir — but
  the model is choosing *which* thing starves, and it should not be.

## The sink, and what settled it

*Done, as `push` — see the design notes in `using-powers.md` and
`advancement.md`.* This closes the two questions the campaign above left
open: what absorbs the points nothing else wants, and whether points
should constrain combat at all.

Everything above was measured before the ladder campaign landed. Redoing
the headline measurement afterwards gave a worse number than the one it
records, and the reason matters.

### The surplus had grown, and the ladder work grew it

Dead points — unspent, plus points sunk into a reservoir past the size
the day model says a fight can empty — across the panel:

| | L1 | L5 | L10 | L15 |
|---|---|---|---|---|
| as measured above | 0.6% | 5.4% | 13.4% | 18.5% |
| after the ladder campaign | 16.0% | 14.5% | 18.4% | 23.1% |

Both rows are the same measurement on the same panel; the first is the
current checkout with the three caps that moved in the ladder campaign
put back (`power_source_per_point` 3,
`max_power_source_bought_per_level` 3, `max_starting_mastery_hp` 25).

So tightening those ceilings did not remove a surplus. It **converted
reservoir waste into unspent points and added more on top.** Level 1 is
the plainest case: it went from a budget with nothing spare to one
throwing away a sixth of itself, because cutting the starting mastery
cap from 25 to 8 took nine points of capacity out of a pool that did not
shrink. The caps were a fix for what they aimed at — the reservoir
really was oversized — and they made this worse. A ceiling is not a
sink. It is the opposite of one.

### Why a supply cut could not do it

The obvious repair was measured first, and it is worth recording in full
because it is the change anybody would try.

- **13 points a level is free, because it is worthless.** `--check` at
  `points_per_level: 13` returns output *identical* to 15 — the same
  single failure, the same 4.1 / 5.4 / 4.1 / 6.7 party rounds, the same
  3.16 / 3.48 / 3.87 / 3.92 cleared. Not "within noise": the same
  numbers. The two points removed were points no character could spend.
- **Clearing it by supply alone needs 15 down to 9.** Dead points reach
  zero at 9 and not before: 14 → 18.7%, 13 → 13.8%, 12 → 8.9%, 11 →
  4.1%, 10 → 1.5%, 9 → 0%.
- **And level 1 still would not move.** A first level is the pool in
  `character-creation.md`, not `points_per_level`, so it sits at 16.0%
  at every one of those values. Clearing it too needs the skill pool
  from 30 down to about 21.
- **Once a sink existed, the same cut stopped being free.** With push in
  and `points_per_level` at 13, the gates go from one failure to seven —
  a level 10 evoker that can neither land nor afford a field, two builds
  over the empty-reservoir ceiling, a contribution spread of 2.6x. A
  supply cut is painless exactly while the supply is worthless.

That is the whole answer to "fewer points per level": it is an
accounting change, it cannot create a choice, and it is only safe while
there is nothing to choose.

### Why the offence side had to be the one that got deeper

The campaign above named the target: *"not the balance between the ends,
but the depth of the offensive one."* Measured as a share of what there
is to place, the offence ceiling — every attack skill at its cap plus
the reservoir at its cap — is about a fifth of the budget at every
level: 20.0% / 22.4% / 22.4% / 21.1%. You can buy all the offence there
is with pocket change, which is the same fact as the inert dial, seen
from the supply side.

### Push

A bought ceiling on the highest difficulty a character may declare, with
any power or any spell. A grade decides which rungs exist for you; push
decides how high you can stand on the one you have.

It satisfies both rules the campaign above set for a competing sink. It
is gated by points spent rather than by level, and it is deeper than the
budget: opening every band in the game costs 42 points against a level 1
discretionary budget of 30.

It is also the only item on the advancement menu that can honestly be
sold without a per-level ceiling, and that is what makes it deep enough
to matter. Everything else needs a cap because nothing in play limits
how much of it is useful. Push limits itself: buying more than your
skill can roll to buys the right to declare a difficulty you will miss,
and missing spends the action and costs the minimum anyway.

What it measures:

| | L1 | L5 | L10 | L15 |
|---|---|---|---|---|
| dead points, before | 16.0% | 14.5% | 18.4% | 23.1% |
| dead points, with push | 0.0% | 0.5% | 3.1% | 7.6% |
| offence ceiling as a share of budget, before | 20.0% | 22.4% | 22.4% | 21.1% |
| offence ceiling, with push | 160% | 76% | 52% | 40% |
| points a build puts into push | 8-12 | 12-22 | 20-42 | 42 |

**Gates: one failure, the same one as before it** — the level 5
spellblade at 85% on an empty reservoir, which is a chronic complaint
about that one build and predates this. Party fight length is unchanged
at levels 5, 10 and 15, and level 1 lengthens slightly, from 4.1 rounds
to 4.4, with the duels under the three-round floor going from 26 to 23.
Level 1 was the one place fights were measurably too short, so the
direction is the right one.

### The other open question: yes, points constrain combat now

The campaign above left "whether points should constrain combat at all"
undecided, and noted that from level 5 they did not. `--spectrum` run on
both rulesets through the same code answers it. Builds whose
contribution moves at all across the tank-to-striker dial, out of ten:

| | L1 | L5 | L10 | L15 |
|---|---|---|---|---|
| before | 1 | 0 | 0 | 0 |
| with push | 10 | 10 | 8 | 1 |

Two honest qualifications on that, because the number alone flatters it.

The dial's legend says a flat row is a real choice, and before push
every row was flat — but flat for the wrong reason. A berserker built at
0 and at 1 was the *same character*, every rank identical, so the row
was flat because nothing was being chosen. What push changes is that the
dial now builds different characters; whether the two ends are *fairly*
priced against each other is the next question and not this one. The
shape is encouraging rather than settled: rows run flat across most of
the dial and fall only at the extreme, which is a broad plateau with the
all-offence corner punished for buying no hit points at all.

And level 15 is still inert, 1 build out of 10. That is the same fact as
the 7.6% below, from the other side: a level 15 budget can afford the
whole of push and both ends besides. Headroom is still negative there
(-35 for a berserker against a capacity of 185), so the dial has nothing
left to decide.

### What is left, and why it is not a pricing problem

7.6% at level 15 survives. It is not a price that wants raising: it is
that the deepest band in the game tops out at difficulty 48, and a level
15 character has bought all of it. `hardest_rung()` derives that number
from the rules rather than naming it, so a rung above the present top
deepens the sink by itself — which makes this the same item as the spell
list's missing third rung in `TODO.md`, not a separate one.

Raising `rank_cost_peripheral` from 3 to 5 does absorb the residual
(7.6% → 1.6%), and it was rejected rather than missed. It absorbs by
charging more for the same character, and a 5-to-1 spread between a
focused rank and a peripheral one prices dabbling outside your
disciplines out of the game. Adding content is the better answer than
raising the rent.

### The caveat on every number above

"Dead points" means *points the combat sheet could not absorb*, because
`sim/` tracks five skills and the real list runs to about thirty-five
plus languages. A level 15 berserker with 77 points spare in this model
spends them on Climb and Diplomacy in play; it does not burn them.

That does not make the finding go away, it sharpens what the finding
is. The complaint was never that characters throw points away. It is
that **combat power stopped being a budget decision** — every tracked
skill at its ceiling from level 5 on, both pools capped, and the
marginal point reaching nothing that fights. A sink the simulator
cannot see would have left that exactly as it was, which is why the
thirty untracked skills were never the answer even though they are
where the points really go.

### Two things found on the way

- **The deepest band in the game belongs to no discipline.**
  `hardest_rung` is 48, and it is Quick Attack's — a general power, open
  to everybody from first level. That is why push, and not grade
  gating, was the thing that could close the hole.
- **The cascade was choosing which thing starves.** The entry above ends
  by naming this fault against the reservoir. Threading push through hit
  it immediately: filling every skill to its cap first left a level 10
  build with a push of 6, which is a character no player would make.
  `usable_push()` fixes it — buy the push your skill can actually roll
  to, then skills, then leftovers into more push. The same fault is
  still there for the reservoir under a cut budget, and is recorded in
  `TODO.md`.

## Every band opens on something now

*Done, as a `base_*` grant on thirteen powers.* `TODO.md` carried this
as "most powers deliver nothing at the bottom of their own band": the
ladder gave every power a base difficulty and a maximum, and for most of
them the base was the first number you could **say** rather than the
first that bought anything.

### It was thirteen, not ten, and the list was wrong in both directions

Counting them mechanically -- a power has a hole if it carries a
`*_per_step` effect and no matching `base_*` -- turns up thirteen:
Precise Strike, Forewarned, Weak Point, Read the Room, Winning Manner,
Sidestep, Redouble, Rattle, Find the Gap, Call the Shot, Second Wind,
**Deflect** and **Follow Through**.

The last two were on the entry's list of powers that *read correctly*,
and they behaved correctly, and the reason they did is the interesting
part: the simulator was hardcoding their base grant. `chain_length`
computed `per + steps * per` and `deflect_plan` computed
`per_step * (1 + steps)`. Both are mechanic values living in `sim/` and
nowhere else, which is exactly what the single-source rule exists to
prevent -- the rules said Follow Through chained into nothing at its own
base difficulty and the model said it chained into a body.

Their **prose** was right all along, and so was Read the Room's: all
three described a base grant in words while the mechanics block had no
key for it. So on those three the frontmatter was the odd one out, and
the fix is that the prose now interpolates a real `base_*` key instead
of borrowing the per-step value. Moving the hardcodes into the rules is
numerically neutral, which is how the reading was checked.

### The minor powers are the whole of the difficulty

Five of the thirteen are **minor**, and minor powers ignore the minimum
cost, so they trend to free. A base grant on one is therefore a
permanent free bonus from first level -- which is why Precise Strike was
given a base once before and had it taken away again.

Measured one at a time, Precise Strike is the entire effect. Paragon
floor ratio at level 5:

| | L5 | L10 |
|---|---|---|
| no base grants on the minor five | 74% | 57% |
| all five, Precise Strike at base difficulty `2` | **81%** | 60% |
| Weak Point's grant removed | 81% | 60% |
| Sidestep's grant removed | 81% | 60% |

Weak Point and Sidestep move nothing. Precise Strike moves everything,
and the mechanism is visible in the floor itself: at base difficulty `2`
it became the best free option for **every** martial build, taking a
level 5 paragon's empty-reservoir damage from `8.39` to `9.34` for
nothing, for ever.

### The fix for a free power is its base difficulty, not its grant

A dead end worth recording, because it is the obvious first thought and
it cannot work: raising `base_difficulty` *instead of* adding a grant
fixes nothing. Steps are `(difficulty - base_difficulty) // step`, so
the base always buys zero whatever the base is -- moving it only
relabels the same hole.

The two together do work, and for a free power they are the right
answer. A minor power costs nothing once the roll beats
`base_cost + difficulty`, so its base difficulty is what decides *when*
the floor becomes free:

| Precise Strike | paragon L5 | L10 |
|---|---|---|
| unfixed | 74% | 57% |
| base `2` + grant | 81% | 60% |
| base `6` + grant | **76%** | 57% |
| base `8` + grant | 72% | 55% |

`6` is what landed: a band that opens on something, at a cost of two
points of floor ratio at level 5 and none at level 10. It also lands
exactly on `character-creation.starting_push`, so the beginner's free
trick sits precisely at the beginner's reach.

### What the gates say, and what they cannot

`all gates pass`. Party fight length goes from 4.4 / 5.4 / 4.0 / 6.6 to
4.4 / 5.3 / 3.6 / 6.4, and the duels under the three-round floor drop
from 28 to 26. The number to watch is level 10 at `3.6` rounds against a
floor of `3.0`: this is a buff to thirteen powers and that is where it
shows.

**Six of the thirteen are invisible to `sim/`.** Second Wind, Rattle,
Forewarned, Call the Shot, Read the Room and Winning Manner appear
nowhere in it -- initiative, social checks, facts and mastery hit point
restoration are all outside what it scores. For those six the gate run
says nothing broke; it does not say the values are right, and no
measurement here should be read as though it did.

## The spell list's third rung

*Done, as the comets.* `TODO.md` asked "whether the damaging spells need
a third rung the way the martial line did". They did, and the obvious
version of it would have done nothing.

### A rung above Lance would have been decorative

The first design was a rung opening where Lance tops out, at difficulty
34. Measuring where casters actually declare killed it:

| | declares | unconstrained optimum | band tops at |
|---|---|---|---|
| L1 evoker | d14 | d12 | 34 |
| L5 evoker | d16 | d16 | 34 |
| L10 priest | d24 | d20 | 34 |
| L15 priest | d28 | d24 | 34 |

**Lance's ceiling never binds at any level.** A caster's declaration is
limited by the arithmetic -- more damage against a worse chance of
meeting it -- and not by the rung, so a rung opening at 34 would never
have been reached by anybody.

### Why the martial line works and this one did not

The same measurement on the martial side:

| | Power Attack | Hammer Blow |
|---|---|---|
| L5 berserker | d12 | no grade |
| L10 berserker | **d18, its ceiling** | d20 |
| L15 paragon | **d18, its ceiling** | d24 |

Power Attack is pinned at its ceiling from level 10 onward, and Hammer
Blow opens at exactly that number. **The ceiling binding is what makes
the next rung get taken.** Lance was simply too wide for that to
happen: 26 points of band at `0.5` damage per difficulty, where Power
Attack gets 14 at the same rate.

### What landed

Lance's band comes down to where it starts to bind, and the comet opens
there at double the rate:

| | band | damage | per difficulty | minimum spirit |
|---|---|---|---|---|
| bolt | 2-14 | 6-10 | 0.33 | 0 |
| lance | 8-**22** | 10-17 | 0.50 | 2 |
| comet | **22-38** | 17-33 | **1.00** | 6 |

Continuity holds the way the ladder design note asks: a lance at 22
deals 17, which is where the comet opens, exactly as Hammer Blow opens
at the 8 Power Attack ends on. The comet carries the same conditions as
the lance of its type, so the rung buys slope and nothing else -- the
same thing Hammer Blow buys over Power Attack.

`minimum_spirit` is what gates it, at 6 against a lance's 2 and a
bolt's 0, so the three rungs arrive in the order a caster grows into
them. No model change was needed: `combat_spells` finds any spell with
a `damage` key, so a new chassis is a rule-file edit and nothing else.

### What it measures

`all gates pass`, and party fight length does not move at all -- 4.4 /
5.3 / 3.6 / 6.4 either side. What moves is the top of a caster's career:
the level 15 evoker goes from `17.8` to `22.6` expected damage, the
priest from `26.9` to `30.2`, the spellblade from `15.0` to `18.5`, and
declared difficulty now climbs to 30 where it stopped at 28. Duels under
the three-round floor go from 26 to 28. Contribution spread stays inside
the band at 2.15 / 1.62 / 2.24 / 2.22.

**It does not deepen the push sink**, which had been suggested as a
reason to want it. `hardest_rung` is still 48 and still Quick Attack's,
so the residual dead points at level 15 are untouched -- and a spell
rung could never have helped a martial build there anyway, since
`hardest_rung` is asked per character.


## The round band's floor, and why it is level-aware

The question was whether the floor of `TARGET_ROUNDS` should vary by
level. Level 1 duels sat on it — median `2.99` rounds with `24` of `45`
pairings under three, against one to three of forty-five at every other
level — and `TODO.md` recorded two possible readings without deciding
between them: either the floor was wrong for level 1, or first-level
damage was too high for first-level hit points.

**Both readings were wrong, and the floor is level-aware anyway.**

### There is no curve

The first thing measured was the shape, because "level-aware" quietly
assumes a curve and a curve is a thing you can check for. Duel length
by level, median across all `45` pairings:

| level | 1 | 2 | 3 | 4 | 5 | 10 | 15 |
|---|---|---|---|---|---|---|---|
| median rounds | 2.99 | 4.29 | 4.73 | 4.73 | 4.78 | 4.19 | 4.47 |
| under three | 24/45 | 1/45 | 1/45 | 3/45 | 1/45 | 1/45 | 2/45 |

There is no curve. There is one riser, between level 1 and level 2, and
a flat population above it. So whatever the answer was, it was not a
function of level — it was an exception for one level.

### It is not hit points

Measured against a *fixed* foe, so that neither side's kit or build can
move, hit points come to `3.27` rounds of the median build's attention
at level 1 against `3.58`, `3.46` and `3.67` at levels 5, 10 and 15.
The first-order arithmetic of a level 1 fight — hit points over damage —
is the arithmetic of a level 15 fight, within a tenth of a round.

So first-level damage is not too high for first-level hit points, and
the second of the two readings is dead. Note that this measurement only
works *because* it holds the foe fixed: peer against peer the number
does move, and that is the next section rather than a contradiction.

### It is not the reservoir either

This was the obvious candidate and it is why `RESERVOIR_MATTERS_FROM_LEVEL`
is **not** the threshold the floor ends up using. What an empty
reservoir costs the median build slopes smoothly — it keeps 88% of its
damage at level 1, then 83, 81, 79 and 71% through level 5 — and a
smooth slope cannot produce a step.

### It is partly the armour, and that part is not for sale

What *is* discontinuous at level 1 is the kit. The starting purse is
`150` gold and a breastplate costs `200`, so it is out of reach before
a weapon is bought at all. A level 1 party wears a chain shirt, scale
mail or studded leather; from level 2 to level 15 nine builds in ten
wear a breastplate or better and never take it off. That is a point of
damage reduction on every hit in both directions — a raw `10` lands as
`6` at level 1 and as `5` above it.

It looks like the whole answer. It is not, and the measurement that
shows it is the most useful thing in this entry, because *funding the
armour was the obvious fix and it does not work.* Raising the purse
saturates almost immediately:

| starting gold | median | under three | armour worn |
|---|---|---|---|
| 150 | 2.99 | 24/45 | chain shirt, scale mail, studded leather |
| 250 | 3.27 | 21/45 | breastplate ×6, chain mail ×3 |
| 400 | 3.27 | 21/45 | breastplate ×9 |
| 800 | 3.27 | 21/45 | breastplate ×9 |

By `250` gold everybody who wants a breastplate has one, and from there
the purse can be raised fivefold and *nothing whatever changes* — same
median, same twenty-one. The armour gap is real and it closes three of
the twenty-four. The other twenty-one are not for sale at any price.

### What the riser actually is

With the kit equalised, a level 1 fight runs at almost exactly its own
first-order arithmetic, and every level above it runs a fifth to a third
longer than its arithmetic. That is the content of the step. A fight
gets long by somebody spending something to stretch it — a power, a
guard, a heal, a point of push — and at level 1 there is nothing yet to
spend: no advancement bought, and the gear you could afford rather than
the gear you want.

**Three rounds is a statement about a character with a toolbox.** A
level 1 character has not got one, so the floor was measuring the game
against something it does not yet have.

### The value

`FIRST_LEVEL_ROUNDS_FLOOR = 2.0`, applied at level 1 only, through a
`round_floor(level)` that every caller uses in place of
`TARGET_ROUNDS[0]`. The ceiling is unchanged and is the same at every
level.

Two was not fitted to the data — it is calibrated so that the floor
makes the **same statement** at level 1 that three makes everywhere
else. Three catches one pairing in forty-five at levels 2, 3, 5, 10 and
15, and three of forty-five at level 4: the glass cannon against the
glass cannon that the constant's own comment already blesses as those
builds working. Two catches one of forty-five at level 1. Three at level
1 catches twenty-four, and **a floor that half the field is under is not
a floor, it is a mislabel** — which is the real fault being fixed here.

### What it changes

Nothing fails differently: no gate outcome moves, because the gated
number is the party encounter and a level 1 party's fights run `4.4`
rounds, comfortably inside the band either way. What moves is the
diagnostic, which stops printing twenty-four lines at level 1 that mean
nothing, and the gate's honesty about what it would catch in future — a
level 1 party fight that dropped to `2.8` rounds used to fail and now
does not, which is correct, and one that dropped to `1.9` still fails,
which is also correct.

No mechanic value moved: this is `sim/` only, and a release carrying it
alone would be a PATCH.

### Left open

The armour finding was not a fault but it is a design fact nobody had
written down, and it went to `TODO.md` in the one form that is still
open: the first level is the only stretch of the game where the armour
table's expensive rows are out of reach, so it is the only time that
table presents a real choice — and no gate looks at whether that choice
is a good one.
