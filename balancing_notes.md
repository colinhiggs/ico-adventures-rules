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

## Reworking powers into a ladder of difficulties

The measurements above ended with three things a ladder would have to
settle, and this is the ladder built against them. It landed in the
rules rather than staying here, so what follows is the case for the
numbers rather than an undecided question — with one genuine surprise
in the middle, which is why it is written down at this length.

### What a rung is

A power now names a **band**: a base difficulty, which is the least it
may be declared at, and a `max_difficulty`, which is the most. Above the
top of a band there is no bigger number to say. Reaching further means
owning the next power up.

Powers therefore come in rungs, and the martial damage line is the pair
the rest is built around:

| rung | grade | band | damage added |
|---|---|---|---|
| Precise Strike (minor) | Initiate | 2–10 | 0 to +2 |
| Power Attack | Initiate | 4–18 | +1 to +8 |
| Hammer Blow | Adept | 18–34 | +8 to +24 |

`base_damage` is the new key that makes this work, in the same idiom as
`base_allies` and `base_targets`: **the rung above opens at exactly the
damage the rung below closes at**, and then climbs at twice the rate
over twice the span. Buying the grade is never a step backwards and
never a discontinuity.

### Why a rung and not a steeper line

Because a steeper line cannot move the ratio, and the arithmetic says so
in one step. With a fixed exchange rate `r` of damage per point of
difficulty, a base difficulty `bd`, plain damage `B` and attack skill
`A`, maximising `hit chance x damage` puts the best declaration at

    D* = (A + 21 + bd - B/r) / 2

and the damage the power adds there at `(r(A + 21 - bd) - B) / 2`.
Turning `r` multiplies level 1 and level 15 by the same factor. Only
`bd` and `r` *changing together above a difficulty a beginner cannot
reach* moves the ratio, and that is what a second rung is.

Measured on the reference striker against the standard foe, which is
the same measurement the earlier entries in this file use:

| level | before | after |
|---|---|---|
| 1 | Fast Attack d16, `+5.38` | Power Attack d10, `+3.65` |
| 5 | Fast Attack d16, `+8.33` | Power Attack d14, `+5.45` |
| 10 | Fast Attack d16, `+10.28` | Fast Attack d22, `+8.38` |
| 15 | Fast Attack d31, `+11.92` | Hammer Blow d24, `+12.70` |

**The effect lever goes from 2.2x to 3.5x**, which is the number the
multiplicative design needed and could not get: it had effect 2.5x doing
a third of the work while frequency 3.8x did the rest, against a
frequency lever that saturates at every round. The rungs also give the
progression something to be about — the crossovers land at level 10 and
level 15 rather than nowhere.

### Fast Attack was the whole problem

The left column above is the finding. **Every reference build declared
Fast Attack at difficulty 16 from level 1 to level 10 and nothing else
was ever close**, because one extra swing is worth more than any amount
of extra damage on one and it was reachable at first level. With one
power answering every question at every level, the damage ladder was
decorative before it was built.

Its band moved to 22–47, one extra attack at the base and a second at
the top. The base difficulty was chosen by sweeping it:

| base | L1 | L5 | L10 | L15 |
|---|---|---|---|---|
| 14 | Fast | Fast | Fast | Hammer |
| 18 | Fast | Fast | Fast | Hammer |
| **22** | **Power** | **Power** | **Fast** | **Hammer** |
| 26 | Power | Power | Hammer | Hammer |

At 22 it is out of reach early, a live competitor with the Adept rung in
the middle, and beaten by it at the top — which is the relationship a
general power and a bought one should have. At 26 it is dead.

Quick Attack, its minor twin, went to 18–48 with a *coarser* step than
Fast Attack's rather than a finer one. That is load-bearing and was
nearly got wrong: a minor power whose steps are cheaper than its
standard twin's overtakes it somewhere, and a free version of the best
power in the game is not a trade-off. `minor_beaten_by_twin` did not
catch it, because its skip rule asked whether the standard power was
"above its first step" rather than whether it granted anything at all,
and a rung with a base effect grants something at its first number. Both
are fixed.

### Creatures got their own rung, which was the point

The third open question was creatures, and the band answers it directly.
Against the reference line-holder:

| creature | martial grade | before | after |
|---|---|---|---|
| hobgoblin | Initiate | Power Attack d18, `5.13` | d18, `5.37` |
| gnoll | Initiate | Power Attack d22, `12.24` | d18, `12.04`, cost `7.3`→`6.0` |
| hill giant | Adept | Power Attack d28, `20.04` | **Hammer Blow** d28, `25.79` |

The gnoll was declaring at `22` on a reservoir of `34` because nothing
stopped it; now its grade does, and the power it can still afford costs
it less. The giant gained a fifth of its output by standing on the rung
its grade already said it held. Neither creature's stat block moved.

That is the mechanism `creature-advancement.md` needed and did not have:
a dangerous individual of an ordinary kind is now a creature that bought
a grade, rather than a creature with an invented weapon.

### The simulator fault that nearly became the headline

The first ladder run reported the failing level 10 party fight length
falling from `12.4` rounds to `4.2`, and clearing `3.34` of the day to
`4.02`. That would have been the headline. It was wrong, and finding out
why is the most useful thing in this entry.

Every first-order number said the opposite. Party damage per round was
**down** about a fifth at both levels after the change; creature damage
was flat or up. Nothing in the arithmetic could produce a fight three
times shorter.

`_swarm_plan` picks one power and one difficulty for a round against a
crowd, and it scored the options in **whole kills**. Where nothing a
build holds can one-shot the mook in front of it, every option scores
exactly zero, and the comparison falls to whichever one *could* kill on
a face nobody rolls. The only faces that drop a hobgoblin at level 5 are
runaway criticals — and a runaway critical clears a declared `44` as
easily as a declared `4`. So the difficulty cost nothing in the measure
while costing the whole action in the fight, since `_swarm_act` spends
the round on a failed declaration:

| Follow Through at | chance of making it | scored kills |
|---|---|---|
| 4 | 1.00 | 0.0038 |
| 20 | 0.60 | 0.0075 |
| 44 | 0.02 | **0.0131** |

The level 5 and level 10 reference parties were declaring Follow Through
at `44` and standing there for most of the fight. The ladder's ceilings
made that declaration impossible, so the fight length improved — for a
reason that had nothing to do with the rules being better.

`_expected_kills` is now `_expected_bodies` and scores **fractions of a
body**: damage capped at one mook's hit points, divided by them. At
level 5 that is a plain attack at half a hobgoblin against a lottery
ticket at a fiftieth of one, and the plain attack wins. On identical
rules:

| level | kill count | body fractions |
|---|---|---|
| 5 | 9.8 rounds | 6.2 |
| 10 | 12.4 rounds | 5.0 |

**Every party number in this file taken before that fix is worth less
than it looks**, including the ones that motivated this whole effort.

### What the ladder actually does to a party, honestly

Both columns below use the corrected planner, so the only difference is
the rules:

| level | before: rounds / cleared | after: rounds / cleared |
|---|---|---|
| 1 | 3.9 / 4.99 | 3.8 / 5.00 |
| 5 | 6.2 / 4.35 | 6.0 / 4.45 |
| 10 | 5.0 / 5.25 | 4.2 / 4.50 |
| 15 | 6.4 / 4.53 | 6.5 / 4.00 |

Fight length barely moves, which is what the first-order arithmetic
predicted and what should have been expected all along. What does move
is the **day**, and in the right direction: level 10 was clearing more
than the whole of it — `5.25` of `5`, a day that was not a day — and
level 15 tightened from `4.53` to `4.00`. The giant's rung is most of
the second.

Gate count is unchanged at one, and the failure is a different one:

- before: `L10 berserker takes 4.4 rounds to clear 6 goblins (target 4)`
- after: `L5 spellblade keeps 85% of its damage with an empty reservoir
  (band 35-85%)`

The second is a hairline — one build, one level, exactly on the bound —
and it is the fresh side that moved rather than the floor: a level 5
spellblade can no longer reach Fast Attack, so its reservoir buys it
less. Read with `CLAUDE.md`'s rule about comparing numbers rather than
counts, this is the change costing about half a point on one build.

Precise Strike was given a `base_damage` for continuity and it was taken
away again, measured: **a floor on a power that costs nothing is a
permanent floor**, and it alone put that spellblade at 94% — nine points
outside the band rather than on it — and pushed three more duels under
the three-round floor. That is the cleanest argument in this entry for
why the other ten powers whose bands open on nothing should be fixed
together and measured, rather than tidied up one at a time.

### Still open

- **The spell list has two rungs and stops.** Bolt into Lance is a
  ladder; nothing sits above Lance, so a caster's top rung arrives early
  and afterwards only widens. Bands are on every spell so the mechanic
  is universal, but whether the damaging spells need a third rung the
  way the martial line did has not been measured.
- **Ten powers open their bands on nothing.** See `TODO.md`. The fix is
  a flat buff to ten powers and has to be measured as one.
- **A floor ratio above 100% is incoherent and the level 1 skirmisher
  now reports one.** `floor_offence` can exceed `expected_offence`
  because they are different computations rather than a restriction of
  one another — the blend over rounds and conditional availability is in
  one and not the other. It was 89% before the ladder and 103% after,
  so the ladder made an existing fault visible rather than causing it.
  The gate exempts level 1 from the ceiling, which is why nothing failed.
- **The multiplicative design has not been re-measured on the ladder.**
  That was the point of building it: effect 3.5x and frequency somewhere
  under 3x would land near the 10.5x the scaling needs, without the flat
  minimum having to do all the work that broke the bestiary. The knobs
  are unchanged and uncommitted.

## Re-measuring the multiplicative design on the ladder

The ladder was built to make the multiplicative design work. It does,
and the useful result is that **the half of it that needed a new
mechanic turns out not to be needed at all.**

Everything below uses the corrected crowd planner, so it is comparable
with the entry above it and *not* with the multiplicative entry before
that.

### The configurations

The "knobs" are the five uncommitted progression values the earlier
entry settled on: `max_starting_mastery_hp: 5`,
`max_power_source_bought_per_level: 1`, `power_source_per_point: 4`,
`base_cost: 12`, and `minimum_cost_flat: 2`.

| | configuration | fails | day cleared, L1/L5/L10/L15 |
|---|---|---|---|
| 1 | no ladder, committed | 1 | 4.99 / 4.35 / 5.25 / 4.53 |
| 2 | ladder, committed | 1 | 5.00 / 4.45 / 4.50 / 4.00 |
| 3 | no ladder + all knobs | **5** | 2.72 / 3.29 / 4.26 / 4.00 |
| 4 | ladder + knobs, **proportional** floor | **3** | 2.56 / 3.37 / 3.93 / 3.93 |
| 5 | ladder + knobs, **flat** floor | **3** | 2.72 / 3.31 / 3.84 / 3.77 |
| 6 | ladder + mastery knob only | 2 | 3.16 / 3.41 / 3.84 / 3.87 |
| 7 | ladder + pool and cost knobs only | 2 | 4.31 / 3.94 / 3.97 / 4.00 |

Fight length is inside the 3–12 band at every level of all seven.

### The ladder takes the design from five failures to three

Rows 3 and 5 are the same design with and without the ladder. The two
failures it removes are precisely the two that were about powers:

- `L5 spellblade keeps 91% of its damage with an empty reservoir` — gone,
  because the ladder gives the spellblade something to spend a fresh
  reservoir on that a beginner cannot reach.
- `L10 berserker takes 4.4 rounds to clear 6 goblins` — gone.

The three that survive are **all at level 1 and none of them is about the
cost rule**. Rows 6 and 7 split them cleanly:

| failure | caused by |
|---|---|
| L1 evoker can neither land nor afford any field | the spirit pool knobs |
| L1 priest keeps 34% with an empty reservoir (floor 35%) | the spirit pool knobs |
| L1 contribution spread 2.6x (priest 74 vs spellblade 28) | the mastery knob |

All three are the brief's own instructions arriving: mastery hit points
starting near core (`35` down to `15`) and a reservoir that grows slowly
from a smaller start. Level 1 has not been re-tuned for either, and the
level 1 day says so — `5.00` of five encounters cleared becomes `3.16`
under the mastery knob alone and `4.31` under the pool knobs alone.

### The flat minimum is no longer worth having

This is the result worth keeping. Rows 4 and 5 differ **only** in the
floor rule, and they measure the same: three failures, the same three,
and a day within a rounding error at every level. `minimum_cost_flat`
buys nothing the gates can see once the ladder is in.

It is not that the floor stopped mattering — it still nearly doubles the
frequency lever:

| ladder + knobs, floor rule | effect | frequency | product |
|---|---|---|---|
| proportional, `difficulty / 3` | 3.5x | 2.75x | **9.6x** |
| flat `2` | 3.5x | 4.50x | **15.7x** |

It is that **the effect lever now covers the ground on its own**. Before
the ladder, the same two rows were 3.3x x 1.4x = 4.6x and 2.5x x 3.8x =
9.5x: only the flat floor could reach ten, and it had to carry the
design. With the rungs in, the proportional floor reaches 9.6x — what
the flat floor used to reach — using the lever that costs no new
mechanic.

Frequency ratios are only comparable between rows carrying the same
reservoir knobs, which is worth stating because it is what the earlier
entry got wrong. On the committed pool, which grows eightfold on its
own, frequency is 4.70x without the ladder and 4.41x with it — the
ladder does not touch that lever, and any comparison that mixes pool
settings will say it does.

### The bestiary objection was smaller than recorded

The earlier entry's reason for rejecting the flat minimum was that it is
worth far more to a creature than to a character. Measured like for like
— same reservoir knobs on both sides, which the earlier table did not do
— it is worth roughly the same to both:

| who | uses a day, proportional -> flat | gain |
|---|---|---|
| hobgoblin | 2.9 -> 4.3 | 1.50x |
| gnoll | 5.4 -> 10.0 | 1.85x |
| hill giant | 5.2 -> 10.4 | 1.99x |
| striker L5 | 5.7 -> 7.0 | 1.23x |
| striker L10 | 6.8 -> 11.3 | 1.65x |
| striker L15 | 8.6 -> 15.7 | 1.82x |

The ladder is why: a level 15 striker used to declare Fast Attack at
`31` and pay a proportional floor of `10`, so the flat rule was an
enormous discount to creatures and a small one to characters. Capped at
Hammer Blow's `24`, the character is in the same position the creature
was. The asymmetry was real and the ceilings closed it — which removes
the objection rather than vindicating it, and leaves the argument
against the flat floor resting on it buying nothing.

### Reservoir dependence stays healthy

The wall the quadratic hit is nowhere near. Share of damage kept with an
empty reservoir, across all ten builds:

| configuration | L5 | L10 | L15 |
|---|---|---|---|
| ladder, committed | 46–85% | 51–64% | 48–67% |
| ladder + knobs, flat floor | 43–84% | 46–61% | 47–63% |
| (the quadratic, for contrast) | — | 22–31% | — |

Note that the level 5 spellblade at `85%` — the single hairline failure
the ladder alone carries — comes *inside* the band at `84%` once the
pool knobs are in. The progression knobs fix it.

### What this settles and what it leaves

**Settled.** The multiplicative design works on the ladder, and it works
without `minimum_cost_flat`. Neither experimental key —
`damage_pitch_divisor` or `minimum_cost_flat` — needs to enter the
ruleset. The model keeps both behind absent-key fallbacks so this can be
re-run, but nothing is waiting on them.

**Left open.** The five progression knobs are still uncommitted, and
what stands between them and the rules is level 1 rather than anything
about powers: three gate failures, all at level 1, all downstream of
mastery hit points starting at `15` and a reservoir starting smaller.
That is a level 1 tuning job — starting spirit, the evoker's field
affordability, and the spread between a priest and a spellblade on their
first day — and it is now the only thing between the brief's principles
and the rules.
