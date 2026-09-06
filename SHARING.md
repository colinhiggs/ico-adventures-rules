# Sharing the Ico rules

Who may change what in this repository, and how a project built on top
of it makes a change without treading on anybody else.

This repository has more than one writer. It is developed in its own
working directory alongside the toolset, and it is also checked out as
a git submodule by the projects built on it — the adventures project
first, the game server and character tools later. Those projects are
not read-only consumers. Writing an adventure creates monsters, and
monsters belong in the bestiary, so the ruleset has to be writeable
from outside.

That is deliberate, and it is the reason this document exists. Two
projects writing to one repository is only safe if they write to
different parts of it, agree on which changes need whose consent, and
never hand-edit the parts that are generated.

Its companion is `SHARING.md` in the `rpg-master` repository, which
says the same kind of thing about the toolset. `VERSIONING.md` says
what the version numbers mean; this document says who is allowed to
move them.

## The write surface

| Area | Who writes it | Why |
|---|---|---|
| `rules/bestiary/` | anyone | Adventures make monsters. This is the shared area, open by design. |
| `rules/*.md` | the rules project | Every value here is measured by `sim/`, and moving one moves numbers under every adventure at once. |
| `book/` | the rules project | Chapter order and the include tree are a whole-book property. |
| `sim/` | the rules project | It is the thing that decides whether a change to the rules is allowed. |
| `VERSION`, `CHANGELOG.md`, tags | the rules project | One authority over the number — see `VERSIONING.md`. |
| `TODO.md` | anyone | The place to park a question rather than answer it in passing. |
| `build/` | nobody | Generated. See below. |

The line those rows draw is the same one `VERSIONING.md` already draws,
so there is only one idea to remember:

**A change that moves no mechanic value may come from anywhere. A
change that moves one comes from the rules project.**

So a typo, a clearer sentence, a better worked example or a missing
design note is welcome from any project and in any file, including the
core rules. A difficulty, a cost, a die size or a bonus is not, however
obviously wrong it looks from inside an adventure — it is measured, and
the measurement lives here.

## Adding a creature

The common case, and the one the shared area exists for.

1. Take an up-to-date `main`, and branch. From a consumer project's
   submodule, name the branch for that project: `adv/bestiary-ogre`
   rather than `bestiary-ogre`, so that two projects pushing to this
   one remote can always tell whose branch is whose.
2. Write `rules/bestiary/<slug>.md`, `kind: creature`, following
   `rules/bestiary/goblin.md`. It is the format-fixing example and is
   meant to be copied.
3. Check the name first. Document ids are one flat namespace across the
   whole ruleset — a creature called `guard` collides with a rule
   document called `guard`, and the build fails. The ids in use are the
   keys of `build/snippets.json`.
4. Rebuild, so `build/` moves with the source in the same commit. See
   "Building from a consuming project" below for the command.
5. `python3 tools/test_rules.py ico` must pass — or, from a consuming
   project's layout, the same command with `--path`. See below.

A new creature is a MINOR change: it adds a name and takes nothing
away. It does not need a release of its own — the rules project tags
when it next merges to `main`.

One thing to know while writing it: `challenge_level` is an author's
estimate. The simulator cannot yet load a creature and measure it
against the archetype panel, so nothing has checked that number. Pitch
it against the goblin, and expect it to be revised when the loader
lands.

## What belongs here, and what stays in the adventure

Ask whether another adventure, written by somebody else, could use the
creature without knowing your plot.

- **Yes — it belongs in `rules/bestiary/`.** An ogre, a wolf pack, a
  temple guard. Generic, reusable, part of the world's furniture.
- **Not yet, or not quite** — it belongs in the consuming project's own
  shared area, such as the adventures repository's
  `_shared/creatures/`. That is the staging area: reused across that
  project's own adventures, but bound to its setting, or simply not
  settled enough to be worth everybody's attention.
- **No — it stays in the adventure.** A named villain, a unique
  construct, anything whose stat block is a plot point. Those are NPCs
  in the adventure that owns them, and promoting them here would put
  somebody else's story in the rulebook.

The middle case is the one to be honest about. A creature earns a place
here by being wanted twice.

## When an adventure needs a rule changed

Do not change the value, and do not work around it locally either — a
local override is a fork of the mechanic that nothing will ever
reconcile.

Write it in `TODO.md` instead, naming the adventure that motivated it
and what the adventure needed. A rule value is a whole-system property:
it is chosen by `sim/balance.py` against every archetype at once, and
the case for moving it is made there, not in the one encounter that
noticed. Real pressure from a real adventure is the best evidence that
a rule is wrong, which is exactly why it is worth recording rather than
absorbing.

## Working in a submodule checkout

A consuming project holds this repository as a submodule, which makes
three ordinary mistakes easy.

**Know which repository you are in.** A commit made inside the
submodule does not appear in the outer project's history. The outer
project records only which commit this one is pinned to.

**Never commit on a detached HEAD.** `git submodule update` leaves the
checkout detached, and a commit made there belongs to no branch and is
lost by the next update. Check out a branch first:

```bash
git -C rules-ico checkout main && git -C rules-ico pull
```

**Push this repository before pushing the pin.** If the outer project
pushes a pin to a commit that has not been pushed here, every other
checkout breaks: it is told to fetch a commit the remote does not have.
Push here first, or let git do both in the right order with
`git push --recurse-submodules=on-demand`.

Then bump the pin deliberately, in a commit of its own, whose message
names the version it moved to.

## Building from a consuming project

The toolset looks a ruleset up by name in two directories relative to
itself, neither of which exists in a project that holds both
repositories as sibling submodules. Build by path instead:

```bash
cd rpg-master/rules-toolset
python3 tools/build.py --path ../../rules-ico
python3 tools/test_rules.py --path ../../rules-ico
```

Both print the directory's name back at you, so from that layout they
say `rules-ico` rather than `ico`. Only the label differs; the outputs
are identical either way — the same sources build byte-for-byte
identical files from either checkout, which is what makes the conflict
recipe below work.

## Conflicts in `build/`

`build/` is tracked on purpose — the server and the adventures read it
without this repository attached — and being generated and tracked at
once makes it the place where two branches most often collide. It is
also the easiest conflict there is, because the outputs are
reproducible: the same sources build byte-for-byte identical files.

Never merge them by hand, and never read the conflict. Take either
side to clear the markers, rebuild, and commit the result:

```bash
git checkout --ours -- build/
python3 tools/build.py ico      # from the toolset directory
git add build/
```

The rebuild overwrites whatever you took, so which side you take does
not matter. What matters is that the merged *sources* are what produced
the committed outputs.

The same reasoning is why `build/` is never hand-edited even when the
edit would be trivially correct: the next rebuild silently reverts it,
and until then the committed data disagrees with the rules it claims to
come from.

## What a consuming project can rely on

- The three build outputs, in the shapes described in `VERSIONING.md` —
  `book.html`, `snippets.json`, `mechanics.json`.
- A top-level key beginning with `_` is metadata about the build, not a
  document. `_version` holds the ruleset version.
- The version tiers: MAJOR means a name went away and adventures must be
  revisited, MINOR means something was added or a value moved, PATCH
  means no mechanic value changed at all.
- Every MAJOR entry in `CHANGELOG.md` names its renames and removals
  old-to-new, so revisiting is a substitution rather than a search.

An adventure records `rules_version:` in its frontmatter, meaning *last
checked against*. Nothing here reads that field; it is a note to the
next person who has to decide whether the adventure still holds.
