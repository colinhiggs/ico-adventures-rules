---
id: attributes
title: Attributes
tags: [core, character]
summary: >
  Every character has six attributes — three physical, three mental —
  that describe their raw potential.
mechanics:
  attribute_count: 6
  physical: [strength, dexterity, constitution]
  mental: [intelligence, willpower, charisma]
  average_score: 10
  points_per_bonus_step: 2
---

A character's core potential is captured by
{{ mechanics.attribute_count }} attributes. The physical ones are
**strength**, **dexterity** and **constitution**; the mental ones are
**intelligence**, **willpower** and **charisma**.

## Reading a score

A score of {{ mechanics.average_score }} is average for a capable adult.
Every {{ mechanics.points_per_bonus_step }} points above
{{ mechanics.average_score }} gives a `+1` bonus that applies to rolls
governed by that attribute; every
{{ mechanics.points_per_bonus_step }} points below gives a matching
`-1` penalty. A character's race can modify the raw scores before this
bonus is worked out.

Which attribute governs which action is set by the skill in use — see
[[skills]] — and attribute bonuses are one of the inputs to
[[core-resolution|the core roll]].

## Example

Ashri has strength `16` and intelligence `9`.

Her strength is `6` above average, which at one step per two points
gives her a `+3` bonus. That `+3` is added to every roll strength
governs, including her melee attacks.

Her intelligence is `1` below average — not a full step — so it gives
her no penalty at all. Scores only move the bonus when they cross a
whole step, so `9` and `10` play identically.

{% book-only %}
## Design note

Six attributes split evenly between body and mind keeps the sheet small
enough to hold in the head while still letting two characters with the
same discipline feel unalike. The step of two points per bonus means a
raw score is a meaningful description in its own right rather than
merely a number waiting to be converted.
{% endbook-only %}
