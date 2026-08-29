---
id: discipline-powers
title: Discipline Powers
tags: [powers, progression, reference]
summary: >
  The powers each discipline opens, and the signature ability each
  grants at Master grade. Every power scales — you choose how hard to
  push it.
mechanics:
  power_attack:
    grade: initiate
    source: stamina
    skill: attack_melee
    base_difficulty: 4
    difficulty_per_step: 2
    damage_per_step: 1
  find_the_gap:
    grade: adept
    source: stamina
    skill: attack_melee
    base_difficulty: 6
    difficulty_per_step: 2
    reduction_ignored_per_step: 1
  redouble:
    grade: initiate
    source: stamina
    skill: dodge
    base_difficulty: 4
    difficulty_per_step: 10
    dodge_bonus_per_step: 1
  sneak_attack:
    grade: adept
    source: stamina
    skill: attack_melee
    base_difficulty: 6
    difficulty_per_step: 2
    damage_per_step: 2
  forewarned:
    grade: initiate
    source: stamina
    skill: spot
    base_difficulty: 4
    difficulty_per_step: 2
    initiative_bonus_per_step: 2
  killing_blow:
    grade: master
    margin_to_damage_fraction: 1
  untouchable:
    grade: master
    ignores_armour_skill_penalty_when_dodging: true
  read_the_blow:
    grade: master
    choose_stance_after_attack_roll: true
  school_mastery:
    grade: master
    difficulty_reduction: 5
  granted_domain:
    grade: master
    difficulty_reduction: 10
---

These powers are opened by holding the matching discipline at the
matching grade — see [[disciplines]]. The [[general-powers]] stay open
to everyone regardless. All of them are used as [[using-powers]]
describes: you declare a difficulty, roll, and pay for what you asked
for.

## Martial

**Power Attack** *(Initiate; stamina, melee attack, base difficulty
{{ mechanics.power_attack.base_difficulty }})* — a heavier swing at the
cost of control. Each further
{{ mechanics.power_attack.difficulty_per_step }} points of difficulty
adds {{ mechanics.power_attack.damage_per_step }} damage to the blow.

**Find the Gap** *(Adept; stamina, melee attack, base difficulty
{{ mechanics.find_the_gap.base_difficulty }})* — a blow aimed at a
join or a strap. Each further
{{ mechanics.find_the_gap.difficulty_per_step }} points of difficulty
ignores {{ mechanics.find_the_gap.reduction_ignored_per_step }} point of
the target's damage reduction -- worn armour and a raised shield alike,
since the whole point is that you are not hitting either of them. This
is the answer to heavy armour, and it is deliberately a power rather
than a weapon property.

**Killing Blow** *(Master signature)* — your attacks convert margin
into damage at
{{ mechanics.killing_blow.margin_to_damage_fraction }} per point
instead of the usual half. See [[damage]].

## Athletic

**Redouble** *(Initiate; stamina, dodge, base difficulty
{{ mechanics.redouble.base_difficulty }})* — thrown weight and a
second movement. Each further
{{ mechanics.redouble.difficulty_per_step }} points of difficulty adds
{{ mechanics.redouble.dodge_bonus_per_step }} to your targeting
difficulty against one attack, if you are dodging.

The price per point looks steep next to Power Attack, and it is:
a point of targeting difficulty applies to every attack aimed at you
for as long as you can pay for it, while a point of damage is spent
once. Priced to match Power Attack point for point, this power made a
practised dodger effectively unhittable.

**Sneak Attack** *(Adept; stamina, melee attack, base difficulty
{{ mechanics.sneak_attack.base_difficulty }})* — usable only against a
target who is unaware of you or already engaged with someone else. Each
further {{ mechanics.sneak_attack.difficulty_per_step }} points of
difficulty adds {{ mechanics.sneak_attack.damage_per_step }} damage.

**Untouchable** *(Master signature)* — armour's skill penalty no longer
worsens your targeting difficulty while dodging, so you may wear real
protection without surrendering your defence. See [[armour]].

## Awareness

**Forewarned** *(Initiate; stamina, spot, base difficulty
{{ mechanics.forewarned.base_difficulty }})* — you saw it coming. Each
further {{ mechanics.forewarned.difficulty_per_step }} points of
difficulty adds {{ mechanics.forewarned.initiative_bonus_per_step }} to
your place in the order for the coming fight.

**Read the Blow** *(Master signature)* — you may choose whether to
dodge or block after the attack roll has been made rather than before,
inverting the usual guess in [[hitting]].

## Magical and Spiritual

Both of these disciplines take their powers from the spell lists rather
than from a separate pool — a spell *is* a power, as [[spellcasting]]
explains. What their grades buy is reach: an Initiate may hold and cast
spells at all, and an Adept's focused spellcasting skill lets them
carry a much higher difficulty.

**School Mastery** *(Magical, Master signature)* — choose one school of
magic. Spells of that school are cast at
{{ mechanics.school_mastery.difficulty_reduction }} less difficulty.

**Granted Domain** *(Spiritual, Master signature)* — choose one domain
of influence. Spells of that domain are cast at
{{ mechanics.granted_domain.difficulty_reduction }} less difficulty.
This is the mechanical weight of having a god as your power source, and
it is larger than School Mastery because it is narrower: a domain is a
subject, a school is a technique.
