---
id: spell-properties
title: Standard Spell Properties
tags: [magic, reference]
summary: >
  Range, duration, area and accuracy work the same across almost all
  spells, and can usually be boosted by casting at a higher difficulty.
mechanics:
  long_range_multiplier: 2
  range_extend_squares_per_difficulty: 1
  base_accuracy: 0
  accuracy_bonus_per_difficulty: 1
---

Most spells share these properties. Unless a spell says otherwise, each
can be boosted by choosing to cast at a higher difficulty than the
minimum — see [[spellcasting]] and [[using-powers]] for what raising
the difficulty costs.

## Range

A spell's range is **self**, **touch**, or a **number**.

- **Self** — the spell only ever affects the caster.
- **Touch** — the caster affects themselves or another recipient by
  touching them. Touching an unwilling target needs a melee attack roll.
- **A number** — a range in grid squares, measured exactly as
  [[movement]] measures them. If the spell needs an
  attack roll to land, the listed number is short range and long range
  is {{ mechanics.long_range_multiplier }} times it, and the casting
  roll is the attack roll — see below. Aiming into long range costs
  accuracy, exactly as it costs an archer accuracy; that is under
  **Accuracy** below. Range can be extended by
  {{ mechanics.range_extend_squares_per_difficulty }} square per point
  of added difficulty, which is how a caster buys their way out of the
  penalty rather than paying it.

## Duration and area

Both have rules of their own: [[spell-duration]] for how long a spell
lasts, and [[spell-area]] for the shapes an area spell can take and what
each square of it costs.

## Aiming a spell

A spell that needs an attack roll is aimed with the **casting roll
itself**. You do not roll twice: the one roll settles whether the spell
happened, what it cost, and whether it landed, exactly as a melee power
rolled on melee attack does — see [[using-powers]].

## Accuracy

A spell's standard accuracy is
`{{ mechanics.base_accuracy }}` — no bonus or penalty to the attack
roll. Accuracy increases by
`+{{ mechanics.accuracy_bonus_per_difficulty }}` for every point of
added difficulty.

A spell aimed past its short range loses accuracy instead of gaining
it: `{{ ranged-weapons:mechanics.long_range_penalty }}` on the attack
roll. That is the same figure [[ranged-weapons]] charges anybody shooting at that
distance, and it is the same rule: how far away a thing is does not
care what launched it.

Being accuracy rather than difficulty settles which of the casting
roll's two jobs it touches. [[using-powers]] has the roll answering the
declared difficulty first and the target's targeting difficulty second;
an accuracy penalty applies only to the second. Reaching a long way
does not make a spell harder to *cast* — it makes it harder to
**place**. A caster who misjudges the distance loses the bolt, not the
spirit.

## Example

Sela casts a bolt at a target `14` squares away. The spell's listed
range is `10`, which is short range; long range is double that, so `14`
is within reach but at long range.

Cast from there it would land at
`{{ ranged-weapons:mechanics.long_range_penalty }}` accuracy, so she
boosts the range instead: each point of added difficulty extends it by
a square, so declaring `4` points above the base brings the target
inside short range. Those `4` points are added to the difficulty she
declares, and are paid for in spirit exactly as any other reach would
be.

That is the choice the penalty exists to offer. She can spend spirit to
stand closer than she is, or spend accuracy and hope. An archer at the
same distance has only the second of those.

Because the bolt needs an attack roll, that same casting roll is what
places it: one roll, compared first to the difficulty she declared and
then to her target's targeting difficulty.

{% book-only %}
## Design note

Boosting works through the same declared-difficulty mechanism as every
other power, so there is no separate list of metamagic rules to learn.
A caster who understands how reaching further works for a physical power
already understands how it works for range, accuracy and area.

Aiming with the casting roll rather than with the ranged attack skill
is not a convenience. A caster's discipline does not grant the ranged
attack skill at all, so under the alternative every bolt-thrower in the
game was aiming with a peripheral skill: measured, a Master of the
Magical discipline landed sixty per cent of their bolts at level fifteen
and could do nothing about it except buy a skill their discipline
charges them triple for. A spell is a power, and a power rolled on its
own skill hits with that roll.

Spell ranges count the same squares movement does, rather than carrying
a measure of their own. A caster who knows how far they can walk knows
how far they can reach, and nobody converts units mid-fight.

Long range costs a caster exactly what it costs an archer, because the
alternative is a game in which distance is a real problem for one half
of the party and a printed number for the other. Two bands and one
penalty is also the least a rule can be and still be a rule: there is
nothing to look up, and the answer for a bolt is the answer for an
arrow.

Charging it as accuracy rather than as difficulty is what keeps the two
fair to each other. Difficulty is the caster's price for the spell
happening at all, and loading distance onto it would mean a spell
thrown a long way could fail outright and still cost spirit — a
punishment an archer never faces for the same misjudgement, in a
subsystem that already has enough ways to go wrong. Accuracy touches
only the aiming, which is the part distance actually has an opinion
about.
{% endbook-only %}
