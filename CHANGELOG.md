# Changelog

What changed between versions of the Ico rules, and what an adventure
built against an earlier one has to do about it. The three tiers and
what they oblige are defined in `VERSIONING.md`.

Every MAJOR entry must name its renames and removals old-to-new. That
list is the whole reason this file exists: without it, "revisit your
adventure" is a search, and with it, it is a substitution.

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
