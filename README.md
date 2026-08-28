# ico

Empty on purpose — this is where the ico system's rules will live once
you start writing them.

## Getting started

Give this directory the same shape as `../demo/` (a working example
worth looking at before starting):

```
rules/ico/
  rules/           one .md file per rule — mechanics + prose, see below
  book/
    rulebook.md     the root document — includes chapters in order
    ch-*.md         chapters — intro prose + {% include %} of rules
```

A minimal first rule, `rules/ico/rules/example.md`:

```markdown
---
id: example
title: Example Rule
summary: One or two sentences — this is the in-game tooltip text.
mechanics:
  some_value: 3
---

Prose goes here. Interpolate values instead of restating them:
{{ mechanics.some_value }}, not the literal number.
```

And `rules/ico/book/rulebook.md`, the minimum needed for a buildable
(if tiny) book:

```markdown
---
id: rulebook
title: ico
kind: section
summary: The ico rules.
---

{% include example %}
```

## Build it

From `rules-toolset/`:

```bash
python3 tools/build.py ico
python3 tools/test_rules.py ico
```

Until there's at least a `rulebook.md`, both commands fail with a clear
message rather than silently doing nothing — see
`../../rules-toolset/README.md` for what those messages look like and
why that's the intended behaviour, not a bug to work around.

See `../demo/` for a complete worked example (six rules, three
chapters, cross-links, mechanics interpolation) and
`../../rules-toolset/README.md` for the full format reference.
