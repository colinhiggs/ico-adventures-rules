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
    discipline: martial
    grade: initiate
    source: stamina
    skill: attack_melee
    base_difficulty: 4
    difficulty_per_step: 2
    damage_per_step: 1
  precise_strike:
    discipline: martial
    grade: initiate
    tier: minor
    source: stamina
    skill: attack_melee
    base_difficulty: 2
    difficulty_per_step: 4
    damage_per_step: 1
  follow_through:
    discipline: martial
    grade: initiate
    source: stamina
    skill: attack_melee
    base_difficulty: 4
    difficulty_per_step: 8
    extra_follow_through_per_step: 1
    triggers_on_dropping_a_target: true
  guard:
    discipline: martial
    grade: initiate
    source: stamina
    skill: block
    base_difficulty: 6
    base_allies: 1
    difficulty_per_step: 5
    extra_allies_per_step: 1
  riposte:
    discipline: martial
    grade: adept
    source: stamina
    skill: attack_melee
    base_difficulty: 6
    base_ripostes: 1
    difficulty_per_step: 4
    extra_ripostes_per_step: 1
  find_the_gap:
    discipline: martial
    grade: adept
    source: stamina
    skill: attack_melee
    base_difficulty: 6
    difficulty_per_step: 2
    reduction_ignored_per_step: 1
  redouble:
    discipline: athletic
    grade: initiate
    source: stamina
    skill: dodge
    base_difficulty: 4
    difficulty_per_step: 10
    dodge_bonus_per_step: 1
  sidestep:
    discipline: athletic
    grade: initiate
    tier: minor
    source: stamina
    skill: dodge
    base_difficulty: 2
    difficulty_per_step: 14
    dodge_bonus_per_step: 1
  whirl:
    discipline: athletic
    grade: adept
    source: stamina
    skill: attack_melee
    base_difficulty: 8
    base_targets: 2
    difficulty_per_step: 4
    extra_targets_per_step: 1
    converts_margin_to_damage: false
  deflect:
    discipline: athletic
    grade: initiate
    source: stamina
    skill: dodge
    base_difficulty: 5
    difficulty_per_step: 3
    damage_reduced_per_step: 2
  sneak_attack:
    discipline: athletic
    grade: adept
    source: stamina
    skill: attack_melee
    base_difficulty: 6
    difficulty_per_step: 2
    damage_per_step: 2
  forewarned:
    discipline: awareness
    grade: initiate
    source: stamina
    skill: spot
    base_difficulty: 4
    difficulty_per_step: 2
    initiative_bonus_per_step: 2
  weak_point:
    discipline: awareness
    grade: initiate
    tier: minor
    source: stamina
    skill: spot
    base_difficulty: 2
    difficulty_per_step: 6
    reduction_ignored_per_step: 1
  read_the_room:
    discipline: awareness
    grade: initiate
    tier: minor
    source: stamina
    skill: spot
    base_difficulty: 2
    difficulty_per_step: 5
    facts_per_step: 1
  call_the_shot:
    discipline: awareness
    grade: adept
    source: stamina
    skill: spot
    base_difficulty: 6
    difficulty_per_step: 3
    ally_bonus_per_step: 1
  anticipate:
    discipline: awareness
    grade: adept
    source: stamina
    skill: spot
    base_difficulty: 10
    base_interruptions: 1
    difficulty_per_step: 5
    extra_interruptions_per_step: 1
  turn_undead:
    discipline: spiritual
    grade: adept
    source: spirit
    skill: willpower
    base_difficulty: 8
    base_undead: 2
    difficulty_per_step: 3
    extra_undead_per_step: 1
  killing_blow:
    discipline: martial
    grade: master
    margin_to_damage_fraction: 1
  untouchable:
    discipline: athletic
    grade: master
    ignores_armour_skill_penalty_when_dodging: true
  read_the_blow:
    discipline: awareness
    grade: master
    choose_stance_after_attack_roll: true
  winning_manner:
    discipline: social
    grade: initiate
    tier: minor
    source: spirit
    skill: bluff
    base_difficulty: 2
    difficulty_per_step: 6
    check_bonus_per_step: 1
  rattle:
    discipline: social
    grade: initiate
    source: spirit
    skill: intimidate
    base_difficulty: 4
    difficulty_per_step: 3
    penalty_per_step: 1
  command:
    discipline: social
    grade: adept
    source: spirit
    skill: diplomacy
    base_difficulty: 10
    base_creatures: 1
    difficulty_per_step: 5
    extra_creatures_per_step: 1
    resisted_with: resolve
  command_the_room:
    discipline: social
    grade: master
    affects_everyone_who_can_see_and_hear: true
  expanded_memory:
    discipline: magical
    grade: initiate
    extra_memory_slots: 2
    may_be_taken_again: true
  school_mastery:
    discipline: magical
    grade: master
    difficulty_reduction: 5
  full_communion:
    discipline: spiritual
    grade: master
    major_bonus_applies_to_all_domains: true
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

**Precise Strike** *(Initiate, **minor**; stamina, melee attack, base
difficulty {{ mechanics.precise_strike.base_difficulty }})* — placing
the blow rather than forcing it. Each further
{{ mechanics.precise_strike.difficulty_per_step }} points of difficulty
adds {{ mechanics.precise_strike.damage_per_step }} damage.

**Follow Through** *(Initiate; stamina, melee attack, base
difficulty {{ mechanics.follow_through.base_difficulty }})* — when your
attack drops a target outright, carry the same swing into another enemy
you can reach and resolve it as a fresh attack. The chain runs
{{ mechanics.follow_through.extra_follow_through_per_step }} body deep
for the base difficulty, and
{{ mechanics.follow_through.extra_follow_through_per_step }} deeper for
each further {{ mechanics.follow_through.difficulty_per_step }} points.

Nothing happens unless a target actually falls, which limits the power
to opposition you can drop in a single blow.

**Guard** *(Initiate; stamina, block, base difficulty
{{ mechanics.guard.base_difficulty }})* — you place yourself between an
ally and what is coming. Until your next turn, attacks aimed at
{{ mechanics.guard.base_allies }} ally within your reach (see
[[movement]]) are aimed at you instead, resolved against your own targeting difficulty. Each further
{{ mechanics.guard.difficulty_per_step }} points of difficulty covers
{{ mechanics.guard.extra_allies_per_step }} more ally.

**Riposte** *(Adept, **reaction**; stamina, melee attack, base difficulty
{{ mechanics.riposte.base_difficulty }})* — a defence that answers back.
When an attack against you misses, spend your reaction (see
[[turn-order]]) to make an immediate attack against whoever made it. You may answer
{{ mechanics.riposte.base_ripostes }} attack this way, and
{{ mechanics.riposte.extra_ripostes_per_step }} more for each further
{{ mechanics.riposte.difficulty_per_step }} points of difficulty.

**Find the Gap** *(Adept; stamina, melee attack, base difficulty
{{ mechanics.find_the_gap.base_difficulty }})* — a blow aimed at a
join or a strap. Each further
{{ mechanics.find_the_gap.difficulty_per_step }} points of difficulty
ignores {{ mechanics.find_the_gap.reduction_ignored_per_step }} point of
the target's damage reduction — worn armour and a raised shield alike.

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

**Sidestep** *(Initiate, **minor**; stamina, dodge, base difficulty
{{ mechanics.sidestep.base_difficulty }})* — a small, cheap shift of
weight. Each further
{{ mechanics.sidestep.difficulty_per_step }} points of difficulty adds
{{ mechanics.sidestep.dodge_bonus_per_step }} to your targeting
difficulty against one attack, if you are dodging.

**Whirl** *(Adept; stamina, melee attack, base difficulty
{{ mechanics.whirl.base_difficulty }})* — one sweeping cut taken at
everything within reach. Make a single attack roll and compare it to the
targeting difficulty of {{ mechanics.whirl.base_targets }} enemies you
can reach; each further {{ mechanics.whirl.difficulty_per_step }} points
of difficulty reaches {{ mechanics.whirl.extra_targets_per_step }} more.

A sweep has no time for precision, so **Whirl converts no margin into
damage**: each blow deals the weapon's rating plus the damage your skill
adds, and nothing for how cleanly the roll landed.

**Deflect** *(Initiate, **reaction**; stamina, dodge, base difficulty
{{ mechanics.deflect.base_difficulty }})* — you cannot avoid the blow,
so you take it at an angle. Spend your reaction (see [[turn-order]]) to
reduce the damage of one blow that has already landed by {{ mechanics.deflect.damage_reduced_per_step }}, and
by {{ mechanics.deflect.damage_reduced_per_step }} more for each further
{{ mechanics.deflect.difficulty_per_step }} points of difficulty. This
reduction is not armour and is not subject to the cap in [[damage]].

**Sneak Attack** *(Adept; stamina, melee attack, base difficulty
{{ mechanics.sneak_attack.base_difficulty }})* — usable only against a
target who is unaware of you or already engaged with someone else. Each
further {{ mechanics.sneak_attack.difficulty_per_step }} points of
difficulty adds {{ mechanics.sneak_attack.damage_per_step }} damage.

**Untouchable** *(Master signature)* — armour's skill penalty does not
worsen your targeting difficulty while dodging. See [[armour]].

## Awareness

**Forewarned** *(Initiate; stamina, spot, base difficulty
{{ mechanics.forewarned.base_difficulty }})* — you saw it coming. Each
further {{ mechanics.forewarned.difficulty_per_step }} points of
difficulty adds {{ mechanics.forewarned.initiative_bonus_per_step }} to
your place in the order for the coming fight — see [[turn-order]].

**Weak Point** *(Initiate, **minor**; stamina, spot, base difficulty
{{ mechanics.weak_point.base_difficulty }})* — you spot the strap, the
gap, the badly-set plate, and say so. Each further
{{ mechanics.weak_point.difficulty_per_step }} points of difficulty
ignores {{ mechanics.weak_point.reduction_ignored_per_step }} point of
the target's damage reduction on your next blow.

**Read the Room** *(Initiate, **minor**; stamina, spot, base difficulty
{{ mechanics.read_the_room.base_difficulty }})* — a moment spent working
out who actually matters. Learn
{{ mechanics.read_the_room.facts_per_step }} true thing about the
opposition — which of them is the most dangerous, which is the least
armoured, which is about to break — and
{{ mechanics.read_the_room.facts_per_step }} more for each further
{{ mechanics.read_the_room.difficulty_per_step }} points of difficulty.
The Dungeon Master answers honestly.

**Call the Shot** *(Adept; stamina, spot, base difficulty
{{ mechanics.call_the_shot.base_difficulty }})* — you saw the opening
and said so in time. An ally's next attack gains
`+{{ mechanics.call_the_shot.ally_bonus_per_step }}` for each
{{ mechanics.call_the_shot.difficulty_per_step }} points of difficulty
beyond the base.

**Anticipate** *(Adept, **reaction**; stamina, spot, base difficulty
{{ mechanics.anticipate.base_difficulty }})* — you were already moving.
Spend your reaction (see [[turn-order]]) to act immediately, out of
turn, interrupting whoever is acting.
{{ mechanics.anticipate.base_interruptions }} interruption comes with
the base difficulty, and
{{ mechanics.anticipate.extra_interruptions_per_step }} more for each
further {{ mechanics.anticipate.difficulty_per_step }} points.

**Read the Blow** *(Master signature)* — you may choose whether to
dodge or block after the attack roll has been made rather than before,
inverting the usual guess in [[hitting]].

## Social

**Winning Manner** *(Initiate, **minor**; spirit, bluff, base difficulty
{{ mechanics.winning_manner.base_difficulty }})* — you are simply easy
to agree with. Add `+{{ mechanics.winning_manner.check_bonus_per_step }}`
to one social skill check for each
{{ mechanics.winning_manner.difficulty_per_step }} points of difficulty
beyond the base.

**Rattle** *(Initiate; spirit, intimidate, base difficulty
{{ mechanics.rattle.base_difficulty }})* — a word, a look, a laugh at
the wrong moment. One creature that can see and hear you takes
`-{{ mechanics.rattle.penalty_per_step }}` on its next roll for each
further {{ mechanics.rattle.difficulty_per_step }} points of difficulty.
This is Social's contribution to a fight, and it works on anything with
a mind to unsettle.

**Command** *(Adept; spirit, diplomacy, base difficulty
{{ mechanics.command.base_difficulty }})* — one word, obeyed before the
creature has decided whether to. Name a single simple instruction —
*drop it*, *stop*, *run* — and
{{ mechanics.command.base_creatures }} creature must obey unless it
resists with {{ mechanics.command.resisted_with }}. Each further
{{ mechanics.command.difficulty_per_step }} points of difficulty commands
{{ mechanics.command.extra_creatures_per_step }} more creature.

**Command the Room** *(Master signature)* — a Social power that would
affect one creature affects every creature that can see and hear you
instead.

## Magical and Spiritual

Both of these disciplines take their powers from the spell lists rather
than from a separate pool — a spell *is* a power, as [[spellcasting]]
explains. What their grades buy is reach: an Initiate may hold and cast
spells at all, and an Adept's focused spellcasting skill lets them
carry a much higher difficulty.

**Expanded Memory** *(Magical, Initiate)* — you carry more spells in
your head. {{ mechanics.expanded_memory.extra_memory_slots }} more
memory slots, per [[spell-preparation]]. This is the one power on any of
these lists that is not used during a fight and has no difficulty at
all; it may be taken again at a later level, and stacks.

**Turn Undead** *(Spiritual, Adept; spirit, willpower, base difficulty
{{ mechanics.turn_undead.base_difficulty }})* — you hold up what you
believe in and the dead give ground. {{ mechanics.turn_undead.base_undead }}
undead creatures within sight flee from you, and
{{ mechanics.turn_undead.extra_undead_per_step }} more for each further
{{ mechanics.turn_undead.difficulty_per_step }} points of difficulty.
Undead substantially mightier than the caster are unmoved; the Dungeon
Master decides which those are.

**School Mastery** *(Magical, Master signature)* — choose one school of
magic. Spells of that school are cast at
{{ mechanics.school_mastery.difficulty_reduction }} less difficulty.

**Full Communion** *(Spiritual, Master signature)* — the favour your god
shows you in your major domain extends to every domain you were granted.
The `+{{ domains:mechanics.major_domain_bonus }}` that applied to one
now applies to all of them. See [[domains]].

## Example

Bramm is in full plate. Ashri, who holds Martial at Adept, has both
Power Attack and Find the Gap available and must pick one.

Power Attack would add damage to a blow that plate is going to blunt
heavily. Find the Gap instead strips reduction: declaring a difficulty
of `14` against its base of `6` buys four steps, ignoring `4` points of
Bramm's armour.

Against an unarmoured opponent the choice reverses — there is no
reduction to strip, and every point of difficulty spent on Find the Gap
would be wasted where Power Attack would have added damage.

Her Martial Master signature, Killing Blow, applies to either: whichever
power she uses, her margin converts to damage at full value rather than
half.

{% book-only %}
## Design note

Find the Gap is deliberately a power rather than a weapon property. Flat
armour reduction is what makes heavy plate frightening, and the answer
to it should be something a character *chooses to train*, not something
that comes free with the right purchase.

Redouble's price per point looks steep next to Power Attack, and it is.
A point of targeting difficulty applies to every attack aimed at you for
as long as you can pay for it, while a point of damage is spent once.
Priced to match Power Attack point for point, it would make a practised
dodger effectively unhittable.

The minor powers — Precise Strike, Sidestep and Weak Point — scale far
more slowly than their standard counterparts and will never match them.
That is the trade for a power that still works with an empty reservoir.

Whirl and Quick Attack answer the same question differently, and the
difference is the point of specialising. Quick Attack is open to
everyone, costs nothing once a character is practised enough, and its
extra swings are stripped back to the bare weapon. Whirl is bought with
a discipline grade, is paid for every time it is used, and its blows
land with a trained arm behind them. The generalist can always clear
rabble slowly; the one who trained for it clears rabble properly.

Follow Through and Turn Undead are crowd answers of a third and fourth
kind, and it is worth noticing that none of the four works the same way.
Quick Attack allocates weak swings, Whirl sweeps everything at once,
Follow Through cascades out of a body that has already fallen, and Turn
Undead removes a crowd without killing any of it. A discipline that has
trained for rabble should feel unlike the others doing it.

Follow Through is a standard power rather than a minor one, and that is
what keeps [[general-powers|Quick Attack]] worth having. A cascade of
full blows is far stronger than a handful of bare weapon swings, so if
it were also free there would be no reason for anyone holding a Martial
grade to ever reach for the general power. Paid for, it is what a
fighter opens with; Quick Attack is what the same fighter still has on
the fourth fight of the day.

Social is the only discipline whose powers are worth taking by a
character who never intends to fight, and Rattle is deliberately the
exception that keeps it from being a non-combat discipline. A penalty on
an enemy's next roll is worth roughly what a point of damage is worth,
except that it can land on a spell, a save or an attack, and it works on
anything that has a mind to unsettle.

Command the Room turns single-target powers into area ones, which is a
larger multiplier than any other signature grants. It is priced by being
the capstone of a discipline that does no damage: a Master of Social has
spent a career on a power pool that cannot, on its own, kill anything.

Guard, Deflect, Call the Shot and Read the Room are the first powers
here that do nothing on their own turn and nothing to a target. They
exist because a party is not four characters taking turns at the same
problem, and a discipline whose only expression is damage has nothing to
offer the fight it is not built for.

Whirl scales in reach rather than in force. Pushing the difficulty finds
one more body, not a heavier cut — which is what makes it a crowd
answer rather than a better way to fight one opponent.

School Mastery and Full Communion are worth roughly the same and reach
it from opposite directions. A school is a technique and a broad one, so
mastering it is worth a large bonus on one thing. A domain is a subject
and a narrow one, so the priest's signature is a small bonus spread
across everything they can cast at all. The wizard gets deeper in one
place; the priest gets their whole god at once.

Neither of them is where a priest's domain bonus comes from. Every
priest has that from the first level, because having a god is not an
achievement — it is the arrangement. What the signature buys is the god
paying full attention to all of it rather than to one part.
{% endbook-only %}
