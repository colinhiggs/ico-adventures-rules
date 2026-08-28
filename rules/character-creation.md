---
id: character-creation
title: Creating a Character
tags: [character, setup]
summary: >
  Spend a fixed pool of attribute points, choose skill focus, trade
  mastery hit points against skill points, take one power, and start
  with a set purse.
mechanics:
  attribute_points: 80
  attribute_min: 3
  attribute_max: 18
  starting_discipline_budget: 20
  max_starting_mastery_hp: 25
  skill_point_pool: 30
  starting_powers: 1
  starting_gold: 150
---

Build a starting character in this order.

## Attributes

Split {{ mechanics.attribute_points }} points among the six
[[attributes]]. No score may start below {{ mechanics.attribute_min }}
or above {{ mechanics.attribute_max }}. Race modifiers apply after this
spread, and the bonus for a high score is worked out from the final
number.

## Disciplines

Spend a budget of {{ mechanics.starting_discipline_budget }} points on
[[disciplines]]. That is enough for Adept in one, or Initiate in
several — the first is a specialist, the second a generalist, and both
are legitimate opening positions. The grades you buy set which skill
groups are focused, unfocused and peripheral, per [[skills]].

## Mastery hit points and skill points

You have {{ mechanics.skill_point_pool }} points for skill ranks and
mastery hit points together, spent at the same prices [[advancement]]
uses at every later level — there is no special chargen exchange rate.
You may start with at most
{{ mechanics.max_starting_mastery_hp }} mastery hit points however much
you are willing to spend.

That ceiling is deliberately generous compared with what a level adds
later. A starting character has almost no cushion in front of their
core hit points, and without a real opening reserve first-level fights
end in two exchanges.

## Powers and money

Take {{ mechanics.starting_powers }} power (see [[using-powers]]) and
{{ mechanics.starting_gold }} gold pieces to equip yourself from
[[weapons]] and [[armour]].

## Priorities

Finally, apply your [[priorities]] — the trades that let one character
start stronger in an area at the cost of being weaker, or more
encumbered by circumstance, elsewhere.
