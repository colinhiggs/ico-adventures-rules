---
id: reach
title: Reach and Closing
tags: [core, combat, map]
summary: >
  A longer weapon holds a band its opponent can be struck in and cannot
  strike from. Crossing it costs a free attack, or the reaching fighter
  gives ground to hold it — one or the other, once a round. In a tight
  space it is a liability.
mechanics:
  outside_reach_cannot_strike: true
  closing_costs_the_move: true
  withdrawing_costs_the_move: true
  free_attack_on_closing: true
  free_attacks_per_round: 1
  reach_choice_costs_the_reaction: true
  step_back_move_cost_multiplier: 2
  tight_space_radius_offset: 1
  tight_space_penalty_per_square: -1
  tight_space_penalty_max: -4
  quick_strikes_first_inside: true
---

A polearm keeps you at arm's length and a dagger does not, and the fight
between the two is decided by whether the dagger ever gets close.

## The band

[[movement]] gives every combatant a **reach** in squares. Put two of
them on the grid and there are three distances that matter:

- **Apart** — further away than either reach. Nobody strikes anybody.
- **The band** — inside the longer reach and outside the shorter. The
  longer weapon strikes; the shorter cannot answer.
- **Close** — inside both reaches. Both strike.

Two equal reaches have no band, and their fight has no rule in it
beyond who moves first. A longer reach *imposes* a band, and everything
below is about that strip of ground and who is standing in it.

## Crossing it

The band is not a wall. Anyone may walk through it, and against a
shorter weapon somebody has to.

When an opponent standing in your band moves **towards** you, you may
spend your **reaction** to answer it. Both answers cost that same one
reaction, so you take one or the other and never both:

- **Strike them as they come.** One free attack, resolved as
  [[hitting]] resolves any other.
- **Give ground.** Step back, so that the band opens in front of them
  again and they have crossed nothing.

One reaction is all anybody has in a round — see [[turn-order]] — so
this is {{ mechanics.free_attacks_per_round }} answer per round, and it
is the same reaction Riposte and Deflect are paid out of. A fighter
holding a long weapon is choosing between their reach and their defence
every round of the fight.

Nothing here triggers on somebody who is merely standing in the band, or
who is walking out of it, or who is already close. It is the approach
that is answered.

## Giving ground

Stepping back costs `{{ mechanics.step_back_move_cost_multiplier }}`
squares of your **move** for every square you give up. You are walking
backwards with your eyes on somebody who is trying to kill you, and that
is half the speed of walking. Those squares come out of your own move,
spent from whenever your next one falls.

Two things can stop you. You may not step back through a wall, a
table, or anything else solid — and unlike a fight in the open, a fight
in a corridor often has one directly behind you. And you may not step
back further than your move can pay for, which is where the movement
penalty on heavy [[armour]] is felt: a character in plate can give up
perhaps one square and then has nothing left to move with on their own
turn, while a lightly armoured one gives up the same square and barely
notices.

## When giving ground is the right answer

Do the arithmetic before you reach for it. They come forward at the
ordinary price and you go backwards at double, so holding somebody off
by stepping back alone asks you to be **twice as quick as they are**.
Against anyone with movement still in hand you will not manage it: they
follow, you have spent your reaction and two squares' worth of move to
go one, and you are exactly where you started with nothing to show.

What makes it worth having is that an opponent who has just crossed your
band has usually spent their move getting there. Give up one square and
they need one more, out of whatever is left — and if that is nothing,
they finish their turn standing in the band with no attack at all. They
must cross again next round, and you may answer that too.

So the free attack is the ordinary answer, and giving ground is the
answer to somebody who has over-committed. Knowing which you are looking
at is the skill the rule is asking for.

## Coming again

If your opponent cannot cross the whole band in the movement they have,
they end their turn inside it, where you may strike them and they may
not strike you. That is the whole of what a reach advantage buys and it
is worth having.

They will come again next round, and closing again is another approach,
so you may answer it again — once, as before. A slow opponent crossing a
wide band therefore pays for it every round until they arrive, and a
fast one pays once and is inside.

## What reach does not buy

Not one attack per square. However far you outreach somebody, the
crossing is answered
{{ mechanics.free_attacks_per_round }} time and no more, and if they
have the movement to cross the band and keep coming, they arrive. You
cannot hold somebody off with reach alone.

What extra reach *does* buy is the band itself, and a band against the
other long weapons: a size {{ weapons:mechanics.two_handed_size }} weapon
imposes one on every ordinary weapon in [[weapons]], and a longer one
still would impose a band on that.

## A long weapon in a tight space

A weapon that needs room is worth less where there is none. Take your
reach, subtract {{ mechanics.tight_space_radius_offset }}, and count
every square within that distance of you that is **blocked** — a wall, a
pillar, a closed door, the low ceiling of a tunnel. Anything immobile
and solid counts. Every blocked square is
`{{ mechanics.tight_space_penalty_per_square }}` on your attack rolls,
to a maximum of `{{ mechanics.tight_space_penalty_max }}`.

Other creatures never count, however crowded it is. A press of bodies is
something a spear is *for*; a doorway is not.

A weapon with no reach beyond the ordinary subtracts
{{ mechanics.tight_space_radius_offset }} from a reach of the same size
and so counts no squares at all. This rule reaches only the weapons that
reach.

The practical effect is that the corridor and the doorway are where a
long weapon stops being the obvious choice, and both of those are where
a dungeon spends most of its time.

## Quick weapons inside

A **quick** weapon — see [[weapons]] — is short enough to be used where
a longer one is fouled. While you are inside the reach of a weapon
larger than your own, your attacks come **before** your opponent's,
whatever [[turn-order]] settled at the start of the fight.

So the exchange has two halves. The long weapon owns the band, and the
quick weapon owns what happens once the band has been crossed.

## Example

Bram carries a great axe: size L, reach `2`. Sela carries a dagger,
reach `1`, and is wearing plate, which leaves her a move of `2`.
Bram's band is the ring of squares exactly `2` away from him.

She spends her turn crossing the open ground and ends `2` squares off,
inside the band. She cannot strike from there.

Next round she moves the last square. That is an approach inside his
band, so Bram answers it: he takes the free attack, spending his
reaction, and hits her as she comes. She arrives and strikes him with
her own action.

On his turn Bram steps back a square. This is not the reaction: it is
ordinary movement on his own turn, going where he likes at the ordinary
price. Then he attacks her from `2` again, and she is in the band once
more.

From here it repeats, and the shape of the fight is set. Every round
Sela chooses between standing in the band doing nothing and walking into
a free attack to get her one blow in. Every round Bram spends his move
backing off and his reaction hitting her for it, which means he never
Ripostes and never Deflects all fight.

Note which of his two withdrawals was which. Backing off on his own turn
is ordinary movement and costs him only his move. Backing off as a
reaction would cost double and buy him nothing here, because Sela has a
square of movement left every round and would simply follow. He is
holding the band with his turn, not with his reaction, and spending the
reaction on the free attack instead.

Had Sela come at him in a corridor instead, `6` of the `8` squares
around Bram would be wall — everything but the length of the passage —
which is well past the cap, so his axe swings at
`{{ mechanics.tight_space_penalty_max }}` and his band is a strip of
floor one square wide. At that point her dagger is the better weapon,
which is exactly what it is in a corridor.

{% book-only %}
## Design note

Reach is a band of ground rather than a bonus, because a bonus would be
a number on a sheet and a band is a thing on the table that both players
can see. The question a reach advantage asks — *are you willing to walk
into that* — is a real one, asked once a round, and answered differently
depending on how badly the shorter weapon needs to be in the fight.

A fighter willing to spend everything on their reach can hold it every
round: the move to back off, the reaction to strike whoever follows.
That is meant to be available and it is meant to be expensive. It costs
them their move for the whole fight, so they go nowhere and help nobody,
and it costs them the reaction Riposte and Deflect are paid out of, so
their defence is whatever armour and dodge can manage alone.

Making striking and giving ground the *same* reaction is what stops the
two being stacked inside one round. A long weapon can answer an approach
or refuse it, and having to choose means the fighter crossing the band
always learns something about what is waiting for them.

Charging double for backwards movement is what keeps giving ground from
being free, and it is the first place in the game where the movement
penalty on armour changes what happens in a round rather than what
happens between them. A heavily armoured fighter with a polearm holds a
band for one step and then cannot hold it at all, which is the correct
answer: the polearm wants a light fighter behind it.

Capping the crossing at one answer a round, rather than one per square,
is the difference between a weapon and a wall. A reach advantage should
make an approach expensive; it should never make an approach impossible,
because a rule that stops the other side arriving stops the fight.

The tight-space penalty exists because everything above makes a long
weapon strong, and a strong thing wants somewhere it is weak. Bodies
deliberately do not block: a spear in a shield wall is the oldest good
idea in warfare, and a rule that punished a polearm for standing next to
its friends would be describing some other game. Walls block, and walls
are what a dungeon is made of, so the weapon that owns the open field
gives it back at the door.
{% endbook-only %}
