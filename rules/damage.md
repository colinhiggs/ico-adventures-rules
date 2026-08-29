---
id: damage
title: Working Out Damage
tags: [core, combat, health]
summary: >
  Damage is the weapon's rating plus half the amount the attack beat the
  targeting difficulty, then reduced by armour and any block.
mechanics:
  margin_to_damage_fraction: 0.5
  damage_per_attack_skill_step: 8
  round: down
  armour_reduces_each_blow: true
  max_reduction_fraction: 0.5
  block_reduces_with_armour_points: true
  damage_depletes_mastery_first: true
---

Damage is worked out only once a blow has landed — see [[hitting]].

## The raw figure

Take the weapon's **damage rating** and add
`{{ mechanics.margin_to_damage_fraction }}` times the **margin** — the
amount by which the attack roll beat the targeting difficulty —
rounding {{ mechanics.round }}.

## Skill in the blow

Add one further point of damage for every
{{ mechanics.damage_per_attack_skill_step }} full ranks of the attack
skill you used, counting the bonus from its governing attribute.

## Reductions

The raw figure is then reduced:

- by the **armour rating** of whatever the target is wearing, applied to
  every blow — see [[armour]];
- and, if the defender was blocking, by the armour points of the weapon
  or shield used to block.

Armour and a raised shield together may never take more than
{{ mechanics.max_reduction_fraction }} of a blow's raw damage. However
heavy the plate and however broad the shield, at least half of what got
through the defence gets through the armour too.

## Applying it

Whatever is left comes off the target's hit points, taking
[[hit-points|mastery hit points]] first and reaching core hit points
only once mastery is gone.

## Example

Continuing the blow from [[hitting]]: Ashri landed on Bramm with a
margin of `8`, using a sword rated at `8` damage, with an attack skill
of `9`. Bramm is in chain mail rated `5`, and he was dodging, so no
shield applies.

- Weapon damage: `8`.
- Margin: `8`, halved and rounded down, is `4`.
- Skill: `9` ranks at one point per eight full ranks is `1`.
- Raw figure: `8` plus `4` plus `1`, which is `13`.
- Reduction: chain mail takes `5`. That is less than half of `13`, so
  the cap does not bite.
- Damage dealt: `8`.

Those `8` come off Bramm's mastery hit points first.

Had Bramm been in full plate behind a great shield, his reduction would
have come to `13` — the entire blow. The cap stops that: reduction is
held to half of `13`, so `6` gets through regardless.

{% book-only %}
## Design note

Two terms here exist to solve the same problem from opposite ends.

The skill term keeps the game moving as characters advance. Attack and
defence rise together, so the margin on a typical hit does not grow;
without a term tied directly to skill, a veteran's blows would land
exactly as hard as a novice's while everyone's mastery hit points
climbed every level, and every fight would take longer than the last.

The reduction cap stops the arithmetic breaking at the top end. Plate
and a great shield subtract more than a sword's entire damage rating, so
without a cap the best-armoured character in the party stops being hard
to kill and becomes impossible to kill, while every light weapon in
[[weapons]] turns into a prop.
{% endbook-only %}
