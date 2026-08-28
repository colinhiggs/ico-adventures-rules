---
id: core-resolution
title: The Core Roll
tags: [core, resolution]
summary: >
  Most actions are a d20 plus bonuses against either a fixed difficulty
  or an opposed roll. Beating the target by more means a better result.
mechanics:
  standard_die: "1d20"
  higher_beats_lower: true
  beating_target_scales_outcome: true
---

When the outcome of an action is in doubt, you roll for it, and it is
almost always the same roll.

## The roll

Roll `{{ mechanics.standard_die }}` and add your bonuses — from
attributes, from the relevant skill, and from environmental factors the
Dungeon Master calls out. Compare the total to a target, which is
either:

- a fixed **difficulty** set by the Dungeon Master, or
- an **opposed** roll: someone else's `{{ mechanics.standard_die }}`
  plus their own bonuses.

Meet or beat the target and you succeed.

## Margin matters

Beating the target by more points is a better outcome, not just a
success: more damage on a blow, less effort spent on a power, a faster
or cleaner result. Individual rules say how their own margin is spent —
see [[hitting]] and [[damage]] for the combat case, and [[using-powers]]
for powers.
