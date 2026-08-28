---
id: damage
title: Working Out Damage
tags: [core, combat, health]
summary: >
  Damage is the weapon's rating plus half the amount the attack beat the
  targeting difficulty, then reduced by armour and any block.
mechanics:
  margin_to_damage_fraction: 0.5
  round: down
  armour_reduces_each_blow: true
  block_reduces_with_armour_points: true
  damage_depletes_mastery_first: true
---

Damage is only worked out once a blow has landed — see [[hitting]].

## The raw figure

Take the weapon's **damage rating** and add
`{{ mechanics.margin_to_damage_fraction }}` times the amount by which
the attack roll beat the targeting difficulty, rounding
{{ mechanics.round }}. A weapon that beats a defence cleanly therefore
does noticeably more than one that scrapes past it.

## Reductions

The raw figure is then reduced:

- by the **armour rating** of whatever the target is wearing, applied to
  every blow — see [[armour]];
- and, if the defender was blocking, by the armour points of the weapon
  or shield used to block.

## Applying it

Whatever is left comes off the target's hit points, taking
[[hit-points|mastery hit points]] first and reaching core hit points
only once mastery is gone.
