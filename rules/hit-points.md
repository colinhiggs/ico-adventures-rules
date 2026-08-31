---
id: hit-points
title: Core and Mastery Hit Points
tags: [core, character, health]
summary: >
  Core hit points are your body and equal your constitution. Mastery
  hit points are luck and skill, and soak harm first.
mechanics:
  core_hp_equals: constitution
  core_hp_is_real_injury: true
  mastery_hp_is_near_miss: true
  damage_order: [mastery, core]
---

Characters have two separate pools of hit points, and they mean
different things.

## Core hit points

Core hit points (CHP) are physical hardiness and the sheer will to keep
going. A character's core hit points equal their
{{ mechanics.core_hp_equals }}. Losing core hit points means real
damage — a wound that actually landed.

## Mastery hit points

Mastery hit points (MHP) are an accumulated cushion of luck, skill and
experience. Losing mastery hit points is a near miss, a blow softened by
rolling with it, a fight-ending strike that turned out to graze. They
are bought as a character is built and advanced — see
[[character-creation]] and [[advancement]].

## Getting them back

Mastery hit points come back between fights; core hit points very nearly
do not. See [[recovery]].

## Which pool takes the hit

Harm comes off mastery hit points first, and reaches core hit points
only once mastery is exhausted. [[damage]] covers how the size of a hit
is worked out before it is applied here.

## Example

Dune has constitution `13`, so `13` core hit points, and has bought
`22` mastery hit points. He takes a blow for `9`.

All `9` come off mastery, leaving him on `13` mastery and `13` core. He
is untouched in the fiction: the axe went past his ear.

Later in the same fight he takes another `17`. The first `13` empty his
mastery pool; the remaining `4` come off core. Now he is genuinely cut,
and the Dungeon Master should describe it that way — the first wound of
the fight arrives at the moment his luck runs out, not before.

{% book-only %}
## Design note

The split exists so that losing hit points can mean two different things
without needing two different rules. It also means a character's real
durability barely changes over a career, since core hit points follow
constitution and nothing else: veterans get a bigger cushion of luck and
skill, not tougher flesh. A blow that reaches core hit points is as
serious at level twenty as it was at level one.
{% endbook-only %}
