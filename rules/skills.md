---
id: skills
title: Using and Focusing Skills
tags: [core, character]
summary: >
  A skill check is d20 plus the skill. Focus — set by the disciplines
  you hold — decides how high a skill can be raised and what each rank
  costs.
mechanics:
  skill_check_roll: "1d20"
  focus_tiers: [focused, unfocused, peripheral]
  governing_attribute_per_skill: true
  cap_base_focused: 3
  cap_base_unfocused: 2
  cap_base_peripheral: 0
  cap_per_level: 1
  rank_cost_focused: 1
  rank_cost_unfocused: 2
  rank_cost_peripheral: 3
---

## Making a check

A skill check is the [[core-resolution|core roll]]:
`{{ mechanics.skill_check_roll }}` plus the skill's rank plus the bonus
from its governing attribute, against a fixed difficulty or an opposed
roll. Each skill has one governing attribute, listed in the
[[skill-list]].

## Focus

Skills are grouped, and each group sits at one of three tiers —
**focused**, **unfocused** or **peripheral** — decided entirely by
which [[disciplines]] you hold and at what grade. You never choose a
focus tier directly.

Focus does two things.

**It sets a ceiling.** The highest rank a skill can be raised to is
{{ mechanics.cap_per_level }} per level, on top of a base that depends
on focus: {{ mechanics.cap_base_focused }} for focused skills,
{{ mechanics.cap_base_unfocused }} for unfocused, and
{{ mechanics.cap_base_peripheral }} for peripheral. The gaps are
narrow on purpose — a specialist should be reliably better, not the
only person in the party who can attempt the thing at all.

**It sets a price.** One rank costs
{{ mechanics.rank_cost_focused }} advancement point in a focused skill,
{{ mechanics.rank_cost_unfocused }} in an unfocused one, and
{{ mechanics.rank_cost_peripheral }} in a peripheral one — see
[[advancement]]. This is where specialisation is really expressed: a
generalist is not forbidden from keeping pace, merely made to spend
everything doing it.
