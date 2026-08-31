---
id: spell-properties
title: Standard Spell Properties
tags: [magic, reference]
summary: >
  Range, duration, area and accuracy work the same across almost all
  spells, and can usually be boosted by casting at a higher difficulty.
mechanics:
  long_range_multiplier: 2
  range_extend_squares_per_difficulty: 1
  base_accuracy: 0
  accuracy_bonus_per_difficulty: 1
---

Most spells share these properties. Unless a spell says otherwise, each
can be boosted by choosing to cast at a higher difficulty than the
minimum — see [[spellcasting]] and [[using-powers]] for what raising
the difficulty costs.

## Range

A spell's range is **self**, **touch**, or a **number**.

- **Self** — the spell only ever affects the caster.
- **Touch** — the caster affects themselves or another recipient by
  touching them. Touching an unwilling target needs a melee attack roll.
- **A number** — a range in grid squares, measured exactly as
  [[movement]] measures them. If the spell needs an
  attack roll to land, the listed number is short range and long range
  is {{ mechanics.long_range_multiplier }} times it; use the ranged
  attack skill to hit. Range can be extended by
  {{ mechanics.range_extend_squares_per_difficulty }} square per point
  of added difficulty.

## Duration and area of effect

These are defined per spell for now; there is no general rule yet.

## Accuracy

A spell's standard accuracy is
`{{ mechanics.base_accuracy }}` — no bonus or penalty to the attack
roll. Accuracy increases by
`+{{ mechanics.accuracy_bonus_per_difficulty }}` for every point of
added difficulty.

## Example

Sela casts a bolt at a target `14` squares away. The spell's listed
range is `10`, which is short range; long range is double that, so `14`
is within reach but at long range.

She would rather not rely on that, so she boosts the range instead:
each point of added difficulty extends it by a square, so declaring `4`
points above the base brings the target inside short range. Those `4`
points are added to the difficulty she declares, and are paid for in
spirit exactly as any other reach would be.

Because the bolt needs an attack roll, she uses her ranged attack skill
to place it, not her spellcasting skill — spellcasting settled whether
the spell happened at all.

{% book-only %}
## Design note

Boosting works through the same declared-difficulty mechanism as every
other power, so there is no separate list of metamagic rules to learn.
A caster who understands how reaching further works for a physical power
already understands how it works for range, accuracy and area.

Spell ranges count the same squares movement does, rather than carrying
a measure of their own. A caster who knows how far they can walk knows
how far they can reach, and nobody converts units mid-fight.
{% endbook-only %}
