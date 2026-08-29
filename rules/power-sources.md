---
id: power-sources
title: Stamina and Spirit
tags: [core, powers]
summary: >
  Physical powers spend stamina, based on constitution. Magical powers
  spend spirit, based on will.
mechanics:
  stamina_base: constitution
  spirit_base: will
  physical_powers_cost: stamina
  magical_powers_cost: spirit
---

There are two power sources, and every power draws on one of them.

- **Stamina** fuels physical powers. Its base value is a character's
  {{ mechanics.stamina_base }}.
- **Spirit** fuels magical powers, spells included. Its base value is a
  character's {{ mechanics.spirit_base }}.

Both can be widened by spending advancement points — see
[[advancement]] — and possibly by items. [[using-powers]] covers what a
power costs from its source and how a good roll reduces that cost.

## Example

Sela has willpower `15`, giving her a base spirit of `15`, and has spent
advancement points to widen it to `27`. Her constitution of `11` gives
her a stamina of `11`, which she has never bothered to raise.

She can therefore push her spells hard and often, but the one physical
power she took is something she can afford perhaps twice in a fight
before it is out of reach.

{% book-only %}
## Design note

Tying the two reservoirs to different attributes means a character
cannot be equally good at both without paying for it twice over in
attribute points. It also gives constitution and willpower a second job
each, so neither is a dump statistic for anyone who intends to use
powers at all.
{% endbook-only %}
