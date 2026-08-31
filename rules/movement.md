---
id: movement
title: Movement and Distance
tags: [core, combat, map]
summary: >
  The battle map is a grid of two-metre squares. How far a creature
  moves depends on its size and how it is built to travel, plus its
  dexterity, less what its armour costs it.
mechanics:
  square_metres: 2
  square_yards: 2
  feet_per_yard: 3
  move_base_by_size:
    small: 3
    medium: 4
    large: 5
    huge: 6
  move_bonus_by_gait:
    shambling: -1
    upright: 0
    quadruped: 2
  move_bonus_attribute: dexterity
  diagonal_cost_squares: 1
  difficult_ground_multiplier: 2
  reach_by_size:
    small: 1
    medium: 1
    large: 2
    huge: 3
  large_weapon_reach_bonus: 1
---

Distance is counted in **squares** on the battle grid.

## The square

One square is {{ mechanics.square_metres }} metres.

Ico is metric, and converts to imperial by treating a metre as a yard:
one square is {{ mechanics.square_yards }} yards — six feet, at
{{ mechanics.feet_per_yard }} feet to the yard. The conversion is
deliberately approximate: nothing in the game turns on the difference,
and a table that has to multiply by anything awkward mid-fight will stop
counting squares at all.

## How far you go

A creature's move is its **size base**, plus a bonus for how it is built
to travel, plus its {{ mechanics.move_bonus_attribute }} bonus, less the
movement penalty of any armour it wears — see [[armour]].

**Size base**, in squares:

- Small — {{ mechanics.move_base_by_size.small }}
- Medium — {{ mechanics.move_base_by_size.medium }}
- Large — {{ mechanics.move_base_by_size.large }}
- Huge — {{ mechanics.move_base_by_size.huge }}

**Gait**, added to that:

- Shambling, dragging or barely animate —
  {{ mechanics.move_bonus_by_gait.shambling }}
- Upright, walking on two legs —
  {{ mechanics.move_bonus_by_gait.upright }}
- Built to run on four —
  `+{{ mechanics.move_bonus_by_gait.quadruped }}`

A human is medium and upright, so a human's base move is
{{ mechanics.move_base_by_size.medium }} squares before dexterity and
armour. Flight and swimming are separate movement modes rather than a
gait bonus, and a creature that has them lists its speed in each.

You get one move per turn; see [[turn-order]].

Diagonal steps cost {{ mechanics.diagonal_cost_squares }} square, the
same as orthogonal ones. **Difficult ground** — rubble, deep water, a
floor of broken glass — costs
{{ mechanics.difficult_ground_multiplier }} squares for every square
entered. The Dungeon Master declares difficult ground when the scene is
described, not once someone has committed to a route.

## Reach

A creature can make a melee attack against anything within its
**reach**, counting diagonals:

- Small or medium — {{ mechanics.reach_by_size.small }} square
- Large — {{ mechanics.reach_by_size.large }} squares
- Huge — {{ mechanics.reach_by_size.huge }} squares

A weapon of size L adds {{ mechanics.large_weapon_reach_bonus }} to
that — see [[weapons]].

Reach is what powers mean by *within reach*: Whirl sweeps everything
inside it, Guard covers an ally standing inside it, and the extra
attacks from Fast Attack may be split between anything inside it. See
[[discipline-powers]] and [[general-powers]].

## Example

Dune is a human — medium, upright — with dexterity `18` for a bonus of
`+4`, wearing studded leather with no movement penalty. His move is the
medium base of `4`, plus nothing for walking upright, plus `4`, for `8`
squares: `16` metres, or `16` yards in imperial. His reach is one
square, and his short sword does not extend it.

A wolf is small but built to run on four legs: base `3`, plus `2` for
its gait, plus a dexterity bonus of `+3`, for `8` squares. It keeps pace
with Dune despite being the smaller animal, which is the point of the
gait bonus.

An ogre is large and upright: base `5`, plus a dexterity bonus of `+1`,
for `6` squares. It is slower over open ground than either of them — but
its reach is `2` squares, so Dune cannot stop one square short of it and
be safe, and with a size L club it threatens `3`.

{% book-only %}
## Design note

Movement had to come from the creature rather than from a single
constant, because the constant is only ever right for humans. An ogre
covers more ground per stride than a person does, and a wolf covers more
than either without being larger than a person — those are two
independent facts about an animal, so they are two independent terms
here. Size sets the stride, gait sets the cadence, and dexterity is the
individual on top of both.

Reach scaling with size follows from the same thought, and fixes a
tactical dead spot: without it, standing one square from a giant is
exactly as safe as standing one square from a child, and the whole
question of how to close with something enormous disappears.

Movement scales with dexterity because otherwise nothing does. Strength
already governs melee attack and block, constitution governs both core
hit points and stamina, and dexterity had only dodge to its name.

Armour paying for protection twice — once in the skill penalty, once in
movement — is intentional. Plate should be a decision rather than an
obvious purchase for anyone who can afford it.

Large weapons adding to reach is the counterweight to being unable to
carry a shield. Size was previously a stat that did nothing except
decide which weapons could use dexterity to hit; now it cuts both ways.
{% endbook-only %}
