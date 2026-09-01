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
  flame_burst:
    school: energy
    domain: war
    damage_type: fire
    base_difficulty: 4
    template: circle
    area_archetype: concentrated
    minimum_spirit: 1
    needs_attack_roll: false
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

## Flame Burst ({{ mechanics.flame_burst.base_difficulty }})

- **School:** {{ mechanics.flame_burst.school }}
- **Domain:** {{ mechanics.flame_burst.domain }}
- **Template:** {{ mechanics.flame_burst.template }}, priced as a
  {{ mechanics.flame_burst.area_archetype }} area — see [[spell-area]]
- **Damage type:** {{ mechanics.flame_burst.damage_type }}
- **Minimum spirit:** {{ mechanics.flame_burst.minimum_spirit }}

Fire blooms outward from a point the caster can see. Everything in the
circle takes the damage; there is no attack roll to make and nothing to
dodge, which is what an area spell buys with its difficulty.

Being concentrated, it is dear to spread and cheap to sharpen: a small
fierce burst rather than a blanket of flame.

## Cure / Cause Wounds ({{ mechanics.cure_wounds.base_difficulty }})

- **School:** {{ mechanics.cure_wounds.school }}
- **Domain:** {{ mechanics.cure_wounds.domain }}, or harm when reversed
- **Range:** {{ mechanics.cure_wounds.range }}
- **Minimum spirit:** {{ mechanics.cure_wounds.minimum_spirit }}

Restores hit point damage to the recipient. Cast as *Cause Wounds*, the
same spell instead inflicts damage. This is a standard spell, not a
minor one.

## Example

Sela has a spellcasting skill of `18` and no spirit left at all.

She casts Force Bolt, declaring its base difficulty with no boosts. She
rolls `7`, for a total of `25` — beating the declared difficulty by far
more than the base cost, so the bolt costs her nothing. She still has to
land it: the bolt needs a ranged attack roll, as [[spell-properties]]
describes.

Fresh, she would have declared much higher. At a difficulty of `14` the
same spell buys four steps of extra damage, and at `18` she could
instead have thrown a second bolt. Both would have cost real spirit.

The bolt she throws with an empty reservoir is a fraction of the one she
opens a fight with — but she is still casting, and still choosing a
damage type to suit the target.

{% book-only %}
## Design note

The bolts are one spell written several times because a family of
identical spells differing only in damage type is a table, not four
rules. Keeping the shared numbers in one place means the family cannot
drift apart as it grows, and adding a fifth bolt is an entry rather than
a rewrite.

Their boost rates are deliberately poor. A spell that can cost nothing
to cast cannot also be the best damage in the game; a bolt is the thing
a caster does when they have nothing left, not the thing they open
with.

Cure Wounds stays standard rather than minor for the same reason from
the other direction. Healing available on demand for nothing would empty
every fight of consequence, since any damage that did not drop a
character outright could simply be undone afterwards at no cost.
{% endbook-only %}
