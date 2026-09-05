# ico

The Ico adventure system: a d20 system with no classes, built from the
`Ico Adventure System.md` draft and extended with a discipline-based
specialisation and advancement layer.

```
rules/ico/
  rules/     one .md per rule — mechanics in frontmatter, prose interpolates them
  book/      rulebook.md (the root) plus ch-*.md chapters that include the rules
  sim/       the balance simulator — see sim/README.md
  build/     generated; never edit
  VERSION    the released version — see VERSIONING.md and CHANGELOG.md
```

This directory is its own git repository and is developed independently
of the game. It is a **plug-in**: to play it, the whole directory is
dropped into the game's installed ruleset folder at
`rpg-master/rpg-master/rules/`. Until then it lives in the outer
`rules/` working directory, and the build tool finds it in either place.

## Build and check

From `rpg-master/rpg-master/rules-toolset/`:

```bash
python3 tools/build.py ico
python3 tools/test_rules.py ico
```

From `rules/ico/`, after building:

```bash
python3 sim/balance.py --check
```

The first two prove the book, the snippets and the server data agree.
The third measures whether the resulting game is balanced. Both matter
and they catch entirely different things.

## What is and is not here

Present: the core roll, characters and attributes, the two hit point
pools, character creation and priorities, combat, skills and focus,
disciplines and advancement, powers, equipment, and spellcasting.

Deliberately partial: the skill list has around thirty skills with no
governing attribute assigned yet; ranged weapons are unstatted; and the
bestiary has one creature in it, which is enough to fix the stat block
format and no more.

Not here: the class and levelling system from the original draft. It was
mid-revamp and internally inconsistent, and disciplines replace it.

## Versioning

The rules are versioned so that anything built on them — an adventure
above all — can record which version it was checked against, and find
out later whether that still holds. `VERSION` holds the number, an
annotated git tag mirrors it, and the build stamps it into all three
outputs.

The three tiers mean what an adventure author has to *do* about a
change rather than how large it was, which is the whole of the
convention worth remembering:

- **MAJOR** — a name went away; an adventure must be revisited.
- **MINOR** — a name was added or a value moved; nothing breaks.
- **PATCH** — no mechanic value changed at all.

`VERSIONING.md` has the full convention and how to cut a release.

## House style for a rule document

Every rule keeps three kinds of writing visibly separate, in this order,
so a reader looking something up never has to pick the rule out of a
discussion about why it was designed that way:

1. **The mechanic itself** — what a player actually does. This is the
   main text and is not interleaved with commentary.
2. **`## Example`** — a worked example of the rule in use, always under
   that heading. Every rule has one.
3. **`## Design note`** — rationale, history, and why a decision went
   the way it did. Always last, always under that heading, and always
   wrapped in `{% book-only %}` … `{% endbook-only %}` so it reaches the
   printed book but never an in-game tooltip.

When writing an example, put its invented arithmetic — die rolls, a
sample character's skill values — inside `inline code spans`. The
linter strips those before checking, so they will not be mistaken for a
game constant; a literal number in prose that matches one of the
document's own `mechanics:` values is a hard build error. Where an
example refers to a number that genuinely *is* a mechanic, interpolate
it with `{{ mechanics.key }}` like anywhere else. Example text is not
exempt from the single-source rule.

The examples use a small recurring cast — Ashri the fighter, Dune the
skirmisher, Sela the priest, and Bramm as the opposition — so the book
reads as one document rather than twenty unrelated ones.

## The rule that holds it together

A value exists in exactly one place. Prose never restates a number that
lives in `mechanics:` — it interpolates it, the linter fails the build
otherwise, and the simulator reads the same file the server does. See
`../../rpg-master/rules-toolset/README.md` for the full format
reference.
