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
  domains: [healing, war, trickery, love, death, nature, magic]
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
- a **domain of influence** — what the spell actually does: healing,
  war, trickery, love, death, nature, or magic.

A caster's access to spells, and any bonus when casting them, is
described in terms of these schools and domains.

## Shared properties

Beyond its own effect, every spell has a standard set of properties —
range, duration, area of effect, accuracy — covered in
[[spell-properties]]. The [[spell-list]] gives the spells themselves.

## Example

Sela is a priest of a god of healing, holding Spiritual at Master. Her
granted domain is healing.

She casts Cure Wounds. It is a life-force spell of the healing domain,
and because healing is her granted domain its difficulty drops by the
amount her signature allows before she declares anything. She then rolls
her spellcasting skill against that reduced difficulty, exactly as she
would for any other power, and pays the result out of her spirit.

A wizard with no divine patron may cast the same spell. It costs him a
great deal more, because he is reaching the full difficulty without a
god shouldering part of it.

{% book-only %}
## Design note

Making a spell a power rather than a separate subsystem is the largest
simplification in the game. There is one resolution procedure, one
resource rule, one way that reaching further costs more — and spells
inherit all of it rather than restating it in different words.

School and domain then carry the specialisation without needing access
lists. Rather than saying who *may* cast what, the rules say what each
spell *costs* whom, and a caster reaching outside their speciality is
limited by economics rather than by permission. It also means a new
spell needs no ruling about who can learn it: tag it with a school and a
domain and the existing signatures do the rest.
{% endbook-only %}
