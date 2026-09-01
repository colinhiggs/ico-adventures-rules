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
    school: energy
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
    domain: magic
  flame_bolt:
    family: bolt
    damage_type: fire
    domain: war
  frost_bolt:
    family: bolt
    damage_type: cold
    domain: nature
  shock_bolt:
    family: bolt
    damage_type: lightning
    domain: war
  lance:
    school: energy
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
    domain: magic
    condition: stunned
  flame_lance:
    family: lance
    damage_type: fire
    domain: war
    condition: burning
  frost_lance:
    family: lance
    damage_type: cold
    domain: nature
    condition: slowed
  storm_lance:
    family: lance
    damage_type: lightning
    domain: war
    condition: dazed
  burst:
    school: energy
    base_difficulty: 6
    template: circle
    area_archetype: concentrated
    minimum_spirit: 2
    needs_attack_roll: false
    applies_condition: true
  blast:
    school: energy
    base_difficulty: 6
    template: any
    area_archetype: balanced
    minimum_spirit: 2
    needs_attack_roll: false
  field:
    school: energy
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
    domain: magic
    condition: stunned
  flame_burst:
    family: burst
    damage_type: fire
    domain: war
    condition: burning
  frost_burst:
    family: burst
    damage_type: cold
    domain: nature
    condition: slowed
  storm_burst:
    family: burst
    damage_type: lightning
    domain: war
    condition: dazed
  force_blast:
    family: blast
    damage_type: force
    domain: magic
  flame_blast:
    family: blast
    damage_type: fire
    domain: war
  frost_blast:
    family: blast
    damage_type: cold
    domain: nature
  storm_blast:
    family: blast
    damage_type: lightning
    domain: war
  force_field:
    family: field
    damage_type: force
    domain: magic
  flame_field:
    family: field
    damage_type: fire
    domain: war
  frost_field:
    family: field
    damage_type: cold
    domain: nature
  storm_field:
    family: field
    damage_type: lightning
    domain: war
  heal_order: [core, mastery]
  mend:
    tier: minor
    base_difficulty: 4
    school: life_force
    domain: healing
    range: touch
    restores: 4
    difficulty_per_step: 3
    restored_per_step: 1
    pools: [mastery]
    minimum_spirit: 0
  cure_wounds:
    base_difficulty: 16
    school: life_force
    domain: healing
    range: touch
    restores: 3
    difficulty_per_step: 4
    restored_per_step: 1
    pools: [core, mastery]
    minimum_spirit: 3
    minimum_spirit_per_point: 3
  cleanse:
    base_difficulty: 10
    school: life_force
    domain: healing
    range: touch
    ends_conditions: true
    ends_lasting: false
    minimum_spirit: 2
  restoration:
    base_difficulty: 14
    school: life_force
    domain: healing
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
- **School:** {{ mechanics.bolt.school }}
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
  of {{ mechanics.force_bolt.domain }}.
- **Flame Bolt** — {{ mechanics.flame_bolt.damage_type }} damage, domain
  of {{ mechanics.flame_bolt.domain }}.
- **Frost Bolt** — {{ mechanics.frost_bolt.damage_type }} damage, domain
  of {{ mechanics.frost_bolt.domain }}.
- **Shock Bolt** — {{ mechanics.shock_bolt.damage_type }} damage, domain
  of {{ mechanics.shock_bolt.domain }}.

Because the domain differs, a caster's [[discipline-powers|Granted
Domain]] makes one bolt markedly cheaper than the rest — a priest of war
throws flame where a druid throws frost, without either of them needing
a separate rule.

## The lances

Where a bolt is what a caster throws when there is nothing left, a
**lance** is what they open with. One spell again written four times,
sharing a chassis:

- **School:** {{ mechanics.lance.school }}
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
  domain of {{ mechanics.force_lance.domain }}, leaves the target
  **{{ mechanics.force_lance.condition }}**.
- **Flame Lance** — {{ mechanics.flame_lance.damage_type }} damage,
  domain of {{ mechanics.flame_lance.domain }}, leaves the target
  **{{ mechanics.flame_lance.condition }}**.
- **Frost Lance** — {{ mechanics.frost_lance.damage_type }} damage,
  domain of {{ mechanics.frost_lance.domain }}, leaves the target
  **{{ mechanics.frost_lance.condition }}**.
- **Storm Lance** — {{ mechanics.storm_lance.damage_type }} damage,
  domain of {{ mechanics.storm_lance.domain }}, leaves the target
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
- **School:** {{ mechanics.mend.school }}
- **Domain:** {{ mechanics.mend.domain }}
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

- **School:** {{ mechanics.cure_wounds.school }}
- **Domain:** {{ mechanics.cure_wounds.domain }}, or harm when reversed
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

- **School:** {{ mechanics.cleanse.school }}
- **Domain:** {{ mechanics.cleanse.domain }}
- **Range:** {{ mechanics.cleanse.range }}
- **Minimum spirit:** {{ mechanics.cleanse.minimum_spirit }}

Ends one condition on the creature you touch, if the difficulty you
declare meets or beats the difficulty that imposed it. It cannot touch a
lasting condition — see [[conditions]].

You are undoing somebody else's work, and the price is that you have to
match it. A stun laid on at difficulty `30` needs a Cleanse at `30`, and
the caster who laid it on paid for that difficulty too.

### Restoration ({{ mechanics.restoration.base_difficulty }})

- **School:** {{ mechanics.restoration.school }}
- **Domain:** {{ mechanics.restoration.domain }}
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
