---
id: free-hands
title: Free Hands
tags: [core, skills, powers]
summary: >
  Some skills and powers need a hand free, or both. What you are holding
  decides whether you can use them, and a quick weapon can be put away
  and brought back without spending an action.
mechanics:
  hands_total: 2
  stowing_costs_an_action: true
  quick_stow_is_free: true
  hands_needed:
    spellcasting: 1
    heal: 1
    use_magic_device: 1
    sleight_of_hand: 1
    disable_device: 2
    climb: 2
---

You have {{ mechanics.hands_total }} hands, and what is in them decides
what you can do with them.

## What a hand is holding

A weapon takes the hands its size says it takes, and a shield takes one
— see [[weapons]] and [[armour]]. Whatever is left over is free.

A skill or power that needs a free hand cannot be used without one:

- **{{ mechanics.hands_needed.spellcasting }} hand** — spellcasting,
  heal, use magic device, sleight of hand.
- **{{ mechanics.hands_needed.climb }} hands** — climb, disable device.

So a one-handed weapon and no shield leaves a hand for a spell; the same
weapon with a shield does not; and a two-handed weapon leaves nothing
for anything.

## Putting it away

Stowing what you are holding, or drawing it again, costs your **action**
for the round. A **quick** weapon is the exception: it may be put away
and brought back freely, as often as you like, and costs nothing.

That is what quickness is for beyond [[reach]]. A character whose work
needs a hand — a caster, a healer, anyone who opens a lock in the middle
of a fight — can carry a quick weapon and still do that work on the same
turn. Carrying anything else means choosing, every round, between the
thing in your hand and the thing you cannot do while holding it.

## Example

Sela is a caster, and spellcasting needs
{{ mechanics.hands_needed.spellcasting }} free hand.

With a dagger and no shield she has a free hand already, and casts
without having to do anything about it. If she wants a shield as well,
both hands are full — but the dagger is quick, so she puts it away for
nothing, casts, and has it back in her hand before the round ends.

Give her a two-handed sword instead and none of that works. Both hands
are on the weapon, and putting it away costs the action she wanted to
cast with. She may cast this round or hold the sword, and not both.

Bram, who casts nothing and picks no locks, notices none of this.

{% book-only %}
## Design note

This is the second axis weapon size needed. Damage and accuracy trade
against each other along a single line, and where two numbers trade on
one line there is always a best point on it — the rest of the table is
then decoration. Reach is one way off that line and free hands is
another, and neither can be settled by reading off a bigger number.

It is also how Ico says a caster should not be in plate with a
greatsword without ever writing that down. Nothing here forbids anybody
anything. The greatsword is available to the caster and costs them the
action they wanted; the plate is available too, and costs them what
[[armour]] says it costs. A character declines the equipment that
interferes with what they are for, and the rule does the arguing rather
than the Dungeon Master.
{% endbook-only %}
