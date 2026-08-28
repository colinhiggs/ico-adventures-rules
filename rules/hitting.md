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
attacker must beat.

- Against a **dodging** defender, the TD is
  {{ mechanics.dodge_targeting_base }} plus the defender's dodge skill,
  before other modifiers. Most armour carries a dodge penalty, which
  *lowers* this number and makes a dodging wearer easier to hit.
- Against a **blocking** defender, the TD is the defender's block skill,
  usually modified by the block bonus or penalty of the weapon or
  shield being used.

## The attacker rolls

The attacker rolls `{{ mechanics.attack_roll }}` plus their attack skill
and applicable modifiers — see [[core-resolution]], and [[skills]] for
which attack skill applies to which weapon. If the total **matches or
beats** the targeting difficulty, the blow lands and [[damage]] is
worked out. A total exactly equal to the TD is a hit that carries no
margin: it lands for the weapon's damage and nothing more.

The amount by which the roll exceeded the TD is carried into the damage
step, so a cleaner hit hurts more. Combat uses the same threshold as
every other roll in the game — see
[[core-resolution|the core roll]] — rather than a stricter one of its
own.

Weapon and shield block values used above are listed with the
[[weapons]] and [[armour]].
