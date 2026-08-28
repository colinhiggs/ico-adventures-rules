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
[[character-creation]] — there is nothing you can buy on levelling that
you could not have bought at the start, and nothing you bought at the
start that is now closed to you.

## What a level gives

- {{ mechanics.points_per_level }} points to spend, as below.
- {{ mechanics.free_mastery_hp_per_level }} mastery hit points, free
  and automatic. Everyone gets these; they are the baseline survival
  curve that used to come from a class.
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
  {{ mechanics.mastery_hp_per_point }} of them, but no more than
  {{ mechanics.max_mastery_hp_bought_per_level }} bought per level may
  be added on top of the free grant. Without that ceiling a character
  with nothing else to buy turns every spare point into padding, and
  fights get longer every level rather than deadlier.
- **Stamina or spirit** — one point buys
  {{ mechanics.power_source_per_point }} points of one
  [[power-sources|power source]], to a limit of
  {{ mechanics.max_power_source_bought_per_level }} points spent per
  level. Powers get more expensive as you reach further with them, so a
  character who never widens the reservoir slowly loses access to their
  own best tricks.

Both ceilings are per level and cumulative: a character who skipped
them last level may catch up on this one. What they prevent is a
character with nothing left to buy converting an entire level into one
runaway statistic.

Mastery hit points are cheap per point precisely because a skill rank
keeps paying out on every roll you ever make and a mastery hit point
absorbs its damage once. Both are worth buying; neither should be
obviously correct.

The per-level mastery grant is deliberately small next to the opening
reserve in [[character-creation]]. Hit points that climb steeply every
level while damage stays flat do not make a character heroic, they make
every fight longer than the last; the curve here is meant to be nearly
flat, with the growth in what a character can *do* rather than in how
long they take to kill.

Core hit points are not on this list. They remain equal to your
constitution and grow only when that attribute does — see
[[hit-points]]. A character's real durability stays almost flat for
life, and everything the levels add is the cushion in front of it.
