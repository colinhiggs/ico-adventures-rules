---
id: spell-list
title: The Spell List
tags: [magic, reference]
summary: >
  The spells defined so far. The bolts are minor spells — weak, endlessly
  repeatable, and what a caster falls back on with an empty reservoir.
mechanics:
  list_incomplete: true
  bolt:
    tier: minor
    base_difficulty: 2
    schools: [energy]
    range: 10
    needs_attack_roll: true
    damage: 6
    difficulty_per_step: 3
    damage_per_step: 1
    difficulty_per_extra_bolt: 8
    minimum_spirit: 0
  force_bolt:
    family: bolt
    damage_type: force
    domains: [magic]
  flame_bolt:
    family: bolt
    damage_type: fire
    domains: [war]
  frost_bolt:
    family: bolt
    damage_type: cold
    domains: [nature]
  shock_bolt:
    family: bolt
    damage_type: lightning
    domains: [war]
  lance:
    schools: [energy]
    base_difficulty: 8
    damage: 10
    difficulty_per_step: 2
    damage_per_step: 1
    difficulty_per_extra_bolt: 20
    minimum_spirit: 2
    needs_attack_roll: true
    range: 10
    applies_condition: true
  force_lance:
    family: lance
    damage_type: force
    domains: [magic]
    condition: stunned
  flame_lance:
    family: lance
    damage_type: fire
    domains: [war]
    condition: burning
  frost_lance:
    family: lance
    damage_type: cold
    domains: [nature]
    condition: slowed
  storm_lance:
    family: lance
    damage_type: lightning
    domains: [war]
    condition: dazed
  burst:
    schools: [energy]
    base_difficulty: 6
    template: circle
    area_archetype: concentrated
    minimum_spirit: 2
    needs_attack_roll: false
    applies_condition: true
  blast:
    schools: [energy]
    base_difficulty: 6
    template: any
    area_archetype: balanced
    minimum_spirit: 2
    needs_attack_roll: false
  field:
    schools: [energy]
    base_difficulty: 8
    template: circle
    area_archetype: diffuse
    difficulty_per_damage: 2
    minimum_spirit: 3
    needs_attack_roll: false
    duration_rounds: 2
    rounds_per_difficulty: 1
  force_burst:
    family: burst
    damage_type: force
    domains: [magic]
    condition: stunned
  flame_burst:
    family: burst
    damage_type: fire
    domains: [war]
    condition: burning
  frost_burst:
    family: burst
    damage_type: cold
    domains: [nature]
    condition: slowed
  storm_burst:
    family: burst
    damage_type: lightning
    domains: [war]
    condition: dazed
  force_blast:
    family: blast
    damage_type: force
    domains: [magic]
  flame_blast:
    family: blast
    damage_type: fire
    domains: [war]
  frost_blast:
    family: blast
    damage_type: cold
    domains: [nature]
  storm_blast:
    family: blast
    damage_type: lightning
    domains: [war]
  force_field:
    family: field
    damage_type: force
    domains: [magic]
  flame_field:
    family: field
    damage_type: fire
    domains: [war]
  frost_field:
    family: field
    damage_type: cold
    domains: [nature]
  storm_field:
    family: field
    damage_type: lightning
    domains: [war]
  ward:
    base_difficulty: 6
    template: circle
    area_archetype: diffuse
    minimum_spirit: 2
    needs_attack_roll: false
    no_damage: true
    duration_rounds: 3
    rounds_per_difficulty: 1
  fog_bank:
    family: ward
    schools: [matter]
    domains: [nature, sea]
    condition_inside: blinded
  shroud:
    family: ward
    schools: [illusion]
    domains: [darkness, trickery]
    condition_inside: blinded
  briar_patch:
    family: ward
    schools: [matter]
    domains: [nature]
    condition_inside: rooted
  sleet_storm:
    family: ward
    schools: [energy]
    domains: [storm, nature]
    condition_inside: slowed
  hallowed_ground:
    family: ward
    schools: [influence_and_command]
    domains: [light, justice]
    condition_inside: dazed
  ring_of_silence:
    family: ward
    schools: [matter]
    domains: [knowledge, magic]
    condition_inside: silenced
  heal_order: [core, mastery]
  mend:
    tier: minor
    base_difficulty: 4
    schools: [life_force]
    domains: [healing]
    range: touch
    restores: 4
    difficulty_per_step: 3
    restored_per_step: 1
    pools: [mastery]
    minimum_spirit: 0
  cure_wounds:
    base_difficulty: 16
    schools: [life_force]
    domains: [healing]
    range: touch
    restores: 3
    difficulty_per_step: 4
    restored_per_step: 1
    pools: [core, mastery]
    minimum_spirit: 3
    minimum_spirit_per_point: 3
  cleanse:
    base_difficulty: 10
    schools: [life_force]
    domains: [healing]
    range: touch
    ends_conditions: true
    ends_lasting: false
    minimum_spirit: 2
  restoration:
    base_difficulty: 14
    schools: [life_force]
    domains: [healing]
    range: touch
    ends_conditions: true
    ends_lasting: true
    minimum_spirit: 4
---

Difficulty, cost and boosting all work as [[spellcasting]] and
[[spell-properties]] describe. A spell marked **minor** is a minor
power, and the minimum cost does not apply to it — see [[using-powers]].

## The bolts

The bolts are one spell written several times, differing only in the
damage they deal. Every one of them shares a chassis:

- **Tier:** {{ mechanics.bolt.tier }}
- **Schools:** {{ mechanics.bolt.schools }}
- **Range:** {{ mechanics.bolt.range }}, needing a ranged attack roll
- **Base difficulty:** {{ mechanics.bolt.base_difficulty }}
- **Damage:** {{ mechanics.bolt.damage }}
- **Minimum spirit:** {{ mechanics.bolt.minimum_spirit }}

and both standard boosts:

- **More damage:** {{ mechanics.bolt.damage_per_step }} per further
  {{ mechanics.bolt.difficulty_per_step }} points of difficulty.
- **More bolts:** one extra bolt per further
  {{ mechanics.bolt.difficulty_per_extra_bolt }} points of difficulty.

The variants are then only a damage type and a domain:

- **Force Bolt** — {{ mechanics.force_bolt.damage_type }} damage, domain
  of {{ mechanics.force_bolt.domains }}.
- **Flame Bolt** — {{ mechanics.flame_bolt.damage_type }} damage, domain
  of {{ mechanics.flame_bolt.domains }}.
- **Frost Bolt** — {{ mechanics.frost_bolt.damage_type }} damage, domain
  of {{ mechanics.frost_bolt.domains }}.
- **Shock Bolt** — {{ mechanics.shock_bolt.damage_type }} damage, domain
  of {{ mechanics.shock_bolt.domains }}.

Because the domain differs, a caster's [[discipline-powers|Granted
Domain]] makes one bolt markedly cheaper than the rest — a priest of war
throws flame where a druid throws frost, without either of them needing
a separate rule.

## The lances

Where a bolt is what a caster throws when there is nothing left, a
**lance** is what they open with. One spell again written four times,
sharing a chassis:

- **Schools:** {{ mechanics.lance.schools }}
- **Range:** {{ mechanics.lance.range }}, aimed with the casting roll
- **Base difficulty:** {{ mechanics.lance.base_difficulty }}
- **Damage:** {{ mechanics.lance.damage }}, plus
  {{ mechanics.lance.damage_per_step }} for each further
  {{ mechanics.lance.difficulty_per_step }} points of difficulty
- **Minimum spirit:** {{ mechanics.lance.minimum_spirit }}

A lance that hits also applies a **condition**, which the target may
resist — see [[conditions]]. That is what a lance buys over a bolt, and
why it is worth the spirit a bolt does not cost.

The variants differ in damage type, domain, and which condition they
carry:

- **Force Lance** — {{ mechanics.force_lance.damage_type }} damage,
  domain of {{ mechanics.force_lance.domains }}, leaves the target
  **{{ mechanics.force_lance.condition }}**.
- **Flame Lance** — {{ mechanics.flame_lance.damage_type }} damage,
  domain of {{ mechanics.flame_lance.domains }}, leaves the target
  **{{ mechanics.flame_lance.condition }}**.
- **Frost Lance** — {{ mechanics.frost_lance.damage_type }} damage,
  domain of {{ mechanics.frost_lance.domains }}, leaves the target
  **{{ mechanics.frost_lance.condition }}**.
- **Storm Lance** — {{ mechanics.storm_lance.damage_type }} damage,
  domain of {{ mechanics.storm_lance.domains }}, leaves the target
  **{{ mechanics.storm_lance.condition }}**.

Which lance to carry is a question about the fight rather than about the
numbers: they deal the same damage, and the condition is the whole
difference.

## The area spells

Three families, and each of the four damage types appears in all three.
None of them needs an attack roll: everything under the template takes
the damage, and having nothing to dodge is what an area spell buys with
its difficulty.

The family decides what kind of spell it is; the damage type decides how
it looks and, for a burst, what it leaves behind.

### Bursts — {{ mechanics.burst.area_archetype }}

*Base difficulty {{ mechanics.burst.base_difficulty }}, circle,
minimum spirit {{ mechanics.burst.minimum_spirit }}.*

Small and fierce, and the only area family that applies a condition —
the same conditions the lances carry, resisted the same way. See
[[conditions]].

- **Force Burst** — {{ mechanics.force_burst.damage_type }} damage,
  leaves the target **{{ mechanics.force_burst.condition }}**.
- **Flame Burst** — {{ mechanics.flame_burst.damage_type }} damage,
  leaves the target **{{ mechanics.flame_burst.condition }}**.
- **Frost Burst** — {{ mechanics.frost_burst.damage_type }} damage,
  leaves the target **{{ mechanics.frost_burst.condition }}**.
- **Storm Burst** — {{ mechanics.storm_burst.damage_type }} damage,
  leaves the target **{{ mechanics.storm_burst.condition }}**.

### Blasts — {{ mechanics.blast.area_archetype }}

*Base difficulty {{ mechanics.blast.base_difficulty }}, minimum spirit
{{ mechanics.blast.minimum_spirit }}.*

A blast takes **any template in [[spell-area]]** — circle, cone, line,
square or rectangle — chosen as it is cast. That flexibility is the
family's whole character: a blast carries no condition and lasts no
time, but it is the only area spell that can be poured down a corridor
or swept across a rank.

Force, Flame, Frost and Storm Blast differ only in damage type and
domain.

### Fields — {{ mechanics.field.area_archetype }}

*Base difficulty {{ mechanics.field.base_difficulty }}, circle,
minimum spirit {{ mechanics.field.minimum_spirit }}.*

A field does not go off; it stays. It lasts
{{ mechanics.field.duration_rounds }} rounds, plus
{{ mechanics.field.rounds_per_difficulty }} for each further point of
difficulty spent on duration, and anything inside it takes the damage at
the start of its turn. It is the only way a caster denies ground rather
than clearing it.

A field spreads at the {{ mechanics.field.area_archetype }} rate, so it
covers more ground per point than anything else in [[spell-area]] — but
it pays for its damage at {{ mechanics.field.difficulty_per_damage }}
points each, the same rate a blast pays, rather than the diffuse rate.
A field that nobody minds walking through is not denying anything.

Force, Flame, Frost and Storm Field differ only in damage type and
domain.

{% book-only %}
### Design note

Wide and weak was the original idea, and it does not work: a field that
deals a scratch is a field the enemy walks straight across, which leaves
the spell with no job at all. Area denial only denies if crossing costs
something worth avoiding, so a damaging field buys its damage at the
same rate a blast does and simply pays a great deal of difficulty for
covering so much ground.

That makes the damaging fields expensive, which is correct — most fields
will not be damaging at all. Fog, tangling ground, silence and the rest
deny ground by what they do rather than by what they deal, and those are
the ones the archetype's cheap spread was written for.
{% endbook-only %}

## The wards

A **ward** covers ground and does nothing to it. Everything standing
inside has the ward's condition, for exactly as long as it stands
there; step out and it stops. There is no attack roll, no damage, and —
unlike every other condition in the game — **no roll to resist**. You
are in the fog or you are not.

That is what makes area denial a different thing from an area attack. A
blast asks whether it beat you; a ward asks where you are standing. The
counter to a ward is not a good Fortitude score, it is your feet.

Wards spread at the {{ mechanics.ward.area_archetype }} rate, the widest
in [[spell-area]], because covering ground is the whole of what they
buy. Difficulty goes to area and to duration and to nothing else: a ward
does the same thing however hard it was cast, over more or less of the
map, for more or less of the fight.

All six share a chassis:

- **Base difficulty:** {{ mechanics.ward.base_difficulty }}
- **Template:** {{ mechanics.ward.template }}, priced as
  {{ mechanics.ward.area_archetype }} — see [[spell-area]]
- **Duration:** {{ mechanics.ward.duration_rounds }} rounds, plus
  {{ mechanics.ward.rounds_per_difficulty }} for each further point of
  difficulty spent on it
- **Minimum spirit:** {{ mechanics.ward.minimum_spirit }}

### Fog Bank

*{{ mechanics.fog_bank.schools }}; {{ mechanics.fog_bank.domains }}.*
Cold grey fog, too thick to see an arm's length through. Anything
inside is **{{ mechanics.fog_bank.condition_inside }}** — see
[[conditions]] — which makes a fog bank as bad for the caster's own side
as for anyone else, and is the reason it is usually put somewhere nobody
friendly intends to stand.

### Shroud

*{{ mechanics.shroud.schools }}; {{ mechanics.shroud.domains }}.*
Darkness that is not the absence of light but the presence of something
else. Anything inside is
**{{ mechanics.shroud.condition_inside }}**. It does the same work as a
Fog Bank and belongs to a different pair of gods, which is the point of
having both.

### Briar Patch

*{{ mechanics.briar_patch.schools }};
{{ mechanics.briar_patch.domains }}.* Thorned growth erupts from the
ground and takes hold of whatever is standing in it. Anything inside is
**{{ mechanics.briar_patch.condition_inside }}**: it may fight, it may
defend itself, it may not go anywhere. The most straightforwardly
obstructive ward, and the one that most resembles a wall.

### Sleet Storm

*{{ mechanics.sleet_storm.schools }};
{{ mechanics.sleet_storm.domains }}.* Freezing rain and treacherous
footing. Anything inside is
**{{ mechanics.sleet_storm.condition_inside }}**. It denies less than a
Briar Patch and is far harder to simply avoid, since a creature can
still cross it — slowly, and while being shot at.

### Hallowed Ground

*{{ mechanics.hallowed_ground.schools }};
{{ mechanics.hallowed_ground.domains }}.* Ground given over to something
larger, which does not want a fight happening on it. Anything inside is
**{{ mechanics.hallowed_ground.condition_inside }}**. The only ward that
leaves its occupants entirely mobile and merely worse at everything.

### Ring of Silence

*{{ mechanics.ring_of_silence.schools }};
{{ mechanics.ring_of_silence.domains }}.* Sound stops at the edge.
Anything inside is
**{{ mechanics.ring_of_silence.condition_inside }}**, which is aimed at
one kind of enemy in particular and does very little to the rest.

{% book-only %}
### Design note

The wards do not allow a resistance roll, and that is the most important
thing about them.

Every other condition in the game lands by beating somebody, which makes
a condition a contest and its duration a matter of how badly they lost.
That is right for something a caster does *to* a creature. It is wrong
for something a caster does to a *place*. A fog bank is not trying to
beat you; it is fog. Rolling against it would say that a strong-willed
character can see through weather, which is a strange thing for a rule
to claim and an annoying one to adjudicate.

Making them terrain also gives them a counter that has nothing to do
with character sheets. A ward is beaten by moving, by going round, by
waiting it out, or by making the enemy come to you anyway — decisions
rather than dice. That is a different kind of pressure from anything
else in the spell list, which is the reason for having the category at
all.

The price is that difficulty buys only ground and time. A ward cast
enormously hard is a bigger, longer-lasting fog and not a thicker one,
which keeps the whole family out of the arms race the damaging spells
are in.
{% endbook-only %}

## The restorative spells

Harm is undone in the reverse of the order it was done. [[hit-points]]
sends damage through mastery first and into core only when mastery is
gone; healing goes to **core first**, and reaches mastery only once the
real wound has closed. A wound mends before the luck comes back.

That is why there are two spells and not one. Mastery hit points return
between fights on their own, and core hit points return at the rate
[[recovery]] gives them, which is barely at all — so the shallow pool is
worth a cheap spell cast often, and the deep pool is worth an expensive
one cast rarely.

### Mend ({{ mechanics.mend.base_difficulty }})

- **Tier:** {{ mechanics.mend.tier }}
- **Schools:** {{ mechanics.mend.schools }}
- **Domains:** {{ mechanics.mend.domains }}
- **Range:** {{ mechanics.mend.range }}
- **Minimum spirit:** {{ mechanics.mend.minimum_spirit }}

Restores {{ mechanics.mend.restores }} mastery hit points, plus
{{ mechanics.mend.restored_per_step }} for each further
{{ mechanics.mend.difficulty_per_step }} points of difficulty. It cannot
touch core hit points: it puts back the cushion, not the wound.

Being a minor spell it has no minimum cost, so a caster who has run dry
can still mend — which is the point of it. It is to healing what a bolt
is to harm.

### Cure Wounds ({{ mechanics.cure_wounds.base_difficulty }})

- **Schools:** {{ mechanics.cure_wounds.schools }}
- **Domains:** {{ mechanics.cure_wounds.domains }}, or harm when
  reversed
- **Range:** {{ mechanics.cure_wounds.range }}
- **Minimum spirit:** {{ mechanics.cure_wounds.minimum_spirit }}

Restores {{ mechanics.cure_wounds.restores }} hit points, plus
{{ mechanics.cure_wounds.restored_per_step }} for each further
{{ mechanics.cure_wounds.difficulty_per_step }} points of difficulty,
to core hit points first and to mastery once core is full.

However well you roll, this spell costs at least
{{ mechanics.cure_wounds.minimum_spirit_per_point }} spirit for every
hit point it puts back. A good roll makes an ordinary spell cheaper; it
does not make this one cheaper, because what it is buying is not
measured in difficulty.

It restores far less per point than Mend and costs a great deal more.
That is not a mistake. A point of core is a night's rest, and this is
the only thing in the game that gives one back in the middle of an
adventure.

Cast as *Cause Wounds*, the same spell inflicts that much damage
instead, applied the ordinary way round.

### Cleanse ({{ mechanics.cleanse.base_difficulty }})

- **Schools:** {{ mechanics.cleanse.schools }}
- **Domains:** {{ mechanics.cleanse.domains }}
- **Range:** {{ mechanics.cleanse.range }}
- **Minimum spirit:** {{ mechanics.cleanse.minimum_spirit }}

Ends one condition on the creature you touch, if the difficulty you
declare meets or beats the difficulty that imposed it. It cannot touch a
lasting condition — see [[conditions]].

You are undoing somebody else's work, and the price is that you have to
match it. A stun laid on at difficulty `30` needs a Cleanse at `30`, and
the caster who laid it on paid for that difficulty too.

### Restoration ({{ mechanics.restoration.base_difficulty }})

- **Schools:** {{ mechanics.restoration.schools }}
- **Domains:** {{ mechanics.restoration.domains }}
- **Range:** {{ mechanics.restoration.range }}
- **Minimum spirit:** {{ mechanics.restoration.minimum_spirit }}

The same, for the conditions Cleanse cannot reach: blindness, disease, a
curse. Ends one lasting condition on the creature you touch, again if
your declared difficulty meets or beats the difficulty that imposed it.

Nothing else in the rules ends a lasting condition. Waiting does not.

{% book-only %}
### Design note

Undoing a condition by matching the difficulty that imposed it needed no
new machinery at all, and it prices itself. The difficulty a caster
declared is already the number the victim had to beat, already what the
caster paid for, and already recorded in the fiction as how hard the
effect was to shrug off. Asking a healer to meet the same number makes a
powerful affliction genuinely hard to lift and a casual one easy, with
no table of removal difficulties to write or look up.

Splitting the two hit point pools between two spells does the same
trick with the recovery rules rather than the condition rules. The
question "how much healing is too much" has an answer already: mastery
hit points come back on their own between fights, so restoring them
cheaply changes the pace of a fight and nothing else. Core hit points do
not come back, so restoring them changes the length of the adventuring
day — which is the resource the whole day model turns on, and the reason
Cure Wounds is priced where a caster feels it.

Pinning the price to the hit point rather than to the roll is what stops
the spell running away. Every other cost in the game falls as a caster's
skill rises, which is correct where the effect is measured in
difficulty: you are getting better at the same trick. Core hit points
are not measured in difficulty. They are a fixed, small pool that
scarcely refills, and a reservoir that grows sixfold over a career would
otherwise turn into six times as much healing at a steadily better rate
-- a senior caster undoing several characters' worth of real injury in
an afternoon, which is precisely what [[recovery]] exists to prevent.
An exchange rate that holds at every level leaves magic as the exception
to that rule without letting it swallow the rule.

Reversing the order harm travels in is the small piece that makes both
of them behave. If healing filled mastery first, a badly wounded
character would get their luck back before their wound closed, and a
healer could keep somebody nominally upright for ever without ever
mending them. Core first means healing a hurt character is expensive
precisely when it matters.
{% endbook-only %}

## Example

Sela has a spellcasting skill of `18` and no spirit left at all.

She casts Force Bolt, declaring its base difficulty with no boosts. She
rolls `7`, for a total of `25` — beating the declared difficulty by far
more than the base cost, so the bolt costs her nothing. She still has to
land it: the bolt needs a ranged attack roll, as [[spell-properties]]
describes.

Fresh, she would have declared much higher. At a difficulty of `14` the
same spell buys four steps of extra damage, and at `18` she could
instead have thrown a second bolt. Both would have cost real spirit.

The bolt she throws with an empty reservoir is a fraction of the one she
opens a fight with — but she is still casting, and still choosing a
damage type to suit the target.

{% book-only %}
## Design note

The bolts are one spell written several times because a family of
identical spells differing only in damage type is a table, not four
rules. Keeping the shared numbers in one place means the family cannot
drift apart as it grows, and adding a fifth bolt is an entry rather than
a rewrite.

Their boost rate is deliberately poor while their base damage is not.
That combination is what makes a bolt a floor rather than a ceiling: it
opens respectably and then barely improves however hard it is pushed, so
it is worth having with an empty reservoir and never worth preferring to
a lance when there is spirit to spend.

The base was raised once the lances existed. Measured against a caster's
new best turn, the old bolt left an empty caster on under a quarter of
their output -- past diminished and into sidelined, which is exactly what
the minor tier exists to prevent. The rate was left alone, because the
rate is what keeps minor and standard apart.

Cure Wounds stays standard rather than minor for the same reason from
the other direction. Healing available on demand for nothing would empty
every fight of consequence, since any damage that did not drop a
character outright could simply be undone afterwards at no cost.
{% endbook-only %}
