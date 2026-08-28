---
id: priorities
title: Setting Priorities
tags: [character, setup]
summary: >
  A pool of priority points buys advantages at character creation, and
  can be topped up by taking matching disadvantages.
mechanics:
  standard_priority_points: 4
  attribute_points_per_point: 4
  skill_points_per_point: 5
  gold_gained_per_point: 500
  gold_lost_per_point: 100
  power_source_bonus_per_point: 3
---

Each character gets a number of **priority points** set by the Dungeon
Master; the standard allowance is
{{ mechanics.standard_priority_points }}. Spend them on advantages, and
take disadvantages to get more. This is done once, as part of
[[character-creation]].

## Attributes

- Spend `1` point for {{ mechanics.attribute_points_per_point }} extra
  attribute points.
- Gain `1` point by giving up
  {{ mechanics.attribute_points_per_point }} attribute points.

## Skills

- Spend `1` point for {{ mechanics.skill_points_per_point }} extra skill
  points, up to the normal skill maxima.
- Spend `1` point to raise the maximum level of a single skill by one
  step; this persists as the character advances.
- Gain `1` point by giving up {{ mechanics.skill_points_per_point }}
  skill points.

## Powers

- Spend `1` point for one extra power.
- Gain `1` point by taking one fewer power.
- Spend `1` point for a permanent
  `+{{ mechanics.power_source_bonus_per_point }}` bonus to one power
  source. This may only be taken once.

## Wealth and circumstance

- Spend `1` point for {{ mechanics.gold_gained_per_point }} extra
  starting gold.
- Spend `1` point for low-level connections;
  spend two for high-level connections.
- Spend two points to begin play landed.
- Gain `1` point by starting with
  {{ mechanics.gold_lost_per_point }} less gold.
- Gain `1` point by taking low-level enemies;
  gain two by taking high-level enemies.
