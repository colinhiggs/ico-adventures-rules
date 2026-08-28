---
id: using-powers
title: Using a Power
tags: [core, powers]
summary: >
  Roll the power's listed skill against its difficulty. Success costs 10
  from its power source, reduced by 1 for every point the roll beat the
  difficulty.
mechanics:
  base_cost: 10
  cost_reduction_per_point_over: 1
  cost_formula: "10 + difficulty - skill_roll"
  some_powers_have_minimum_cost: true
---

## The roll

Every power lists a **difficulty** and the **skill** used to invoke it.
Roll that skill (the [[core-resolution|core roll]]) against the
difficulty. Meeting it means the power works.

## The cost

A successful power costs {{ mechanics.base_cost }} points from its
[[power-sources|power source]] — stamina or spirit. Every point by which
the roll beat the difficulty reduces that cost by
{{ mechanics.cost_reduction_per_point_over }}, so the cost is
`{{ mechanics.cost_formula }}`.

A well-practised character will eventually invoke some powers for no
cost at all. A few powers set a minimum cost that this reduction cannot
take you below; those say so in their own description.

The [[general-powers]] are open to every character; others come from a
character's chosen area of specialisation.
