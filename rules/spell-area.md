---
id: spell-area
title: Spell Areas
tags: [magic, core, map]
summary: >
  An area spell picks a shape and a size, and pays for every square it
  covers and every point of damage it deals. The two rates vary by
  spell, and their balance is what makes one spell wide and weak and
  another small and fierce.
mechanics:
  templates: [circle, cone, line, square, rectangle]
  default_archetype: balanced
  archetypes:
    diffuse:
      squares_per_difficulty: 6
      difficulty_per_damage: 4
    balanced:
      squares_per_difficulty: 3
      difficulty_per_damage: 2
    concentrated:
      squares_per_difficulty: 1
      difficulty_per_damage: 1
  circle_squares:
    radius_1: 5
    radius_2: 13
    radius_3: 29
    radius_4: 49
    radius_5: 81
  cone_squares:
    length_2: 3
    length_3: 6
    length_4: 10
    length_5: 15
---

A spell with an area names one of five **templates**. The caster chooses
how large to make it, counts the squares it covers, and pays for them —
on top of everything else the spell is being asked to do.

Squares are the ones [[movement]] measures.

## The templates

**Circle** — a ball or burst, measured by radius from a centre square:

- Radius one — {{ mechanics.circle_squares.radius_1 }} squares
- Radius two — {{ mechanics.circle_squares.radius_2 }} squares
- Radius three — {{ mechanics.circle_squares.radius_3 }} squares
- Radius four — {{ mechanics.circle_squares.radius_4 }} squares
- Radius five — {{ mechanics.circle_squares.radius_5 }} squares

**Cone** — spreading from the caster, measured by length:

- Length two — {{ mechanics.cone_squares.length_2 }} squares
- Length three — {{ mechanics.cone_squares.length_3 }} squares
- Length four — {{ mechanics.cone_squares.length_4 }} squares
- Length five — {{ mechanics.cone_squares.length_5 }} squares

**Line** — one square wide. Its area is its length.

**Square** — its area is the side length multiplied by itself.

**Rectangle** — the caster picks two side lengths, and the area is one
multiplied by the other.

Beyond the listed sizes, count the squares on the map. The tables exist
to save arithmetic at the common sizes, not to cap the shapes.

## The two rates

Every area spell lists two rates of its own:

- **Coverage** — how many squares one point of difficulty covers.
- **Per damage** — the difficulty each point of damage costs, dealt to
  everything the area covers.

Total difficulty is the spell's base, plus the squares divided by the
coverage rate and rounded up, plus damage times the second rate. A spell
that deals no damage pays only for its squares.

The two rates move against each other, and their balance *is* the
spell's character. Three shapes cover almost everything:

- **Diffuse** —
  {{ mechanics.archetypes.diffuse.squares_per_difficulty }} squares per
  point, {{ mechanics.archetypes.diffuse.difficulty_per_damage }} per
  damage. Cheap to spread, dear to sharpen: a spell that blankets ground
  and barely stings.
- **Balanced** —
  {{ mechanics.archetypes.balanced.squares_per_difficulty }} squares per
  point, {{ mechanics.archetypes.balanced.difficulty_per_damage }} per
  damage.
- **Concentrated** —
  {{ mechanics.archetypes.concentrated.squares_per_difficulty }} square
  per point,
  {{ mechanics.archetypes.concentrated.difficulty_per_damage }} per
  damage. Dear to spread, cheap to sharpen: a small, fierce burst.

A spell that names no rates uses the
{{ mechanics.default_archetype }} pair.

## Example

Sela has `36` points of difficulty to spend on a burst with a base of
`4`, and three orcs are standing close together.

Her spell is **concentrated**. A radius-one circle covers `5` squares at
`3` each, so `15` of her budget goes on area, leaving `17` for damage at
`2` a point: `8` damage to everything in those five squares. Against
three orcs that is `24` damage delivered.

A bolt on the same budget would have dealt `11` to one of them. The
burst wins because the orcs bunched — and had they been spread out, it
would have been the worse spell. That is the trade, and it is decided by
where the enemy is standing rather than by which spell is better.

Had the same budget gone into a **diffuse** spell she could have covered
`13` squares, but for `3` damage each.

{% book-only %}
## Design note

Charging by the square rather than by the template is what keeps area
magic honest. A spell that catches a dozen creatures is worth roughly a
dozen times one that catches a single creature, and pricing per *shape*
instead invites the caster to always take the largest version of
whichever shape is cheapest.

Two rates rather than one, moving inversely, is the part that took
measuring. A single per-square dial does not produce a trade-off at all:
cheaper squares are simply better, since the cost only ever subtracts
from the budget, and a designer choosing an expensive rate would just be
writing a worse spell. It is only when cheap coverage is paid for with
expensive damage that "wide and weak" and "small and fierce" become two
real options rather than one good one and one bad one.

Two invariants hold the rates in place, and both are checked by
measurement rather than argued.

**No area spell beats a lance against a single target.** Area magic
should be the answer to a crowd, never a better way to hurt one person,
or the single-target spells stop being worth writing at all.

**A caster clears a crowd at least as fast as a melee character built
to do it.** That is the point of the family, and it was not true when
these rates were first written: they were calibrated against whether an
area spell beat a bolt if it caught two creatures, and nobody checked
whether a caster could afford a useful radius in the first place. They
could not. At level fifteen no archetype could reach radius two with
enough damage left to kill anything, which is why the rates are now
expressed as squares covered per point rather than points per square —
coverage had to get several times cheaper before the family worked at
all.

The tables cover the sizes that actually come up, so that nobody
multiplies by pi at the table. Past radius five, a caster who can afford
something that large can afford to count it.
{% endbook-only %}
