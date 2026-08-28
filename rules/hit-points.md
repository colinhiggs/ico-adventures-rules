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
are bought as a character is built and advanced, traded against skill
points — see [[character-creation]].

## Which pool takes the hit

Harm comes off mastery hit points first, and only reaches core hit
points once mastery is exhausted. [[damage]] covers how the size of a
hit is worked out before it is applied here.
