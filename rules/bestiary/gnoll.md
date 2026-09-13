---
id: gnoll
title: Gnoll
kind: creature
tags: [bestiary, creature, humanoid]
summary: >
  A pack hunter that fights the wounded and the separated by choice.
  Fast, accurate, and entirely uninterested in a fair fight.
mechanics:
  challenge_level: 10
  typical_number: 9
  attributes:
    strength: 16
    dexterity: 14
    constitution: 14
    intelligence: 8
    willpower: 10
    charisma: 8
  skills:
    attack_melee: 17
    dodge: 8
    spot: 7
    stealth: 6
    fortitude: 6
    resolve: 3
  disciplines:
    martial: initiate
    athletic: adept
  powers: [power_attack, sneak_attack, redouble]
  push: 24
  levels_up: true
  preferred_disciplines: [athletic, martial]
  outlawed_disciplines: [magical, social]
  mastery_hit_points: 6
  core_hit_points: 14
  stamina: 34
  spirit: 0
  stance: dodge
  weapon: battle_axe
  armour: chain_shirt
  shield: none
  morale_breaks_at_core_fraction: 0.34
---

A gnoll is a head taller than a man and moves like something that has
never had to think about it. It hunts in a pack, it hunts by choice, and
what it is choosing is whoever is already hurt.

{% table mechanics.attributes header=Attribute value_header=Score %}

{% table mechanics.skills header=Skill value_header=Rank %}

## How it fights

It has Sneak Attack — see [[discipline-powers]] — and the whole of its
tactics is arranging to use it. A gnoll pack does not form a line. It
goes round one, and the thing it is going round the line to reach is the
character with the fewest hit points left rather than the one with the
fewest defences.

At Athletic adept it dodges rather than blocks, and Redouble means the
stamina in `stamina` is a targeting difficulty it can hold up for most
of a fight. Against a tenth-level party that is not enough to make it
hard to hit. It is enough to make it take three rounds instead of two,
and three rounds is another character down.

Unlike a [[hobgoblin|hobgoblin]] it will break, and it breaks upward:
a pack that has lost a third of its number does not run home, it runs at
whoever is furthest from help.

## Gnolls with a career

It levels — see [[creature-advancement]]. It prefers **Athletic**, which
is most of what it is, and **Martial**, which is the axe. It is barred
from **Magical** and from **Social**: a gnoll pack has a leader because
something has to be biggest, and no gnoll has ever given an order that
was not a noise.

- **Gnoll pack-leader** *(`3` levels, threat `13`)*. Athletic master,
  which is Untouchable — it wears its mail and dodges in it with no
  penalty at all. The pack's targeting difficulty problem, standing
  where the pack can see it.
- **Gnoll fang** *(`7` levels, threat `17`)*. Martial adept and
  everything else into Attack and Sneak Attack. It exists to remove one
  character from the fight in one round, and against anybody already
  wounded it usually does.

{% book-only %}
## Design note

The gnoll is the crowd creature for the level where crowds stop working.
Six of them is a real encounter for a tenth-level party where forty
goblins is not, and the difference is entirely accuracy: Attack
{{ mechanics.skills.attack_melee }} reaches a tenth-level character's
targeting difficulty and a goblin's {{ goblin:mechanics.skills.attack_melee }}
does not.

It is given Sneak Attack rather than more hit points on purpose. A
creature that punishes an existing weakness makes the party's own
attrition into a threat, which is what a day of encounters is supposed
to be about, and it does that without needing a bigger number anywhere.

It is also, deliberately, *less* durable than a
[[hobgoblin|hobgoblin]] three threat levels beneath it, and the reason
is the whole argument of this bestiary. A creature's threat is its
accuracy. Attack {{ mechanics.skills.attack_melee }} lands on a
tenth-level party most of the time and
{{ mechanics.mastery_hit_points }} mastery hit points means the party
kills better than two of them a round, so a gnoll pack is a race rather
than a grind — which is what the measurement asked for. Hit points only
ever bought duration.
{% endbook-only %}
