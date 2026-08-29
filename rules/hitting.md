---
id: hitting
title: Landing a Blow
tags: [core, combat]
summary: >
  The defender dodges or blocks, which sets the targeting difficulty.
  The attacker rolls d20 plus attack skill and must match or beat it.
mechanics:
  attack_roll: "1d20"
  dodge_targeting_base: 10
  block_targeting_base: block_skill
---

Every blow is one attacker against one defender.

## The defender chooses

Before the attack is rolled, the defender chooses to **dodge** or
**block**, and that choice sets the **targeting difficulty** (TD) the
attacker must reach.

- Against a **dodging** defender, the TD is
  {{ mechanics.dodge_targeting_base }} plus the defender's dodge skill.
  Most armour carries a skill penalty, which *lowers* this number and
  makes a dodging wearer easier to hit.
- Against a **blocking** defender, the TD is the defender's block skill,
  modified by the block bonus of the weapon or shield being used.

## The attacker rolls

The attacker rolls `{{ mechanics.attack_roll }}` plus their attack skill
and their weapon's accuracy — see [[core-resolution]], and [[skills]]
for which attack skill a weapon calls for. If the total matches or beats
the targeting difficulty, the blow lands and [[damage]] is worked out.

The amount by which the roll exceeded the TD is the **margin**, and it
is carried into the damage step, so a cleaner hit hurts more. A total
exactly equal to the TD is a hit with a margin of nothing.

Weapon and shield block values are listed with the [[weapons]] and
[[armour]].

## Example

Ashri swings at Bramm, who is wearing chain mail and chooses to dodge.
Bramm's dodge skill is `7`, and his chain mail carries a skill penalty
of `-4`, so his targeting difficulty is the base plus `7` less `4` —
`13`.

Ashri rolls `11` and adds her attack skill of `9` and her sword's
accuracy of `+1`, for `21`. That beats `13`, so the blow lands with a
margin of `8`.

Had Bramm chosen to block instead, his targeting difficulty would have
been built from his block skill rather than his dodge, with no base
added — a much lower number, and a much easier target — but every blow
that did land would have been blunted by his shield.

{% book-only %}
## Design note

The stance choice is made before the roll on purpose: it is a guess
about what is coming, not a reaction to it. Dodging is the safer stance
against a weapon that hits hard and rarely, blocking against one that
hits often and lightly, and neither is correct in general. The Awareness
discipline's Master signature exists precisely to break this rule — see
[[discipline-powers]] — and it is worth a capstone because inverting a
guess into a decision is genuinely powerful.

Armour making a dodging wearer *easier* to hit is deliberate rather than
an oversight. Heavy plate is protection bought at the price of agility,
and a character who wants both has to go looking for a rule that gives
it to them.
{% endbook-only %}
