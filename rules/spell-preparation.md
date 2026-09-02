---
id: spell-preparation
title: Learning and Carrying Spells
tags: [magic, core, character]
summary: >
  A wizard writes spells in a book and carries a few of them in memory,
  changing which after a night's sleep. A priest carries their god's
  domains and prepares nothing.
mechanics:
  magical_casters_memorise: true
  spiritual_casters_memorise: false
  base_memory_slots: 3
  slots_per_expanded_memory: 2
  standard_spells_per_slot: 1
  minor_spells_per_slot: 2
  memorised_spells_swap_after_sleep: true
  spell_book_capacity_is_unlimited: true
---

Knowing a spell and being able to cast it today are different things,
and which of them is your problem depends on where your magic comes
from.

## Wizards: the book and the memory

A caster with the Magical discipline keeps a **spell book**. It holds as
many spells as they have ever learned; a book is a book, and there is no
limit on it. What is in the book cannot be cast.

What can be cast is what is in **memory**. You have
{{ mechanics.base_memory_slots }} memory slots, and each slot holds
either:

- {{ mechanics.standard_spells_per_slot }} standard spell, or
- {{ mechanics.minor_spells_per_slot }} minor spells.

A memorised spell is not spent by casting it. It stays memorised, and
you may cast it as often as you can pay for it out of your spirit — see
[[power-sources]]. Memory decides *which* spells you have today, never
how many times.

### More slots

**Expanded Memory** is a power, taken like any other power at a level
(see [[advancement]]), and each one taken grants
{{ mechanics.slots_per_expanded_memory }} more slots. It may be taken
more than once. See [[discipline-powers]].

### Changing what you carry

After a night's sleep — the same sleep [[recovery]] describes — you may
exchange any or all of your memorised spells for any others in your
book. Nothing else changes what you are carrying: a wizard who meets a
troll at noon has whatever they chose over breakfast.

## Priests: domains instead

A caster with the Spiritual discipline memorises nothing and keeps no
book. Their god grants them domains, and every spell in those domains is
available to them at all times — see [[domains]]. They can never cast
anything outside those domains, no matter what it is written in.

## Example

Ferren is a wizard with {{ mechanics.base_memory_slots }} slots and one
Expanded Memory, so {{ mechanics.base_memory_slots }} plus
{{ mechanics.slots_per_expanded_memory }} in all. His book holds
thirty-odd spells.

This morning he carries Flame Lance, Frost Blast and Force Burst in
three slots, and fills the other two with four minor spells — a Flame
Bolt and a Frost Bolt in one, a Force Bolt and a Mend in the other. That
is five slots holding seven spells, and he may cast any of the seven as
often as his spirit allows.

At noon he learns the thing in the cellar is immune to fire. Everything
he would want is in the book and none of it is in his head, and it will
stay that way until he has slept. He goes down with what he chose this
morning, which is the whole of the wizard's problem.

Sela, beside him, is a priest of a goddess of mercy. She prepared
nothing, carries nothing, and can cast every healing spell that exists.
She also cannot cast a single one of Ferren's, and never will be able
to.

{% book-only %}
## Design note

Memory holds *which* spells and never *how many castings*, because the
number of castings is already answered. Spirit is the resource, powers
are priced against it, and a second resource counting uses per spell
would be two answers to one question — the thing this system has avoided
everywhere else.

That leaves memorisation doing the one job it is good at: making a
wizard commit in advance. The interesting moment in a memorisation
system is never the arithmetic, it is walking into the cellar with the
wrong spells, and that moment survives perfectly well without slots
being consumed on use.

Letting a slot hold two minor spells instead of one standard is what
keeps the minor tier alive. Minor spells are the ones a caster falls
back on when the reservoir is dry, so a wizard who filled every slot
with the big ones would have nothing left to do on the fourth fight of
the day. Two-for-one makes carrying the small ones cheap enough to be
worth doing, without making the big ones a bad idea.

Putting the extra slots on a power rather than on a grade keeps
[[disciplines]] honest: a grade does three things and this is not one of
them. It also means breadth is bought with the same currency as
everything else, and a wizard who wants to carry more must give up
another power to do it.
{% endbook-only %}
