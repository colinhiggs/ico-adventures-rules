---
id: hobgoblin
title: Hobgoblin
kind: creature
tags: [bestiary, creature, humanoid]
summary: >
  Drilled infantry. It holds a line, it does not break, and it is the
  first thing in this book that fights as a unit rather than as a
  number of individuals.
mechanics:
  challenge_level: 5
  typical_number: 8
  attributes:
    strength: 14
    dexterity: 12
    constitution: 14
    intelligence: 10
    willpower: 12
    charisma: 10
  skills:
    attack_melee: 6
    block: 6
    dodge: 3
    spot: 3
    fortitude: 4
    resolve: 4
  disciplines:
    martial: initiate
  powers: [power_attack, guard]
  push: 21
  levels_up: true
  preferred_disciplines: [martial, social]
  outlawed_disciplines: [magical]
  mastery_hit_points: 12
  core_hit_points: 14
  stamina: 20
  spirit: 0
  stance: block
  weapon: sword
  armour: scale_mail
  shield: shield
  morale_breaks_at_core_fraction: 0.25
---

A hobgoblin is what a goblin is not: tall, disciplined, and entirely
willing to be in front. It wears armour issued to it rather than taken
off something, it has been taught to use the sword it carries, and it
has been taught it standing next to somebody else.

{% table mechanics.attributes header=Attribute value_header=Score %}

{% table mechanics.skills header=Skill value_header=Rank %}

## How it fights

It blocks. Strength {{ mechanics.attributes.strength }} and Block
{{ mechanics.skills.block }} behind a [[armour|shield]] is a targeting
difficulty a fifth-level party has to work at, and unlike a
[[goblin|goblin]] it is not trying to be somewhere else — it is trying
to be exactly where it is, for as long as that is useful.

It has Guard — see [[discipline-powers]] — and it is the first creature
in this book that will spend a reaction on somebody else. A line of
hobgoblins is not {{ mechanics.typical_number }} separate fights. The
ones in front cover the ones behind, and a party that concentrates on
one of them finds the blow arriving somewhere it did not aim.

Hobgoblins do not break. The fraction in
`morale_breaks_at_core_fraction` is half what a goblin band will take,
and it is there for form's sake: a hobgoblin unit that is losing
withdraws in order and comes back, which is a different problem for
whoever is running the fight and not an easier one.

## Hobgoblins with a career

It levels — see [[creature-advancement]]. The block above is a soldier
in the ranks, and the ranks are where hobgoblins put the ones who have
not done anything yet.

It prefers **Martial**, which is what it already is, and **Social**,
which is the one thing this book's bestiary has otherwise had no use
for: Rally and Hold the Line are powers for somebody with people to
give orders to, and a hobgoblin has those. It is barred from
**Magical**. Hobgoblin sorcery exists and belongs to something else.

- **Hobgoblin sergeant** *(`2` levels, threat `7`)*. Martial adept and
  Social initiate, carrying Rally. It spends its own action making four
  other hobgoblins better, which is the first enemy in this book whose
  action does not point at a character at all.
- **Hobgoblin captain** *(`6` levels, threat `11`)*. Martial adept,
  Social adept, Hold the Line. Its unit does not rout, and it has the
  Block to survive being the one the party goes for.
- **Hobgoblin warlord** *(`12` levels, threat `17`)*. Martial master,
  which is Killing Blow, and Social adept. A single one of these in
  front of a line of ordinary hobgoblins is a fifteenth-level
  encounter, and the line is what makes it one.

{% book-only %}
## Design note

The hobgoblin exists because the bestiary needed a creature that was not
a crowd. A [[goblin|goblin]] band is a number, and past the engagement
limit a bigger number is a longer fight rather than a harder one — so
scaling a fight by adding goblins stops working long before fifteenth
level.

What it does instead is hold together. Guard in a stat block is the
first time anything on this side of the table has spent a reaction to
protect somebody, and Social is here for the same reason: Rally and Hold
the Line were written for a character with allies and no character in
the panel has ever had a use for them. A hobgoblin unit does.

It is deliberately not tougher than the arithmetic needs. Its hit points
are barely twice a goblin's; almost all of what makes it a fifth-level
problem is that it can hit a fifth-level character and a goblin cannot.
Accuracy is what scales, which is the whole argument of
[[creature-advancement]].
{% endbook-only %}
