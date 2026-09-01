---
id: reach
title: Reach and Closing
tags: [core, combat, map]
summary: >
  A longer weapon strikes at a distance a shorter one cannot answer, and
  is paid for that once as the shorter weapon closes. Inside, a quick
  weapon strikes first.
mechanics:
  outside_reach_cannot_strike: true
  closing_costs_the_move: true
  opening_attacks_per_square: 1
  withdrawing_costs_the_move: true
  quick_strikes_first_inside: true
---

A polearm keeps you at arm's length and a dagger does not, and the fight
between the two is decided by whether the dagger ever gets close.

## Inside and outside

[[movement]] gives every combatant a **reach** in squares. Against a
particular opponent you are either:

- **outside** — further away than your own reach but within theirs, so
  they may strike you and you may not strike them; or
- **inside** — within your own reach, where both of you may strike.

A fight between equal reaches has no outside. A fight where one reach is
longer has one, and it belongs entirely to the longer weapon.

## Closing

Moving from outside to inside costs your **move** for the round, and
your action is still yours. You lose nothing but the chance to strike on
the way in, and what that costs you is
{{ mechanics.opening_attacks_per_square }} unanswered blow for every
square of reach you had to give away.

Your opponent may back out again, which costs *them* their move and puts
you outside once more. Closing and withdrawing cancel: each spends one
move, and the two of you end where you began. So the longer weapon is
paid for its reach **once**, as the fight is joined, and not again for
as long as neither of you can spare a move for anything else.

## Quick weapons inside

A **quick** weapon — see [[weapons]] — is short enough to be used where
a longer one is fouled. While you are inside the reach of a weapon
larger than your own, your attacks come **before** your opponent's,
whatever [[turn-order]] settled at the start of the fight.

That is the whole of the exchange. A long weapon takes the first blow of
the fight for free; a quick weapon takes the first blow of every round
after that. Which is worth more depends on how long the fight lasts,
which is exactly the choice a player should be making when they pick a
weapon.

## Example

Bram carries a great axe, size L, so his reach is `2` squares. Sela
carries a dagger: quick, and reach `1`.

They join battle two squares apart. Sela is outside — Bram can reach her
and she cannot reach him — so Bram strikes, unanswered, for the one
square of reach she has to give away. Sela then spends her move to
close, and is inside.

From there Sela strikes first every round, dagger before axe, whatever
the initiative order was. Bram can spend his move to back off and make
her close again, but that costs him the move and buys him nothing: she
spends hers to follow, and they are back where they were.

Bram's axe bought him one free blow. Sela's dagger buys her the first
blow of every round for the rest of the fight.

{% book-only %}
## Design note

Reach sat on the movement table and did nothing. A number that is
printed, measured and never consulted is worse than no number at all,
because it implies a rule the reader then goes looking for.

The rule it implies is this one, and it is deliberately paid **once**. A
reach advantage granting a free attack every round would make the
longest weapon the only weapon; the alternative — tracking who stepped
where, round by round — is the kind of bookkeeping that stops a table
counting squares at all. Letting closing and withdrawing cancel says the
same thing in one sentence and needs no adjudication.

Quickness is the answer to it, and the two together are what stop weapon
size being a single scale with one right answer at the top. A long
weapon wants a short fight and a quick weapon wants a long one. Neither
dominates, and a player choosing between them is choosing between two
bets rather than reading off which number is bigger.
{% endbook-only %}
