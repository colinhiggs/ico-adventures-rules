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
    extra_attacks_may_be_split_between_targets: true
  quick_attack:
    tier: minor
    source: stamina
    skill: attack_used
    base_difficulty: 1
    difficulty_per_extra_attack: 14
    extra_attacks_may_be_split_between_targets: true
    extra_attacks_deal_weapon_damage_only: true
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

The extra attacks need not all fall on the same creature: split them
between any targets you can reach, and compare that one roll to each
target's own targeting difficulty in turn. A single roll can therefore
sail past one opponent's defence and bounce off another's.

Melee and ranged both use this one power, taking whichever attack skill
the weapon calls for.

## Quick Attack

*(**minor**; stamina, the attack skill in use, base difficulty
{{ mechanics.quick_attack.base_difficulty }}; each further
{{ mechanics.quick_attack.difficulty_per_extra_attack }} points of
difficulty grants one more extra attack)*

Attack again, faster and less carefully. Quick Attack works exactly as
Fast Attack does — one roll, extra attacks that may be split between
targets — with one difference: **its extra attacks deal the weapon's
damage rating and nothing else.** No margin is converted, and the
attacker's skill adds nothing.

Being minor, it has no minimum cost, so a practised fighter can expect
to use it for nothing at all.

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

That same total of `21` is then compared to each target's targeting
difficulty. She spends one attack on the orc in front of her, whose
targeting difficulty is `14`, and one on the goblin beside it, whose
targeting difficulty is `11`. Both land, and each is resolved as its own
blow with its own margin.

Later, out of stamina entirely, she uses Quick Attack instead. One extra
attack costs `14` above the base, so she declares `15`. She rolls `13`,
for `25` — ten clear of her declared difficulty, which matches the base
cost, so it costs her nothing. Her second swing deals her
sword's damage rating flat: enough to drop a goblin, barely a scratch on
anything in armour.

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

Quick Attack's extra swings are stripped back to the weapon's damage
rating on purpose, and that single restriction is what lets it be
cheap enough to become free. A blow with no margin and no skill behind
it is lethal to something with a handful of hit points and no armour,
and close to worthless against anything serious — so the power that a
veteran can use every round without paying for it is precisely a
crowd-clearing tool, and never an answer to a real opponent.

Splitting extra attacks between targets matters more than it looks.
Against a crowd the difficulty was never damage per creature — one solid
blow kills a goblin — it was reaching them all before they surround you.

Second Wind recovers only mastery hit points, never core. Real wounds do
not respond to willpower, and a power that healed them would remove the
distinction the two pools exist to draw.
{% endbook-only %}
