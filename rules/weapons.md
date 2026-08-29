---
id: weapons
title: Weapons
tags: [equipment, reference, combat]
summary: >
  Weapon statistics: accuracy modifier, damage rating, size, and the
  armour points it contributes when used to block.
mechanics:
  finesse_size: S
  dagger:
    accuracy: 2
    damage: 4
    size: S
    block_ap: 2
    cost_gp: 2
  short_sword:
    accuracy: 1
    damage: 6
    size: S
    block_ap: 6
    cost_gp: 10
  hand_axe:
    accuracy: 0
    damage: 7
    size: S
    block_ap: 3
    cost_gp: 8
  staff:
    accuracy: 0
    damage: 5
    size: M
    block_ap: 7
    cost_gp: 1
  sword:
    accuracy: 1
    damage: 8
    size: M
    block_ap: 5
    cost_gp: 20
  battle_axe:
    accuracy: 0
    damage: 9
    size: M
    block_ap: 3
    cost_gp: 20
  two_handed_sword:
    accuracy: 0
    damage: 12
    size: L
    block_ap: 4
    cost_gp: 50
  great_axe:
    accuracy: 0
    damage: 12
    size: L
    block_ap: 2
    cost_gp: 45
---

Each weapon carries the statistics that feed [[hitting]] and
[[damage]]: an **accuracy** modifier to the attack roll, a **damage**
rating, a **size**, and the **block value** in armour points it
subtracts from a blow when you use it to block rather than dodge.

## Simple melee weapons

- **Dagger** — accuracy +{{ mechanics.dagger.accuracy }}, damage
  {{ mechanics.dagger.damage }}, size {{ mechanics.dagger.size }},
  block {{ mechanics.dagger.block_ap }},
  {{ mechanics.dagger.cost_gp }}gp.
- **Short sword** — accuracy +{{ mechanics.short_sword.accuracy }},
  damage {{ mechanics.short_sword.damage }}, size
  {{ mechanics.short_sword.size }}, block
  {{ mechanics.short_sword.block_ap }},
  {{ mechanics.short_sword.cost_gp }}gp.
- **Hand axe** — accuracy +{{ mechanics.hand_axe.accuracy }}, damage
  {{ mechanics.hand_axe.damage }}, size {{ mechanics.hand_axe.size }},
  block {{ mechanics.hand_axe.block_ap }},
  {{ mechanics.hand_axe.cost_gp }}gp.
- **Staff** — accuracy +{{ mechanics.staff.accuracy }}, damage
  {{ mechanics.staff.damage }}, size {{ mechanics.staff.size }}, block
  {{ mechanics.staff.block_ap }}, {{ mechanics.staff.cost_gp }}gp.

## Martial melee weapons

- **Sword** — accuracy +{{ mechanics.sword.accuracy }}, damage
  {{ mechanics.sword.damage }}, size {{ mechanics.sword.size }}, block
  {{ mechanics.sword.block_ap }}, {{ mechanics.sword.cost_gp }}gp.
- **Battle axe** — accuracy +{{ mechanics.battle_axe.accuracy }},
  damage {{ mechanics.battle_axe.damage }}, size
  {{ mechanics.battle_axe.size }}, block
  {{ mechanics.battle_axe.block_ap }},
  {{ mechanics.battle_axe.cost_gp }}gp.
- **Two-handed sword** — accuracy
  +{{ mechanics.two_handed_sword.accuracy }}, damage
  {{ mechanics.two_handed_sword.damage }}, size
  {{ mechanics.two_handed_sword.size }}, block
  {{ mechanics.two_handed_sword.block_ap }},
  {{ mechanics.two_handed_sword.cost_gp }}gp.
- **Great axe** — accuracy +{{ mechanics.great_axe.accuracy }}, damage
  {{ mechanics.great_axe.damage }}, size
  {{ mechanics.great_axe.size }}, block
  {{ mechanics.great_axe.block_ap }},
  {{ mechanics.great_axe.cost_gp }}gp.

## Finesse

A weapon of size {{ mechanics.finesse_size }} may use **dexterity**
instead of strength for its attack skill. Without this the game has no
nimble fighter in it at all: melee attack is a strength skill while
dodge is a dexterity one, so a character built around speed was obliged
to be bad at hitting things no matter which weapon they picked, and the
whole light-and-quick archetype collapsed into a worse heavy fighter.

Ranged weapons are not yet statted. The larger weapons are two-handed
and cannot be combined with a shield from [[armour]].
