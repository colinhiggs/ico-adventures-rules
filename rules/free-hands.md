---
id: free-hands
title: Free Hands
tags: [core, skills, powers]
summary: >
  Some skills and powers want a hand free, or both. You may always try
  them with your hands full, at a penalty for each hand you are short,
  and a quick weapon can be put away and brought back for nothing.
mechanics:
  hands_total: 2
  penalty_per_missing_hand: 2
  stowing_costs_an_action: true
  quick_stow_is_free: true
  hands_needed:
    spellcasting: 2
    heal: 1
    use_magic_device: 1
    sleight_of_hand: 1
    disable_device: 2
    climb: 2
---

You have {{ mechanics.hands_total }} hands, and what is in them decides
how well you can do the things that want them.

## What a hand is holding

A weapon takes the hands its size says it takes, and a shield takes one
— see [[weapons]] and [[armour]]. Whatever is left over is free.

Each skill or power says how many hands it wants:

- **{{ mechanics.hands_needed.spellcasting }} hands** — spellcasting,
  climb, disable device.
- **{{ mechanics.hands_needed.heal }} hand** — heal, use magic device,
  sleight of hand.

## Being short a hand

Nothing here stops you. You may always make the attempt with your hands
as full as they are, and take
`-{{ mechanics.penalty_per_missing_hand }}` on the roll for each hand
you are short of what the thing wants.

So a caster with both hands empty casts at no penalty; one holding a
single one-handed weapon is a hand short and casts at
`-{{ mechanics.penalty_per_missing_hand }}`; and one holding a
two-handed weapon, or a weapon and a shield, is two hands short.

That is a real cost and it is meant to be. A character who casts as
their main work will feel it every round and will mostly keep their
hands empty. A character who fights and casts is buying the second at a
discount on the first, which is the trade that build is making anyway.

## Putting it away

Stowing what you are holding, or drawing it again, costs your **action**
for the round — which is usually the action you wanted to use. A
**quick** weapon is the exception: it may be put away and brought back
freely, as often as you like, and costs nothing.

So a caster carrying a quick weapon has the best of it. The weapon is in
hand when somebody swings at them and out of it when they cast, and
neither costs them anything.

## Staffs

A staff is the exception to the penalty rather than to the rules about
hands. See [[weapons]]: it is held while casting at no penalty at all.

## Example

Sela casts, and casting wants
{{ mechanics.hands_needed.spellcasting }} hands.

Empty-handed, she casts at no penalty. With a sword in one hand she is a
hand short and casts at
`-{{ mechanics.penalty_per_missing_hand }}` — enough that she notices it
on every spell, not enough to stop her. With a two-handed sword she is
two hands short and casting is a poor idea, though still an idea.

Her dagger is quick, so on the round she wants a spell she puts it away
for nothing, casts unencumbered, and has it back in her hand before
anybody reaches her.

Bram fights and casts both. He carries a sword and accepts the
`-{{ mechanics.penalty_per_missing_hand }}` on the spells he does cast,
because he was never going to be the one out-casting Sela and he would
rather have the sword in his hand when the door opens.

Neither of them is doing anything the rules forbid. They are paying
different prices for different habits.

{% book-only %}
## Design note

The first version of this rule was a prohibition: no free hand, no
spell. It was tidy and it quietly banned two of the oldest characters in
the genre — the wizard who carries a sword, and the fighter who learned
some magic. A rule that cannot express Gandalf is the wrong rule
whatever its arithmetic says.

A penalty says the same thing without forbidding it. The pure caster
still keeps their hands empty, because a penalty on every spell of every
round is the largest cost in their game. The fighter who casts a little
pays it and shrugs, because they were only ever going to cast a little,
and a penalty on the occasional spell is a small price for having a
sword in hand the rest of the time. The rule sorts the two builds
without either of them being told what they may not do.

Asking for both hands rather than one is what makes it bite at all. With
one hand wanted, a sword in the other cost nothing, and the trade was
invisible for everybody except the two-handed-weapon user. Wanting both
means every weapon is felt and the size of the weapon decides how much
— which is the same shape as everything else equipment does here.
{% endbook-only %}
