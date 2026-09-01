---
id: disciplines
title: Disciplines
tags: [core, character, progression]
summary: >
  Disciplines replace classes. Each is bought in three named grades, and
  the grade you hold sets your focus in that discipline's skill group
  and opens its power pool.
mechanics:
  initiate_cost: 5
  adept_cost: 15
  master_cost: 20
  master_minimum_level: 8
  grades: [initiate, adept, master]
  grades_bought_in_order: true
  disciplines_held_is_unlimited: true
  focus_from_grade:
    none: peripheral
    initiate: unfocused
    adept: focused
    master: focused
---

Ico has no classes. What a character is good at comes from the
**disciplines** they have taken, and a character may hold as many as
they can afford.

## Grades

Every discipline is bought in three grades — **Initiate**, **Adept**,
then **Master** — in that order, paid for with advancement points (see
[[advancement]]):

- **Initiate** costs {{ mechanics.initiate_cost }} points.
- **Adept** costs a further {{ mechanics.adept_cost }} points.
- **Master** costs a further {{ mechanics.master_cost }} points, and
  cannot be taken before **level
  {{ mechanics.master_minimum_level }}**.

Master is the only grade with a level requirement. Holding Adept is
already required, since grades are bought in order; the level is a
second gate on top of it, and there is no way to buy past either.

The cost curve is what limits how many disciplines you hold; the level
requirement is what stops any of them running ahead of your career.

## What a grade does

A grade does exactly three things, and nothing else:

- It sets your **focus** in that discipline's skill group. A discipline
  held at Initiate makes its group *unfocused*; at Adept or Master it
  makes the group *focused*. Any group you hold no discipline in stays
  *peripheral*. Focus governs how far a skill can be raised and what
  each rank costs — see [[skills]].
- It opens that discipline's **power pool** at the matching grade, so
  you may take its powers when you gain one. See [[discipline-powers]].
- At **Master** only, it grants that discipline's single **signature**
  ability.

The six disciplines and their signatures are listed in the
[[discipline-list]].

## Example

Ashri begins play with a discipline budget she spends entirely on
Martial, reaching Adept. Her Martial skill group — melee attack, ranged
attack, block and fortitude — is therefore *focused*, and every other
group in the game is *peripheral*, because she holds nothing else.

Over the next few levels she saves up and buys Athletic at Initiate.
Dodge, climb and the rest are now *unfocused* rather than peripheral:
cheaper to raise and with a higher ceiling, though still short of her
Martial skills.

She could not take Martial to Master before level
{{ mechanics.master_minimum_level }} however she spent her points, so
she reaches it there and gains Killing Blow. Her focus does not change —
Adept had already made the group focused — so what the final and most
expensive grade buys her is the signature and the deepest tier of
Martial powers, nothing more.

{% book-only %}
## Design note

Because focus is derived from grade, there is no separate multiclassing
rule and nothing to reconcile when a character advances in two
directions at once. Where classes each grant their own list of focused
skills, a character holding two needs a further rule deciding whose list
applies, and that rule tends to be where such systems come apart. Here
the question cannot arise: the grades a character holds *are* the
answer.

Nothing stops you building the classic adventuring roles; they are
combinations rather than categories. A fighter is Martial and Athletic;
a rogue is Athletic and Awareness; a wizard is Magical and Awareness; a
priest is Spiritual with a little Martial; the player who wants to talk
their way through the dungeon is Social and Awareness. A character who spreads
Initiate grades across four disciplines is a generalist, and that is a
legitimate build rather than a mistake.

Going wide is cheap and going deep is gated, and those are two different
tools doing two different jobs.

Price is a poor gate on depth. A price high enough to keep Master out of
reach early is also high enough to be paid the moment a character has
saved for it, so it delays the grade by a while and prevents it never;
and for as long as it is being saved for, it is taking points out of
everything else. A character who spends the equivalent of several levels
on one grade arrives at their deepest powers with the skill ranks and
the power source of someone junior to them — worse, for a while, at the
very thing they have just mastered. That is the opposite of what the
grade is for.

A level requirement holds depth back exactly, and holds nothing else
back at all. With it doing that job, the price has only one left —
keeping Master the largest single purchase in the game — and can be set
where nobody has to gut a character to pay it.
{% endbook-only %}
