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

Damage is only worked out once a blow has landed — see [[hitting]].

## The raw figure

Take the weapon's **damage rating** and add
`{{ mechanics.margin_to_damage_fraction }}` times the amount by which
the attack roll beat the targeting difficulty, rounding
{{ mechanics.round }}. A weapon that beats a defence cleanly therefore
does noticeably more than one that scrapes past it.

## Skill in the blow

Add one further point of damage for every
{{ mechanics.damage_per_attack_skill_step }} full ranks of the attack
skill you used, counting the bonus from its governing attribute.

This is the term that keeps the game moving. Attack and defence rise
together as characters advance, so the margin on a typical hit does not
grow — without a term tied directly to skill, a veteran's blows would
land exactly as hard as a novice's while everyone's
[[hit-points|mastery hit points]] climbed every level, and every fight
would take longer than the last one. A more practised fighter does not
merely connect more often; they land blows that matter.

## Reductions

The raw figure is then reduced:

- by the **armour rating** of whatever the target is wearing, applied to
  every blow — see [[armour]];
- and, if the defender was blocking, by the armour points of the weapon
  or shield used to block.

## The half a blow that always lands

Armour and a raised shield together may never take more than
{{ mechanics.max_reduction_fraction }} of a blow's raw damage. However
heavy the plate and however broad the shield, at least half of what got
through the defence gets through the armour too.

Without this floor the arithmetic breaks at the top end: plate and a
great shield subtract more than a sword's entire damage rating, so the
best-armoured character in the party stops being hard to kill and
becomes impossible to kill, and every light weapon in
[[weapons]] turns into a prop. The cap keeps heavy armour excellent
without letting it leave the game.

## Applying it

Whatever is left comes off the target's hit points, taking
[[hit-points|mastery hit points]] first and reaching core hit points
only once mastery is gone.
