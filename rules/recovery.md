---
id: recovery
title: Recovery Between Fights
tags: [core, combat, health]
summary: >
  After a fight, characters get back a share of their stamina, spirit
  and mastery hit points. The Dungeon Master says whether the interval
  was a breather or a rest. Core hit points are not on the list.
mechanics:
  recovery_is_once_per_encounter: true
  fraction_of_maximum: true
  breather_percent: 25
  rest_percent: 50
  night_restores_all_of: [stamina, spirit, mastery_hit_points]
  core_hit_points_per_night: 1
  core_hit_points_recover_between_fights: false
---

A fight ends. Before the next one begins, everyone gets something back.

## What comes back

Each character recovers a share of their **maximum** stamina, spirit and
mastery hit points — not a share of what is left, which would give
nothing at all to the character who most needs it.

The Dungeon Master says which of two intervals has passed:

- A **breather** returns {{ mechanics.breather_percent }}% of each
  maximum. Long enough to stop shaking and re-strap a shield, and no
  longer.
- A **rest** returns {{ mechanics.rest_percent }}% of each maximum. An
  hour or more, somewhere the party is not expecting to be found.

Recovery happens **once** between one fight and the next. Sitting
around a second time does not pay again; sitting around longer is what
turns a breather into a rest.

A **night's sleep**, somewhere safe, restores stamina, spirit and
mastery hit points completely.

## What does not

Core hit points are not recovered this way at all. They are real
wounds — see [[hit-points]] — and a night's sleep mends
{{ mechanics.core_hit_points_per_night }} of them. An adventuring party
that is losing core hit points faster than that needs a healer, and
Cure Wounds in [[spell-list]] is the reason one travels with them.

## Guidance for the Dungeon Master

Ask what the party actually did, not how many minutes passed:

- **Breather** — they pressed on. They are still in hostile ground,
  still lit, still audible. Wounds bound in a doorway.
- **Rest** — they stopped properly. A barred door, a spiked corridor, a
  watch set. Food, water, and enough quiet to think.
- **Neither** — the next fight arrives before they have caught their
  breath at all. Reinforcements, a pursuing patrol, a second wave.

The last of those is the one worth remembering. Denying recovery is how
a Dungeon Master makes a fight frightening without making the enemies
stronger, and a dungeon that never denies it will find its later fights
easier than its earlier ones.

## Example

Ashri has `40` maximum stamina and has spent all but `4` of it clearing
a guardroom.

The party bars the door, binds wounds and listens for ten minutes before
moving on. The Dungeon Master calls that a breather, so Ashri gets back
a quarter of `40` — `10` — and starts the next fight on `14`.

Later they find a storeroom, spike both doors and set a watch for an
hour. That is a rest: half of `40`, so `20` back. Sitting there for a
second hour gains her nothing more; the hour is what made it a rest
rather than a breather in the first place.

She also took `6` core hit points of damage from a spear in the
guardroom. None of that comes back tonight beyond a single point, and
Sela's Cure Wounds is the only thing that will fix it before the week is
out.

{% book-only %}
## Design note

A dungeon is many fights in a day, and without recovery a character is
empty by the third and a spectator by the fourth — with the boss fight,
the one that should be the most interesting, being the one where nobody
can afford to do anything. Cutting the price of powers would fix that,
but it would do so by making every individual fight easier, which is the
opposite of the intent.

Recovery is a fraction of the maximum rather than a flat number so that
it scales with the character without anyone tuning a second curve, and
because a fraction of what remains would pay nothing to the character
who has run dry.

Once per encounter rather than per unit of time is what stops a party
from resting on the spot until they are full. That behaviour is the
predictable consequence of any recovery rule with no limit on how often
it applies, and it hollows out the whole day: the fights are all fought
at full strength and attrition stops existing. Here, sitting longer
improves the tier of the rest, and there is no second helping to be had.

Tracking hours was the alternative and was rejected. It makes the
Dungeon Master into a timekeeper, and every player learns to ask what
time it is before deciding anything — which is bookkeeping standing
exactly where the tension should be.

Simulating a hard day changed what this rule is for. The expectation was
that characters would run dry and later fights would go flat. What
actually happens is that a drained character still fights at four fifths
of their best, because the minor powers cost nothing and are always
there — so the interest does not drain out of the day at all.

What drains is mastery hit points, and what happens at the fourth fight
is not that the character becomes boring but that they die. Recovery is
therefore a survivability rule first and a power-source rule second, and
including mastery hit points in it is the part doing nearly all of the
work. The fractions bear that out: across a punishing day at low level,
a breather leaves about a fifth of characters standing at the last fight
and a proper rest about half.

Core hit points staying out of it is what keeps the two pools meaning
different things. Mastery is luck, skill and the willingness to keep
going, all of which come back with a sit-down. A wound does not, and a
party accumulating real damage should feel the day getting more
dangerous rather than resetting after each fight.
{% endbook-only %}
