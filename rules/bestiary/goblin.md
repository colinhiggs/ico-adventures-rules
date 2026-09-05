---
id: goblin
title: Goblin
kind: creature
tags: [bestiary, creature, humanoid]
summary: >
  A small, quick, cowardly raider that fights in numbers, from cover,
  and only for as long as it is winning.
mechanics:
  challenge_level: 1
  typical_number: 6
  attributes:
    strength: 8
    dexterity: 14
    constitution: 8
    intelligence: 8
    willpower: 8
    charisma: 6
  skills:
    attack_melee: 2
    dodge: 3
    stealth: 4
    spot: 2
    fortitude: 1
  disciplines: {}
  powers: []
  mastery_hit_points: 4
  core_hit_points: 8
  stamina: 5
  spirit: 0
  stance: dodge
  weapon: short_sword
  armour: partial_leather
  shield: none
  morale_breaks_at_core_fraction: 0.5
---

A goblin stands about waist high to a human, and knows it. It carries a
blade too big for it, wears whatever leather it has taken off something
else, and would very much rather be behind you than in front of you.

{% table mechanics.attributes header=Attribute value_header=Score %}

{% table mechanics.skills header=Skill value_header=Rank %}

Alone a goblin is barely a fight. The reason it is the first thing in
this book is that it is never alone: a raiding band is
{{ mechanics.typical_number }} of them, and
{{ mechanics.typical_number }} attacks a round against one target is a
different proposition from one attack six times.

## How it fights

It opens from hiding — Stealth {{ mechanics.skills.stealth }} is the
best thing about it — and it dodges rather than blocks, because at
strength {{ mechanics.attributes.strength }} it has nothing to block
with. Against a dodging goblin an attacker is looking at a target set by
dexterity {{ mechanics.attributes.dexterity }} and Dodge
{{ mechanics.skills.dodge }}, which is more than a first-level party
expects from something this small.

It is fragile in exactly the way that suggests. With
{{ mechanics.mastery_hit_points }} mastery hit points and
{{ mechanics.core_hit_points }} core, a solid hit from a
[[weapons|two-handed weapon]] ends it outright, and any hit at all is
likely to leave it [[dying|wounded]].

Goblins break. When a band has lost
{{ mechanics.morale_breaks_at_core_fraction }} of its number the rest
run, and a group that runs on the third round is the difference between
a goblin ambush and a goblin massacre. This is a judgement for whoever
is running the fight, not a roll.

## Variants

- **Goblin archer.** Swap the short sword for a bow and put the points
  in Attack Ranged instead of Attack Melee. It stays behind the others
  and is the reason the others are there.
- **Goblin boss.** One grade of the Martial discipline, a shield, and
  enough stamina to spend on a power. Worth roughly two ordinary
  goblins and worth killing first, since the band's morale is really
  its morale.

{% book-only %}
## Design note

The goblin is deliberately built the same way a character is built —
six attributes, ranked skills, a weapon and armour off the same tables,
hit points in the same two pools — and not off a separate monster
statistics system. Two reasons. A creature built out of the same parts
can be run through the balance simulator against any archetype, so
"is this a fair fight at level {{ mechanics.challenge_level }}" is a
measurement rather than a guess. And anything the players can do to a
goblin, a goblin can do back, which is the whole argument for not
having a second set of rules for the other side of the table.

What it does not get is a level or an advancement budget. A goblin was
never built by spending points; `challenge_level` says which party this
is a fair fight for and nothing else, and it is chosen by measuring, not
by adding up what the creature has.
{% endbook-only %}
