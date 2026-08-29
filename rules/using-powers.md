---
id: using-powers
title: Using a Power
tags: [core, powers]
summary: >
  Declare how hard you are pushing, roll the power's skill against that
  difficulty, and pay 10 plus the difficulty minus your roll — never
  less than a third of the difficulty, unless the power is minor.
mechanics:
  base_cost: 10
  cost_reduction_per_point_over: 1
  cost_formula: "base_cost + difficulty - skill_roll"
  minimum_cost_divisor: 3
  minor_powers_ignore_minimum_cost: true
  difficulty_declared_before_rolling: true
  failure_spends_the_action: true
  failure_costs_the_minimum: true
  one_roll_serves_both_when_skills_match: true
---

## Declare, then roll

Every power lists a **base difficulty**, a **skill**, and a **step**:
how much extra difficulty buys one more increment of effect. Before
rolling, you declare the difficulty you are attempting — the base, plus
however many steps you want. Then roll that skill as the
[[core-resolution|core roll]]. Meeting the declared difficulty means the
power works, at the scale you asked for.

This is why a power never becomes free with experience. Growing skill
does not make the same effect cheaper; it makes a *larger* effect
reachable at the same price. The scaling steps for each power are given
in [[general-powers]] and [[discipline-powers]]; spells work the same
way and call it boosting, in [[spell-properties]].

## The cost

A successful power costs
`{{ mechanics.cost_formula }}` points from its
[[power-sources|power source]], where the base cost is
{{ mechanics.base_cost }} and every point by which the roll beat the
difficulty takes {{ mechanics.cost_reduction_per_point_over }} off.

No power ever costs less than its declared difficulty divided by
{{ mechanics.minimum_cost_divisor }}, rounded down. Reaching further
always costs more, however good the roll, and this floor is what keeps
stamina and spirit meaningful for a veteran.

## One roll, two jobs

When a power is invoked on an action that uses the *same* skill — a
melee attack power rolled on melee attack, say — you make one roll and
it serves both purposes: first against the declared difficulty to
settle whether the power worked and what it cost, then against the
target's [[hitting|targeting difficulty]] to resolve the action itself.
You never roll twice for one swing.

## Minor powers

Some powers are marked **minor**. A minor power is declared, rolled and
paid for exactly like any other, with one difference: the minimum cost
does not apply to it. Beat the difficulty well enough and a minor power
costs nothing at all.

That does not make minor powers free on demand. The cost formula still
runs, so a minor power costs nothing only when the roll beats the
declared difficulty by the full base cost — which means the difficulty
you can reliably get for nothing is roughly your skill less the base
cost, and no higher. Reach past that band and a minor power costs
stamina or spirit like anything else.

The band widens as the character improves, and that is the point. A
minor power is what you always have: the trick you can still pull on the
fourth fight of a long day with an empty reservoir, growing quietly more
impressive as you do, while never rivalling what you could do fresh.
Minor powers scale more slowly than standard ones for exactly that
reason — see [[discipline-powers]], and the bolt spells in
[[spell-list]], which are the magical case.

## Failure

If the roll misses the declared difficulty, the power does not happen,
the action is spent, and you pay the minimum cost anyway — which for a
minor power is nothing, so a failed minor power costs only the action. That risk is
the reason not to declare the highest difficulty you can imagine every
time: pushing further increases the effect, the price, and the chance
of getting nothing.
