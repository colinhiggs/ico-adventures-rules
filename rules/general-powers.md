---
id: general-powers
title: General Powers
tags: [powers, reference]
summary: >
  Powers open to every character regardless of discipline. Like all
  powers they scale: you choose how far to push the difficulty.
mechanics:
  fast_attack:
    source: stamina
    skill: attack_used
    base_difficulty: 1
    difficulty_per_extra_attack: 15
  second_wind:
    source: stamina
    skill: fortitude
    base_difficulty: 8
    difficulty_per_step: 3
    mastery_hp_per_step: 2
---

These powers are open to any character, whatever [[disciplines]] they
hold. Each is written with its power source, its skill, and its base
difficulty; all are resolved as [[using-powers]] describes.

## Fast Attack

*(stamina, the attack skill in use, base difficulty
{{ mechanics.fast_attack.base_difficulty }}; each further
{{ mechanics.fast_attack.difficulty_per_extra_attack }} points of
difficulty grants one more extra attack)*

Attack again, after your first. Declare how many extra attacks you are
going for, roll once, and use that single roll for two things: first
against the declared difficulty to see whether the power worked and what
it cost, then against the target's [[hitting|targeting difficulty]] for
each attack it granted.

Melee and ranged both use this one power, taking whichever attack skill
the weapon calls for. It replaces the separate Fast Melee and Fast
Ranged powers of earlier drafts, which were the same power written
three times.

## Second Wind

*(stamina, fortitude, base difficulty
{{ mechanics.second_wind.base_difficulty }}; each further
{{ mechanics.second_wind.difficulty_per_step }} points of difficulty
recovers {{ mechanics.second_wind.mastery_hp_per_step }} more)*

Shrug off a near miss and keep going, recovering
[[hit-points|mastery hit points]] but never core hit points. Real
wounds do not respond to willpower.
