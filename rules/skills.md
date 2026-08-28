---
id: skills
title: Using and Focusing Skills
tags: [core, character]
summary: >
  A skill check is d20 plus the skill against a difficulty or an opposed
  roll. Focus tier — focused, unfocused or peripheral — caps how high
  the skill can be raised.
mechanics:
  skill_check_roll: "1d20"
  focus_tiers: [focused, unfocused, peripheral]
  governing_attribute_per_skill: true
---

## Making a check

A skill check is the [[core-resolution|core roll]]: `{{ mechanics.skill_check_roll }}`
plus the skill's level plus the bonus from its governing attribute,
against a fixed difficulty or an opposed roll. Each skill has one
governing attribute, listed in the [[skill-list]].

## Focus tiers

Skills are organised into groups, and each character's groups sit at one
of three tiers:

- **Focused** — the character's speciality; skills here can be raised
  the highest.
- **Unfocused** — competent but not specialised; a lower ceiling than
  focused.
- **Peripheral** — everything else, with the lowest ceiling.

The tier a group sits in only limits how far its skills can be *raised*;
it does not stop the character attempting anything. Which groups are
focused and unfocused is set at [[character-creation]], and the
[[priorities]] rules can buy an exception for a single skill.
