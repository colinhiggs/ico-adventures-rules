---
id: armour
title: Armour and Shields
tags: [equipment, reference, combat]
summary: >
  Armour points reduce every blow that lands, at the price of a skill
  penalty that also makes a dodging wearer easier to hit. Shields add
  to a block instead.
mechanics:
  unarmoured:
    move_penalty: 0
    ap: 0
    skill_penalty: 0
    cost_gp: 0
  partial_leather:
    move_penalty: 0
    ap: 1
    skill_penalty: 0
    cost_gp: 5
  leather:
    move_penalty: 0
    ap: 2
    skill_penalty: -1
    cost_gp: 10
  studded_leather:
    move_penalty: 0
    ap: 3
    skill_penalty: -2
    cost_gp: 25
  chain_shirt:
    move_penalty: 0
    ap: 4
    skill_penalty: -3
    cost_gp: 100
  scale_mail:
    move_penalty: 1
    ap: 4
    skill_penalty: -4
    cost_gp: 50
  chain_mail:
    move_penalty: 1
    ap: 5
    skill_penalty: -4
    cost_gp: 150
  breastplate:
    move_penalty: 1
    ap: 5
    skill_penalty: -3
    cost_gp: 200
  full_plate:
    move_penalty: 2
    ap: 8
    skill_penalty: -6
    cost_gp: 1500
  buckler:
    block_td_bonus: 1
    block_ap: 2
    skill_penalty: 0
    cost_gp: 5
  shield:
    block_td_bonus: 2
    block_ap: 3
    skill_penalty: 0
    cost_gp: 15
  great_shield:
    block_td_bonus: 3
    block_ap: 5
    skill_penalty: -1
    cost_gp: 40
---

Armour is worn for its **armour points** (AP), subtracted from every
blow that lands — see [[damage]]. It also carries a **movement
penalty**, in squares, taken off every move — see [[movement]]. The
further price is a **skill penalty** that
applies while it is worn and, because a dodging defender's targeting
difficulty is built from their dodge skill, makes the wearer easier to
hit when dodging — see [[hitting]]. The Untouchable signature in
[[discipline-powers]] removes exactly that penalty.

## Light armour

{% table mechanics
   rows=unarmoured,partial_leather,leather,studded_leather,
        chain_shirt
   columns=ap:AP,move_penalty:Move,skill_penalty:Skill,
           cost_gp:"Cost (gp)"
   header=Armour %}

## Medium and heavy armour

{% table mechanics
   rows=scale_mail,chain_mail,breastplate,full_plate
   columns=ap:AP,move_penalty:Move,skill_penalty:Skill,
           cost_gp:"Cost (gp)"
   header=Armour %}

## Shields

A shield does nothing while you dodge. While you block, it adds to your
targeting difficulty and its armour points come off the blow on top of
your worn armour.

{% table mechanics
   rows=buckler,shield,great_shield
   columns=block_td_bonus:"Block bonus",block_ap:"Block AP",
           skill_penalty:Skill,cost_gp:"Cost (gp)"
   header=Shield %}

## Example

Bramm wears chain mail and carries a shield.

While he dodges, only the chain mail matters: its armour points come off
every blow that lands, and its skill penalty comes off his targeting
difficulty, making him easier to hit than he would be unarmoured. The
shield does nothing at all.

When he switches to blocking, his targeting difficulty is rebuilt from
his block skill plus the shield's block bonus, and a landing blow is now
reduced by his chain mail *and* the shield's block armour points
together — though never by more than the cap in [[damage]] allows.

{% book-only %}
## Design note

Armour making a dodging wearer easier to hit is the central trade in the
list, not a quirk. Heavy plate is protection bought at the price of
agility, and the numbers are set so that the heaviest armour is a poor
choice for a character who intends to dodge and an excellent one for a
character who intends to block.

Shields do nothing while dodging for the same reason: a shield is
something you actively interpose, so it belongs to the stance that
represents interposing things.
{% endbook-only %}
