---
id: experience
title: Experience
tags: [core, character, progression]
summary: >
  Experience is advancement points, one for one, awarded for milestones
  the adventure names rather than for bodies. Spend it as it arrives;
  your career total is what sets your level.
mechanics:
  xp_per_point: 1
  milestone_minor: 2
  milestone_major: 5
  milestone_adventure: 8
  awarded_to_everyone_present: true
  career_xp_sets_level: true
  unspent_xp_carries_over: true
---

Experience points **are** the points [[advancement]] hands out. One
experience point is {{ mechanics.xp_per_point }} advancement point, and
there is no exchange rate, no table to look up and no waiting for a
level before you may spend it. The shop from [[character-creation]] is
open, it has always been open, and experience is simply how you come to
have money in it.

## What a milestone is worth

Experience is awarded for **milestones**, which the adventure names in
advance. There are three sizes:

- **Minor** — {{ mechanics.milestone_minor }} points. A scene resolved
  in a way that mattered: a witness who talked, a door opened without
  waking the house, a bargain struck that held.
- **Major** — {{ mechanics.milestone_major }} points. An objective the
  adventure was built around. Usually two or three of these exist and
  usually not all of them are reached.
- **Completing the adventure** — {{ mechanics.milestone_adventure }}
  points, for reaching an ending rather than the best ending. A party
  that got out alive having failed at most of it still learned the
  trade.

Every character present takes the **full award**. Nothing is divided by
the size of the party, because a milestone is a thing that happened and
not a pile of coins.

### What an adventure should put on the table

The slate is declared for a party that does well, not for one that does
everything. A typical adventure offers two majors, two minors and its
ending, which is `22` points if every one of them is taken. A party that
reaches the ending and most of what was on offer takes about
{{ advancement:mechanics.points_per_level }}, and that is the pace this
is written for: **one adventure, one level**. A party that gets out with
nothing but the ending takes `8` and has still moved.

A party that takes all of it advances a little faster than a level an
adventure, and should. The slack is the reward, and it is small enough
that it cannot run away.

A campaign that wants slower going declares a thinner slate rather than
making each milestone worth less. The sizes above are the unit of
account and moving them moves every adventure ever written.

## Two numbers, and only one of them goes down

Write down both:

- **Career** — every point you have ever been awarded. It only ever
  rises. Your **level** is your career total divided by
  {{ advancement:mechanics.points_per_level }}, rounded down, and then
  one more, so a character begins play at level one with a career of
  nothing.
- **Unspent** — what you have not yet spent. It falls when you buy
  something and it carries over indefinitely, which is what lets you
  save toward a grade you cannot afford outright.

Keeping them apart is what stops a character buying their way back down
a level. Spending is a decision about what you are; your level is a
record of what you have done.

## What still happens at a level

Crossing a level is not the moment you get your points — you already
had those. It is the moment [[advancement]]'s other grants land: the
free mastery hit points, the power, a rank of headroom on every ceiling
in [[skills]], and every fourth level an attribute point. The purchase
ceilings are per level and cumulative there too, so a level crossed
without spending is not a level wasted.

The level requirement on a Master grade in [[disciplines]] is checked
against your career total like any other, which means you can be holding
enough unspent points for a Master you are not yet senior enough to buy.

## Example

Sela's party finish *The Miller's Coin*. Along the way they got the
miller's daughter out of the mill alive, which was a minor milestone
worth `2`, and they broke the band at the ford, which was a major one
worth `5`. Reaching an ending is worth `8`. Everyone present takes all
three: `15` points each, and Bramm — who spent most of the last scene
unconscious — takes exactly the same `15`, because he was there.

Sela began the adventure with a career of `26` and `4` unspent, which
put her at level `2`. Her career is now `41`, so she is level `3`: she
crossed the boundary at `30`, part way through the fight at the ford.

At that boundary she took her free mastery hit points, a power, and a
rank of headroom on every ceiling. Level `3` is not divisible by four,
so no attribute point this time.

That leaves her `19` unspent. She spends `15` of it on Adept in
Martial — a grade she has been saving for since two adventures ago —
and keeps the last `4` in hand.

{% book-only %}
## Design note: why the two currencies collapsed

Most games run experience as a separate currency that converts into
advancement at a shifting rate, because most games make later levels
cost more. This one does not, and the reason is measured rather than
felt.

A level here is worth the same at the top of the game as at the bottom.
It is always {{ advancement:mechanics.points_per_level }} points, and
the simulator says the game does not get slower or faster with them:
fights run about five rounds at first level and about five at fifteenth,
a drift of `1.04`. A rising cost curve asserts that a late level is a
bigger prize than an early one. Nothing here supports that, so charging
more for one would be a fiction the rest of the system contradicts.

Once every level costs the same, the second currency has nothing to do.
Experience can simply *be* the points, and the exchange rate is written
down as {{ mechanics.xp_per_point }} rather than as a table. The whole
of the conversion machinery — thresholds, tiers, the awkward stretch
where you have earned most of a level and can do nothing with it —
disappears, and what is left is a character who gets a little better on
the evening they earned it.

That identity is why this document does not declare how much a level
costs. It reads it out of [[advancement]], because it is not a second
fact. Move the budget there and the cost of a level moves with it, which
is correct: they were always the same number wearing two hats.

## Design note: why milestones, and what comes next

**Threat is meant to become a milestone too.** The obvious way to earn
experience is to earn it from what you defeated, every creature already
carries a `challenge_level`, and a hybrid of the two is where this is
headed. It is not here yet for a specific reason: nothing has measured
`challenge_level`. It is an author's estimate, and the simulator cannot
yet load a creature and pit it against the archetype panel the way the
archetypes are pitted against each other. Every other number in these
rules is measured, and denominating the entire advancement economy in a
guess would be the one place that stopped being true.

So the shape of this document is deliberate: an award is a milestone
with a size, and a threat award will be another kind of milestone
rather than a second system bolted alongside. When the creature loader
lands, `challenge_level` becomes a fourth entry in the list above and
nothing else here has to move.

Three other ways to earn it were considered and set aside.

**Gold.** The oldest answer, and a poor fit here. The equipment table
was deliberately compressed so that the gap between the cheapest and
the dearest weapon is small; equipment is explicitly not a progression
axis in this game, so making wealth the engine of progression would
push hard against a decision taken elsewhere on purpose.

**Practice — you advance what you use.** Thematically the best of them,
and structurally the worst. Ico has no classes and buys specialisation
in pieces, so "you get better at what you did" is the same idea from
the other end. But it fragments experience into a pool per skill, and
then there is no single number left for a level to derive from — the
ceilings, the attribute every fourth level and the Master gate all lose
their clock. It would need a second currency to put the clock back,
which is precisely what the design above got rid of.

**Adversity — experience for what nearly killed you.** Unusual, and the
system is already instrumented for it, with two hit point pools and a
dying rule. It pays out for recklessness and taxes competence: a party
that scouts, opens from hiding and wins cleanly would advance slower
than one that blundered in. That is a strange thing to teach.

## Design note: a known softness at the top

One number this rests on is not yet true at the top of the game. A
level is worth {{ advancement:mechanics.points_per_level }} points
everywhere, and at the top of the game a fifth of them buy nothing that
can be measured — partly points nobody can place, and mostly a power
source reservoir far past the size any fight can empty. The share is
about a fourteenth at level five and a seventh at level ten, so it
grows with the career. The flat cost charges as though none of that were
happening.

The fix is a change to the advancement menu rather than anything in this
document, and it is worth making before these numbers are treated as
settled. What is written here is honest about the middle of the game,
where it was designed, and slightly generous to the top, where the menu
runs out before the budget does.
{% endbook-only %}
