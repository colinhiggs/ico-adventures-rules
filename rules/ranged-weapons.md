---
id: ranged-weapons
title: Ranged Weapons
tags: [equipment, reference, combat]
summary: >
  Bows, crossbows, slings and thrown weapons: accuracy, damage, range,
  hands and reload, and what it costs to shoot beyond that range, to
  shoot with somebody standing over you, or to draw a bow you are not
  strong enough for.
mechanics:
  long_range_penalty: -4
  engaged_penalty: -4
  into_melee_penalty: -2
  draw_penalty_per_point: -2
  weapon_block_applies_to_shots: false
  shield_block_applies_to_shots: true
  ammunition_recovered_fraction: 0.5
  sling:
    accuracy: 0
    damage: 4
    range: 6
    hands: 1
    ammunition: stones
    cost_gp: 1
  shortbow:
    accuracy: 1
    damage: 6
    range: 10
    hands: 2
    ammunition: arrows
    cost_gp: 30
  longbow:
    accuracy: 0
    damage: 8
    range: 18
    hands: 2
    ammunition: arrows
    draw_strength: 1
    cost_gp: 75
  light_crossbow:
    accuracy: 2
    damage: 8
    range: 12
    hands: 2
    ammunition: bolts
    reload: move
    cost_gp: 35
  heavy_crossbow:
    accuracy: 1
    damage: 11
    range: 16
    hands: 2
    ammunition: bolts
    reload: action
    cost_gp: 50
  javelin:
    accuracy: 0
    damage: 6
    range: 4
    hands: 1
    thrown: true
    cost_gp: 1
  arrows:
    used_by: bows
    quantity: 20
    cost_gp: 1
  bolts:
    used_by: crossbows
    quantity: 20
    cost_gp: 2
  stones:
    used_by: slings
    quantity: 20
    cost_gp: 0
---

A ranged weapon is aimed rather than swung, and it is the only way to
hurt something you are not standing next to.

Each carries the **accuracy** and **damage** a melee weapon carries, and
three things a melee weapon has no use for: the **range** it is accurate
to, the **hands** it occupies, and — for some — a **reload** that must
be paid before it can shoot again.

## The weapons

{% table mechanics
   rows=sling,shortbow,longbow,light_crossbow,heavy_crossbow,javelin
   columns=accuracy:Accuracy,damage:Damage,range:Range,hands:Hands,
           reload:Reload,cost_gp:"Cost (gp)"
   flags=thrown:thrown,draw_strength:"strong draw"
   header=Weapon %}

Range and reach are counted in the same squares, so a range column and
the [[movement]] table are read against each other without converting
anything.

## Throwing what you were holding

The dagger and the hand axe in [[weapons]] are balanced well enough to
be thrown, and each carries the range it can be thrown to. Thrown, a
weapon keeps its own accuracy and damage — it is the same object
arriving by a different route — and everything else on this page applies
to it.

{% table weapons:mechanics
   rows=dagger,hand_axe
   columns=accuracy:Accuracy,damage:Damage,thrown_range:Range,
           cost_gp:"Cost (gp)"
   header=Weapon %}

A thrown weapon is no longer in your hand. Picking it up again is a
matter of walking over to it, which is why anyone who means to throw
things carries several.

## Shooting

Shooting is an action, and it is the same exchange as any other blow.
The attacker rolls against a targeting difficulty the defender set by
choosing to dodge or block, the margin is carried into the damage step,
and both are worked out exactly as [[hitting]] and [[damage]] say.

The skill is **Attack (ranged)**, governed by dexterity — see
[[skill-list]]. That is the whole of the difference in the roll: a
ranged attack is a dexterity attack the way a melee attack is a strength
one, and the damage a shot does grows with the ranged attack skill at
the rate [[damage]] gives every weapon.

## Range

A weapon's listed range is its **short range**, measured in the squares
[[movement]] measures. Inside it you shoot at no penalty.

**Long range** is
{{ spell-properties:mechanics.long_range_multiplier }} times the listed
figure — the same doubling that carries a spell out to its own long
range, see [[spell-properties]] — and shooting into it costs
`{{ mechanics.long_range_penalty }}` on the attack roll.

A spell aimed into its own long range pays the same, out of the same
figure. Distance is not interested in what launched the thing, so
[[spell-properties]] charges a bolt what this page charges an arrow.

Beyond long range there is no shot. The arrow goes somewhere; it does
not go where you were aiming, and the Dungeon Master is not obliged to
say where it went.

## Defending against a shot

The defender chooses dodge or block before the roll, exactly as
[[hitting]] describes, and a shot is dodged exactly as a swing is.

Blocking is where the two part. A **shield** stops an arrow as well as
it stops a sword, and its block value applies in full. A **weapon's**
does not: a blade is no use against something that was never going to
touch it. A defender holding a weapon and no shield is choosing between
dodging and standing still, and should dodge.

## Shooting in a fight

Two things get in the way of a shot, and neither of them forbids it.

**Somebody standing over you.** While an enemy is inside your own reach
— see [[reach]] — a bow is the wrong length for the fight you are in,
and every shot you take costs `{{ mechanics.engaged_penalty }}`.

**Somebody standing over your target.** Shooting at a target that is
inside an ally's reach costs `{{ mechanics.into_melee_penalty }}`. The
two of them are moving, and some of what you are aiming at is your
friend's back.

## Drawing weight

A bow is drawn with the shoulders and the back, and a heavy one asks
more of them than a light one. An entry marked as wanting a strong draw
names the strength bonus it is built around: the longbow wants
`+{{ mechanics.longbow.draw_strength }}`.

Nothing stops you shooting one you are not built for. You take
`{{ mechanics.draw_penalty_per_point }}` on the attack roll for every
point of strength bonus you are short of what the bow asks, and you go
on shooting.

## Reloading

A bow is reloaded as it is drawn, and a sling as it is whirled; neither
costs anything beyond the shot itself. A crossbow is a spanned weapon
and has to be made ready again, and its entry says what that costs out
of the turn [[turn-order]] gives you:

- **move** — reloading takes your move for the round. You shoot every
  round and go nowhere while you do it.
- **action** — reloading takes your action. You shoot every other
  round.

That is what the crossbows are buying. A light crossbow is the most
accurate thing on the table and roots the shooter to the spot; a heavy
one hits nearly as hard as anything in the game and spends half the
fight being wound.

## Hands, and changing your mind

A ranged weapon states outright how many hands it takes, rather than
inheriting them from a size the way a melee weapon does. Size on the
melee table also settles finesse, reach and block value, and none of
those three describes a bow.

Whatever is left over is free, and [[free-hands]] charges its usual
penalty for every hand a skill or a power wanted and did not get. A bow
in both hands is the most expensive thing a caster can be holding. A
sling or a javelin leaves a hand, and so leaves room for a shield.

Putting a bow away and drawing a sword costs your action, as
[[free-hands]] says. An archer caught at close quarters therefore
spends a round becoming a swordsman, or keeps shooting at the penalty
above and hopes the round goes well.

## Ammunition

{% table mechanics
   rows=arrows,bolts,stones
   columns=used_by:"Used by",quantity:Quantity,cost_gp:"Cost (gp)"
   header=Ammunition %}

You recover `{{ mechanics.ammunition_recovered_fraction }}` of what you
shot once a fight is over, rounding down. The rest is broken, trodden
on, or still in something that ran away.

Stones cost nothing because they are underfoot, and a sling is the only
weapon here that can be resupplied from a riverbed.

## Example

Dune carries a shortbow, and a goblin is `9` squares off.

The bow's short range is {{ mechanics.shortbow.range }} squares, so `9`
costs him nothing. He rolls the die, adds his ranged attack skill with
his dexterity bonus of `+4`, and adds the bow's accuracy of
`+{{ mechanics.shortbow.accuracy }}`. The goblin dodges, so its
targeting difficulty is {{ hitting:mechanics.dodge_targeting_base }}
plus its dodge, and the shot is settled by [[hitting]] like any other.

A second goblin closes to arm's length. Dune is now shooting with
something standing over him, at `{{ mechanics.engaged_penalty }}` a
shot. He can put the bow away and draw his short sword, which costs him
his action and the round with it, or he can keep shooting and wear the
penalty. He keeps shooting: one goblin at arm's length is a smaller
problem than the three still out at range.

Ashri would rather have the longbow — {{ mechanics.longbow.damage }}
damage against the shortbow's {{ mechanics.shortbow.damage }}, and
{{ mechanics.longbow.range }} squares of range against
{{ mechanics.shortbow.range }}. Her strength bonus of `+3` is well past
the draw it asks for, so it costs her nothing at all. Sela, with no
strength bonus to speak of, would shoot the same bow at
`{{ mechanics.draw_penalty_per_point }}` every time she loosed, which is
why she carries a sling and keeps her shield.

{% book-only %}
## Design note

Range is one number and a doubling rather than a ladder of increments,
because the ladder is arithmetic done in the middle of a fight to
produce a modifier nobody enjoys. Two bands can be read off the table at
a glance: you are inside the number, inside twice the number, or you do
not have a shot. It is the same shape a spell's range already has, which
means the archer and the caster are asking the map the same question.

The crossbows are priced in the turn rather than in the attack roll.
Every character already has an action and a move, and spending one or
the other is a cost every player at the table understands without a new
resource being invented for it. Out of that come two genuinely different
weapons: one that shoots every round from a spot it cannot leave, and
one that shoots every other round for the hardest hit in this list. The
bows, which cost neither, are correspondingly less accurate and less
damaging than the crossbow that sits beside them.

Draw weight is interference rather than a requirement. Nothing here says
who may carry a longbow — a rule that says so is a rule about the
character sheet rather than about the bow — and a character who wants
one badly enough may have one and shoot it worse. What that buys is a
reason for the shortbow, the sling and the crossbows to exist for the
character who is quick rather than strong, and a reason for the longbow
to be the weapon of somebody who is both.

The close-quarters penalty does the same job from the other end. An
archer who simply could not shoot with an enemy adjacent would be a
character whose whole contribution is switched off by one goblin walking
four squares, and the answer at the table would be to never play one.
A penalty leaves the decision where it belongs: shoot badly at the thing
in front of you, shoot badly at the things behind it, or spend a round
drawing the sword you were sensible enough to bring.

A shield stopping a shot and a weapon not stopping one is the one place
a shot is resolved differently from a swing, and it is the difference
between the two objects rather than a special case. Blocking with a
weapon is deflecting something that is coming to meet the blade; an
arrow was never going to. This is also what keeps the sling and the
javelin worth their place — they are the ranged weapons a shield-bearer
can carry, and a shield is the only thing that answers a shot with
anything except distance.
{% endbook-only %}
