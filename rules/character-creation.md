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
  max_starting_mastery_hp: 8
  free_starting_mastery_hp: 10
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

Everybody begins with {{ mechanics.free_starting_mastery_hp }} mastery
hit points, free and before anything is spent. Nobody chooses them and
nobody pays for them: a character who has survived long enough to become
an adventurer has learned something about not being hit.

You then have {{ mechanics.skill_point_pool }} points for skill ranks
and further mastery hit points together, spent at the same prices
[[advancement]] uses at every later level — there is no special chargen
exchange rate. You may **buy** at most
{{ mechanics.max_starting_mastery_hp }} mastery hit points on top of the
free ones.

## Languages

Take the languages your background gives you — see [[languages]]. They
are not skills and cost nothing at creation.

## Powers and money

Take {{ mechanics.starting_powers }} power (see [[using-powers]]) and
{{ mechanics.starting_gold }} gold pieces to equip yourself from
[[weapons]], [[ranged-weapons]] and [[armour]].

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

Of her pool for skills and mastery she puts `4` points into mastery hit
points, buying the maximum she is allowed, and the remaining `26` into
skill ranks — which at a point each in her focused group takes her melee
attack and block to their ceilings with plenty left for fortitude.

She takes Power Attack as her power, buys a sword, a shield and a chain
shirt, and pockets the change.

{% book-only %}
## Design note: the free ten

A first-level fight was measurably too short — duels averaged barely
above the three-round floor and a third of the pairings fell under it,
while the same builds at level `8` and `15` sat comfortably inside the
band. First level had too few hit points, and nothing else about it was
wrong.

The obvious lever was the cap on what a starting character may buy, and
it does work: raising it clears every short fight. It also quietly
raises the *price* of surviving, and the bill lands on whoever has the
least to spare. A caster raising its hit points that way pays in power
source — a level one wizard went from twenty-five spirit to nineteen,
which is two fewer spells in the only fight it will be in that day, and
raising the cap further made the same character give up on casting
altogether and buy an axe.

Granting the hit points instead costs nobody anything. The character
that results has the same hit points, the same skills and the same
reservoir it always had, and the fights come out the right length: mean
rounds of `5.65` at level `1` against `4.81` at level `8` and `5.77` at
level `15`,
which is as flat as this game has ever measured.

The general lesson is worth keeping. Raising a *cap* looks free and is
not — it changes what a build can afford, and the builds it changes
most are the ones already shortest of points.

## Design note: and then the ceiling came down anyway

Those numbers are no longer what this document measures, and the reason
is a deliberate decision taken later: **mastery hit points should start
at about the same size as core hit points**, so that the cushion in
front of a character's body is something they accumulate over a career
rather than something they are handed at creation. The ceiling on what a
starting character may buy came down accordingly, and a first-level
character now begins with roughly the mastery its constitution is worth
rather than several times it.

What that costs is exactly what the note above predicted it would buy,
run backwards. Mean duel length at level `1` is `3.01` rounds, with `26`
of the `45` pairings under three; at level `8` it is `4.21` and at level
`15` `4.51`. First-level duels are short again.

That is accepted rather than overlooked, for two reasons. A duel is not
the unit the game is balanced on — a **party's** fights run `4.1` rounds
at first level, comfortably inside the band, and that is the measure
that gates. And the arithmetic leaves no room to have it both ways: a
first-level character deals about `11` damage a round and would need
something near `44` hit points between them to trade blows for four
rounds, which is three times a starting constitution. Either mastery
starts far above core or first-level fights are quick. This ruleset now
chooses quick.

The grant-versus-cap lesson survives intact, and is now visible in the
numbers themselves: the free grant is larger than the amount a character
may buy on top of it. Most of a starting character's cushion is given,
and only the last of it is paid for.

## Design note

Creation and levelling deliberately use the same shop at the same
prices. There is nothing you can buy on levelling that you could not
have bought at the start, and nothing bought at the start that is later
closed to you, which removes a whole category of rules that would
otherwise need writing and reconciling.
{% endbook-only %}
