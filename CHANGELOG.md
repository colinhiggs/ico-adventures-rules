# Changelog

What changed between versions of the Ico rules, and what an adventure
built against an earlier one has to do about it. The three tiers and
what they oblige are defined in `VERSIONING.md`.

Every MAJOR entry must name its renames and removals old-to-new. That
list is the whole reason this file exists: without it, "revisit your
adventure" is a search, and with it, it is a substitution.

## 2.0.0

**Two mechanics keys went away.** Both are in the substitution table
below. No document id was renamed or removed, so every `[[link]]` and
every `snippets.json` key an adventure holds still resolves; if your
adventure names neither key, nothing here breaks it and you need only
read the new reach rules to see whether an encounter you built around a
polearm still plays the way you meant.

### Renames and removals, old to new

| Gone | Use instead |
|---|---|
| `reach.opening_attacks_per_square` | `reach.free_attacks_per_round` — but read the note below, because the meaning changed and not only the name |
| `movement.large_weapon_reach_bonus` | the weapon's own `reach_bonus`, e.g. `weapons.great_axe.reach_bonus` |

`opening_attacks_per_square` is not a rename. It said a reach advantage
was worth one unanswered blow **per square** of advantage, collected
once as the fight was joined. `free_attacks_per_round` says an approach
across the band is answered once **per round**, however wide the band
is. Both happen to be `1`, and for every weapon in this ruleset the two
produced the same number, because no weapon imposes a band more than one
square wide. A substitution is safe here. It would not have been if
anything reached further.

### Reach is a band of ground, and there is a choice in it

The old rule resolved itself: the longer weapon landed a blow as the
shorter one closed, and nobody decided anything. Reach is now the strip
of ground inside the longer reach and outside the shorter — where one
combatant can strike and the other cannot — and crossing it is
**answered**.

The fighter with the longer weapon spends their **reaction** on one of
two answers, never both:

- **strike** whoever is crossing, one free attack; or
- **give ground**, opening the band in front of them again.

Giving ground costs `step_back_move_cost_multiplier` squares of move for
every square surrendered, because it is walking backwards, and it needs
somewhere to walk to. That makes it the narrower option: you would have
to be twice as quick as your opponent to hold them off with it against
anyone who has movement in hand. What it is for is the opponent who has
just spent their move crossing — one square is then enough to leave them
in the band with no attack at all.

An approach is answered `free_attacks_per_round` time however wide the
band. A reach advantage makes an approach expensive; it can never make
one impossible.

### Long weapons are bad in tight spaces

New, and the counterweight to the above. Take your reach, subtract
`tight_space_radius_offset`, and count the blocked squares within that
distance — walls, pillars, a closed door. Each is
`tight_space_penalty_per_square` on your attack rolls, to a maximum of
`tight_space_penalty_max`.

Other creatures never block. A press of bodies is what a spear is for; a
doorway is not. A weapon with no reach beyond the ordinary counts no
squares and never suffers this.

A one-square corridor blocks six of the eight squares around you, which
is past the cap, so a polearm in a dungeon swings at
`tight_space_penalty_max`. **This is the rule most likely to change an
encounter you have already written**, and it changes it in the players'
favour or against it depending on who is holding the long weapon.

### Reach now lives in the weapon

`movement.large_weapon_reach_bonus` gave every size L weapon an extra
square from a rule in another document, while the staff declared its own
`reach_bonus` in its table entry. The two-handed sword and the great axe
now declare theirs the same way, and the size-keyed rule is gone.

Nothing about any weapon's reach changed — the great axe reached `2`
squares before and reaches `2` now. What changed is that the Reach
column of the weapon tables used to print a dash for weapons that
reach, and now prints the figure.

`movement` keeps `reach_by_size`, which is the reach a **creature** has
from being large, and really is a general rule.

### Also

`turn-order` gains a paragraph: reactions are not only ever powers, and
this is the first rule outside a power to spend one. A fighter with a
long weapon is choosing between their reach and their Riposte every
round.

### What is not measured

None of this has been through `sim/`. The free attack needs positions
and the tight-space penalty needs walls, and the balance model has
neither — every fight it runs is one-on-one on open ground, which is a
listed assumption rather than an oversight. `balance.py --check` reports
the same six failures with the same numbers as 1.3.0, which is the model
being unable to see the change rather than the change being small.

Read the reach rules as a design judgement, and expect them to be a buff
to long weapons: a fighter who spends their move backing off and their
reaction striking collects a free attack most rounds. What that is
bought with is the move, the reaction that Riposte and Deflect come out
of, and `tight_space_penalty_max` indoors. `TODO.md` carries it.

## 1.3.0

Two names were added to one creature and nothing was renamed, removed or
moved. An adventure using goblins keeps working and should re-read its
goblin encounters, because the creature is more dangerous than it was.

### The goblin carries a shortbow

`goblin` gains `ranged_weapon: shortbow` beside its existing `weapon`,
and `skills.attack_ranged`, set to the rank `attack_melee` already had.
No existing value changed: `attack_melee`, the attributes, the hit point
pools, the armour and `challenge_level` are all exactly what they were.

A stat block now has two weapon keys rather than one. `weapon` still
holds a melee weapon and is still a string, so anything reading
`goblin.weapon` reads what it always read; `ranged_weapon` is a new
optional key that a creature without one simply does not carry.

### What it does to an encounter

The goblin is much better with the bow than with the blade — an attack
bonus of `+4` at range against `+1` in melee — but that gap is dexterity
`14` against strength `8`, not a retune. Its damage is unchanged, since
a shortbow and a short sword have the same damage rating.

The practical difference is that a band can now hurt a party while the
party crosses the ground to it, where before it could only hurt them
after. Against that, the bow takes both hands: a goblin that is reached
either spends its action drawing its blade or goes on shooting at the
engaged penalty in `ranged-weapons`. Closing with goblins is now
something a party does on purpose.

`challenge_level` is unchanged at `1` and remains an author's estimate.
It cannot be more than that until `sim/` can load a creature, which
`TODO.md` still carries.

### Removed from the prose, not from the data

The **Goblin archer** variant is gone. It said to swap the short sword
for a bow and move the skill points across, which no longer names a
difference from the creature above it. No id or mechanics key went with
it; the variants were always prose.

## 1.2.1

No mechanic value changed and no rule document was touched. An adventure
needs to do nothing.

`VERSIONING.md` no longer claims that the correct bump for a change is
computable from the build outputs alone. A diff of two builds gives a
floor and not an answer: it sees the data half of a rule document and
not the prose half, which is where a value's meaning lives, and the
single-source rule pushes a change towards reusing an existing key
rather than declaring a new one -- so the better the prose behaves, the
less a diff can see.

The previous release is the worked example, and is named as one. The
tool that section has always wanted is unaffected, with its job stated
more precisely: it can refuse a release numbered below the floor, and it
can never raise one.

## 1.2.0

No name was added, renamed or removed, and `mechanics.json` is
byte-identical to 1.1.0. An adventure needs to do nothing to keep
working, but an encounter that assumed a caster could bolt at any
distance for free should be re-read.

### Long range costs a caster what it costs an archer

`spell-properties` has always given an attack-roll spell a short range
and a long range, and has never said what being at the long one costs.
It does now: a spell aimed past its short range takes the same penalty
`ranged-weapons` charges anyone shooting at that distance.

It is charged as **accuracy**, not as difficulty. `using-powers` has
one casting roll answering two questions — the declared difficulty
first, the target's targeting difficulty second — and an accuracy
penalty applies only to the second. So a spell thrown a long way is
harder to place and no harder to cast: a caster who misjudges the
distance loses the bolt, not the spirit.

The caster keeps the out they already had. Range extends by a square
per point of added difficulty, so a caster may spend spirit to bring
the target inside short range instead of spending accuracy. An archer
at the same distance has only the second option.

No new mechanics key was added for this. `spell-properties`
interpolates `ranged-weapons.long_range_penalty` rather than declaring
a second copy of it, which is why the data outputs did not move.

### Why this is MINOR and not PATCH

`VERSIONING.md` defines the tiers by what an adventure author has to
do, and observes that the correct tier is therefore computable from the
build outputs. This release is a counterexample worth recording: every
name and every value is exactly what it was in 1.1.0, and the game
still moved, because the change is entirely in the prose that tells you
what an existing value applies to. A caster's effective accuracy at
long range is lower than it was.

PATCH promises an adventure that nothing it was tuned against has
changed, and that promise would not have been true here.

## 1.1.0

Names were added and nothing was renamed or removed. An adventure
written against any 1.0.x still resolves every name it uses, and needs
to do nothing unless it wants the new material.

### Ranged weapons exist

A new rule document, `ranged-weapons`, carrying the common set: sling,
shortbow, longbow, light crossbow, heavy crossbow and javelin, with
accuracy, damage, range in squares, hands, reload and cost. Arrows,
bolts and sling stones are listed with a quantity and a price.

It is a separate document from `weapons` rather than more rows in it. A
ranged weapon has no size, and size on the melee table decides three
different things — finesse, reach and block value — none of which
describes a bow, so a ranged entry states the hands it takes outright.

The rules that come with them reuse what the game already had rather
than adding machinery:

- **Range** is the listed number as short range, doubled for long range
  by the same multiplier `spell-properties` already applies to a spell,
  with a penalty to shoot into it and no shot at all beyond it.
- **Reloading** is paid out of the turn `turn-order` gives you. A light
  crossbow reloads with the move, so it shoots every round from a spot
  it cannot leave; a heavy crossbow reloads with the action, so it
  shoots every other round.
- **A longbow names a draw strength**, and a character short of it
  shoots at a penalty for each point they are short rather than being
  forbidden the bow.
- **An archer with an enemy inside their reach** shoots at a penalty,
  and so does anyone shooting at a target inside an ally's reach.
- **A shield's block value stops a shot; a weapon's does not.** This is
  the only place a shot is resolved differently from a swing.

### Throwing

`weapons.dagger` and `weapons.hand_axe` each gain a `thrown_range`.
Thrown, a weapon keeps its own accuracy and damage and is aimed with
Attack (ranged) like anything else on the new page. No other value in
`weapons` moved.

### What this does not carry

None of these numbers has been through `sim/`. The simulator has no
positions, so it cannot represent the one thing an archer is buying, and
it reads only `weapons` for the gear a character shops from — which is
the second reason the bows live elsewhere. They are a first pass priced
by eye against the melee table, and `TODO.md` records that. The balance
gates are unchanged: the same six failures with the same numbers, either
side of this release.

No creature in the bestiary has been given a ranged weapon.

## 1.0.5

No mechanic value changed. An adventure written against any earlier
1.0.x needs to do nothing.

Four `related` lists in `snippets.json` lost one entry each: `damage`
no longer lists `weapons`, `discipline-powers` no longer lists
`spell-list`, `hitting` no longer lists `discipline-powers`, and
`spell-preparation` no longer lists `disciplines`. Every one of those
links appears only inside a `{% book-only %}` design note, which the
snippet does not carry — so the snippet was offering an onward link to
a document its own text never mentions.

The toolset was building that list once per document, over the whole
source, and then writing it into every output regardless of what each
output actually contains. It now builds the list per output, from the
links still standing after that output's audience rules have been
applied, so an entry's `related` agrees with its `html`.

Here that is a tidiness fix. It was found somewhere it is not: the
adventures project uses the same mechanism with `{% gm-only %}`, where
the equivalent list was handing a printed player handout the name of a
document the handout exists to withhold, with a link to a page that was
not in the file. The fix is in the toolset rather than in these rules,
and this release is only the rebuild that carries it.

`book.html` and `mechanics.json` are unchanged apart from the version
stamp.

## 1.0.4

No mechanic value changed. An adventure written against any earlier
1.0.x needs to do nothing.

`SHARING.md` points at `WORKING.md` in the `rpg-master` repository, the
practical half of the pair: which working copy to open, why the rules
and the adventures are separate Claude projects by default and when to
deliberately combine them, and step-by-step procedures for the common
jobs — adding a creature from the adventures side among them.

The gate note in `README.md` and `sim/README.md` still says "as of
1.0.3" and is meant to. That date is when the six failures were last
measured, not the version the sentence ships in, and nothing since has
touched a value the gates read. Re-dating it every release would turn a
statement about evidence into a statement about the version number.

## 1.0.3

No mechanic value changed. An adventure written against any earlier
1.0.x needs to do nothing.

The README now says that `sim/balance.py --check` does not pass. It
reports six failures and exits 1, and it has done for some time: the
paragon's lead at level 10, three pairings outside the round band, the
spellblade's floor with an empty reservoir, and the dagger and hand axe
that no build chooses. Every one is an open tuning question `TODO.md`
already carries. The README had listed `--check` beside the build and
the test suite as though it were a check that passes, which left
somebody running it for the first time to wonder what they had broken.

`sim/README.md` says the same in its own terms, and adds what a failing
check is still good for: run it either side of a change to a rule
value, and the same six failures with the same numbers means the change
was neutral.

Nothing about the gates themselves moved. A target is changed because
the design intent moved, never to make the report quiet.

## 1.0.2

No mechanic value changed. An adventure written against 1.0.0 or 1.0.1
needs to do nothing.

`sim/balance.py` and `sim/sweep.py` take `--path`, naming the ruleset
to measure the same way `tools/build.py` does. Without it they read the
`build/` beside themselves, which is right almost always, since the
simulator ships inside the ruleset it measures; with it they can
measure a ruleset that is not this one — an older pinned version
against the current one, or a tag worked out into a temporary clone to
find when a gate started failing. `sweep.py` now prints the file it
read, as `balance.py` already did.

## 1.0.1

No mechanic value changed. An adventure written against 1.0.0 needs to
do nothing.

`SHARING.md` is new: who may write to which part of this repository,
now that the projects built on these rules hold it as a git submodule
and write to it. The short of it is that `rules/bestiary/` is open to
anyone — writing an adventure creates monsters — and that a change
moving a mechanic value comes from here, because the value is measured
against the whole system rather than against the encounter that
noticed it. It also covers where a new creature belongs, how to add
one, and the submodule habits that keep two writers apart.

`README.md` gained a pointer to it.

Worth knowing on the toolset side, though it is not part of this
version: `tools/test_rules.py` now takes `--path`, so a project holding
the rules and the toolset as sibling submodules can run the ruleset's
suite where it lies instead of only building it.

## 1.0.0

The first tagged version. Nothing to compare it against — this entry
records what an adventure written today can rely on.

The ruleset is complete enough to play: character creation, the six
attributes and six disciplines, the two hit point pools, combat with the
block and dodge stances, skills, powers and advancement, the equipment
tables, and magic — schools, domains, spell preparation, and a spell
list of forty-three spells built on eight shared chassis, covering the
damaging families, the guards, blessings and wards, and the restorative
and revival spells.

Two things an adventure should know are deliberately unfinished:

- **The bestiary has one creature in it.** The stat block format is
  settled (`rules/bestiary/`, `kind: creature`) and the goblin
  demonstrates it, but the bestiary is expected to grow largely from
  the adventures that need creatures.
- **`challenge_level` in a stat block is an author's estimate.** The
  simulator cannot yet load a creature and measure it against the
  archetype panel, so that number has not been checked by anything.
  See `TODO.md`.

Ranged weapons are not statted at all, and there are no positions in the
simulator, so anything an adventure does at a distance is unmeasured.
