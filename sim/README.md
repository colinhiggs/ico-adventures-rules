# sim — measuring what the rules actually do

The build pipeline proves the book, the snippets and the server agree on
every **number**. It proves nothing about whether those numbers make a
good game. This directory does the second job.

```bash
python3 sim/balance.py                 # full report
python3 sim/balance.py --check         # gates only, exit 1 on failure
python3 sim/balance.py --levels 1,5,10,15 --trials 5000
```

Run it from `rules/ico/`, after `python3 tools/build.py ico`.

## Asking "what if this number were different?"

`balance.py` says whether the current ruleset is balanced. `sweep.py`
answers the question that follows — which value a mechanic should take,
and what that choice costs elsewhere. It overrides mechanics **in memory
only**, so a sweep never touches a rule file.

```bash
# one mechanic, several values
python3 sim/sweep.py -m character-creation.max_starting_mastery_hp=15,20,25

# two at once: every combination, as a grid
python3 sim/sweep.py -m damage.damage_per_attack_skill_step=6,8,10 \
                     -m advancement.free_mastery_hp_per_level=2,3,4

# nested keys work
python3 sim/sweep.py -m discipline-powers.power_attack.damage_per_step=1,2
```

The column to watch when matching two curves against each other is
**drift**: mean rounds at the top level divided by mean rounds at the
bottom. `1.0` means a fight at level 15 takes as many rounds as one at
level 1 — hit points and damage growing in step. Above `1.0` the game
grinds as characters advance; below `1.0` it gets swingier.

Drift is what makes this tool worth having. Any single mechanic can be
tuned to fix the level it is measured at and quietly wreck another;
`damage_per_attack_skill_step` and the mastery hit point curve are a
matched pair, and raising either alone makes the game worse.

## Why it lives here and not in the toolset

The toolset in `rpg-master/rules-toolset/` is generic and contains no
game content. This model knows that a blow is `d20 + attack` against a
targeting difficulty and that margin becomes damage — that is Ico's
*logic*, not Ico's *values*, and the toolset's README is explicit that
`mechanics.json` holds data and never logic. So the data stays with the
ruleset, the logic that consumes it sits beside it, and the toolset
stays generic.

## The one rule it inherits

**No game number is written in this code.** Every constant is read from
`build/mechanics.json`, and a missing key raises instead of defaulting —
the same fail-fast contract `tools/rules_runtime.py` gives the server.
Rename a mechanic and the simulator breaks loudly rather than quietly
measuring the wrong game.

That is also why the workflow is *edit a rule file, rebuild, re-run*.
There is no second place to change a number.

## What it reports

- **Character sheets** — what each build actually looks like at a level,
  including points it could not spend. A large "unspent" column means
  the advancement menu has a hole in it.
- **Damage per round** against a standard foe, plain and with the best
  available power.
- **Power economy** — the difficulty each build should declare, what it
  costs, and how many times a fight it can afford. If cost trends to
  zero, the power source has stopped being a resource.
- **Attrition** — damage per round fresh versus with an empty
  reservoir, and the percentage kept. This is what the minor-power tier
  exists to raise: a long adventure should wear a character down, not
  switch them off. The band is 35-85%; the lower bound applies at every
  level, the upper only from level 5, since a junior character has
  barely any reservoir for running dry to matter to.
- **Stance check** — whether blocking is ever better than dodging.
  A stance nobody should ever pick is a dead rule.
- **Duels** — Monte Carlo, every build against every other.
- **Weapon × armour matrix** — expected damage per swing for every
  combination, to catch pairings where a weapon is inert.

## Gates

`--check` runs the report's measurements against the design targets at
the top of `balance.py` and exits non-zero if any fail. They encode the
goals stated in the book's opening chapter:

| Gate | Why |
|---|---|
| `TARGET_ROUNDS` | Fights should be decisive but not a grind |
| `MAX_CONTRIBUTION_SPREAD` | Every build should be worth playing |
| `MIN_DAMAGE_VS_ANY_ARMOUR` | No weapon should be a prop |
| `MIN_POWER_COST` | Powers must not become free with experience |
| `FLOOR_RATIO_BAND` | Empty should mean diminished, never sidelined |
| `MIN_FIELD_BITE_FRACTION` | Area denial has to actually deny |

Contribution is deliberately damage per round **times** rounds survived,
not damage alone: a defensive signature scores zero on a damage-only
measure, which made the most over-powered build in an early run look
like the weakest.

Contribution is `(offence + control) x survival`. **Control** is damage
the enemy never gets to deal because a condition took its round away:
a stun that holds for two rounds is worth two rounds of that creature's
output, and quoting it as damage is the only way a stun and a sword
swing can be compared at all. It is zero for every build that applies
no conditions, which today means every martial build.

**Contribution is still a single-target, melee-range measure.** It
counts damage to one creature and how long the build survives being
stood next to. It does not count clearing six goblins in a round, and
it does not count doing so from thirty metres away without being hit at
all -- read the rank-and-file table alongside it before concluding
anything.

These are targets, not rules. When a gate fails the honest options are
to change the rules or to change the target — but change the target
because the design intent moved, never to make the report quiet.

## Shopping

Builds are not handed their gear; they buy it. An archetype names
disciplines, attributes and a stance -- what the character *is* -- and
the kit is chosen afterwards, on the objective the contribution gate
uses: damage per round times rounds survived.

It shops against a **panel**, not one opponent, and it has to.
Quickness is worth nothing except against a weapon longer than your own
and reach is worth nothing except against a shorter one, so no single
yardstick can price either: one sword-armed opponent makes quickness
look worthless, and one spear-armed opponent makes it look compulsory.
The panel is the standard foe and the same foe carrying a two-handed
sword. Equipping for offence alone puts everybody in no armour, and
equipping for defence alone puts everybody in plate.

This matters beyond tidiness. **Fixed gear quietly flatters any rule
change aimed at gear.** A change that makes full plate a bad idea looks
decisive while the build is still wearing full plate, and gives most of
its gain back the moment it is allowed to put on a chain shirt instead.

Two things are deliberately not shopped for. **Stance** stays in the
archetype, because how a character defends is part of what the build is,
and the stance report exists to ask whether that choice is real -- each
stance does shop separately, since a blocker who cannot buy a shield is
no test of blocking. **The standard foe** keeps its kit pinned, because
everybody shops against it and a standard of comparison that re-equips
in response to what it is being compared with is no standard at all.

The purse is the one number the rules do not supply. Character creation
gives a starting sum and says nothing about what is earned afterwards,
so the model assumes one more starting purse per level -- inventing no
number the rules do not already give. A level 1 character can afford a
sword, a chain shirt and a shield; full plate arrives at level 11. It is
the assumption to argue with first if gear choices look wrong.

Shopping is cheap because what a character carries changes what it deals
only through the **weapon** -- its own armour and shield are read when
it is struck, never when it strikes. Offence is therefore worked out
once per weapon rather than once per kit, which is the difference
between a report that runs in a minute and one that runs in an hour.

The report prints what every build bought, and which weapons nobody
bought. A weapon nobody chooses is dead content the same way a weapon
that cannot hurt anybody is; a weapon *everybody* chooses is the more
expensive problem, because it makes the rest of the table decoration.
The gate is the mirror of `MIN_DAMAGE_VS_ANY_ARMOUR`: that one asks
whether any weapon is useless, this one whether any is redundant.

### Interference, as a lever

Ico does not forbid a caster plate or an acrobat a great axe; it lets
equipment get in the way of what the character is good at, and lets them
decline it themselves. Two optional keys make that measurable, and both
are absent by default, so the model behaves as the book reads until one
is switched on:

- `weapons.size_skill_penalty` -- a map from weapon size to what
  carrying one costs the skills it gets in the way of. It comes off
  defending, whichever way you defend.
- `armour.hampers_casting` -- when true, armour's skill penalty comes
  off spellcasting as well as off dodging.

**A trap worth knowing about**, because the first measurement of the
second lever quietly reported nothing at all. `choose_gear` works
offence out once per weapon, on the reasoning that a character's own
armour is read when it is struck and never when it strikes. Armour that
interferes with casting breaks that reasoning: it changes what a caster
deals. The cache key now widens to include the armour whenever the
interference is switched on and the character can cast. Any further
interference that touches offence has to widen it again, or it will be
priced at zero and look harmless.

## Reach, quickness and free hands

Three rules that exist to give weapon size a second axis, since damage
and accuracy trade along one line and a line has a best point on it.

**Reach** is paid once. Whoever reaches further strikes while the other
closes -- one blow per square of difference -- and after that closing
and withdrawing cancel, so it never pays again. In a duel those blows
are resolved before the first round. **Quickness** is the answer: a
quick weapon inside a longer one strikes first every round, whatever
initiative said, which in practice is worth about one avoided blow over
a fight, because a corpse does not answer. **Free hands** decides how
well a character can do a thing while holding what it is holding:
casting wants
both hands, and each hand short of that is a penalty on the roll rather
than a bar. A quick weapon is stowed and drawn for free and a staff does
not get in the way at all, so neither costs a caster anything.

**The size of that penalty cannot be settled here, and the report should
not pretend otherwise.** Every decision it could influence is already
decided by a much larger margin: against one target a martial build's
swing beats its own best spell by about forty per cent, so a
fighter-mage fights whatever the penalty; against a crowd an area spell
beats swinging by so much that a `spellblade` still casts with a great
axe in hand at a penalty of six; and a pure caster carries a dagger or a
staff, which cost nothing either way. The value is a design choice made
on the scale armour already uses, and what it *costs* is the part worth
measuring -- a level 10 caster loses 12% of its best spell turn to a
one-handed weapon and 21% to a two-handed one.

The chooser prices all three first-order: a reach advantage is extra
swings gained over a fight of typical length, a reach disadvantage is
extra swings suffered, and quickness is one swing avoided. The
alternative was a positionless model pricing two positional rules at
nothing.

Duels resolve them properly, including initiative -- rolled on the
initiative skill, fixed for the fight, and overridden by a quick weapon
inside a longer one. Before this, `a` simply always struck first, which
was a quiet thumb on the scale in every duel the report printed.

Duels also **cast**. A caster's plan is weighed in the same currency the
contribution gate uses, damage plus control, and resolved with the
conditions and persisting fields the crowd loop already understood: a
burn bites at the start of a turn, a stun takes it away, and a burning
combatant may spend the turn putting itself out. Until this was added,
every duel in the report measured a wizard on whatever it happened to be
holding -- which mattered much more once the gear chooser started
handing it a dagger for its free hand.

## The adventuring day

A single fight from full is not the question a dungeon asks. `model.py`
can run a sequence of encounters with recovery between them:

```python
import model as m, balance as b
M = m.Mechanics()
hero = b.build_all(10, M)["duellist"]
hard = [("orc", 4), ("orc", 6), ("orc", 6), ("orc", 8), ("orc", 8)]
m.adventuring_day(hero, M, schedule=hard, tier="breather")
```

It returns, per encounter, the share of the character's fresh offence
they bring to it, the share of their hit points left, and the share of
days they are still standing for it. `tier` is `"breather"`, `"rest"` or
`None`, and reads its fractions from the recovery rule like everything
else.

Offence is looked up from a cache keyed on stamina rather than
recomputed per trial; the difficulty search is far too slow to run
inside the loop, and stamina is what actually varies.

## Conditions and persistence

Conditions are read out of `conditions.md` and resolved the way the book
resolves them: the **declared difficulty** is the number to beat, the
defender rolls Fortitude or Resolve against it, and the margin sets the
duration. Because the difficulty is the target, a caster who wants an
effect to stick buys that the same way they buy damage or area -- which
is also why measuring conditions was worth doing, since the version that
resolved against the roll rewarded declaring the lowest difficulty that
worked and hoping.

What each condition then *does* is read from its own mechanics entry
rather than switched on its name, so a new condition needs no code here
as long as it is described in the same vocabulary -- an entry with
`loses_action` gates the action, one with `attack_penalty` comes off the
roll and off the difficulty of hitting that creature, one with
`movement_fraction` costs the action whenever movement was what the
creature needed, and one with `repeats_damage` bites again each turn.

Halved movement is the one that cannot be resolved literally, because
the model has no positions. `MOVEMENT_GATES_ATTACK` is the share of a
crowd member's rounds in which closing the distance, rather than the
swing, is the binding constraint; slowing therefore costs a creature
`MOVEMENT_GATES_ATTACK x (1 - movement_fraction)` of its actions.

A field stays on the ground. `FIELD_LINGER` is the chance a creature it
caught is still standing in it at the start of its next turn -- the
midpoint between a crowd that must cross the field to reach the caster
and one that simply walks around it. It is the number to argue with
first if fields look wrong.

`FIELD_LINGER` is also what the area-denial test is built on: crossing a
field costs one certain tick plus whatever lingering keeps, and
`MIN_FIELD_BITE_FRACTION` is the share of a rank-and-file creature's hit
points that has to cost before anybody would rather go round. The test
only asks it of builds holding Adept or better in a casting discipline,
and only against the same rank-and-file the swarm gates use. Note what
it does *not* say: a field that deals no damage at all is out of scope
here, since a fog or a tangle denies ground by what it does rather than
by what it deals.

Affordability alone is not a good enough filter for that test. Expected
cost *falls* as a declared difficulty runs away, because the spell
simply stops going off, so `MIN_FIELD_SUCCESS` requires the caster to
land the thing at least half the time before it counts.

## Known limits

- **Damaging spells are modelled; nothing else about magic is.** A
  caster's spells are read from the spell list, priced through the same
  declared-difficulty machinery as any power, and paid for out of
  spirit. Healing and every spell cast for a narrative reason are out of
  scope, and always will be -- there is no way to score "talked the door
  open" against damage per round.
- **Duels are melee-only, so no condition and no field ever appears in
  one.** Conditions reach the analytic path (contribution, damage per
  round, the crowd planner) and the skirmish loop, and nothing else.
  `sweep.py` reports duel rounds, so it cannot see a condition either --
  sweeping one of their rates moves nothing in its table.
- A burn is counted for its full expected duration, as though the target
  lives to take every tick. Nothing here models overkill, for spells or
  for swings, so fire is flattered exactly as much as a great axe is.
  Since a burn now shrinks by half a round at a time, the tail it
  overstates is small.
- Whether a burning creature smothers the flames is a judgement the
  rules leave to the player, so the model makes one: it puts itself out
  when what the fire will still take off it is worth more than the turn.
  A cannier or more reckless opponent would do differently.
- Ranged weapons are still not modelled, only ranged *spells*.
- Fresh-versus-empty is measured at the two extremes. A character plans
  for a sustainable spend across roughly four rounds, so the model never
  burns its whole reservoir in one climactic fight the way a player
  might; builds with a small reservoir therefore look closer to their
  own floor than they would in play.
- Only five combat skills are tracked, so a build's spare points have
  fewer sinks here than in a real character, which slightly inflates
  what lands in mastery hit points and stamina.
- The day model is melee only, like everything else here, so it cannot
  see a spellcaster spending spirit on every spell. The bolts are a
  caster's equivalent of the free minor attack powers, so the same
  mechanism probably protects them — but probably is the honest word.
- **Only two of the six Master signatures are modelled**: Killing Blow,
  which doubles what margin is worth, and Untouchable, which cancels
  armour's dodge penalty. Read the Blow, Command the Room, School
  Mastery and Granted Domain do nothing here, so any build resting on
  one of those is measured without its capstone.
- The `priest` archetype casts from a god rather than a book: it can
  cast only its granted domains, and casts them with the major domain
  bonus, which Full Communion extends to all three. Preparation is NOT
  modelled for wizards -- every build is assumed to have memorised what
  the fight in front of it wants, which is the most generous reading and
  the only one a single-fight model can take.
- The `spellblade` archetype exists to check that the free-hands penalty
  leaves a fighter-mage possible. It does not choose to cast against a
  single target at any penalty, including none, which is a statement
  about the caster gap rather than about the penalty.
- The `paragon` archetype exists to stress-test breadth rather than to
  be a sensible character: it is the only pairing whose *both*
  signatures the model implements, and contribution multiplies offence
  by survival, so a build that raises both at once is the worst case the
  metric can be shown. Read its numbers as a bound, not as a build
  anybody would play.
- **Level 1 duels sit on the floor of `TARGET_ROUNDS` and always have.**
  They average barely above three rounds before any weapon rule is
  applied, so anything that makes anybody easier to hit tips several
  pairings under it at once. When a change fails the round-length gate
  at level 1 and passes or improves it everywhere else, suspect the
  level rather than the change.
- **Protection is scored only where the model can see it.** A pool of
  temporary hit points and a change in damage reduction are both
  measurable, and `report_guards` measures them. Resistance to a damage
  type or to a school is not: nothing here tracks which type or school a
  blow came from, so those two guards are written and unmeasured.
- **Party buffs are not modelled at all, and cannot be: there is no
  party.** Rally, Hold the Line and Call the Shot buff allies, and the
  `commander` archetype exists to hold them, so it appears in the report
  as a duellist that spent five points on nothing. The one blessing
  question a single character CAN answer is whether buffing itself beats
  getting on with the fight, which `report_blessings` asks and
  `MAX_SELF_BLESSING_RATIO` gates.
- **Area denial is not modelled at all, and cannot be.** The wards deal
  no damage and impose their condition on whatever is standing in them,
  so their whole value is positional and this model has no positions.
  They are excluded from the spell search rather than scored at zero,
  which would have been a measurement rather than an omission and would
  have read like one.
- **A caster duels toe to toe, which is the last place it would
  choose.** Its spells reach ten squares and the model has no positions,
  so it cannot back away and make a melee build spend the fight
  closing. Every caster duel in the report is therefore the worst case
  for the caster, and the win rates should be read as a floor rather
  than an estimate.
- **Reach and quickness reach duels and the gear chooser, not the
  skirmish loop.** A crowd closing on one character is exactly where
  reach should matter most, and the crowd model has no positions at all.
- Fights are one-on-one, to the death, on open ground. Party
  composition, terrain, morale and action economy across multiple
  opponents are exactly where the remaining balance risk lives.
- Assumptions the rules do not settle are listed in `ASSUMPTIONS` in
  `model.py` and printed at the end of every full report, so they can be
  argued with rather than discovered.
