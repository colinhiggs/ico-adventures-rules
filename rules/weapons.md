---
id: weapons
title: Weapons
tags: [equipment, reference, combat]
summary: >
  Weapon statistics: accuracy modifier, damage rating, size, and the
  armour points it contributes when used to block.
mechanics:
  finesse_size: S
  two_handed_size: L
  large_weapon_skill_penalty: -2
  dagger:
    accuracy: 2
    damage: 5
    size: S
    block_ap: 2
    cost_gp: 2
    quick: true
  short_sword:
    accuracy: 1
    damage: 6
    size: S
    block_ap: 6
    cost_gp: 10
    quick: true
  hand_axe:
    accuracy: 0
    damage: 7
    size: S
    block_ap: 3
    cost_gp: 8
  staff:
    accuracy: 0
    damage: 5
    size: M
    block_ap: 7
    reach_bonus: 1
    aids_spellcasting: true
    cost_gp: 1
  sword:
    accuracy: 1
    damage: 8
    size: M
    block_ap: 5
    cost_gp: 20
  battle_axe:
    accuracy: 0
    damage: 9
    size: M
    block_ap: 3
    cost_gp: 20
  two_handed_sword:
    accuracy: 0
    damage: 12
    unwieldy: true
    size: L
    block_ap: 4
    cost_gp: 50
  great_axe:
    accuracy: 0
    damage: 12
    unwieldy: true
    size: L
    block_ap: 2
    cost_gp: 45
---

Each weapon carries the statistics that feed [[hitting]] and
[[damage]]: an **accuracy** modifier to the attack roll, a **damage**
rating, a **size**, and the **block value** in armour points it
subtracts from a blow when you use it to block rather than dodge.

## Simple melee weapons

- **Dagger** — accuracy +{{ mechanics.dagger.accuracy }}, damage
  {{ mechanics.dagger.damage }}, size {{ mechanics.dagger.size }},
  block {{ mechanics.dagger.block_ap }},
  {{ mechanics.dagger.cost_gp }}gp.
- **Short sword** — accuracy +{{ mechanics.short_sword.accuracy }},
  damage {{ mechanics.short_sword.damage }}, size
  {{ mechanics.short_sword.size }}, block
  {{ mechanics.short_sword.block_ap }},
  {{ mechanics.short_sword.cost_gp }}gp.
- **Hand axe** — accuracy +{{ mechanics.hand_axe.accuracy }}, damage
  {{ mechanics.hand_axe.damage }}, size {{ mechanics.hand_axe.size }},
  block {{ mechanics.hand_axe.block_ap }},
  {{ mechanics.hand_axe.cost_gp }}gp.
- **Staff** — accuracy +{{ mechanics.staff.accuracy }}, damage
  {{ mechanics.staff.damage }}, size {{ mechanics.staff.size }}, block
  {{ mechanics.staff.block_ap }}, {{ mechanics.staff.cost_gp }}gp.

## Martial melee weapons

- **Sword** — accuracy +{{ mechanics.sword.accuracy }}, damage
  {{ mechanics.sword.damage }}, size {{ mechanics.sword.size }}, block
  {{ mechanics.sword.block_ap }}, {{ mechanics.sword.cost_gp }}gp.
- **Battle axe** — accuracy +{{ mechanics.battle_axe.accuracy }},
  damage {{ mechanics.battle_axe.damage }}, size
  {{ mechanics.battle_axe.size }}, block
  {{ mechanics.battle_axe.block_ap }},
  {{ mechanics.battle_axe.cost_gp }}gp.
- **Two-handed sword** — accuracy
  +{{ mechanics.two_handed_sword.accuracy }}, damage
  {{ mechanics.two_handed_sword.damage }}, size
  {{ mechanics.two_handed_sword.size }}, block
  {{ mechanics.two_handed_sword.block_ap }},
  {{ mechanics.two_handed_sword.cost_gp }}gp.
- **Great axe** — accuracy +{{ mechanics.great_axe.accuracy }}, damage
  {{ mechanics.great_axe.damage }}, size
  {{ mechanics.great_axe.size }}, block
  {{ mechanics.great_axe.block_ap }},
  {{ mechanics.great_axe.cost_gp }}gp.

## Finesse

A weapon of size {{ mechanics.finesse_size }} may use **dexterity**
instead of strength for its attack skill.

## Two hands

A weapon of size {{ mechanics.two_handed_size }} takes both hands; every
smaller weapon takes one. A two-handed weapon cannot be carried with a
shield from [[armour]], and it leaves no hand free for anything that
needs one — see [[free-hands]].

## Reach, and what it costs

A weapon of size {{ mechanics.two_handed_size }} extends its wielder's
reach, and so does any weapon whose entry gives it a reach bonus of its
own — the staff is long without being large. Other weapons do not.
What that is worth in a fight is in [[reach]], and how reach is
measured is in [[movement]].

It is long because it is big, and being big is not free. A weapon of
that size takes `{{ mechanics.large_weapon_skill_penalty }}` off your
defence, whichever way you defend — the same kind of interference heavy
[[armour]] causes, and for the same reason. You are carrying something
that gets in your way.

## Staffs

A staff is the one weapon a caster may hold and cast with as though
their hands were empty. It cancels the penalty [[free-hands]] would
otherwise charge for holding something, entirely.

This is not a magical property of the wood. Casters practise with a
staff precisely because it does this: the shape of the thing suits the
work, the movements a spell wants are movements a staff can be part of
rather than get in the way of, and every apprentice learns to cast
around one from the beginning. That it is also a serviceable club, a
walking aid over rough country, and the object most likely to be
enchanted by someone eventually, is the rest of the reason every caster
in the world seems to have one.

A staff carried by somebody who casts nothing is a stick.

## Unwieldy weapons

A weapon may be **unwieldy**: big enough that bringing it back after a
swing takes time. While you carry one your attacks come **after** any
opponent whose weapon is not unwieldy, whatever [[turn-order]] settled
at the start of the fight — the exact opposite of what a quick weapon
does, and resolved the same way.

Both of the size {{ mechanics.two_handed_size }} weapons are unwieldy.
That is what their damage and their reach are bought with, alongside the
penalty to your defence: you hit hardest, you reach furthest, and
everybody else swings before you do.

## Quick weapons

Some small weapons are **quick**: light enough to be drawn, put away and
brought back on the same breath, and short enough to be used at close
quarters where a longer weapon has run out of room. The dagger and the
short sword are quick; the hand axe is not, being a small weapon rather
than a fast one. What quickness does is in [[reach]] and
[[free-hands]].

Ranged weapons are not yet statted.

## Example

Dune carries a short sword. It is size S, so it is a finesse weapon and
he attacks with his dexterity bonus of `+4` rather than his strength
bonus of `+1` — a swing of three points he would otherwise never see.

Its accuracy of `+1` is added to his attack roll on top of that. Its
damage rating is what a landed blow starts from before margin, skill and
the target's armour are applied, as [[damage]] describes. And if he
chooses to block rather than dodge, its block value is subtracted from
whatever gets through.

Ashri's two-handed sword hits far harder, but it is size L: no finesse,
and no free hand for a shield.

{% book-only %}
## Design note

A large weapon is the best of the table on damage and the only one that
reaches. Left there it would be the only weapon anybody carried, and the
rest of this list would be scenery. The penalty to defence is what buys
the reach, and it is deliberately steep enough to be a decision rather
than a formality: you are choosing to be harder to get near and easier
to hit once somebody is near.

That is how the rest of the table stays alive. A weapon is not chosen by
finding the largest damage figure but by asking what a fight is going to
look like — whether you expect to keep people off you, or to be reached
anyway and want to be hard to land a blow on when you are.

Finesse exists because without it the game has no nimble fighter in it
at all. Melee attack is a strength skill while dodge is a dexterity one,
so a character built around speed was obliged to be bad at hitting
things no matter which weapon they picked, and the whole light-and-quick
archetype collapsed into a worse heavy fighter.

Restricting it to size S keeps that from erasing the reason to carry a
big weapon. A light weapon buys accuracy, a good block value and the
choice of attribute; a heavy one buys damage that armour cannot shrug
off.
{% endbook-only %}
