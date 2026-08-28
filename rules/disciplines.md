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
Going wide is cheap and going deep is expensive, deliberately.

## What a grade does

A grade does exactly three things, and nothing else:

- It sets your **focus** in that discipline's skill group. A discipline
  you hold at Initiate makes its group *unfocused*; at Adept or Master
  it makes the group *focused*. Any group you hold no discipline in
  stays *peripheral*. Focus governs how far a skill can be raised and
  what each rank costs — see [[skills]].
- It opens that discipline's **power pool** at the matching grade, so
  you may take its powers when you gain one. See [[discipline-powers]].
- At **Master** only, it grants that discipline's single **signature**
  ability.

Because focus is derived from grade, there is no separate
multiclassing rule and nothing to reconcile when a character advances
in two directions at once. The five disciplines and their signatures
are listed in the [[discipline-list]].

## The familiar archetypes

Nothing stops you building the classic adventuring roles — they are
combinations rather than categories. A fighter is Martial and Athletic;
a rogue is Athletic and Awareness; a wizard is Magical and Awareness; a
priest is Spiritual with a little Martial. A character who spreads
Initiate grades across four disciplines is a generalist, and that is a
legitimate build rather than a mistake.
