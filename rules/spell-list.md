---
id: spell-list
title: The Spell List
tags: [magic, reference]
summary: >
  The spells defined so far. The bolts are minor spells — weak, endlessly
  repeatable, and what a caster falls back on with an empty reservoir.
mechanics:
  list_incomplete: true
  bolt:
    tier: minor
    base_difficulty: 2
    school: energy
    range: 10
    needs_attack_roll: true
    damage: 4
    difficulty_per_step: 3
    damage_per_step: 1
    difficulty_per_extra_bolt: 8
    minimum_spirit: 0
  force_bolt:
    damage_type: force
    domain: magic
  flame_bolt:
    damage_type: fire
    domain: war
  frost_bolt:
    damage_type: cold
    domain: nature
  shock_bolt:
    damage_type: lightning
    domain: war
  cure_wounds:
    base_difficulty: 16
    school: life_force
    domain: healing
    range: touch
    minimum_spirit: 1
---

Difficulty, cost and boosting all work as [[spellcasting]] and
[[spell-properties]] describe. A spell marked **minor** is a minor
power, and the minimum cost does not apply to it — see [[using-powers]].

## The bolts

The bolts are one spell written several times, differing only in the
damage they deal. Every one of them shares a chassis:

- **Tier:** {{ mechanics.bolt.tier }}
- **School:** {{ mechanics.bolt.school }}
- **Range:** {{ mechanics.bolt.range }}, needing a ranged attack roll
- **Base difficulty:** {{ mechanics.bolt.base_difficulty }}
- **Damage:** {{ mechanics.bolt.damage }}
- **Minimum spirit:** {{ mechanics.bolt.minimum_spirit }}

and both standard boosts:

- **More damage:** {{ mechanics.bolt.damage_per_step }} per further
  {{ mechanics.bolt.difficulty_per_step }} points of difficulty.
- **More bolts:** one extra bolt per further
  {{ mechanics.bolt.difficulty_per_extra_bolt }} points of difficulty.

The variants are then only a damage type and a domain:

- **Force Bolt** — {{ mechanics.force_bolt.damage_type }} damage, domain
  of {{ mechanics.force_bolt.domain }}.
- **Flame Bolt** — {{ mechanics.flame_bolt.damage_type }} damage, domain
  of {{ mechanics.flame_bolt.domain }}.
- **Frost Bolt** — {{ mechanics.frost_bolt.damage_type }} damage, domain
  of {{ mechanics.frost_bolt.domain }}.
- **Shock Bolt** — {{ mechanics.shock_bolt.damage_type }} damage, domain
  of {{ mechanics.shock_bolt.domain }}.

Because the domain differs, a caster's [[discipline-powers|Granted
Domain]] makes one bolt markedly cheaper than the rest — a priest of war
throws flame where a druid throws frost, without either of them needing
a separate rule.

The boost rates above are deliberately poorer than an earlier draft's,
which gave a bolt an extra point of damage for every single point of
difficulty. A spell that costs nothing to cast cannot also be the best
damage in the game; a bolt is the thing a caster does when they have
nothing left, not the thing they open with.

## Cure / Cause Wounds ({{ mechanics.cure_wounds.base_difficulty }})

- **School:** {{ mechanics.cure_wounds.school }}
- **Domain:** {{ mechanics.cure_wounds.domain }}, or harm when reversed
- **Range:** {{ mechanics.cure_wounds.range }}
- **Minimum spirit:** {{ mechanics.cure_wounds.minimum_spirit }}

Restores hit point damage to the recipient. Cast as *Cause Wounds*, the
same spell instead inflicts damage. This one is a standard spell, not a
minor one: healing on demand for nothing would empty every fight of
consequence.
