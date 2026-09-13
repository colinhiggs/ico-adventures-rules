---
id: using-powers
title: Using a Power
tags: [core, powers]
summary: >
  Declare how hard you are pushing, anywhere inside the power's own band
  of difficulties, roll its skill against that, and pay 10 plus the
  difficulty minus your roll — never less than a third of it, unless the
  power is minor.
mechanics:
  base_cost: 10
  cost_reduction_per_point_over: 1
  cost_formula: "base_cost + difficulty - skill_roll"
  minimum_cost_divisor: 3
  minor_powers_ignore_minimum_cost: true
  difficulty_declared_before_rolling: true
  declaration_within_the_powers_band: true
  band_runs_base_difficulty_to_max_difficulty: true
  declaration_capped_by_push: true
  failure_spends_the_action: true
  failure_costs_the_minimum: true
  unaffordable_power_does_not_take_effect: true
  max_cost_of_a_successful_power: 10
  one_roll_serves_both_when_skills_match: true
---

## Declare, then roll

Every power lists a **band** of difficulties, a **skill**, and a
**step**: how much extra difficulty buys one more increment of effect.
The band runs from the power's **base difficulty**, which is the least
you may declare, to its **maximum difficulty**, which is the most.
Before rolling, declare a difficulty inside that band — the base, plus
however many steps you want. Then roll that skill as the
[[core-resolution|core roll]]. Meeting the declared difficulty means the
power works, at the scale you asked for.

## The ladder

A power does not run to whatever a good roll could reach. It covers its
own band and stops, and reaching past the top of it means owning the
next power up rather than declaring a bigger number.

Powers therefore come in **rungs**. A discipline's Initiate powers cover
the low band; its Adept powers begin where those leave off, reach much
further, and buy their effect at a better rate for each point of
difficulty. Power Attack and Hammer Blow in [[discipline-powers]] are
the plainest pair: the second starts at exactly the damage the first
ends at, and then climbs twice as fast.

Three things follow, and they are the whole reason the band is written
down.

- **What a beginner can do is bounded by the rung, not by their luck.**
  A character on the first rung who rolls extravagantly well pays less
  for the power. They do not get a bigger one.
- **A low rung stays useful without staying decisive.** It is the cheap
  trick you can afford every round for the rest of your career, and its
  ceiling is why it never competes with what you keep for the fights
  that matter.
- **Climbing is a choice made in advancement, not in the moment.** The
  next rung is bought with a [[disciplines|grade]], so reaching further
  costs what grades cost, and the character who spent elsewhere reaches
  exactly as far as they did last level.

## How far up the ladder you reach

A band says how far a power goes. **Push** says how far *you* go: it is
a number on your sheet, and it is the highest difficulty you may
declare at all — with any power, and with any spell.

Push is not a second chance at succeeding; the roll still decides
whether the declaration is met. Push decides what you are allowed to
attempt in the first place, and two things follow from it.

- A power whose base difficulty is above your push is not a power you
  can use yet, however good the skill it runs on and however many
  grades opened it.
- A band whose top is above your push stops where you stop.

You begin with {{ character-creation:mechanics.starting_push }} and
raise it by spending advancement points — see [[advancement]]. It is
the only thing on that list with no limit per level, and it needs none:
push you cannot roll to is not a better character, it is a more
expensive way to fail.

## The cost

A successful power costs `{{ mechanics.cost_formula }}` points from its
[[power-sources|power source]], where the base cost is
{{ mechanics.base_cost }} and every point by which the roll beat the
difficulty takes {{ mechanics.cost_reduction_per_point_over }} off.

No power ever costs less than its declared difficulty divided by
{{ mechanics.minimum_cost_divisor }}, rounded down.

## One roll, two jobs

When a power is invoked on an action that uses the *same* skill — a
melee attack power rolled on melee attack, say — you make one roll and
it serves both purposes: first against the declared difficulty to settle
whether the power worked and what it cost, then against the target's
[[hitting|targeting difficulty]] to resolve the action itself. You never
roll twice for one swing.

## Failure

If the roll misses the declared difficulty, the power does not happen,
the action is spent, and you pay the minimum cost anyway.

## Criticals

A critical on a power roll does two things. The high total drives the
cost down as any high roll would, and it grants one extra step of the
power's effect for nothing — see [[core-resolution]]. Without that
second part a critical would be nearly worthless to a character whose
strength is powers, since a power's size is fixed when you declare its
difficulty and only its price depends on the roll.

## What you cannot afford

You can never spend what you do not have. If the cost comes out higher
than the stamina or spirit you have left, the power does not take
effect and the action resolves as though you had not invoked it — an
attack power still leaves you swinging, it simply gains you nothing.

Note that a *successful* power never costs more than
{{ mechanics.max_cost_of_a_successful_power }}, however high a
difficulty you declared: success means the roll reached the difficulty,
and every point it reached beyond takes another point off the price.
Reaching further is paid for in the risk of failing, not in a larger
bill when you succeed.

## Minor powers

Some powers are marked **minor**. A minor power is declared, rolled and
paid for exactly like any other, with one difference: the minimum cost
does not apply to it, so its cost can fall to nothing. A failed minor
power therefore costs only the action.

Minor powers scale more slowly than standard ones — see
[[discipline-powers]], and the bolt spells in [[spell-list]].

With an empty reservoir a minor power is still worth attempting, and
the rule above is what makes it work: declare a difficulty low enough
that the roll is likely to carry the cost to nothing, and you get the
power for free. Declare higher and you are gambling the action against
a bigger effect.

## Example

Ashri has a melee attack skill of `9` and `14` stamina left. She invokes
Power Attack, which runs from difficulty `4` to `18`, adds `1` damage at
the base and `1` more per `2` further points. She declares a difficulty
of `14`: five steps above the base, so `6` damage added.

`14` is a difficulty she is allowed to ask for, on both counts that
matter: it is inside Power Attack's band, and her push is `16`, so she
can reach it. `20` would not have been, however well she rolled — that
is Hammer Blow's band, and she does not hold Martial at Adept. Nor, for
that matter, could she have declared `17` on a power whose band did
run that far, because that is a point above her push.

She rolls `9`, for a total of `18`. That beats her declared `14`, so the
power works. The cost is the base cost plus `14` less `18` — which comes
out at `6`. The minimum for a difficulty of `14` is `4`, lower than `6`,
so she pays `6` and is left with `8` stamina.

Because Power Attack rolls on the same skill as the attack itself, that
same total of `18` is now compared to her target's targeting difficulty
to see whether the blow lands.

Had she rolled `2` instead, her total of `11` would have missed the
declared `14`: no power, no attack, and she would still owe the minimum
of `4`.

Now suppose she uses Precise Strike, a *minor* power, declaring a
difficulty of `3`. She rolls `8`, for `17` — beating the declared
difficulty by `14`. The base cost less `14` is below zero, and since a
minor power has no minimum, it costs her nothing at all.

{% book-only %}
## Design note

Declaring the difficulty before rolling is what stops powers becoming
free as characters improve. Under a fixed difficulty, expected cost is
roughly the difficulty less the skill, so any power with a set number
becomes free the moment skill passes it. Letting the character choose
how far to reach converts that problem into the interesting decision:
growing skill buys a *larger* effect at the same price rather than the
same effect at no price.

The minimum cost is the second half of that. Without it, a veteran
reaching a difficulty far below their skill would pay nothing however
much effect they asked for. With it, reaching further always costs more,
and stamina and spirit stay meaningful for a character who has been
adventuring for years.

Minor powers deliberately opt out of the minimum, and the cost formula
regulates them without needing a cap: a minor power reaches zero only
when the roll beats the declared difficulty by the full base cost, so
the reliably-free band is roughly the character's skill less the base
cost. That band widens as they improve. A minor power is what you always
have — the trick you can still pull on the fourth fight of a long day
with an empty reservoir, growing quietly more impressive as you do,
while never rivalling what you could do fresh.

The maximum difficulty is newer than the rest of this document and
answers a measured fault rather than a theoretical one. Without a
ceiling, one power is the whole of a character's offence for their
entire career: the same declaration at a bigger number, growing with
skill and nothing else. That has three costs. The interesting decision
becomes arithmetic, since the best difficulty to declare is a formula in
your attack bonus and there is only ever one answer. A creature with a
good attack skill and a small reservoir declares as hard as a veteran
does, which is why the bestiary kept coming out stronger than its threat
level said. And the low, cheap version of a power never stops being the
same power, so there is nothing for a character to *reach* for.

Bands fix all three by making the rung the unit. Inside a rung the
choice is the old one — how hard to push, against the risk of missing.
Between rungs it is an advancement choice, and the two are not the same
decision made twice.

Continuity between rungs is deliberate: the rung above begins at the
effect the rung below tops out at, so buying it is never a step
backwards and never a sudden jump either. What the higher rung buys is
a steeper slope and further to climb.

Push is the newest part of this and closes a hole the bands left open.
A grade decides *which* rungs exist for you; until push, nothing decided
how high you could stand on the one you had. A first-level character
with Martial at Initiate could declare Power Attack at the top of its
band on the day they made the character, and the only thing stopping
them was that they would usually miss — which is a reason not to, not a
rule. Worse, the general powers belong to no discipline at all, so the
deepest band in the game was open to everybody from the start.

Making that a purchase does three things at once, and the third is the
one it was built for. It finishes the sentence the bands started, so
that reaching further is always something you bought rather than
something you rolled. It gives a beginner a visible thing to climb
towards inside a power they already own. And it is the only item on the
advancement menu that a character can keep buying: everything else has
a ceiling per level, so a senior character used to reach the end of what
points could buy and hand back a fifth of every level — see the design
note in [[advancement]] for what that was doing to the economy.

{% endbook-only %}
