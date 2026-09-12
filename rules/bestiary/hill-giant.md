---
id: hill-giant
title: Hill Giant
kind: creature
tags: [bestiary, creature, giant]
summary: >
  Two of these is an encounter. It reaches further than anything a party
  carries, it hits once for what a lesser creature manages in a round,
  and there are never enough of it to queue.
mechanics:
  challenge_level: 15
  typical_number: 2
  attributes:
    strength: 18
    dexterity: 8
    constitution: 18
    intelligence: 8
    willpower: 12
    charisma: 8
  skills:
    attack_melee: 14
    block: 11
    dodge: 4
    spot: 6
    fortitude: 12
    resolve: 6
  disciplines:
    martial: adept
  powers: [power_attack, follow_through, find_the_gap]
  levels_up: true
  preferred_disciplines: [martial, awareness]
  outlawed_disciplines: [magical, social]
  mastery_hit_points: 60
  core_hit_points: 18
  stamina: 48
  spirit: 0
  stance: block
  weapon: two_handed_sword
  armour: leather
  shield: none
  morale_breaks_at_core_fraction: 0.5
---

A hill giant is three times the height of a man and swings something
that started as a tree. It is not clever and it does not need to be.
Everything about the encounter is decided by the fact that there are
`2` of it and it reaches further than anything the party is holding.

{% table mechanics.attributes header=Attribute value_header=Score %}

{% table mechanics.skills header=Skill value_header=Rank %}

## How it fights

It is the answer to a problem the rest of this book has: the
[[reach|engagement limit]] means a crowd can only ever get so many
bodies onto a party at once, so past a point more enemies is a longer
fight rather than a harder one. A giant is the other shape. There are
two, both of them can reach, and neither is waiting for a turn.

Its weapon has reach, which almost nothing else on this side of the
table has. A party that wants to fight it has to cross its band, and
[[reach]] says what that costs — a free attack, out of the giant's
reaction, at Attack {{ mechanics.skills.attack_melee }} with a
two-handed sword behind it. Closing on a giant is a decision rather
than a move.

It has Follow Through, which is why {{ mechanics.typical_number }} of
them is worse than the arithmetic suggests: drop a character and the
same swing carries into the next one. And Find the Gap, because
{{ mechanics.mastery_hit_points }} mastery hit points is not actually
its most dangerous number — armour is no answer to it.

It breaks at half, and half of `2` is one. A giant whose companion has
fallen leaves, which is the one mercy in the entry.

## Giants with a career

It levels — see [[creature-advancement]] — and it is the clearest case
in the book for why the rule exists, because there is no larger giant to
reach for. It prefers **Martial** and **Awareness**; it is barred from
**Magical** and **Social**.

- **Giant chieftain** *(`4` levels, threat `19`)*. Martial master,
  which is Killing Blow, on a creature whose margin on a hit is already
  the largest in the book. One of these with two ordinary giants beside
  it.
- **Giant thane** *(`10` levels, threat `25`)*. Martial master and
  Awareness adept, carrying Anticipate. It acts out of turn, which
  means the round in which a party thinks it has an opening is the
  round it does not have.

{% book-only %}
## Design note

Everything in the bestiary before this one is a crowd, and crowds have a
ceiling: eight attackers a defender, so a two-strong front rank is
fighting sixteen creatures however many are in the room. Measured, a
fifteenth-level party clears a day of forty-goblin encounters without
difficulty, and at twenty times the standard day it still clears it
while the fights run past the round band from the other end. More bodies
buys duration and not danger.

The giant is the encounter that is not subject to that at all. Two
creatures, both engaged, both hitting for a great deal. It is deliberate
that its hit points are large and its threat does not mostly come from
them: reach, Follow Through and Find the Gap are all about landing the
blow rather than surviving one.

It levels because there is nowhere else to go. The book could keep
inventing bigger creatures for every tier above this, or it could say
that a giant who has been fighting for forty years is worse than one
who has not, which is both cheaper and truer.
{% endbook-only %}
