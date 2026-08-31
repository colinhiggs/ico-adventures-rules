---
id: languages
title: Languages
tags: [core, character]
summary: >
  Languages are not a skill and have no ranks. You either speak one or
  you do not. Your background gives you some, and more can be bought
  outright.
mechanics:
  languages_have_ranks: false
  starting_languages_from_background: 2
  advancement_cost_per_language: 1
  fluency_is_binary: true
---

A language is something you either have or you have not. There is no
roll to speak one, no rank in it, and no partial fluency: if the
language is on your sheet you converse in it as easily as in your own.

## Getting them

A starting character speaks
{{ mechanics.starting_languages_from_background }} languages, chosen
from what their background makes plausible — a native tongue and
whatever the place they grew up in required of them. The Dungeon Master
is the judge of plausible; a fisherman's daughter from a border town has
a very different list available to her than a cloistered scribe.

Thereafter a language costs
{{ mechanics.advancement_cost_per_language }} advancement point, bought
exactly like anything else on the menu in [[advancement]]. It takes
effect between adventures, not mid-sentence.

## Example

Sela begins play speaking the common tongue of her region and the
liturgical language of her order, which her background makes obvious.

Three levels later the party keeps running into traders from across the
mountains, so she spends a single advancement point and simply speaks
their language from the next session onward. There is no roll and no
rank: she is not *slightly* fluent, and she never rolls to understand
someone.

{% book-only %}
## Design note

Speaking a language really is a skill in life, and people really do sit
at every level of partial fluency. Ico deliberately does not model that,
because the cost of modelling it is out of proportion to what it adds at
a table.

As a skill with ranks, a language competes for points against melee
attack and dodge, and loses every time — the same points buy something
that comes up every session, so a rank in a language is a point wasted
and nobody buys one. Priced instead as a flat purchase of about one
point, the same character can pick up a language on a whim and it stays
worth doing.

The binary also removes a whole category of tedious rolling. Nobody
wants to roll to understand a sentence, and a partial success on such a
roll gives the Dungeon Master the unenviable job of improvising what
half-understanding sounds like, every time it comes up.
{% endbook-only %}
