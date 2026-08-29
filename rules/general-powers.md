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
the weapon calls for.

## Second Wind

*(stamina, fortitude, base difficulty
{{ mechanics.second_wind.base_difficulty }}; each further
{{ mechanics.second_wind.difficulty_per_step }} points of difficulty
recovers {{ mechanics.second_wind.mastery_hp_per_step }} more)*

Shrug off a near miss and keep going, recovering
[[hit-points|mastery hit points]] but never core hit points.

## Example

Ashri, with a melee attack skill of `12`, wants a second swing. Fast
Attack's base difficulty is `1` and one extra attack costs a further
`15`, so she declares `16`.

She rolls `9`, for a total of `21`. That beats her declared `16`, so the
power works and she has two attacks this turn. The cost is the base cost
plus `16` less `21`, which is `5`; the minimum for a difficulty of `16`
is `5` as well, so she pays `5` either way.

That same total of `21` is then compared to her target's targeting
difficulty — twice, once for each attack. Both swings hit or neither
does.

{% book-only %}
## Design note

One scaling power does the work of several. A separate power for each
number of extra attacks, doubled again to cover melee and ranged, is the
same rule written out repeatedly with a different constant in it — and
it makes the ceiling something a character buys rather than something
they decide in the moment.

Extra attacks are priced far above what a point of damage costs
elsewhere, because an extra attack is a whole weapon's damage rather
than an increment of one. Priced to match Power Attack step for step, it
would be strictly the best power in the game at every level.

Second Wind recovers only mastery hit points, never core. Real wounds do
not respond to willpower, and a power that healed them would remove the
distinction the two pools exist to draw.
{% endbook-only %}
