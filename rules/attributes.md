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
