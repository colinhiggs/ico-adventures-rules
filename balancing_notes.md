# Balancing notes

Measurement campaigns that are finished as *measurements* but not
settled as *decisions*. `TODO.md` is for work that is known to be
missing; `DONE.md` is for work that is finished. This file is for the
third thing: a question that has been measured hard enough that the
numbers should not have to be produced again, but not answered.

An entry here should be readable by somebody who was not in the room.
It says what was asked, what was run, what came back, and what is still
open — and it names the dead ends, because those are the expensive part
to rediscover.

When an entry is decided, the decision goes to `DONE.md` and whatever
is left to build goes to `TODO.md`, and the entry leaves this file.

---

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
- **Decide whether Guard belongs at initiate grade.** See above: at
  initiate it is universal, and a universal power differentiates
  nobody.

### What this asks of any competing-sink design

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

### Two simulator faults found on the way

Both belong in `TODO.md` under simulator gaps if they are not fixed
alongside whatever is decided here.

- **`max_cost_of_a_successful_power` is not modelled.** `using-powers`
  says a successful power never costs more than 10; `sim/model.py`
  computes `base_cost + difficulty - roll` with a floor and no ceiling.
  So the simulator overcharges powers, which means it values the
  reservoir *higher* than the rules do. Every reservoir finding above
  is therefore conservative — and the drift cost of capping it is an
  overestimate.
- **The spend priority is fixed, and becomes load-bearing under a tight
  budget.** `build_character` reserves mastery hit points, then buys
  skills to their caps, then dumps whatever is left into the power
  source. That was a fair model of a player while points were
  abundant. Under a cut budget it buys no reservoir at all, which a
  player would not do. Reallocating would move the failures rather than
  remove them — at 190 points with skills wanting 123 and mastery
  wanting 53 there is no allocation that also funds a reservoir — but
  the model is choosing *which* thing starves, and it should not be.
