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
  critical_on: 20
  critical_rerolls_and_adds: true
  critical_chains: true
  critical_power_effect_steps: 1
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

## Criticals

Roll the highest face the die has —
{{ mechanics.critical_on }} — and it is a **critical**: roll the die
again and add the new result to it. If that roll is also
{{ mechanics.critical_on }}, roll again and keep adding, for as long as
your luck holds.

A critical needs no separate rule for what it does, because the game
already pays out on margin. A bigger total is a bigger margin, and a
bigger margin is more damage on a blow, a cheaper power, a longer reach
on a spell, a cleaner success on anything else — whatever the rule in
question already converts margin into.

The one thing margin does not already reach is the *size* of a power's
effect, which is fixed when you declare its difficulty rather than when
you roll. So a critical also grants
{{ mechanics.critical_power_effect_steps }} extra step of that power's
effect, free: one more point of damage on Power Attack, one more body in
a Whirl, one more attack from Fast Attack. See [[using-powers]].

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

Later, swinging at an orc, she rolls the highest face on the die. That
is a critical, so she rolls again and adds: an `11`, for a roll of `31`
before her bonuses. Nothing special happens to the blow as such — it is
simply an enormous margin, and [[damage]] turns margin into damage the
way it always does.

{% book-only %}
## Design note

Combat uses the same threshold as every other roll. A game that reads
the die one way for blows and another for powers asks its players to
remember which is which at exactly the moment they are least inclined
to check, and buys nothing for it. One threshold, defined once, cannot
drift out of step with itself.
{% endbook-only %}
