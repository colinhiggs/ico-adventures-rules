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
  success_on_matching_target: true
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

Meet or beat the target and you succeed. A total exactly equal to the
target is a success.

## Margin matters

Beating the target by more points is a better outcome, not merely a
success: more damage on a blow, less effort spent on a power, a faster
or cleaner result. Each rule says how its own margin is spent — see
[[hitting]] and [[damage]] for the combat case, and [[using-powers]]
for powers.

## Example

Ashri wants to force a stuck door. The Dungeon Master sets a difficulty
of `15`. Ashri has a relevant skill of `+3` and a strength bonus of
`+2`, so she rolls the die and adds `5`.

She rolls `10`, for a total of `15`. That exactly matches the
difficulty, so she succeeds — with a margin of `0`. The door gives, but
only just: no style, no speed, and the Dungeon Master is entitled to
narrate it as a shoulder-first scramble.

Had she rolled `16`, her total of `21` would have beaten the difficulty
by `6`, and that margin would be hers to spend on whatever the rule in
question converts margin into.

{% book-only %}
## Design note

Combat deliberately uses the same threshold as every other roll. An
earlier draft had blows land only on a total *greater* than the
targeting difficulty while powers succeeded on a match, which meant two
different rules for reading the same die. One threshold is easier to
remember and, since the value now lives in one place, impossible for
the two halves of the game to disagree about.
{% endbook-only %}
