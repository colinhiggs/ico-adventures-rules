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
    base_difficulty: 22
    max_difficulty: 47
    base_extra_attacks: 1
    difficulty_per_extra_attack: 25
    extra_attacks_may_be_split_between_targets: true
  quick_attack:
    tier: minor
    source: stamina
    skill: attack_used
    base_difficulty: 18
    max_difficulty: 48
    base_extra_attacks: 1
    difficulty_per_extra_attack: 30
    extra_attacks_may_be_split_between_targets: true
    extra_attacks_deal_weapon_damage_only: true
  second_wind:
    source: stamina
    skill: fortitude
    base_difficulty: 8
    max_difficulty: 26
    difficulty_per_step: 3
    mastery_hp_per_step: 2
---

These powers are open to any character, whatever [[disciplines]] they
hold. Each is written with its power source, its skill, and the band of
difficulties it can be declared at; all are resolved as
[[using-powers]] describes.

## Fast Attack

*(stamina, the attack skill in use, difficulty
{{ mechanics.fast_attack.base_difficulty }} to
{{ mechanics.fast_attack.max_difficulty }};
{{ mechanics.fast_attack.base_extra_attacks }} extra attack at the base
difficulty, and one more for each further
{{ mechanics.fast_attack.difficulty_per_extra_attack }} points)*

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

A second swing is the largest single thing any power does to a round, so
it sits high on the ladder: its base difficulty is out of reach for most
beginners and routine for nobody until they have spent years on the
skill. Below that difficulty there is no partial version of it — see
[[discipline-powers]] for the damage rungs, which is where a character
who cannot yet reach this one spends their stamina instead.

## Quick Attack

*(**minor**; stamina, the attack skill in use, difficulty
{{ mechanics.quick_attack.base_difficulty }} to
{{ mechanics.quick_attack.max_difficulty }};
{{ mechanics.quick_attack.base_extra_attacks }} extra attack at the base
difficulty, and one more for each further
{{ mechanics.quick_attack.difficulty_per_extra_attack }} points)*

Attack again, faster and less carefully. Quick Attack works exactly as
Fast Attack does — one roll, extra attacks that may be split between
targets — with one difference: **its extra attacks deal the weapon's
damage rating and nothing else.** No margin is converted, and the
attacker's skill adds nothing.

Being minor, it has no minimum cost, so a veteran can expect to use it
for nothing more often than not — and a beginner cannot reach it at all,
which is the same statement about the same band read from the other
end.

## Second Wind

*(stamina, fortitude, difficulty
{{ mechanics.second_wind.base_difficulty }} to
{{ mechanics.second_wind.max_difficulty }}; each further
{{ mechanics.second_wind.difficulty_per_step }} points of difficulty
recovers {{ mechanics.second_wind.mastery_hp_per_step }} more)*

Shrug off a near miss and keep going, recovering
[[hit-points|mastery hit points]] but never core hit points.

## Example

Ashri, with a melee attack skill of `12`, wants a second swing. Fast
Attack's band opens at `22` and the first extra attack comes with it, so
`22` is what she declares; there is nothing cheaper to ask for.

She rolls `13`, for a total of `25`. That beats her declared `22`, so
the power works and she has two attacks this turn. The cost is the base
cost plus `22` less `25`, which is `7`; the minimum for a difficulty of
`22` is `7` as well, so she pays `7` either way.

That same total of `25` is then compared to each target's targeting
difficulty. She spends one attack on the orc in front of her, whose
targeting difficulty is `14`, and one on the goblin beside it, whose
targeting difficulty is `11`. Both land, and each is resolved as its own
blow with its own margin.

Later, out of stamina entirely, she uses Quick Attack instead, whose
band opens lower at `18`. She rolls `16`, for `28` — ten clear of her
declared difficulty, which matches the base cost, so it costs her
nothing. Her second swing deals her sword's damage rating flat: enough
to drop a goblin, barely a scratch on anything in armour.

{% book-only %}
## Design note

One scaling power does the work of several. A separate power for each
number of extra attacks, doubled again to cover melee and ranged, is the
same rule written out repeatedly with a different constant in it.

Extra attacks are priced far above what a point of damage costs
elsewhere, because an extra attack is a whole weapon's damage rather
than an increment of one. Priced to match Power Attack step for step, it
would be strictly the best power in the game at every level. It was, and
that is what moved its band. Measured across fifteen levels, every
reference build declared Fast Attack at one unchanging difficulty from
the first level to well past the middle, and nothing else ever competed,
which made the whole
[[discipline-powers|damage ladder]] decorative. Its base difficulty now
sits where a mid-career character reaches it and a beginner does not, so
the Adept damage rung is a real alternative to it rather than a worse
one.

Quick Attack is pitched to scale more slowly than Fast Attack rather
than merely lower, which is the general rule for a minor power and here
is load-bearing: a minor power whose steps are *cheaper* than its
standard twin's overtakes it somewhere, and a free version of the best
power in the game is not a trade-off.

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
