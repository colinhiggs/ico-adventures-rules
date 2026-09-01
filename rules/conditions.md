---
id: conditions
title: Conditions and Resisting Them
tags: [core, combat]
summary: >
  An effect that does more than damage is resisted with an opposed roll
  against Fortitude or Resolve, and how long it lasts depends on the
  margin.
mechanics:
  resisted_by_opposed_roll: true
  physical_resistance_skill: fortitude
  mental_resistance_skill: resolve
  base_rounds: 1
  margin_per_extra_round: 5
  conditions:
    stunned:
      resisted_with: fortitude
      margin_per_extra_round: 15
    burning:
      resisted_with: fortitude
      margin_per_extra_round: 4
    slowed:
      resisted_with: fortitude
      movement_fraction: 0.5
    dazed:
      resisted_with: resolve
      attack_penalty: 2
---

Some effects do more than damage. Being set alight, knocked senseless or
thrown off your stride are **conditions**, and a creature always gets to
resist one.

## Resisting

Resisting is an opposed roll, exactly as [[core-resolution]] describes.
The effect's own total — for a spell, the casting roll that was already
made — is the target to beat. The defender rolls
`{{ core-resolution:mechanics.standard_die }}` and adds whichever skill
the effect names:

- **{{ mechanics.physical_resistance_skill }}** for anything the body
  fights off: fire, cold, poison, a blow that rattles the skull.
- **{{ mechanics.mental_resistance_skill }}** for anything the mind
  fights off: fear, confusion, compulsion.

Beat the effect's total and nothing happens to you. Fail and the
condition lands.

## How long it lasts

A condition that lands lasts {{ mechanics.base_rounds }} round, plus one
more for every {{ mechanics.margin_per_extra_round }} points by which
the effect's total beat your resistance roll. Some conditions are harder
to sustain than that and say so.

Margin decides duration for the same reason it decides everything else:
a near-thing should be brief and an overwhelming one should stick.

## The conditions

**Stunned** — you lose your action. You may still move, and you still
defend yourself. Resisted with
{{ mechanics.conditions.stunned.resisted_with }}, and it takes
{{ mechanics.conditions.stunned.margin_per_extra_round }} points of
margin to hold someone stunned for a second round, because taking a
character's turn away is the harshest thing an effect can do.

**Burning** — you take the effect's damage again at the start of each
of your turns. Resisted with
{{ mechanics.conditions.burning.resisted_with }}, and it spreads easily:
{{ mechanics.conditions.burning.margin_per_extra_round }} points of
margin buys another round of it.

**Slowed** — your movement is multiplied by
{{ mechanics.conditions.slowed.movement_fraction }} and you have no
reaction. Resisted with
{{ mechanics.conditions.slowed.resisted_with }}.

**Dazed** — you take
`-{{ mechanics.conditions.dazed.attack_penalty }}` on attack rolls, and
your targeting difficulty drops by the same. Resisted with
{{ mechanics.conditions.dazed.resisted_with }}.

## Example

Sela casts a Force Lance at an orc and rolls `27` in total. The lance
hits, deals its damage, and tries to stun.

The orc rolls to resist with Fortitude: `11` on the die plus a Fortitude
of `6`, for `17`. Sela beat that by `10` — but stunning needs `15`
points of margin for each extra round, so the orc is stunned for a
single round. It loses its action, though it may still back away.

Had the orc rolled `28`, it would have shrugged the effect off
completely and taken only the damage.

Against a Flame Lance the same margin of `10` would have set it burning
for three rounds, since fire needs only `4` points of margin a round —
which is the difference between the two spells, and the reason to carry
both.

{% book-only %}
## Design note

Ico did not need saving throws. It already had two skills whose written
purpose was resisting duress — Fortitude against the physical and
Resolve against the mental — and no rule anywhere that used either of
them. An opposed roll against the skill that already claims the job is
one less subsystem than a saving throw, and it means a character who
invested in Fortitude finds out why.

Using the caster's existing roll as the target is the same economy that
runs through the rest of the game. That single roll already settled
whether the spell happened, what it cost and whether it landed; asking
it to also stand as the number to beat costs nothing and keeps a spell
to one roll on the caster's side.

Duration by margin rather than a flat number is what stops every
condition being equally decisive. Stun is the extreme case and is priced
as one: it needs three times the margin of anything else to last a
second round, because removing a character's turn is the harshest thing
in the game and a spell that reliably removes several is the only
spell anyone would ever cast.
{% endbook-only %}
