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
  focused_skill_groups: 1
  unfocused_skill_groups: 1
  max_starting_mastery_hp: 15
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

## Skill focus

Choose {{ mechanics.focused_skill_groups }} skill group to be
**focused** and {{ mechanics.unfocused_skill_groups }} to be
**unfocused**. Every other group is **peripheral**. What these tiers
mean for how far a skill can be pushed is covered in [[skills]].

## Mastery hit points and skill points

Choose how many mastery hit points to start with, up to
{{ mechanics.max_starting_mastery_hp }}. Your starting skill points are
{{ mechanics.skill_point_pool }} minus that number — every mastery hit
point is a skill point you did not spend.

## Powers and money

Take {{ mechanics.starting_powers }} power (see [[using-powers]]) and
{{ mechanics.starting_gold }} gold pieces to equip yourself from
[[weapons]] and [[armour]].

## Priorities

Finally, apply your [[priorities]] — the trades that let one character
start stronger in an area at the cost of being weaker, or more
encumbered by circumstance, elsewhere.
