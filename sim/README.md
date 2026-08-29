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

Contribution is deliberately damage per round **times** rounds survived,
not damage alone: a defensive signature scores zero on a damage-only
measure, which made the most over-powered build in an early run look
like the weakest.

These are targets, not rules. When a gate fails the honest options are
to change the rules or to change the target — but change the target
because the design intent moved, never to make the report quiet.

## Known limits

- The model tracks melee only. Ranged attacks, spells and the
  Magical/Spiritual disciplines are not simulated, so those builds are
  absent from every comparison. The bolt spells are minor powers on the
  same chassis as Precise Strike, so the melee numbers are the best
  available proxy for them, but they are a proxy.
- Fresh-versus-empty is measured at the two extremes. A character plans
  for a sustainable spend across roughly four rounds, so the model never
  burns its whole reservoir in one climactic fight the way a player
  might; builds with a small reservoir therefore look closer to their
  own floor than they would in play.
- Only five combat skills are tracked, so a build's spare points have
  fewer sinks here than in a real character, which slightly inflates
  what lands in mastery hit points and stamina.
- Fights are one-on-one, to the death, on open ground. Party
  composition, terrain, morale and action economy across multiple
  opponents are exactly where the remaining balance risk lives.
- Assumptions the rules do not settle are listed in `ASSUMPTIONS` in
  `model.py` and printed at the end of every full report, so they can be
  argued with rather than discovered.
