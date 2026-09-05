# Versioning the Ico rules

These rules are used by things that are not these rules: adventures,
campaigns, characters, and eventually the game server. Each of them
needs to be able to say which rules it was built against, and to find
out later whether that answer still holds.

This document is the convention that makes that possible. It is short
on purpose — a versioning scheme nobody can remember is a versioning
scheme nobody follows.

## The version

A single line in `VERSION` at the root of this repository, in
`MAJOR.MINOR.PATCH` form, and an annotated git tag `vMAJOR.MINOR.PATCH`
on the commit that sets it.

The file is the source and the tag is its mirror. That way round because
the build outputs travel to their consumers without this repository
attached: an adventure may hold nothing but a copy of `mechanics.json`,
and asking it to run `git describe` to find out what it is holding would
be a dependency on something it does not have.

Tags live on `main` only, and are annotated (`git tag -a`) rather than
lightweight so that each one carries its own date, author and message.

Versioning starts at `1.0.0`. Semantic versioning reserves `0.x` for
"anything may break without warning", which is exactly the signal this
convention exists to send and so cannot be thrown away at the start. The
rules being unfinished is not a reason to leave them unversioned; a
ruleset actually in play at a table is precisely the thing that needs a
version.

## What the three numbers mean

They are defined by what the author of an adventure has to **do** about
the change, not by how large the change is.

- **MAJOR — a name went away.** A document `id` renamed or removed, a
  mechanics key renamed or removed, or a subsystem changed shape:
  stances, the two hit point pools, the way domains grant a priest
  access. An adventure that referred to the old name now refers to
  nothing, or to something else. It must be revisited by hand.

- **MINOR — a name was added, or a value changed.** New spells,
  creatures, weapons, domains or rule documents; a balance retune; a
  spell's difficulty or a weapon's cost moving. Nothing an adventure
  names has gone away, so nothing breaks, but an encounter tuned
  against the old numbers may want re-checking, and there may be new
  material worth using.

- **PATCH — no mechanic value changed at all.** Prose, examples, design
  notes, typos, `TODO.md`, a rebuild of `build/` with no data change.
  An adventure needs to do nothing.

The deliberate call is that **a balance retune is MINOR and not MAJOR**.
The simulator moves numbers often, and if every pass bumped the major
version the number would stop carrying any information within a month.
What MAJOR is worth having for is the failure that actually costs
somebody an evening: a stat block naming a rule or a key that is no
longer there.

The definitions are phrased over names and values on purpose, so that
they can be checked mechanically rather than argued about. Between two
builds, the document ids are the keys of `snippets.json` and the
mechanics keys and values are in `mechanics.json`, which is everything
needed to work out which of the three a change was. See the note at the
end.

## Where the version appears

`tools/build.py` reads `VERSION` and stamps all three build outputs:

- `mechanics.json` — a top-level `_version`, beside `_generated`.
- `snippets.json` — a top-level `_version`, beside the documents.
- `book.html` — printed under the title, so a Dungeon Master reading
  the book can see which rules they are reading without going anywhere
  near a repository.

The convention that makes the second of those safe applies to all three:
**a top-level key beginning with `_` is metadata about the build, not a
document.** No document id can collide with one, because an id is a
filename stem. The alternative — wrapping the snippets in an envelope
the way `mechanics.json` wraps its rules — would change the shape every
existing consumer already reads, to no benefit.

A ruleset with no `VERSION` file is simply unversioned, and its outputs
carry no `_version` at all. That is the right answer for a scratch or
demonstration ruleset, and the toolset stays generic: nothing in it
knows about Ico.

## Cutting a release

One commit, then one tag:

1. Bump `VERSION` to the new number.
2. Add the section to `CHANGELOG.md`, naming any renames or removals
   old-to-new — that table is what turns "must be revisited" into a
   mechanical fix for whoever has to do it.
3. Rebuild: `python3 tools/build.py ico` from the toolset directory, so
   `build/` carries the new stamp.
4. Commit all three together as `Release X.Y.Z`.
5. `git tag -a vX.Y.Z -m "..."`.

Committing the bump, the changelog and the rebuilt outputs together is
what keeps the tag and the stamp inseparable: there is no commit at
which the tag says one thing and `mechanics.json` says another.

Tag on each merge to `main` that lands a coherent piece of work, rather
than saving it up. Versions cost nothing and a running counter is more
useful to somebody trying to place an adventure in time than a sparse
one. A missed release can always be tagged retroactively.

## Who tags

The rules project. One authority, so there is never a race over who owns
the next number.

This matters because the bestiary is written to from both sides: the
adventures project adds creatures as its adventures need them. Those
arrive as branches to be merged here, and each one is a MINOR bump like
any other addition.

## What an adventure records

One field in its frontmatter:

```yaml
rules_version: "1.0.0"
```

It means **last checked against**, not "originally written against", and
is updated whenever somebody re-checks the adventure. The version it was
first written against is already in that adventure's own git history, so
a second field would only duplicate what git knows.

## Not yet done

Because the tiers are defined over names and values, the correct bump
for any change is computable from the build outputs alone. A tool that
diffed two of them could classify a change as MAJOR, MINOR or PATCH and
refuse a release numbered lower than the diff warrants, which would turn
this document from a discipline into a check. It is worth having and it
is not written; the convention stands without it.
