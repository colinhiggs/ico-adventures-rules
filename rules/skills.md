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
**focused**, **unfocused** or **peripheral** — decided entirely by which
[[disciplines]] you hold and at what grade. You never choose a focus
tier directly.

Focus does two things.

**It sets a ceiling.** The highest rank a skill can be raised to is
{{ mechanics.cap_per_level }} per level, on top of a base that depends
on focus: {{ mechanics.cap_base_focused }} for focused skills,
{{ mechanics.cap_base_unfocused }} for unfocused, and
{{ mechanics.cap_base_peripheral }} for peripheral.

**It sets a price.** One rank costs {{ mechanics.rank_cost_focused }}
advancement point in a focused skill,
{{ mechanics.rank_cost_unfocused }} in an unfocused one, and
{{ mechanics.rank_cost_peripheral }} in a peripheral one — see
[[advancement]].

## Example

At level `6`, Ashri holds Martial at Adept and Athletic at Initiate, and
nothing else.

Her melee attack is focused, so its ceiling is the focused base plus one
per level: rank `9`. Each rank costs her a single point, so she has kept
it at the cap throughout her career without much thought.

Her dodge is unfocused, ceiling rank `8`, and each rank costs two
points. She has let it sit at `5`, a little short of what she could
have.

Her stealth is peripheral, ceiling rank `6`, at three points a rank. She
has never bought a single one — but she may still attempt it, rolling
her dexterity bonus alone.

{% book-only %}
## Design note

The ceilings sit close together on purpose. A specialist should be
reliably better, not the only person at the table who can attempt the
thing at all, and a gap of a few points on a twenty-sided die is plainly
noticeable without being decisive.

Specialisation is really expressed in the *price* rather than the
ceiling. A generalist is not forbidden from keeping pace in any one
skill; they are merely made to spend three points where a specialist
spends one, so keeping pace everywhere costs them everything. The
trade-off is then a budget decision the player makes each level, rather
than a wall the rules put in front of them.
{% endbook-only %}
