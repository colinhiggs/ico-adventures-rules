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
several. The grades you buy set which skill groups are focused,
unfocused and peripheral, per [[skills]].

## Skills and mastery hit points

You have {{ mechanics.skill_point_pool }} points for skill ranks and
mastery hit points together, spent at the same prices [[advancement]]
uses at every later level — there is no special chargen exchange rate.
You may start with at most {{ mechanics.max_starting_mastery_hp }}
mastery hit points.

## Languages

Take the languages your background gives you — see [[languages]]. They
are not skills and cost nothing at creation.

## Powers and money

Take {{ mechanics.starting_powers }} power (see [[using-powers]]) and
{{ mechanics.starting_gold }} gold pieces to equip yourself from
[[weapons]] and [[armour]].

## Priorities

Finally, apply your [[priorities]] — the trades that let one character
start stronger in an area at the cost of being weaker, or more
encumbered by circumstance, elsewhere.

## Example

Ashri's player spreads her attribute points to give her strength `16`,
constitution `14`, charisma `13`, intelligence `13`, dexterity `12` and
willpower `12`.

She spends her whole discipline budget on Martial, reaching Adept, which
focuses her combat skills and leaves every other group peripheral.

Of her pool for skills and mastery she puts `13` points into mastery hit
points, buying the maximum she is allowed, and the remaining `17` into
skill ranks — which at a point each in her focused group takes her melee
attack and block to their ceilings with a little left for fortitude.

She takes Power Attack as her power, buys a sword, a shield and a chain
shirt, and pockets the change.

{% book-only %}
## Design note

The opening mastery ceiling is deliberately generous compared with what
a level adds later. A starting character has almost no cushion in front
of their core hit points, and without a real opening reserve first-level
fights end in two exchanges. The rest of the curve is nearly flat by
comparison — see [[advancement]] — so this is the one point in a career
where hit points arrive in bulk.

Creation and levelling deliberately use the same shop at the same
prices. There is nothing you can buy on levelling that you could not
have bought at the start, and nothing bought at the start that is later
closed to you, which removes a whole category of rules that would
otherwise need writing and reconciling.
{% endbook-only %}
