---
id: advancement
title: Advancement
tags: [core, character, progression]
summary: >
  A level is a budget of points, spent in the same shop as character
  creation — discipline grades, skill ranks, or mastery hit points.
mechanics:
  points_per_level: 15
  free_mastery_hp_per_level: 3
  free_mastery_hp_per_constitution: 1
  mastery_hp_per_point: 2
  max_mastery_hp_bought_per_level: 1
  power_source_per_point: 3
  max_power_source_bought_per_level: 3
  powers_per_level: 1
  attribute_point_every_n_levels: 4
  level_is_only_a_budget_and_a_clock: true
---

A **level** in Ico is not a template. It is a budget of
{{ mechanics.points_per_level }} points and a clock that raises your
skill ceilings, and it is spent in exactly the same shop as
[[character-creation]].

## What a level gives

- {{ mechanics.points_per_level }} points to spend, as below.
- {{ mechanics.free_mastery_hp_per_level }} mastery hit points, free
  and automatic, plus
  {{ mechanics.free_mastery_hp_per_constitution }} more for each point
  of your **constitution** bonus. A hardy character accumulates the
  cushion faster, every level, without paying for it.
- {{ mechanics.powers_per_level }} power, chosen from a pool you have
  opened — see [[disciplines]] and [[discipline-powers]].
- Every {{ mechanics.attribute_point_every_n_levels }} levels, one
  attribute point.
- One more rank of headroom on every skill ceiling, per [[skills]].

## What points buy

- **A discipline grade** — at the cost listed in [[disciplines]].
- **One rank in a skill** — at the cost listed in [[skills]], which
  depends on how that skill is focused.
- **Mastery hit points** — one point buys
  {{ mechanics.mastery_hp_per_point }} of them, to a limit of
  {{ mechanics.max_mastery_hp_bought_per_level }} bought per level on
  top of the free grant.
- **A language** — see [[languages]] for what one costs. Languages have
  no ranks; you either speak one or you do not.
- **Stamina or spirit** — one point buys
  {{ mechanics.power_source_per_point }} points of one
  [[power-sources|power source]], to a limit of
  {{ mechanics.max_power_source_bought_per_level }} points spent per
  level.

Both ceilings are per level and cumulative: a character who skipped them
last level may catch up on this one.

Core hit points are not on this list. They remain equal to your
constitution and grow only when that attribute does — see
[[hit-points]].

## Example

Ashri reaches a new level. She receives her free mastery hit points, one
power, and a rank of headroom on every ceiling.

She then spends her points: `4` raising four focused skills by a rank
each at a point apiece, `1` on the mastery hit points she is allowed to
buy this level, `3` on widening her stamina, and banks the remaining `7`
toward Martial Master, which she cannot yet afford outright.

This level happens to be divisible by four, so she also takes an
attribute point and puts it into strength.

{% book-only %}
## Design note: what constitution is for

Constitution was the attribute nobody wanted. It bought core hit points
and the base of a power source, and core hit points are a small slice of
a pool that mastery hit points dominate, so four points spent on it were
worth about three quarters of what the same four were worth in strength
or dexterity. An attribute that is never the right answer is a tax on
the players who did not notice.

Tying free mastery hit points to it fixes that, and the reason it is a
**grant** rather than a **cap** is worth keeping. Two other repairs were
measured and both failed for the same reason. Letting constitution raise
the ceiling on mastery hit points a character may *buy* helps late,
where builds have points spare, and actively hurts in the middle levels,
where they do not and the extra hit points come out of skills:
constitution went from about three quarters of the best attribute to
three fifths of it. Letting constitution and willpower raise the ceiling
on the power source did nothing whatever, at any level — a senior
character already has far more stamina or spirit than a fight can spend,
so converting spare points into more of it converts them into nothing.

A grant costs a character nothing and therefore cannot be paid for out
of the wrong pocket, which is the trap the other two fell into. It takes
constitution to about nine tenths of the value of the best attribute at
every level: worth buying, and still not the obvious answer.
## Design note

The per-level mastery grant is deliberately small next to the opening
reserve in [[character-creation]]. Hit points that climb steeply every
level while damage stays flat do not make a character heroic; they make
every fight longer than the last. The curve here is meant to be nearly
flat, with the growth in what a character can *do* rather than in how
long they take to kill.

The two purchase ceilings exist for the same reason. Without them a
character with nothing else worth buying converts an entire level into
one runaway statistic, and the balance between damage and durability
that the rest of the system rests on quietly stops holding.

Mastery hit points are cheap per point precisely because a skill rank
keeps paying out on every roll you ever make while a mastery hit point
absorbs its damage once. Both are worth buying; neither should be
obviously correct.
{% endbook-only %}
