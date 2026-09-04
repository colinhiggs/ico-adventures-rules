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
  staunch:
    schools: [life_force]
    domains: [healing, death]
    base_difficulty: 6
    range: 10
    minimum_spirit: 2
    needs_attack_roll: false
    no_damage: true
    stabilises: true
  raise_the_dead:
    schools: [life_force]
    domains: [death, healing, light]
    base_difficulty: 30
    range: touch
    minimum_spirit: 10
    needs_attack_roll: false
    no_damage: true
    raises_the_dead: true
    difficulty_per_hour_dead: 1
    hours_before_beyond_reach: 24
    core_hit_points_from_caster: 3
    caster_pays_only_on_success: true
    cost_cannot_be_healed_by_magic: true
    returns_at_core: 1
  guard:
    base_difficulty: 8
    range: touch
    minimum_spirit: 2
    needs_attack_roll: false
    no_damage: true
    duration_rounds: 3
    rounds_per_difficulty: 1
    protection: 1
    difficulty_per_step: 5
    protection_per_step: 1
  bulwark:
    family: guard
    schools: [matter]
    domains: [forge, light]
    protects: mastery_hit_points
    protection: 4
    difficulty_per_step: 4
    protection_per_step: 2
  stoneskin:
    family: guard
    schools: [matter]
    domains: [nature, forge]
    protects: damage_reduction
  elemental_guard:
    family: guard
    schools: [energy]
    domains: [nature, storm]
    protects: damage_reduction_of_one_type
    protection: 2
    difficulty_per_step: 3
  mantle_of_warding:
    family: guard
    schools: [influence_and_command]
    domains: [magic, knowledge]
    protects: resistance_to_one_school
    difficulty_per_step: 4
  deathward:
    family: guard
    schools: [life_force]
    domains: [death, light]
    protects: resistance_to_the_death_domain
    protection: 2
    difficulty_per_step: 4
  blessing:
    base_difficulty: 8
    range: touch
    minimum_spirit: 2
    needs_attack_roll: false
    no_damage: true
    duration_rounds: 3
    rounds_per_difficulty: 1
    bonus: 1
    difficulty_per_step: 6
    bonus_per_step: 1
  blessing_of_the_blade:
    family: blessing
    schools: [influence_and_command]
    domains: [war, light]
    boosts: attack_rolls
  warding_blessing:
    family: blessing
    schools: [influence_and_command]
    domains: [light, healing]
    boosts: targeting_difficulty
  heart_of_the_lion:
    family: blessing
    schools: [influence_and_command]
    domains: [love, war]
    boosts: resolve
  keen_edge:
    family: blessing
    schools: [matter]
    domains: [forge, war]
    boosts: weapon_damage
    difficulty_per_step: 4
  fleetness:
    family: blessing
    schools: [energy]
    domains: [travel, storm]
    boosts: movement_squares
    bonus: 2
    difficulty_per_step: 5
    bonus_per_step: 1
  fortunes_favour:
    family: blessing
    schools: [influence_and_command]
    domains: [luck, trickery]
    boosts: critical_range
    bonus: 1
    bonus_per_step: 0
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

## Bringing them back

Two spells for the worst moment, and they are not the same spell. One
stops somebody dying. The other undoes it, and costs the caster
something a night's sleep will not give back.

### Staunch ({{ mechanics.staunch.base_difficulty }})

- **Schools:** {{ mechanics.staunch.schools }}
- **Domains:** {{ mechanics.staunch.domains }}
- **Range:** {{ mechanics.staunch.range }}
- **Minimum spirit:** {{ mechanics.staunch.minimum_spirit }}

A creature at death's door is **stable** — see [[dying]]. The dying
count stops. It restores no hit points at all: they are still
unconscious, still on whatever they were reduced to, and still wounded
when they wake.

That is the whole of its value and it is considerable. Cure Wounds can
do this too, by taking them back above nothing, but Cure Wounds charges
by the hit point and hauling somebody up from six under is an enormous
bill in the middle of a fight. Staunch charges once, at a difficulty
anyone can reach, and does it from across the room rather than from
arm's length — which is often the difference between saving them and
walking into whatever put them there.

### Raise the Dead ({{ mechanics.raise_the_dead.base_difficulty }})

- **Schools:** {{ mechanics.raise_the_dead.schools }}
- **Domains:** {{ mechanics.raise_the_dead.domains }}
- **Range:** {{ mechanics.raise_the_dead.range }}
- **Minimum spirit:** {{ mechanics.raise_the_dead.minimum_spirit }}

The dead return, on
{{ mechanics.raise_the_dead.returns_at_core }} core hit point:
unconscious, wounded, and alive.

Three things make it something other than an errand.

**It gets harder every hour.** Add
{{ mechanics.raise_the_dead.difficulty_per_hour_dead }} to the
difficulty for each hour since death, on top of the base — and after
{{ mechanics.raise_the_dead.hours_before_beyond_reach }} hours it cannot
be done at all, at any difficulty, by anyone. Whatever the spell reaches
for is no longer within reach.

**It costs the caster core hit points.** A successful casting takes
{{ mechanics.raise_the_dead.core_hit_points_from_caster }} core hit
points from *you* — and **no magic will put those back**. They are not
an injury. Nobody hurt you; you spent yourself, and healing mends wounds
rather than refunding what was given away. They return only with rest,
at the
{{ recovery:mechanics.core_hit_points_per_night }} a night [[recovery]]
allows. You are paying several days of being worse at everything, and if
the gift takes you to half your core hit points or fewer you are
[[dying|wounded]] for all of them.

A failed casting costs you the spirit and nothing else. You may try
again, and the clock will have moved on while you did.

**It is difficulty {{ mechanics.raise_the_dead.base_difficulty }} before
the clock is added**, which is beyond most casters and out of reach
entirely for a junior one.

{% book-only %}
### Design note

Every resource in this game recovers overnight except one. Spirit comes
back in full, stamina comes back in full, mastery hit points come back
in full, and core hit points come back at one a night. So a spell whose
only cost is spirit is a spell you can cast every day for ever, and
raising the dead is precisely the thing that must not be an errand.

Charging the caster in core hit points is the only price in the system
that a night does not refund — and it has to be exempt from healing, or
it is not a price at all. A caster who could Cure Wounds the cost back
would be paying nine spirit to raise the dead, which is an errand again
by a longer route. The exemption is not a special case bolted on: what
healing does is close wounds, and nothing wounded you. You gave it away.

It is also the right price in the fiction — your own life for somebody
else's — and it lands on the person making the decision rather than on
the player whose character died, which matters. A rule that returns the
dead diminished punishes the one person at the table who has already had
the worst evening.

The rising difficulty does the pacing. A party that fights its way back
to a fallen friend within the hour has a hard spell to cast; a party
that comes back the next day has an impossible one. That gradient is
worth more than a flat cut-off because it makes *hurrying* the decision
rather than merely *deciding*. The hard limit at
{{ mechanics.raise_the_dead.hours_before_beyond_reach }} hours is there
anyway, so that a Dungeon Master never has to adjudicate a caster
rolling enormously well on a week-old corpse.

Staunch exists because Cure Wounds was doing two jobs and doing the
second one badly. Stopping a death and repairing a body are different
problems, and the first is urgent, cheap and needed at range while the
second is expensive and can wait until the fighting stops. Splitting
them gives a junior caster something decisive to do in the worst round
of a fight, which is exactly when a junior caster otherwise has nothing.
{% endbook-only %}

## The guards

A **guard** is laid on one creature you touch and makes harm land more
lightly on it. Where a blessing makes somebody better at what they do, a
guard makes them harder to stop doing it.

All of them share a chassis:

- **Base difficulty:** {{ mechanics.guard.base_difficulty }}
- **Range:** {{ mechanics.guard.range }}
- **Duration:** {{ mechanics.guard.duration_rounds }} rounds, plus
  {{ mechanics.guard.rounds_per_difficulty }} for each further point of
  difficulty spent on it
- **Strength:** {{ mechanics.guard.protection }}, plus
  {{ mechanics.guard.protection_per_step }} for each further
  {{ mechanics.guard.difficulty_per_step }} points of difficulty, unless
  the spell says otherwise
- **Minimum spirit:** {{ mechanics.guard.minimum_spirit }}

### Bulwark

*{{ mechanics.bulwark.schools }}; {{ mechanics.bulwark.domains }}.*
The target gains {{ mechanics.bulwark.protection }} temporary
**mastery** hit points, plus
{{ mechanics.bulwark.protection_per_step }} for each further
{{ mechanics.bulwark.difficulty_per_step }} points of
difficulty. They behave exactly as mastery hit points do — see
[[hit-points]] — and any that are left vanish when the spell ends.

It cannot grant core hit points. Nothing grants core hit points except
Cure Wounds, which is the point of Cure Wounds.

### Stoneskin

*{{ mechanics.stoneskin.schools }}; {{ mechanics.stoneskin.domains }}.*
The target's damage reduction rises by the guard's strength, exactly as
though their armour were better. It is still bound by the cap in
[[damage]]: however much reduction you pile up, half of every blow gets
through.

### Elemental Guard

*{{ mechanics.elemental_guard.schools }};
{{ mechanics.elemental_guard.domains }}.* Name a damage type as you
cast. Damage of that type is reduced by the guard's strength, which
starts at {{ mechanics.elemental_guard.protection }} and buys its steps
every {{ mechanics.elemental_guard.difficulty_per_step }} points —
cheaper than Stoneskin because it only ever answers one thing.

### Mantle of Warding

*{{ mechanics.mantle_of_warding.schools }};
{{ mechanics.mantle_of_warding.domains }}.* Name a school of magic as
you cast. The target adds the guard's strength to every roll to resist
an effect of that school, per [[conditions]].

### Deathward

*{{ mechanics.deathward.schools }}; {{ mechanics.deathward.domains }}.*
The target adds the guard's strength to resist anything of the death
domain, and reduces damage from it by the same. The one guard that
answers a *subject* rather than a technique or an element, and the
reason a priest of a kindly god is worth having in a tomb.

{% book-only %}
### Design note

The guards are four different answers to the question "protected from
what", and the price falls as the question narrows. Stoneskin answers
everything and is dearest per point; Elemental Guard answers one damage
type and is cheapest; the Mantle and Deathward sit between, each
answering a category. That gradient is the whole family: a caster who
knows what is coming buys the narrow spell and a caster who does not
pays for the wide one.

Bulwark is the odd one and the only one that adds rather than subtracts.
Reduction is capped by [[damage]] at half a blow and therefore has a
ceiling no amount of spirit can lift; temporary hit points have no
ceiling at all, which is why they are mastery hit points and vanish with
the spell. A pool that persisted would be a slow way of buying
permanent hit points, and hit points are bought with advancement points
in this game or not at all.

That both of them exist is deliberate. Reduction is worth most against
many small blows and nothing against one enormous one; a pool of hit
points is the reverse. A guard chosen well is worth about twice a guard
chosen badly, and the caster does not know which they are choosing until
the enemy commits.
{% endbook-only %}

## The blessings

A **blessing** is laid on one creature you touch and improves one thing
about it for a while. They cost no attack roll, allow no resistance —
nobody resists being helped — and they are the only spells in the list
whose target is usually on your own side.

All of them share a chassis:

- **Base difficulty:** {{ mechanics.blessing.base_difficulty }}
- **Range:** {{ mechanics.blessing.range }}
- **Duration:** {{ mechanics.blessing.duration_rounds }} rounds, plus
  {{ mechanics.blessing.rounds_per_difficulty }} for each further point
  of difficulty spent on it
- **Strength:** `+{{ mechanics.blessing.bonus }}`, plus
  {{ mechanics.blessing.bonus_per_step }} for each further
  {{ mechanics.blessing.difficulty_per_step }} points of difficulty
- **Minimum spirit:** {{ mechanics.blessing.minimum_spirit }}

You may bless yourself. Most casters do not, because a round spent
making somebody else better at fighting is a round not spent fighting,
and the arithmetic only works when the somebody else is better at it
than you are. That is the whole shape of a support caster: they are
worth having in a party and poor on their own.

### Blessing of the Blade

*{{ mechanics.blessing_of_the_blade.schools }};
{{ mechanics.blessing_of_the_blade.domains }}.* The target's attack
rolls gain the blessing's strength.

### Warding Blessing

*{{ mechanics.warding_blessing.schools }};
{{ mechanics.warding_blessing.domains }}.* The target's targeting
difficulty rises by the blessing's strength — harder to hit, however
they are defending.

### Heart of the Lion

*{{ mechanics.heart_of_the_lion.schools }};
{{ mechanics.heart_of_the_lion.domains }}.* The target's Resolve rises
by the blessing's strength, which is to say they shrug off the things
[[conditions]] makes Resolve the answer to.

### Keen Edge

*{{ mechanics.keen_edge.schools }}; {{ mechanics.keen_edge.domains }}.*
The target's weapon damage rises by the blessing's strength. It buys its
steps every {{ mechanics.keen_edge.difficulty_per_step }} points rather
than the usual rate, because damage is worth less per point than
accuracy and should cost less.

### Fleetness

*{{ mechanics.fleetness.schools }}; {{ mechanics.fleetness.domains }}.*
The target's movement rises by {{ mechanics.fleetness.bonus }} squares,
plus {{ mechanics.fleetness.bonus_per_step }} for each further
{{ mechanics.fleetness.difficulty_per_step }} points. It grants no extra
action of any kind — see the design note.

### Fortune's Favour

*{{ mechanics.fortunes_favour.schools }};
{{ mechanics.fortunes_favour.domains }}.* The target's critical range
widens by {{ mechanics.fortunes_favour.bonus }}: they roll a critical on
the top two faces rather than the top one, with everything
[[core-resolution]] says about criticals following from there. This is
the one blessing that does not grow with difficulty. Luck either favours
you or it does not.

{% book-only %}
### Design note

None of these grants an action, and that is the line the family will not
cross. An extra action is worth more than any bonus the difficulty scale
can price, because it multiplies everything a character does rather than
adding to one part of it; a spell that hands one out is either the only
buff anybody casts or it is priced so far out of reach that it is
decoration. Fleetness moves you further and lets you do exactly as much
when you get there.

Blessings allow no resistance for the same reason the wards allow none,
arrived at from the opposite side. A ward is terrain and does not care
who you are; a blessing is a gift and the recipient is not arguing. The
resistance rules exist for the case in between, where somebody is doing
something to somebody who would rather they did not.

Making them touch range and single target is what keeps the support
caster a party member rather than a force multiplier who never leaves
the back rank. Group buffs exist, but they belong to somebody standing
in the middle of the group shouting — see the Social and Awareness
powers in [[discipline-powers]], which do that job without magic at all.
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
