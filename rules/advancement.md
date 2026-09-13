---
id: advancement
title: Advancement
tags: [core, character, progression]
summary: >
  A level is a budget of points, spent in the same shop as character
  creation — discipline grades, skill ranks, or mastery hit points.
mechanics:
  points_per_level: 15
  free_mastery_hp_per_level: 1
  free_mastery_hp_per_constitution: 1
  mastery_hp_per_point: 2
  max_mastery_hp_bought_per_level: 1
  power_source_per_point: 4
  max_power_source_bought_per_level: 1
  push_per_point: 1
  powers_per_level: 1
  attribute_point_every_n_levels: 4
  level_is_only_a_budget_and_a_clock: true
---

A **level** in Ico is not a template. It is a budget of
{{ mechanics.points_per_level }} points and a clock that raises your
skill ceilings, and it is spent in exactly the same shop as
[[character-creation]].

The points are the same points [[experience]] awards, one for one, so
they arrive over the course of an adventure rather than all at once.
What a level marks is the clock: the grants below that are not points,
and the ceilings that move.

## What a level gives

- {{ mechanics.points_per_level }} points to spend, as below.
- {{ mechanics.free_mastery_hp_per_level }} mastery hit point free and
  automatic, plus
  {{ mechanics.free_mastery_hp_per_constitution }} more for each point
  of your **constitution** bonus. Almost all of the free cushion comes
  from constitution, so a hardy character accumulates it several times
  faster than a frail one, every level, without paying for it.
- {{ mechanics.powers_per_level }} power, chosen from a pool you have
  opened — see [[disciplines]] and [[discipline-powers]].
- Every {{ mechanics.attribute_point_every_n_levels }} levels, one
  attribute point.
- One more rank of headroom on every skill ceiling, per [[skills]].

## What points buy

- **A discipline grade** — at the cost listed in [[disciplines]].
- **One rank in a skill** — at the cost listed in [[skills]], which
  depends on how that skill is focused.
- **Mastery hit points** — one point buys
  {{ mechanics.mastery_hp_per_point }} of them, to a limit of
  {{ mechanics.max_mastery_hp_bought_per_level }} bought per level on
  top of the free grant.
- **A language** — see [[languages]] for what one costs. Languages have
  no ranks; you either speak one or you do not.
- **Stamina or spirit** — one point buys
  {{ mechanics.power_source_per_point }} points of one
  [[power-sources|power source]], to a limit of
  {{ mechanics.max_power_source_bought_per_level }} points spent per
  level.
- **Push** — one point buys {{ mechanics.push_per_point }} point of
  [[using-powers|push]], the hardest difficulty you may declare. This
  is the one purchase with no limit per level.

Both hit point and power source ceilings are per level and cumulative: a
character who skipped them last level may catch up on this one. Push has
no ceiling to catch up on.

Core hit points are not on this list. They remain equal to your
constitution and grow only when that attribute does — see
[[hit-points]].

## Example

Ashri reaches a new level. She receives her free mastery hit points, one
power, and a rank of headroom on every ceiling.

She then spends her points: `4` raising four focused skills by a rank
each at a point apiece, `1` on the mastery hit points she is allowed to
buy this level, `1` on widening her stamina — which is all the widening
a level allows — and `3` on push, taking her from `16` to `19`, which
brings the top of Power Attack's band into reach for the first time.
The remaining `6` she banks toward Martial Master, which she cannot yet
afford outright.

She could have put all `9` of those last points into push instead.
Nothing in the rules stops her; her attack skill is what stops her,
since a difficulty she meets one roll in twenty is not a difficulty she
can use.

This level happens to be divisible by four, so she also takes an
attribute point and puts it into strength.

{% book-only %}
## Design note: what constitution is for

Constitution was the attribute nobody wanted. It bought core hit points
and the base of a power source, and core hit points are a small slice of
a pool that mastery hit points dominate, so four points spent on it were
worth about three quarters of what the same four were worth in strength
or dexterity. An attribute that is never the right answer is a tax on
the players who did not notice.

Tying free mastery hit points to it fixes that, and the reason it is a
**grant** rather than a **cap** is worth keeping. Two other repairs were
measured and both failed for the same reason. Letting constitution raise
the ceiling on mastery hit points a character may *buy* helps late,
where builds have points spare, and actively hurts in the middle levels,
where they do not and the extra hit points come out of skills:
constitution went from about three quarters of the best attribute to
three fifths of it. Letting constitution and willpower raise the ceiling
on the power source did nothing whatever, at any level — a senior
character already has far more stamina or spirit than a fight can spend,
so converting spare points into more of it converts them into nothing.

A grant costs a character nothing and therefore cannot be paid for out
of the wrong pocket, which is the trap the other two fell into.

The flat part of the grant then had to come down, and this is the part
worth understanding. Adding constitution's hit points on top of the flat
three made fights drift badly: mean duel length went from five rounds at
first level to nearly seven at fifteenth, a drift of `1.31` where the
game had been running at `1.08`. Damage does not keep pace with that,
and the obvious lever does not help — one further point of damage per
seven ranks of attack skill instead of eight moved the drift from `1.31`
to `1.29`, because a couple of points of damage cannot answer a quarter
more hit points.

Taking the flat rate down to one and letting constitution supply the
rest fixes it completely. Fights run five rounds at first level and five
at fifteenth, a drift of `1.04` — flatter than before any of this — and
constitution is worth between four fifths and nearly all of the best
attribute in the game. The same hit points are being handed out; they
are simply handed to the characters who bought the attribute for them.
## Design note

Hit points that climb steeply every level while damage stays flat do not
make a character heroic; they make every fight longer than the last. The
growth is meant to be in what a character can *do* rather than in how
long they take to kill, and what makes that possible is the
[[discipline-powers|ladder of difficulties]]: the damage a power adds
climbs with the rungs a character can reach, so the two sides of the
fight move together.

This used to say that the per-level grant was deliberately small next to
the opening reserve in [[character-creation]], and it is no longer true.
The opening reserve came down to roughly what a constitution is worth,
so mastery hit points now arrive mostly over a career rather than mostly
at creation — a starting character has about a quarter of what a
fifteenth-level one carries, where they used to have most of it.

The two purchase ceilings exist for the same reason as the flat curve.
Without them a character with nothing else worth buying converts an
entire level into one runaway statistic, and the balance between damage
and durability that the rest of the system rests on quietly stops
holding.

Push is the exception, and it is the exception on purpose. Every other
item on the menu needs a ceiling because nothing in play limits how much
of it is useful: a character who converts a level into mastery hit
points gets all of them, and they all work. Push limits itself. Buying
more of it than your skill can roll to buys the right to declare a
difficulty you will miss, and missing spends the action and costs you
the minimum anyway. That is why it can be sold without a cap, and being
the one uncapped thing is what makes it the only item on this list deep
enough to take a whole budget.

It had to be, because the list was running out. Measured across the
panel of test builds, the share of a level that bought nothing anything
could detect — points nobody could place, plus reservoir past the size a
fight can empty — ran `16%` at first level, `15%` at fifth, `18%` at
tenth and `23%` at fifteenth. A level was charging full price for four
fifths of a level, and worse at the top than the bottom, so the problem
grew with the career it was meant to reward. With push on the menu the
same measurement gives `0%`, `1%`, `3%` and `8%`.

The obvious alternative was measured first and rejected, which is worth
recording because it is the change anybody would try. Cutting the
budget from `15` points a level to `13` produced *identical* gate
output — the same single failure at the same round counts, to the
decimal — because the two points removed were points nobody could
spend. Clearing the surplus by supply alone needs `15` down to `9`, and
even that leaves first level untouched, since a first-level budget is
the pool in [[character-creation]] and not this number at all. Then,
once push existed to absorb them, the same cut to `13` stopped being
free and cost six new failures. A supply cut is only painless while the
supply is worthless; the honest order is to give the points something
to buy, and then leave the budget alone.

The power source ceiling is the strictest of them: a point buys
{{ mechanics.power_source_per_point }} stamina or spirit, which is
generous, and only {{ mechanics.max_power_source_bought_per_level }} may
be spent on it in a level, which is not. That pairing is deliberate. A
reservoir wide enough to spend freely in every fight makes the
interesting decision — how hard to push a power, and how often — into no
decision at all, and the measurement agrees: under the old ceiling a
fifteenth-level character finished the day with stamina it had never had
a use for. Widening it slowly, from a smaller start, is what keeps the
reservoir a thing a character budgets rather than a number on a sheet.

Mastery hit points are cheap per point precisely because a skill rank
keeps paying out on every roll you ever make while a mastery hit point
absorbs its damage once. Both are worth buying; neither should be
obviously correct.
{% endbook-only %}
