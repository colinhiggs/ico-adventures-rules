---
id: spellcasting
title: How Spellcasting Works
tags: [core, magic, powers]
summary: >
  Spells are powers cast with the spellcasting skill, paid for in
  spirit. Each spell has a school (how it is built) and a domain (what
  it does).
mechanics:
  spells_are_powers: true
  casting_skill: spellcasting
  power_source: spirit
  schools: [life_force, energy, matter, rifts, influence_and_command, illusion]
---

## Spells as powers

Every spell is a [[using-powers|power]]. There is one casting skill —
**spellcasting** — and one power source for all magic: **spirit** (see
[[power-sources]]). A spell's difficulty is used exactly as any other
power's difficulty, and a margin over it reduces the spirit cost the
same way.

## School and domain

Every spell is tagged with both:

- a **school of magic** — how the spell is constructed: life force,
  energy, matter, rifts, influence and command, or illusion;
- a **domain of influence** — what the spell is about. The domains, and
  what they mean to a priest, are in [[domains]].

A caster's access to spells, and any bonus when casting them, is
described in terms of these schools and domains.

## Which spells you can cast today

The two disciplines answer that question differently, and it is the
largest difference between them. A wizard learns spells into a book and
carries a few of them in memory; a priest carries their god's domains
and prepares nothing. See [[spell-preparation]].

## Shared properties

Beyond its own effect, every spell has a standard set of properties —
range, duration, area of effect, accuracy — covered in
[[spell-properties]]. The [[spell-list]] gives the spells themselves.

## Example

Sela is a priest of a goddess of mercy, whose major domain is healing.

She casts Cure Wounds. It is a life-force spell of the healing domain,
so she rolls her spellcasting skill plus her goddess's favour against
the difficulty she declared, exactly as she would for any other power,
and pays the result out of her spirit. She did not prepare it; every
healing spell is hers all the time.

Ferren, a wizard, may cast the same spell — it is in his book — but only
if he memorised it this morning, and he casts it with no favour from
anybody. What he has instead is the Flame Lance, which Sela will never
cast at all.

{% book-only %}
## Design note

Making a spell a power rather than a separate subsystem is the largest
simplification in the game. There is one resolution procedure, one
resource rule, one way that reaching further costs more — and spells
inherit all of it rather than restating it in different words.

School and domain then carry the specialisation. A school says what a
caster is good at and costs them nothing to reach outside; a domain says
what a priest has been given, and is the one place in the magic rules
where the answer is permission rather than price. That is the difference
between studying magic and being lent it.

Either way a new spell needs no ruling about who can learn it. Tag it
with a school and a domain, and preparation, access and every signature
that touches magic already know what to do with it.
{% endbook-only %}
