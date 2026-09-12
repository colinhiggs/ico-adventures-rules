---
id: creature-advancement
title: Creatures That Level
kind: rule
tags: [bestiary, creature, progression]
summary: >
  An intelligent creature's stat block is what it is before it has done
  anything. Give it levels and it advances on exactly the character
  rules, within the disciplines its kind is suited to and outside the
  ones it is barred from.
mechanics:
  advances_as_a_character: true
  stat_block_is_before_any_levels: true
  threat_per_level: 1
  outlawed_disciplines_bar_their_powers: true
  unintelligent_creatures_do_not_level: true
---

A goblin is a person. So is an orc, a hobgoblin, an ogre and a giant,
and a person who has been doing something dangerous for twenty years is
not the same as one who started last week. The stat block in
[[ch-bestiary|the bestiary]] is the second of those: **what the creature
is before it has done anything**, and the floor of what its kind can be
rather than the whole of it.

## Levelling a creature

An entry marked as one that levels advances on the character rules and
no others — see [[advancement]]. Each level gives it
{{ advancement:mechanics.points_per_level }} points to spend on
discipline grades, skill ranks, mastery hit points or a power source, at
the prices [[skills]] charges, under the ceilings [[skills]] sets, plus
the free mastery hit points a level grants anybody.

Nothing here is a second system. A goblin with four levels was built the
way a fourth-level character was built, from a different starting block,
and everything a party can do about a levelled character it can do about
a levelled goblin.

## Grades are what let a creature hit harder

Most of what a level buys a creature is more of the same: ranks, hit
points, a wider reservoir. A **grade** buys something a stat block
cannot, because a grade is what opens the upper rungs of a power — see
[[using-powers]]. A creature holding Martial at Initiate may declare
Power Attack and stop where Power Attack stops, however good its attack
skill; one holding it at Adept may declare Hammer Blow and go on from
there.

This is where a dangerous individual of an ordinary kind comes from. It
is not a bigger weapon or an invented number: it is a creature that has
bought the grade, and its damage climbs the way a character's does
because it is the same ladder.

## Threat

Each level adds about {{ mechanics.threat_per_level }} to the creature's
threat level, which is a starting guess and not a calculation. Threat is
a claim about which party a creature is a fair fight for, and the only
way to know it is to measure it — see the design note in [[goblin]],
which has been saying so since there was one creature in this book.

## What a kind is suited to

A creature that levels carries two lists, and they are about what the
creature *is* rather than what would be convenient:

- **Preferred disciplines** — what it takes first, and what its stat
  block is already leaning towards. A hobgoblin that has been promoted
  has been promoted for soldiering.
- **Outlawed disciplines** — what it may never take at all. A goblin
  does not become a wizard; a thing with no soul of its own does not
  become a priest. An outlawed discipline bars its powers too, so
  nothing can be reached round the back by taking the power without the
  grade.

Preferences are guidance for whoever is building the creature. Outlaws
are not: they are part of what the kind is, and a creature that breaks
one is a different creature and wants its own entry.

An **unintelligent** creature does not level. It has no career to have
had. A dire wolf is a dire wolf, and a bigger one is a different stat
block rather than an advanced one.

## Example

Ashri's party is four levels in when it walks into the goblin warband it
walked into at first level, and the fight goes differently.

The rank and file are the same: threat {{ goblin:mechanics.challenge_level }},
and Dune goes through them. The one giving the orders has four levels
on it. Goblins prefer Athletic and Awareness, so its levels went into
Athletic, which made Dodge cheap and its ceiling high, and its
{{ advancement:mechanics.points_per_level }} points a level bought rank
after rank of it. It is threat `5` by the rule above — one for the
goblin it started as and about one a level — and Sela cannot hit it.

It is still a goblin. It has eight core hit points, it breaks when its
band breaks, and Bramm's first solid blow ends it. What four levels
bought was not durability but the four rounds it took to land one.

{% book-only %}
## Design note

The bestiary used to say, in as many words, that a creature never gets a
level or an advancement budget, and that `challenge_level` was chosen by
measuring rather than by adding up what the creature had. Half of that
was right and is kept: threat is still measured. The other half was a
gap, and the gap showed up in the simulator rather than at a table.

A day of encounters scaled for a fifteenth-level party needed about
forty goblins, because a goblin that cannot reach a fifteenth-level
character's targeting difficulty contributes nothing however many of it
there are — measured, a goblin's expected damage against a reference
party falls by nine tenths between first level and fifteenth. Numbers
were the only lever the book offered, and numbers run out: a creature
past the engagement limit is queueing rather than fighting, so past a
point each extra body adds length to the fight and no danger to it.

What was missing was the obvious thing. Accuracy is what scales, and
accuracy is what a career buys. An enemy who has been doing this for
years is not a bigger crowd, and the rules for becoming one already
existed — they were simply written on the other side of the table.

Outlawed disciplines exist because the alternative is that every kind
converges. Given a free hand and enough levels, every creature in this
book would buy the same cheap ranks in the same effective skills, which
is exactly what happens to characters and is a separate problem. Saying
what a kind cannot be is cheaper than balancing what it can.
{% endbook-only %}
