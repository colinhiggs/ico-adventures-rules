---
id: orc
title: Orc
kind: creature
tags: [bestiary, creature, humanoid]
summary: >
  A raider that comes straight at you, takes a hit to give one, and is
  the first thing in this book a first-level character cannot simply
  out-last.
mechanics:
  challenge_level: 2
  typical_number: 5
  attributes:
    strength: 14
    dexterity: 10
    constitution: 14
    intelligence: 8
    willpower: 10
    charisma: 8
  skills:
    attack_melee: 4
    dodge: 2
    block: 2
    spot: 2
    fortitude: 4
    resolve: 2
  disciplines: {}
  powers: []
  levels_up: true
  preferred_disciplines: [martial, athletic]
  outlawed_disciplines: [magical]
  mastery_hit_points: 6
  core_hit_points: 14
  stamina: 14
  spirit: 0
  stance: dodge
  weapon: hand_axe
  armour: leather
  shield: none
  morale_breaks_at_core_fraction: 0.34
---

Where a [[goblin|goblin]] would rather be behind you, an orc would
rather be in front of you and is quite happy for that to cost it
something. It is bigger, slower and considerably harder to put down.

{% table mechanics.attributes header=Attribute value_header=Score %}

{% table mechanics.skills header=Skill value_header=Rank %}

## How it fights

It closes and it swings. There is no more to it than that at this
threat, and there does not need to be: strength
{{ mechanics.attributes.strength }} behind a
[[weapons|hand axe]] and {{ mechanics.core_hit_points }} core hit
points is an opponent a first-level character trades with rather than
beats.

Its dodge is poor and it wears only [[armour|leather]], so it is easy
to hit. What it is not is easy to finish, and a party that is used to
goblins folding to one blow finds the round it planned for has become
three.

An orc band breaks at about a third, which is later than a goblin band
and sooner than it looks — orcs count a fight as going badly when they
stop making ground, not when they start losing.

## Orcs with a career

It levels — see [[creature-advancement]]. It prefers **Martial**, which
is the axe, and **Athletic**, which is the closing. It is barred from
**Magical**: orc magic exists and is somebody else's entry.

- **Orc veteran** *(`3` levels, threat `5`)*. Martial adept, a shield
  and a real sword, fighting in block. The same creature with the thing
  it lacked — the ability to survive being concentrated on.
- **Orc chieftain** *(`7` levels, threat `9`)*. Martial adept, Athletic
  adept, Riposte. Every blow the party misses with costs it.

{% book-only %}
## Design note

The orc is the second rung and exists to be the first creature that
does not die to one hit. A goblin teaches a party that a crowd is
dangerous; an orc teaches it that a single body can be, which is the
lesson everything above threat {{ mechanics.challenge_level }} in this book depends on.

It had been in the simulator for as long as there has been one, as five
numbers in a table, and only reached this book when the two were made
to agree. That the numbers here are not those numbers is the whole
argument for having written it down.
{% endbook-only %}
