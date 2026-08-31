---
id: turn-order
title: Turn Order
tags: [core, combat]
summary: >
  Combat runs in rounds. Order is set once by a Spot check, everyone
  acts once, and each character holds one reaction for someone else's
  turn.
mechanics:
  initiative_roll: "1d20"
  initiative_skill: spot
  order_fixed_for_the_fight: true
  actions_per_turn: 1
  moves_per_turn: 1
  reactions_per_round: 1
  ties_broken_by: dexterity
---

When talking stops and violence starts, time breaks into **rounds**.
Every combatant acts once per round, in an order settled when the fight
begins.

## Setting the order

Each combatant rolls `{{ mechanics.initiative_roll }}` and adds their
**{{ mechanics.initiative_skill }}** skill. Highest goes first, and that
order holds for the rest of the fight. Ties go to the higher
{{ mechanics.ties_broken_by }}, and if that is level too, to whichever
of them the Dungeon Master judges was already moving.

Initiative is a Spot check because acting first is a matter of noticing
first — see [[skill-list]], and the Forewarned power in
[[discipline-powers]], which buys a better place in the order before the
fight starts.

## What a turn contains

On your turn you have {{ mechanics.actions_per_turn }} **action** and
{{ mechanics.moves_per_turn }} **move**, in either order. Attacking is
an action. Invoking a power is part of the action it belongs to rather
than a separate one, so a power that grants extra attacks is still a
single action — see [[using-powers]]. Moving is measured in squares; see
[[movement]].

You may always do less. Speaking is free within reason: a shouted
warning costs nothing, a speech costs your action.

## Reactions

You also hold {{ mechanics.reactions_per_round }} **reaction**, spent on
someone else's turn rather than your own. It refreshes at the start of
each of your turns, so a reaction spent answering the first enemy to
swing at you is gone when the second does.

Powers say when they are reactions. Riposte answers an attack that
missed you, Deflect blunts one that did not, and Anticipate spends the
reaction to act out of turn entirely.

## Example

Ashri, Dune and two orcs come to blows. Ashri rolls `12` and adds her
Spot of `4` for `16`; Dune rolls `9` and adds his Spot of `11` for
`20`; the orcs roll `17` and `6`, adding `3` each, for `20` and `9`.

Dune and the first orc have tied on `20`. Dune's dexterity is higher, so
he goes first. The order for the whole fight is Dune, orc, Ashri, orc —
and it does not change even when Dune drops the second orc.

On her turn Ashri moves and then attacks, spending her move and her
action. When the surviving orc swings at her and misses, she spends her
reaction on Riposte and hits back. The next orc to attack her that round
finds her reaction already gone.

{% book-only %}
## Design note

One roll at the start, held for the whole fight, is the cheapest
structure that still makes going first worth wanting. Re-rolling every
round doubles the dice and buys only noise.

Tying initiative to Spot rather than to dexterity gives the Awareness
discipline a job in every fight, which it badly needed — it is the one
discipline with no damage of its own, and "you all act in the order I
tell you" is real authority at a table. It also makes Forewarned
coherent: a Spot power that improves a Spot check.

The single reaction is what makes Riposte, Deflect and Guard choices
rather than free extras. Without a cap, a defensive character answers
every attack in the round and the action economy quietly stops meaning
anything.
{% endbook-only %}
