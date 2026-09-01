---
id: spell-duration
title: Spell Duration
tags: [magic, core]
summary: >
  Almost every spell is instantaneous, lasts a number of rounds, lasts
  while it is maintained, or is permanent. Only the second is bought
  with difficulty.
mechanics:
  kinds: [instantaneous, rounds, maintained, permanent]
  rounds_extended_per_difficulty: 1
  maintained_spells_at_once: 1
  maintaining_costs_an_action: false
  concentration_difficulty_equals_damage_taken: true
  permanent_fades_after_years: 1000
---

Every spell names one of four durations.

## Instantaneous

The spell fires, does what it does, and is gone. Most damaging spells
are instantaneous: the fire is not still burning next round, it simply
arrived. Nothing that follows can dispel it, because there is nothing
left to dispel.

## A number of rounds

The spell lasts the listed number of rounds, counted from the end of
the turn on which it was cast. Add
{{ mechanics.rounds_extended_per_difficulty }} round for each point of
difficulty spent on it, exactly as [[spell-properties]] buys range.

## While maintained

The spell lasts as long as the caster maintains it, which costs nothing
on a turn where the caster does nothing that demands their full
attention. Casting a second spell ends the first.

A caster may maintain
{{ mechanics.maintained_spells_at_once }} spell at a time.

**When something disturbs you**, make a **Concentration** check or the
spell ends. Being wounded is the ordinary case, and the difficulty is
the damage that got through. The Dungeon Master sets it for anything
else: a shove, a shout, a corridor collapsing.

## Permanent

The spell either creates something that is naturally permanent — a wall
of real stone, a wound closed — or sustains itself indefinitely.

Nothing lasts for ever. A self-sustaining spell fades after about
{{ mechanics.permanent_fades_after_years }} years, which is never a
consideration in play and occasionally the reason a very old thing has
recently stopped working.

## Example

Sela casts a spell listed at `3` rounds. She spends `2` points of
difficulty on top of what she wanted anyway, and it runs for `5` rounds
instead.

Later she casts a maintained spell to hold a door shut. It costs her
nothing to keep it up while she stands back and watches — but when an
orc gets a spear past her guard for `7` damage, she must make a
Concentration check against `7` or the door swings open. She could
instead have thrown a bolt, but casting anything else would have dropped
the door by itself.

{% book-only %}
## Design note

Four durations rather than a number per spell means a player learns the
system once. The only one that scales with difficulty is the counted
one, because it is the only one where more is straightforwardly better:
buying rounds on a maintained spell is meaningless, and buying rounds on
an instantaneous one is a contradiction.

Maintenance costing nothing by default, but ending when you cast again,
is what stops a caster stacking a wall of concurrent effects while still
throwing bolts. One maintained spell is a standing commitment of the
caster's attention, and the cost of it is everything else they might
have been doing with a spell.

This is also the job Concentration was waiting for. It has sat in the
skill list since the beginning without a single rule referencing it, and
tying it to damage taken gives it a difficulty that scales naturally
with how bad the fight is going rather than needing a table.

A thousand years for permanence is a deliberate compromise between "for
ever", which forecloses a story, and a duration short enough that
players start tracking it. It should never come up at the table except
as the answer to why a ward that held for forty generations failed last
winter.
{% endbook-only %}
