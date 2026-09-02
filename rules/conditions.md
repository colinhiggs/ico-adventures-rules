---
id: conditions
title: Conditions and Resisting Them
tags: [core, combat]
summary: >
  An effect that does more than damage is resisted with an opposed roll
  against Fortitude or Resolve, and how long it lasts depends on the
  margin.
mechanics:
  resisted_by_opposed_roll: true
  resist_target_is_declared_difficulty: true
  physical_resistance_skill: fortitude
  mental_resistance_skill: resolve
  base_rounds: 1
  margin_per_extra_round: 5
  conditions:
    stunned:
      resisted_with: fortitude
      margin_per_extra_round: 15
      loses_action: true
    burning:
      resisted_with: fortitude
      margin_per_extra_round: 4
      repeats_damage: true
      damage_fraction_per_round: 0.5
      smothered_by_action: true
    slowed:
      resisted_with: fortitude
      movement_fraction: 0.5
    dazed:
      resisted_with: resolve
      attack_penalty: 2
    rooted:
      resisted_with: fortitude
      movement_fraction: 0
    silenced:
      resisted_with: resolve
      casting_penalty: 5
    blinded:
      resisted_with: fortitude
      attack_penalty: 5
      lasting: true
    diseased:
      resisted_with: fortitude
      prevents_recovery: true
      lasting: true
    cursed:
      resisted_with: resolve
      loses_ties: true
      lasting: true
---

Some effects do more than damage. Being set alight, knocked senseless or
thrown off your stride are **conditions**, and a creature always gets to
resist one.

## Resisting

Resisting is an opposed roll, exactly as [[core-resolution]] describes.
The number to beat is the **difficulty declared** for the effect — the
one its user chose and paid for under [[using-powers]], not the roll
they happened to make. The defender rolls
`{{ core-resolution:mechanics.standard_die }}` and adds whichever skill
the effect names:

- **{{ mechanics.physical_resistance_skill }}** for anything the body
  fights off: fire, cold, poison, a blow that rattles the skull.
- **{{ mechanics.mental_resistance_skill }}** for anything the mind
  fights off: fear, confusion, compulsion.

Beat the difficulty and nothing happens to you. Fail and the condition
lands.

## Spending to make it stick

Because the difficulty is the number to beat, anyone using a resistable
effect can make it harder to shrug off the same way they make anything
else bigger: by declaring a higher difficulty and paying for it. A
Command spoken at difficulty `10` is a suggestion; the same word at
difficulty `25` is very hard to refuse, and costs accordingly.

This is the only lever, and it is deliberately the same lever that buys
damage, area and reach. You cannot buy an unresistable effect cheaply by
rolling well — a good roll makes the effect *affordable*, not
*irresistible*.

## How long it lasts

A condition that lands lasts {{ mechanics.base_rounds }} round, plus one
more for every {{ mechanics.margin_per_extra_round }} points by which
the difficulty beat your resistance roll. Some conditions are harder to
sustain than that and say so.

Margin decides duration for the same reason it decides everything else:
a near-thing should be brief and an overwhelming one should stick.

## The conditions

**Stunned** — you lose your action. You may still move, and you still
defend yourself. Resisted with
{{ mechanics.conditions.stunned.resisted_with }}, and it takes
{{ mechanics.conditions.stunned.margin_per_extra_round }} points of
margin to hold someone stunned for a second round, because taking a
character's turn away is the harshest thing an effect can do.

**Burning** — the fire keeps eating at the start of each of your turns,
but it is eating what is left of itself: each time it deals
{{ mechanics.conditions.burning.damage_fraction_per_round }} of what it
dealt the time before, rounding down, and when that reaches nothing the
fire is out. You may instead spend your action to smother it, which ends
it at once and needs no roll. Resisted with
{{ mechanics.conditions.burning.resisted_with }}, and it spreads easily:
{{ mechanics.conditions.burning.margin_per_extra_round }} points of
margin buys another round of it.

Burning therefore adds up to about as much again as the blow that
started it, however long it lasts — a fire spell is the one that deals
the most damage, and the price of that is that it shapes the fight
least. What it does offer is a choice: keep swinging and keep burning,
or lose a turn putting yourself out.

**Slowed** — your movement is multiplied by
{{ mechanics.conditions.slowed.movement_fraction }} and you have no
reaction. Resisted with
{{ mechanics.conditions.slowed.resisted_with }}.

**Rooted** — you cannot move at all. Your movement is
{{ mechanics.conditions.rooted.movement_fraction }}, and you have no
reaction. You may still act, and you may still defend yourself; you
simply cannot go anywhere. Resisted with
{{ mechanics.conditions.rooted.resisted_with }}.

**Silenced** — you cannot make yourself heard, and magic will not answer
you properly. You take
`-{{ mechanics.conditions.silenced.casting_penalty }}` on spellcasting,
and anything else that depends on being heard simply fails. Resisted
with {{ mechanics.conditions.silenced.resisted_with }}.

**Dazed** — you take
`-{{ mechanics.conditions.dazed.attack_penalty }}` on attack rolls, and
your targeting difficulty drops by the same. Resisted with
{{ mechanics.conditions.dazed.resisted_with }}.

## Lasting conditions

A few conditions have no duration at all. They do not count down and
waiting does not help; they last until something is done about them,
which in practice means a spell — see [[spell-list]].

They land the same way as anything else: an opposed roll against the
difficulty declared, and beating it means nothing happens to you. What
is different is what happens next, which is nothing, for as long as
nobody addresses it.

**Blinded** — you cannot see. You take
`-{{ mechanics.conditions.blinded.attack_penalty }}` on attack rolls and
your targeting difficulty drops by the same, and you cannot be the one
to choose a target you would have had to see. Resisted with
{{ mechanics.conditions.blinded.resisted_with }}.

**Diseased** — you are ill, and rest does not mend you. You recover no
mastery hit points between fights at all, whatever [[recovery]] would
otherwise have given you, and a night's sleep restores only what it
restores to anyone. Resisted with
{{ mechanics.conditions.diseased.resisted_with }}.

**Cursed** — luck has turned against you. You lose ties: a total that
exactly matches a target succeeds for everyone else and fails for you,
wherever [[core-resolution]] would have let it stand. Resisted with
{{ mechanics.conditions.cursed.resisted_with }}.

## Example

Sela casts a Force Lance at an orc, declaring a difficulty of `27`. She
rolls `29`, so the spell goes off and is cheap; but `27` is the number
the orc has to beat, and rolling well has not made the stun any harder
to resist.

The orc rolls to resist with Fortitude: `11` on the die plus a Fortitude
of `6`, for `17`. The difficulty beat that by `10` — but stunning needs
`15` points of margin for each extra round, so the orc is stunned for a
single round. It loses its action, though it may still back away.

Had the orc rolled `28`, it would have shrugged the effect off
completely and taken only the damage.

Had Sela wanted the stun to stick, the way to buy it was to declare a
higher difficulty in the first place — at `42` the same orc roll would
have been fifteen points short and lost two rounds instead of one. That
is an expensive spell, and it should be.

Against a Flame Lance the same margin of `10` would have set the orc
burning for three rounds, since fire needs only `4` points of margin a
round. If the lance dealt `9` damage, the fire then deals `4`, then `2`,
then `1` — about as much again as the lance itself, spread out and
shrinking. The orc may spend a turn beating the flames out instead,
which is the whole of what a fire spell does to the shape of a fight.

{% book-only %}
## Design note

Ico did not need saving throws. It already had two skills whose written
purpose was resisting duress — Fortitude against the physical and
Resolve against the mental — and no rule anywhere that used either of
them. An opposed roll against the skill that already claims the job is
one less subsystem than a saving throw, and it means a character who
invested in Fortitude finds out why.

The number to beat is the declared difficulty because that is where
every other decision about a power's size is made. Damage, area, reach
and the number of creatures affected are all bought by declaring a
difficulty and paying for it; how hard an effect is to shrug off had
been the one exception, settled by a roll instead. That exception had a
cost: a caster who wanted a stun to stick could not buy one, and was
better off declaring the lowest difficulty that worked and hoping. One
lever, used the same way everywhere, removes both the oddity and the
tactic.

The roll still does its two jobs — whether the spell happens, and what
it costs. It simply no longer decides how strong the effect is, which
keeps a good roll a matter of economy rather than of power.

Duration by margin rather than a flat number is what stops every
condition being equally decisive. Stun is the extreme case and is priced
as one: it needs three times the margin of anything else to last a
second round, because removing a character's turn is the harshest thing
in the game and a spell that reliably removes several is the only
spell anyone would ever cast.

Burning is the opposite case, and had the opposite problem. A condition
that repeats the whole of a spell's damage every round for as long as it
lasts is not a secondary effect, it is a damage multiplier, and it made
the fire spell in every family strictly the best one to cast. Halving
the damage each round bounds the total at roughly one extra blow however
long the fire burns, which is the profile fire ought to have: the most
damage of any element, and the least say in how the fight goes.

Letting the victim smother the flames is the one piece of shape a fire
spell does have, and it belongs to the victim rather than the caster. A
burning creature that keeps fighting keeps burning; one that stops to
put itself out has lost a turn to a spell that never took one. Neither
is a stun, and the choice is better than either.
{% endbook-only %}
