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
```

## Build and check

From `rules-toolset/`:

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
governing attribute assigned yet; ranged weapons are unstatted; the
spell list has two spells; and the Magical and Spiritual disciplines
lean on spells that mostly do not exist yet.

Not here: the class and levelling system from the original draft. It was
mid-revamp and internally inconsistent, and disciplines replace it.

## The rule that holds it together

A value exists in exactly one place. Prose never restates a number that
lives in `mechanics:` — it interpolates it, the linter fails the build
otherwise, and the simulator reads the same file the server does. See
`../../rules-toolset/README.md` for the full format reference.
