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
rolling, declare the difficulty you are attempting — the base, plus
however many steps you want. Then roll that skill as the
[[core-resolution|core roll]]. Meeting the declared difficulty means the
power works, at the scale you asked for.

## The cost

A successful power costs `{{ mechanics.cost_formula }}` points from its
[[power-sources|power source]], where the base cost is
{{ mechanics.base_cost }} and every point by which the roll beat the
difficulty takes {{ mechanics.cost_reduction_per_point_over }} off.

No power ever costs less than its declared difficulty divided by
{{ mechanics.minimum_cost_divisor }}, rounded down.

## One roll, two jobs

When a power is invoked on an action that uses the *same* skill — a
melee attack power rolled on melee attack, say — you make one roll and
it serves both purposes: first against the declared difficulty to settle
whether the power worked and what it cost, then against the target's
[[hitting|targeting difficulty]] to resolve the action itself. You never
roll twice for one swing.

## Failure

If the roll misses the declared difficulty, the power does not happen,
the action is spent, and you pay the minimum cost anyway.

## Minor powers

Some powers are marked **minor**. A minor power is declared, rolled and
paid for exactly like any other, with one difference: the minimum cost
does not apply to it, so its cost can fall to nothing. A failed minor
power therefore costs only the action.

Minor powers scale more slowly than standard ones — see
[[discipline-powers]], and the bolt spells in [[spell-list]].

## Example

Ashri has a melee attack skill of `9` and `14` stamina left. She invokes
Power Attack, whose base difficulty is `4` and which buys `1` damage per
`2` further points of difficulty. She declares a difficulty of `14`,
going for `5` extra damage.

She rolls `9`, for a total of `18`. That beats her declared `14`, so the
power works. The cost is the base cost plus `14` less `18` — which comes
out at `6`. The minimum for a difficulty of `14` is `4`, lower than `6`,
so she pays `6` and is left with `8` stamina.

Because Power Attack rolls on the same skill as the attack itself, that
same total of `18` is now compared to her target's targeting difficulty
to see whether the blow lands.

Had she rolled `2` instead, her total of `11` would have missed the
declared `14`: no power, no attack, and she would still owe the minimum
of `4`.

Now suppose she uses Precise Strike, a *minor* power, declaring a
difficulty of `3`. She rolls `8`, for `17` — beating the declared
difficulty by `14`. The base cost less `14` is below zero, and since a
minor power has no minimum, it costs her nothing at all.

{% book-only %}
## Design note

Declaring the difficulty before rolling is what stops powers becoming
free as characters improve. Under a fixed difficulty, expected cost is
roughly the difficulty less the skill, so any power with a set number
becomes free the moment skill passes it. Letting the character choose
how far to reach converts that problem into the interesting decision:
growing skill buys a *larger* effect at the same price rather than the
same effect at no price.

The minimum cost is the second half of that. Without it, a veteran
reaching a difficulty far below their skill would pay nothing however
much effect they asked for. With it, reaching further always costs more,
and stamina and spirit stay meaningful for a character who has been
adventuring for years.

Minor powers deliberately opt out of the minimum, and the cost formula
regulates them without needing a cap: a minor power reaches zero only
when the roll beats the declared difficulty by the full base cost, so
the reliably-free band is roughly the character's skill less the base
cost. That band widens as they improve. A minor power is what you always
have — the trick you can still pull on the fourth fight of a long day
with an empty reservoir, growing quietly more impressive as you do,
while never rivalling what you could do fresh.
{% endbook-only %}
