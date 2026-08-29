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
  master_cost: 40
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
- **Master** costs a further {{ mechanics.master_cost }} points.

The cost curve is the only limit on how many disciplines you hold.

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

The five disciplines and their signatures are listed in the
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

Much later she takes Martial to Master, gaining Killing Blow. Her focus
does not change — Adept had already made the group focused — so what the
final and most expensive grade buys her is the signature and the deepest
tier of Martial powers, nothing more.

{% book-only %}
## Design note

Because focus is derived from grade, there is no separate multiclassing
rule and nothing to reconcile when a character advances in two
directions at once. An earlier draft had classes, each granting its own
focus list, which meant a character with two classes needed a rule for
whose list applied when — and that rule was where the draft became
inconsistent.

Nothing stops you building the classic adventuring roles; they are
combinations rather than categories. A fighter is Martial and Athletic;
a rogue is Athletic and Awareness; a wizard is Magical and Awareness; a
priest is Spiritual with a little Martial. A character who spreads
Initiate grades across four disciplines is a generalist, and that is a
legitimate build rather than a mistake.

Going wide is cheap and going deep is expensive, deliberately. The
specialist pays most of a career for one signature, so the signature has
to be worth a career.
{% endbook-only %}
