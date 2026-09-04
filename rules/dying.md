---
id: dying
title: Wounds, Death's Door and Dying
tags: [core, combat]
summary: >
  Half your core hit points gone leaves you wounded; all of them gone
  leaves you unconscious and dying, with a few rounds for somebody to do
  something about it.
mechanics:
  wounded_at_or_below_fraction: 0.5
  scar_from_single_blow_fraction: 0.5
  scars_only_from_natural_healing: true
  deaths_door_at_core: 0
  unconscious_at_deaths_door: true
  rounds_before_dying: 3
  self_stabilise_skill: fortitude
  stabilise_base_difficulty: 10
  stabilise_difficulty_per_point_below_zero: 1
  aid_skill: heal
  dead_at_negative_core_of: constitution
  hours_before_waking: 4
---

Losing mastery hit points costs you nothing but your luck. Losing core
hit points is the part that matters, and there are two thresholds in it.

## Wounded

When your core hit points fall to
{{ mechanics.wounded_at_or_below_fraction }} of their maximum or below,
you are **wounded** — see [[conditions]]. Nobody rolls for it and nobody
can resist it. It is simply what being half dead does to a person.

It lasts until your core hit points are above half again, which
[[recovery]] makes clear is not a thing that happens quickly — though
how quickly depends on you. Core hit points mend overnight at a rate
that rises with your constitution bonus, so a tough character shakes a
bad wound off in a couple of nights and a frail one carries it for a
week. A wounded character who cannot find a healer is wounded until
their own body catches up.

## Scars

If a single blow takes
{{ mechanics.scar_from_single_blow_fraction }} or more of your maximum
core hit points, the wound is bad enough to leave a mark — but only if
it is allowed to close on its own. Healed by magic it leaves nothing.
Healed by time and bandages, it leaves a **scar**.

A scar has no game effect whatsoever. It is a note on the character
sheet saying where they have been, and the only reason it is in the
rules at all is that a character who has been carried out of three
dungeons should look like it.

## Death's door

At {{ mechanics.deaths_door_at_core }} core hit points or fewer you are
**at death's door**: unconscious, unable to act, and dying. You have
{{ mechanics.rounds_before_dying }} rounds. If nothing has been done by
the end of them you are dead.

You are also dead immediately if your core hit points ever reach
`-{{ mechanics.dead_at_negative_core_of }}` — negative your
constitution, which is the same size as the pool you started with. You
can lose your hit points twice and no more than that.

Three things can be done about it, and any of them stops the count.

### You save yourself

At the end of each of your turns while dying, roll
`{{ core-resolution:mechanics.standard_die }}` and add your
{{ mechanics.self_stabilise_skill }} against a difficulty of
{{ mechanics.stabilise_base_difficulty }}, plus
{{ mechanics.stabilise_difficulty_per_point_below_zero }} for every
point your core hit points are below
{{ mechanics.deaths_door_at_core }}. Beat it and you are **stable**.

### Somebody else saves you

An ally within reach may spend their action on a
{{ mechanics.aid_skill }} check against that same difficulty. On a
success you are stable. On a failure they may try again next round, and
next round, for as many rounds as you have left — which is what makes a
bad roll here cost so much.

### Magic saves you

**Staunch** stops the count and does nothing else: you remain
unconscious on whatever you were reduced to, and it can be cast from
across the room. It is the cheap answer and usually the right one in the
middle of a fight.

Any spell that restores **core** hit points and takes you above
{{ mechanics.deaths_door_at_core }} does more: you are stable *and*
conscious, and standing up is a matter of your next move. Mend cannot do
this, because it only touches mastery hit points. Cure Wounds can, and
this is the second reason it is priced the way it is.

Both are in the [[spell-list]].

## Stable

A stable character is no longer dying and is still unconscious. They
wake about {{ mechanics.hours_before_waking }} hours later, on
{{ mechanics.deaths_door_at_core }} core hit points and thoroughly
wounded, unless somebody heals them first.

## After death

Death is not always the end of it, but the spell that answers it is
expensive, gets harder every hour, and stops working entirely after a
day — see **Raise the Dead** in the [[spell-list]]. A party that wants
somebody back should be in a hurry.

## Example

Dune has constitution `14`, so `14` core hit points and `7` is half. A
troll hits him for `20` past his mastery pool. That takes him to `-6`.

Two things happen at once. He is at death's door, unconscious with
{{ mechanics.rounds_before_dying }} rounds to live; and because `20` was
more than half his maximum core in one blow, if he lives through this
without magic he will carry the scar.

His own Fortitude check is against `10` plus `6` for being six points
under, so `16` — and he rolls it at the end of each of his turns, if he
has any left. Sela reaches him on the second round and tries a
{{ mechanics.aid_skill }} check against that same `16`. She fails. She
tries again on the third round, which is the last one, and makes it.

Dune is stable at `-6`, wakes four hours later, and spends the next
several days wounded and taking
`-{{ conditions:mechanics.conditions.wounded.roll_penalty }}` on
everything he does.

Had Sela cast Staunch on him on the first round, from where she was
standing, the whole question would have been settled before her second
turn — though he would still have been unconscious at `-6` until
somebody healed him.

Had she cast Cure Wounds instead, for enough to take him to `1` or
better, he would have been conscious immediately — and unscarred.

{% book-only %}
## Design note

The difficulty of stabilising rises with how far under you are, which
means a character dropped by a glancing blow is usually fine and one
dropped by a troll usually is not. That single number does the work that
a table of injury severities would otherwise do, and it uses the
arithmetic the rest of the game already uses: how badly you lost decides
how bad it is.

Dying on a count of rounds rather than a count of failed rolls is what
keeps it a *party* problem. A timer can be beaten by somebody crossing
the room, which makes the rest of the table's decisions matter; a series
of the dying character's own rolls is a solitaire game played while
everyone else watches. The self-stabilise check is there so that being
alone is survivable, not so that it is the main route.

The floor at negative constitution exists so that enormous single hits
can kill outright. Without it, a character felled by a dragon is in
exactly the same position as one felled by a rat, which makes the dragon
less frightening than it should be and the rules less believable than
they are cheap to make.

Wounded is deliberately a penalty on everything rather than on combat
alone. Ico has no separate injury system, and the reason it does not
need one is that a single condition, arriving automatically and leaving
only when the wound is genuinely mended, already says what an injury
system says. It also makes [[recovery]]'s meanness about core hit points
bite: a party that presses on after a bad fight does so at
`-{{ conditions:mechanics.conditions.wounded.roll_penalty }}` a head,
and that is the argument for going home.

Scars have no mechanical weight on purpose. Every version of this rule
that gives them one turns into a system for accumulating permanent
penalties, which punishes exactly the players who take risks and get
carried out. A scar should be something a player wants.
{% endbook-only %}
