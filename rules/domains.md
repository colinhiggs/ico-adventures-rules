---
id: domains
title: Domains and the Gods
tags: [magic, character, reference]
summary: >
  Every spell belongs to a domain. A god grants a priest one major
  domain, cast with a bonus, and one or two minor ones cast without.
mechanics:
  domains: [healing, war, nature, magic, death, trickery, love,
            knowledge, light, darkness, storm, sea, forge, travel,
            luck, justice]
  list_is_open: true
  major_domains_granted: 1
  minor_domains_granted_least: 1
  minor_domains_granted_most: 2
  major_domain_bonus: 3
  spiritual_casts_only_granted_domains: true
  armour_relief_least: 0
  armour_relief_most: 3
---

A **domain** is what a spell is *about*, as opposed to the school, which
is how it is built — see [[spellcasting]]. Fire and lightning belong to
war; frost belongs to nature; mending a wound belongs to healing.

A spell may belong to several. A fog bank is a thing of the wild and a
thing of the sea, and a priest of either god may call one; a shroud of
darkness answers to two quite different sorts of god for two quite
different reasons. Where a domain decides access or a bonus, **one match
is enough** — a spell that is partly your god's business is your god's
business.

## The domains

{{ mechanics.domains }}

The list is open. A Dungeon Master inventing a god is not restricted to
these, and a new domain costs nothing but a word: what it means is
settled by which spells get tagged with it.

Every domain on the list now has at least one spell in it, so any god a
Dungeon Master invents from these has a priest who can do something.
Some are much better served than others — war and healing have a great
deal, forge and luck have very little — and a god granting three thin
domains grants a thin priest.

## What a god grants

A character who takes the Spiritual discipline serves something, and
that something decides what they can do. Every god grants:

- **{{ mechanics.major_domains_granted }} major domain.** Its spells are
  cast with `+{{ mechanics.major_domain_bonus }}` on the spellcasting
  roll. This is the god's own strength lending itself to the work.
- **{{ mechanics.minor_domains_granted_least }} or
  {{ mechanics.minor_domains_granted_most }} minor domains.** Their
  spells are available, and are cast with no bonus at all.

- **Between {{ mechanics.armour_relief_least }} and
  {{ mechanics.armour_relief_most }} points of relief from armour**, on
  the spellcasting roll only. [[armour]] charges its skill penalty
  against casting as well as against dodging, and this many points of
  that are forgiven for a priest of this god. A god of the battlefield
  grants the full {{ mechanics.armour_relief_most }}; a god of libraries
  and quiet grants {{ mechanics.armour_relief_least }}, and its priests
  cast in a robe like anybody else.

The choice is made when the character is made and does not change,
because it is not the character's choice — it is who they serve.

A spiritual caster may cast **any** spell in their granted domains, with
no preparation of any kind, and **no** spell outside them. See
[[spell-preparation]].

## Armour, and what a god thinks of it

The relief is a **grant and not a power**. It costs nothing, it cannot
be bought, and a priest who wants more of it than their god gives has
only one route: train for it, and take Casting in Harness from
[[discipline-powers]] like anybody else who fights and casts. The two
stack — what your god forgives and what your drill-yard forgives are
different debts — and both come off the same penalty, so neither can
turn it into a bonus.

Nor does either reach far enough to make heavy plate free. The most a
god grants is {{ mechanics.armour_relief_most }} points and the heaviest
armour costs a good deal more than that, so a priest in full plate is
still a priest paying for it. That is the intended shape: the grant
makes mail and a breastplate *reasonable* for a war-priest, which they
were not before, and leaves plate a decision with a price on it.

## What a relief of nothing means

A god granting {{ mechanics.armour_relief_least }} is not a defective
god, and the number is not a measure of how good a god is to serve. It
says what this one is *about*. A god of scholarship gives its priests
the run of the knowledge domain and expects them to stand at the back;
a god of battle gives them mail and expects them not to. Both are
playable and neither is a mistake.

This is the first thing beyond domains that varies from god to god, and
it will not be the last. What a religion grants and what it costs is a
balance in its own right, and a pantheon whose gods are all generous is
as flat as one whose gods are all the same.

## Two priests of different gods

A god of the harvest might grant nature as its major domain with healing
and luck beneath it. A god of the battlefield might grant war, with
healing and death. Both are priests, both cast, and they share exactly
one domain between them — which is what makes a pantheon worth having
rather than a single interchangeable clergy.

## Example

Sela serves a goddess of mercy: healing major, with love and light as
minor domains.

She casts Cure Wounds, a healing spell, at
`+{{ mechanics.major_domain_bonus }}` — her goddess is at her shoulder
for that one. She casts anything in love or light at no bonus, but
casts it freely and without preparing it.

She cannot cast a Flame Lance at all. It belongs to war, her goddess has
nothing to do with war, and no amount of spirit will buy what has not
been granted.

Her fellow traveller, a wizard, may cast the Flame Lance and may not
cast anything without having memorised it that morning. Neither of them
can do the other's job.

{% book-only %}
## Design note

Domains do two things at once here, and that is deliberate. For a wizard
a domain is only a label, useful for saying what a spell is about. For a
priest it is the whole of their access: it decides what they can cast
before any question of skill or spirit arises.

That asymmetry is what makes the two kinds of caster feel different
without needing two sets of rules. A wizard's limit is preparation —
they can learn anything and can only hold so much at once. A priest's
limit is identity — they hold everything they were given, all the time,
and cannot reach past it however clever they are. One is a problem of
capacity and the other is a problem of scope, and a player picks which
problem they would rather have.

The major domain bonus is deliberately modest. It is not a signature and
it is not earned; it is the baseline of having a god, held by every
priest from the first level. Something large enough to reshape the
character would leave nothing for the Spiritual signature to be, and a
priest of a war god should be a priest who is *good at* war spells, not
a priest who casts them for free.

Capping the grant at three domains, one of them favoured, is what stops
a priest simply being a wizard who never has to prepare. Three domains
is a narrower list than a wizard's spell book and a far narrower one
than the spell list; the compensation is that all of it is available all
of the time.
{% endbook-only %}
