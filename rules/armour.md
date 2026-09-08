---
id: armour
title: Armour and Shields
tags: [equipment, reference, combat]
summary: >
  Armour points reduce every blow that lands, at the price of a skill
  penalty that also makes a dodging wearer easier to hit. Shields add
  to a block instead.
mechanics:
  hampers_spellcasting: true
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
penalty**, in squares, taken off every move — see [[movement]].

The further price is a **skill penalty**, and it is paid twice.

**It comes off your dodge.** A dodging defender's targeting difficulty
is built from their dodge skill, so the penalty makes the wearer easier
to hit — see [[hitting]]. The Untouchable signature in
[[discipline-powers]] gives back exactly that much of it.

**It comes off your spellcasting.** Spirit is channelled through the
body, and a body in a steel shell channels it badly: the same penalty
comes off the casting roll, every time, whatever the spell — see
[[spell-properties]] and [[using-powers]]. Nothing gives this half
back, which is why the caster who wants to be hard to kill has to want
it enough to be worse at the only thing they are for.

Both prices are paid at once by anybody wearing armour and casting in
it. They do not interact and they are not a choice between two
readings: a wizard in plate is harder to hit than an unarmoured one on
the numbers that matter to a sword, easier to hit than an unarmoured
dodger, and worse at every spell they know.

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

Sela, who casts, would pay for the same chain mail twice over. Its
`{{ mechanics.chain_mail.skill_penalty }}` would come off her dodge and
off every casting roll she made in it, and she has no Untouchable to
give the first half back. She wears
{{ mechanics.partial_leather.ap }} point of partial leather instead:
its skill penalty is `{{ mechanics.partial_leather.skill_penalty }}`,
so it costs her nothing at all, and armour that costs a caster nothing
is the only armour a caster wants.

{% book-only %}
## Design note

Armour making a dodging wearer easier to hit is the central trade in the
list, not a quirk. Heavy plate is protection bought at the price of
agility, and the numbers are set so that the heaviest armour is a poor
choice for a character who intends to dodge and an excellent one for a
character who intends to block.

The casting half was added because the rule as first written named only
the dodge, and a rule that names one consequence is read as having only
that one. The result was a game in which the arithmetic said every
wizard should wear full plate: it cost them a little movement, nothing
else, and bought eight points off every blow. That is not a wizard
anybody has ever drawn.

Note what it is *not*. Nobody is forbidden armour, and no discipline
locks a suit of plate away from anybody — Ico does not ban equipment by
archetype and this rule does not start. A caster in plate is a legal,
playable and occasionally correct character; a bodyguard who casts one
spell a day should absolutely wear the plate. The rule only makes the
choice cost what it ought to, so that wearing steel is a decision a
caster makes rather than free armour they would be foolish to refuse.

It is deliberately not scoped to the *spirit* the spell is paid from,
though `source` exists on every discipline and would have expressed it
in one line. Every spirit-fuelled power that is not a spell is a Social
or Spiritual one — Rally, Command, Hold the Line, Turn Undead — and an
armoured commander shouting orders is the exact picture this rule was
written to protect, not one to penalise. The general sentence catches
the wrong people, so the specific one is the right one.

The price is real and it lands on a character who was already the least
of the party by measurement. That is accepted rather than overlooked: a
caster's protection is supposed to come from the guards in
[[spell-list]] rather than from a breastplate, and if it does not come
from there strongly enough, the guards are what wants fixing.

Shields do nothing while dodging for the same reason: a shield is
something you actively interpose, so it belongs to the stance that
represents interposing things.
{% endbook-only %}
