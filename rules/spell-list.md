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
    damage: 6
    difficulty_per_step: 3
    damage_per_step: 1
    difficulty_per_extra_bolt: 8
    minimum_spirit: 0
  force_bolt:
    family: bolt
    damage_type: force
    domain: magic
  flame_bolt:
    family: bolt
    damage_type: fire
    domain: war
  frost_bolt:
    family: bolt
    damage_type: cold
    domain: nature
  shock_bolt:
    family: bolt
    damage_type: lightning
    domain: war
  lance:
    school: energy
    base_difficulty: 8
    damage: 10
    difficulty_per_step: 2
    damage_per_step: 1
    difficulty_per_extra_bolt: 20
    minimum_spirit: 2
    needs_attack_roll: true
    range: 10
    applies_condition: true
  force_lance:
    family: lance
    damage_type: force
    domain: magic
    condition: stunned
  flame_lance:
    family: lance
    damage_type: fire
    domain: war
    condition: burning
  frost_lance:
    family: lance
    damage_type: cold
    domain: nature
    condition: slowed
  storm_lance:
    family: lance
    damage_type: lightning
    domain: war
    condition: dazed
  burst:
    school: energy
    base_difficulty: 6
    template: circle
    area_archetype: concentrated
    minimum_spirit: 2
    needs_attack_roll: false
    applies_condition: true
  blast:
    school: energy
    base_difficulty: 6
    template: any
    area_archetype: balanced
    minimum_spirit: 2
    needs_attack_roll: false
  field:
    school: energy
    base_difficulty: 8
    template: circle
    area_archetype: diffuse
    minimum_spirit: 3
    needs_attack_roll: false
    duration_rounds: 2
    rounds_per_difficulty: 1
  force_burst:
    family: burst
    damage_type: force
    domain: magic
    condition: stunned
  flame_burst:
    family: burst
    damage_type: fire
    domain: war
    condition: burning
  frost_burst:
    family: burst
    damage_type: cold
    domain: nature
    condition: slowed
  storm_burst:
    family: burst
    damage_type: lightning
    domain: war
    condition: dazed
  force_blast:
    family: blast
    damage_type: force
    domain: magic
  flame_blast:
    family: blast
    damage_type: fire
    domain: war
  frost_blast:
    family: blast
    damage_type: cold
    domain: nature
  storm_blast:
    family: blast
    damage_type: lightning
    domain: war
  force_field:
    family: field
    damage_type: force
    domain: magic
  flame_field:
    family: field
    damage_type: fire
    domain: war
  frost_field:
    family: field
    damage_type: cold
    domain: nature
  storm_field:
    family: field
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

## The lances

Where a bolt is what a caster throws when there is nothing left, a
**lance** is what they open with. One spell again written four times,
sharing a chassis:

- **School:** {{ mechanics.lance.school }}
- **Range:** {{ mechanics.lance.range }}, aimed with the casting roll
- **Base difficulty:** {{ mechanics.lance.base_difficulty }}
- **Damage:** {{ mechanics.lance.damage }}, plus
  {{ mechanics.lance.damage_per_step }} for each further
  {{ mechanics.lance.difficulty_per_step }} points of difficulty
- **Minimum spirit:** {{ mechanics.lance.minimum_spirit }}

A lance that hits also applies a **condition**, which the target may
resist — see [[conditions]]. That is what a lance buys over a bolt, and
why it is worth the spirit a bolt does not cost.

The variants differ in damage type, domain, and which condition they
carry:

- **Force Lance** — {{ mechanics.force_lance.damage_type }} damage,
  domain of {{ mechanics.force_lance.domain }}, leaves the target
  **{{ mechanics.force_lance.condition }}**.
- **Flame Lance** — {{ mechanics.flame_lance.damage_type }} damage,
  domain of {{ mechanics.flame_lance.domain }}, leaves the target
  **{{ mechanics.flame_lance.condition }}**.
- **Frost Lance** — {{ mechanics.frost_lance.damage_type }} damage,
  domain of {{ mechanics.frost_lance.domain }}, leaves the target
  **{{ mechanics.frost_lance.condition }}**.
- **Storm Lance** — {{ mechanics.storm_lance.damage_type }} damage,
  domain of {{ mechanics.storm_lance.domain }}, leaves the target
  **{{ mechanics.storm_lance.condition }}**.

Which lance to carry is a question about the fight rather than about the
numbers: they deal the same damage, and the condition is the whole
difference.

## The area spells

Three families, and each of the four damage types appears in all three.
None of them needs an attack roll: everything under the template takes
the damage, and having nothing to dodge is what an area spell buys with
its difficulty.

The family decides what kind of spell it is; the damage type decides how
it looks and, for a burst, what it leaves behind.

### Bursts — {{ mechanics.burst.area_archetype }}

*Base difficulty {{ mechanics.burst.base_difficulty }}, circle,
minimum spirit {{ mechanics.burst.minimum_spirit }}.*

Small and fierce, and the only area family that applies a condition —
the same conditions the lances carry, resisted the same way. See
[[conditions]].

- **Force Burst** — {{ mechanics.force_burst.damage_type }} damage,
  leaves the target **{{ mechanics.force_burst.condition }}**.
- **Flame Burst** — {{ mechanics.flame_burst.damage_type }} damage,
  leaves the target **{{ mechanics.flame_burst.condition }}**.
- **Frost Burst** — {{ mechanics.frost_burst.damage_type }} damage,
  leaves the target **{{ mechanics.frost_burst.condition }}**.
- **Storm Burst** — {{ mechanics.storm_burst.damage_type }} damage,
  leaves the target **{{ mechanics.storm_burst.condition }}**.

### Blasts — {{ mechanics.blast.area_archetype }}

*Base difficulty {{ mechanics.blast.base_difficulty }}, minimum spirit
{{ mechanics.blast.minimum_spirit }}.*

A blast takes **any template in [[spell-area]]** — circle, cone, line,
square or rectangle — chosen as it is cast. That flexibility is the
family's whole character: a blast carries no condition and lasts no
time, but it is the only area spell that can be poured down a corridor
or swept across a rank.

Force, Flame, Frost and Storm Blast differ only in damage type and
domain.

### Fields — {{ mechanics.field.area_archetype }}

*Base difficulty {{ mechanics.field.base_difficulty }}, circle,
minimum spirit {{ mechanics.field.minimum_spirit }}.*

A field does not go off; it stays. It lasts
{{ mechanics.field.duration_rounds }} rounds, plus
{{ mechanics.field.rounds_per_difficulty }} for each further point of
difficulty spent on duration, and anything inside it takes the damage at
the start of its turn. Wide, weak, and the only way a caster denies
ground rather than clearing it.

Force, Flame, Frost and Storm Field differ only in damage type and
domain.

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

Their boost rate is deliberately poor while their base damage is not.
That combination is what makes a bolt a floor rather than a ceiling: it
opens respectably and then barely improves however hard it is pushed, so
it is worth having with an empty reservoir and never worth preferring to
a lance when there is spirit to spend.

The base was raised once the lances existed. Measured against a caster's
new best turn, the old bolt left an empty caster on under a quarter of
their output -- past diminished and into sidelined, which is exactly what
the minor tier exists to prevent. The rate was left alone, because the
rate is what keeps minor and standard apart.

Cure Wounds stays standard rather than minor for the same reason from
the other direction. Healing available on demand for nothing would empty
every fight of consequence, since any damage that did not drop a
character outright could simply be undone afterwards at no cost.
{% endbook-only %}
