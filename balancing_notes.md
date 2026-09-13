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

## Reworking powers into a ladder of difficulties

The advancement point economy campaign — now settled, and moved to
[DONE.md](DONE.md) — ended with three things a ladder would have to
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
with the entry above it and *not* with the original multiplicative
measurement, which is in [DONE.md](DONE.md) with the rest of the
advancement point economy campaign.

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

The advancement point economy entry in [DONE.md](DONE.md) rejected the
flat minimum on the grounds that it is worth far more to a creature than
to a character. Measured like for like
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

## Level 1, tuned, and the progression knobs landed

The entry above left three gate failures, all at level 1, as the only
thing between the brief's progression principles and the rules. Two of
the three turned out to be one knob that was not needed, and the third
was a real trade that has been taken deliberately.

### Two of the three were `base_cost`, not the reservoir

`base_cost: 12` was introduced to hold level 1 down in the
*flat-minimum* design. Once the flat minimum was dropped it had no job
left, and it was doing damage:

| | evoker's field | priest's floor | contribution spread |
|---|---|---|---|
| `base_cost: 12` | **none affordable** | **34%** (floor 35%) | **2.62x** |
| `base_cost: 10` | flame field at d16 | 39% | 2.51x |

Both failures are the same mechanism. `base_cost` is how far a roll must
beat a declared difficulty before a minor power costs nothing, so
raising it narrows every free band at once — which is exactly what the
reservoir floor measures — and it raises the price of everything else,
which is what priced a first-level evoker out of a field. Neither had
anything to do with the reservoir knobs it was bundled with.

**Committed: `base_cost` stays at `10`.** Only three of the five knobs
were ever needed.

### The third was mastery, and the fix was eight rather than five

The remaining failure — contribution spread `2.62x` against a bound of
`2.5x` — is caused by the mastery cut, and the mechanism is worth
recording because it is not obvious. Offence and damage taken are
*identical* between the two configurations. Only survival moves, and it
moves by the same factor for everybody. What widens the spread is that
`contributions` credits a build's **opening rounds at range** on top of
its melee term: cut hit points and the melee term shrinks while the
opening does not, so builds that can act at a distance lose less than
builds that cannot. Priest against spellblade, not caster against
fighter.

Sweeping the creation cap on bought mastery hit points:

| cap | L1 mastery | L1 spread |
|---|---|---|
| 5 | 15 | 2.51x |
| **8** | **18** | **2.39x** |
| 10 | 20 | 2.32x |
| 25 (before) | 35 | 1.97x |

`8` is the smallest value that clears the bound, and `18` sits inside
the brief's stated zone of ten to twenty. **Committed: `8`.**

### Grant or cap made no difference at all, and that is a finding

`character-creation.md` carries a design note arguing that raising a
*cap* is never free — it changes what a build can afford, and hits the
builds shortest of points hardest — which is why the flat ten was
granted rather than sold. Lowering a cap should by the same argument
hand points back. It does not:

| free grant | cap | L1 mastery | L1 spread | total reservoir |
|---|---|---|---|---|
| 10 | 8 | 18 | 2.39x | 27–36 |
| 14 | 4 | 18 | 2.39x | 27–36 |
| 18 | 0 | 18 | 2.39x | 27–36 |

Every split summing to eighteen measures identically, to the digit. The
reason is the reservoir ceiling that landed beside it: with only
`max_power_source_bought_per_level: 1`, refunded points **cannot** be
spent on stamina or spirit, and at level 1 the skills they could go to
are already at their ceilings. The points come back and have nowhere to
go. So the simplest edit wins — the grant stays at `10` and the cap
comes down to `8`.

### What it cost: level 1 duels

Honestly, this is the bill:

| | L1 mean | under three | L8 mean | L15 mean |
|---|---|---|---|---|
| before | 4.47 | 2 of 45 | 4.78 | 4.76 |
| after | **3.01** | **26 of 45** | 4.21 | 4.51 |

First-level duels are short again — shorter than the state the flat ten
was written to repair, which reported a third of pairings under the
floor. This is accepted rather than missed, on two grounds.

The party is the unit that gates, and a party's first-level fights run
`4.1` rounds, inside the band. And the arithmetic admits no compromise:
a first-level character deals about `11` damage a round, so four rounds
of trading blows needs about `44` hit points between the two pools —
three times a starting constitution. **Either mastery starts far above
core, or first-level fights are quick.** The brief chose the first
clause; this is the second one arriving. Both design notes that claimed
otherwise have been rewritten rather than left standing.

Level 15 is *better* than before on the same measure: `0` of `45`
pairings under three, against `1`.

### Where it leaves the gates

| configuration | fails | day cleared, L1/L5/L10/L15 |
|---|---|---|
| before any of this | 1 | 4.99 / 4.35 / 5.25 / 4.53 |
| ladder only | 1 | 5.00 / 4.45 / 4.50 / 4.00 |
| **ladder + tuned progression** | **1** | 3.16 / 3.48 / 3.87 / 3.92 |

One failure throughout, and at the end it is the same hairline the
ladder alone carried: the level 5 spellblade exactly on the `85%`
reservoir bound. The day is the thing that changed most, and for the
better — it used to run from `5.25` of five encounters at level 10,
which is not a day, down to `4.00`; it now runs `3.16` to `3.92`, which
is the same day at every level.

### Still open

- **The level 5 spellblade.** It has been within a point of that bound
  through every configuration measured in this file, which makes it a
  question about that build rather than about any of these changes: a
  hybrid's reservoir buys it very little, and `Casting in Harness` was
  the last thing to move it.
- ~~**Whether the round band's floor should be level-aware.**~~
  Settled, and neither of the two answers offered here was the right
  one. Hit points measured in rounds turn out to be flat across the
  whole progression, so first-level damage is not too high for
  first-level hit points; and there is no curve for a level-aware floor
  to follow, only a single riser between level 1 and level 2. The
  entry in [DONE.md](DONE.md) has the measurements and the value.
