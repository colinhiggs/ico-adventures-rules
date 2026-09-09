# Done

Work that is finished, moved out of `TODO.md` so that the list of what
is left stays readable. Nothing here needs doing.

It is kept, rather than deleted with the commit that finished it,
because most of these entries are not announcements that something was
done — they are the reasoning that got there, the measurements taken on
the way, and in several cases a record of what was tried and did not
work. That last kind is the most valuable and the easiest to lose: an
idea that looks obvious will be had again by somebody, and the note
saying it was measured and found wanting is what stops it being built
twice.

Entries keep the headings they had in `TODO.md`, and an entry that
still has something outstanding stayed there rather than coming here,
however much of it was finished.

## The spell list

- **Curing and restorative.** *Done: Mend, Cure Wounds, Cleanse,
  Restoration, and now Staunch.*

## Rules gaps found while doing the above

- **Reviving and raising the dead.** *Done, as Staunch and Raise the
  Dead.* Raise the Dead is the only spell in the game whose cost is not
  refunded by a night's sleep, and the only one with an explicit
  exemption from healing. If a second such spell is ever wanted, that
  exemption needs to become a general rule rather than a note on one
  entry.
- **Casting in Harness asked for Magical, and a war-priest had the
  same problem.** *Closed, by the third option -- the tidiest and the
  largest.* `discipline-list` now names a **casting discipline**: one
  whose skill group contains `spellcasting`, which is Magical and
  Spiritual. Nothing declares the membership separately, so a
  discipline given `spellcasting` becomes one by that fact and there is
  no second list to drift. The power asks for `[martial, casting]`.
  A god also grants its priests between `0` and `3` points of relief
  from armour on the casting roll, as part of its package alongside its
  domains -- so a war god's priest wears mail because of who they serve
  rather than because they trained for it, and the two stack for
  somebody who did both.
  Three things measured that are worth keeping.
  *The grant is monotonic but coarse.* At `0` the priest wears partial
  leather, at `2` studded leather, at `3` a chain shirt and later a
  breastplate. A grant of `1` is indistinguishable from none, because
  the relief is on the casting roll only and the dodge still pays, so
  one point of armour buys one point of dodge penalty and the chooser
  declines. The usable span is really `0`, `2`, `3`.
  *`4` would do nothing.* The heaviest armour a priest will take is a
  breastplate at `-3`, so `3` cancels it outright and a fourth point
  has nothing left to forgive.
  *It does not fix the level 1 skirmisher pairing, whatever it looked
  like at first.* Across the whole `0` to `3` span that duel moves from
  `2.988` rounds to `3.001` against a bound of `3.000` -- thirteen
  thousandths, with only the top of the span clearing, and by one
  thousandth. The gate now passes and should not be trusted to stay
  passing; what is actually short there is the skirmisher's level 1
  damage.
- **The damage ratings were compressed, and it made the block axis
  necessary rather than optional.** *Done.* The ratings looked like a
  little over two to one and were nearer four to one where it counts:
  armour is subtracted from every blow and `damage.md`'s cap holds the
  subtraction to half the raw figure, so a small weapon loses a share
  and a large one loses a fixed amount. Against ap `4` the bare ratings
  at the two ends arrived as `2` and `8`. They now arrive as `3` and
  `6`. Ratings went `5,5,6,7,8,9,12,12` to `6,6,6,7,8,8,10,10`.
  It bought a lot. Round-count failures went from seven to four,
  because the biggest weapons had been ending duels before anybody
  spent anything, and the spellblade's empty-reservoir gate came into
  band as a side effect. Six tables were measured; this one has the
  flattest weapon usage of any of them, four weapons within `11` and
  `9` picks across four levels.
  Two things it did not buy, both worth knowing.
  *Accuracy cannot compress a table.* It was the obvious lever and it
  is the wrong one: a point of accuracy is worth `0.71`-`0.87` of a
  damage point to a small weapon and `1.05`-`1.32` to a large one,
  because its extra hits are worth whatever that weapon deals. Adding
  it to the small end was measured and made an extra pairing end too
  fast. It is an identity axis, not a compression lever.
  *Dead weapons went from two to four* -- battle axe, hand axe, short
  sword and two-handed sword. That is the trade that was accepted going
  in, and mostly it is ties rather than rot: a squeezed table has more
  weapons than rungs. But two of the four are **dominated** rather than
  tied, which is a different thing and is not acceptable on its own
  terms: the battle axe and the sword now share a rating and the sword
  has a point of accuracy on it, and the two-handed sword remains the
  great axe's exact twin.
  There is no room left to fix that with damage, which is the point:
  compressing the ratings removed the slack that was hiding the fact
  that **block is dead**. An axe trades block for damage and a sword
  the other way round, and that trade cannot be priced while a 15gp
  shield erases the weapon's block value entirely. The weapon-block
  entry in `TODO.md` is no longer a nice-to-have.
- **The dead-weapon gate measured the wrong thing.** *Replaced by three
  that measure the right ones.* It fired when a weapon was never
  chosen, which under a compressed table is the normal condition rather
  than a defect: equivalent weapons tie, the chooser takes one, and the
  other reads as dead for ever. Reading the scores instead of the
  winner says the table was in much better shape than the gate implied
  -- the four weapons it called dead sit at `1.000`, `0.96`, `0.95` and
  `0.92` of being somebody's first choice, and the two-handed sword was
  "dead" only because it ties the great axe exactly.
  What replaced it: how much the weapon decides about the character
  (median build's best-to-worst gap, `<= 20%`), the same inside one
  class (`<= 30%`), and whether any weapon is beaten on every axis and
  wins on none. Both spread gates fail on the pre-compression table
  (`28%` and `38%`) and pass on this one (`18%` and `26%`), which is
  what makes them gates rather than thresholds fitted to today.
  One reduction was tried and abandoned, recorded so it is not tried
  again: asking whether a weapon is *somebody's* near-miss saturates.
  With ten varied builds nearly every weapon is one, and it scored the
  old wide table `0.959` against the narrow one's `0.921` -- backwards.
- **The caster's single-target gap.** *Closed by giving spells a damage
  rate from casting skill.* Against the best conventional martial build
  a caster now contributes 1.5x to 1.8x less across levels 5 to 15,
  where it was three to five times; the priest sits mid-table at every
  level and casters still clear a crowd in about half the rounds a
  fighter needs. Contribution spread with the paragon set aside is 2.2x,
  2.5x and 2.4x at levels 5, 10 and 15 -- at or inside the gate.
- **The paragon's lead is not the paragon.** Investigated properly and
  it is neither its disciplines nor its weapon: a duellist given the
  paragon's attributes and told to dodge scores exactly what the paragon
  scores, 478 at level 8 and 732 at level 15, to the point. Athletic
  Adept is worth literally nothing to a blocker — 404 before and 404
  after — because Redouble needs the dodge stance and a blocker's
  targeting difficulty comes from a skill Athletic does not touch.

  Both stances are healthy. Four builds of ten prefer to block, and the
  duellist at dexterity 12 is better blocking (617) than dodging (536),
  while the paragon at dexterity 16 is better dodging (732) than
  blocking (606). Neither is right in general, which is what the design
  note says it wants.

  What the investigation actually turned up is about ATTRIBUTES, and it
  is the more useful finding. Measured from a common 76-point base with
  four points to place, at levels 8 and 15:

      +4 strength, blocking     464   725
      +4 dexterity, dodging     440   656
      +4 strength, dodging      385   630
      +4 constitution, blocking 353   520
      +4 constitution, dodging  343   529

  Two things fall out. **Strength is the best attribute a martial build
  can buy**, because block skill is governed by strength and melee
  attack is too, so one attribute raises offence and defence together
  where dexterity raises only defence. And **constitution is the worst
  by a distance**, because core hit points are a small slice of a total
  pool that mastery hit points dominate, so the attribute that buys them
  buys very little.

  It also means the strongest build is not in the roster at all: a
  strength-heavy blocker beats the paragon on a like-for-like base, so
  the contribution spread is understated rather than overstated.

  Moving block to constitution was measured and does fix the
  double-dip — the spread of the five options narrows from 1.39x to
  1.24x at level 15 — but it makes blocking worse than dodging across
  the board, which risks a stance choice currently in good health. It
  is a real design decision and is not taken.

  Constitution has since been given free mastery hit points, faster
  recovery and quicker healing, and that closed most of it.

- **The strength double-dip is real, worth about ten per cent, and
  should be left alone.** Block skill and melee attack do share an
  attribute, so strength raises offence and defence together. Measured
  across the pairings anybody would actually choose, though, the gap is
  small — at level 15, strength-and-block 100%, constitution-and-dodge
  97%, constitution-and-block 95%, dexterity-and-dodge 91%, a spread of
  1.10x. At level 8 it is 1.11x.

  Three repairs were measured and every one is worse:

  - **Block governed by constitution** widens the spread to 1.56x and
    1.59x. It does not remove the double-dip, it moves it onto the
    attribute that now also grants hit points, recovery and healing.
  - **Block governed by dexterity** gives the tightest spread of raw
    pairings but drops the count of builds that prefer to block from
    four in ten to two: every defensive option would run on one
    attribute, and blocking stops being a real choice.
  - **Finesse extended to medium weapons** keeps all four blockers and
    reads 1.06x at level 15, but 1.20x at level 8 — better at one end
    and worse at the other.

  A ten per cent premium for a coherent build is not a defect. The gate
  that is actually failing fails on the paragon against the spellblade,
  which is a different quarrel entirely.

- **The area spells now say how far away they can be put.** *Done:
  `blast`, `burst`, `field` and `ward` carry `range: 10`, the same
  figure a bolt and a lance already had, and the prose says once that
  an area spell is placed rather than centred on the caster.* What it
  changed is smaller than it looks and worth recording: a caster
  clearing six goblins already did it in one round to one and a half,
  so opening at ten squares instead of two did not make it faster --
  it made it **free**. The evoker, the priest and the spellblade now
  finish untouched, where the spellblade in particular was losing
  `9%` of its hit points. The crowd gate never bound on any of them,
  so nothing moved in `--check`. The contribution spread did not move
  either, and the reason given here was wrong: it is not measured from
  duels. `contributions` is analytic -- `attack_expectation` times
  `expected_offence` -- and the duel loop feeds only `TARGET_ROUNDS`.
  So giving duels an opening distance could never have moved it. What
  moved it was giving `contributions` one; see the caster entry in
  `TODO.md`.

## Simulator gaps

- **The simulator was thirteen minutes, then under three, and is
  now under two.**
  *Done, and recorded here because the next person to profile it should
  know where the easy wins have already gone.* Values and the figures
  derived from them are cached on the `Mechanics` instance; a blow is
  split into the part the margin changes and the part it does not; a
  combatant is copied by hand rather than by `deepcopy`; `duel` asks
  what each side will do and what a round of it is worth off one search
  rather than two; and the spell search no longer rebuilds a spell's
  definition seven million times a level. Every one of those was
  checked by dumping duels, skirmishes, contributions and offence
  figures on a fixed seed and diffing -- byte-identical, every time.
  Two lessons worth keeping. Guesses about where the time goes were
  wrong twice: sharing the duel planning was estimated at a third and
  measured at five per cent, because planning happens once a duel and
  the trials happen three thousand times. And this machine varies by
  twenty-five per cent between batches, so a timing is only worth
  quoting when the two versions were run back to back.
  *Then parallelised, and it is now a hundred seconds.* A profile put
  56% of `--check` in gear shopping and 41% in duels, and both are
  piles of pieces that say nothing to each other, so both go to a pool
  of workers. Eight of them take `--check` from `4m36s` to `1m43s` on
  a sixteen-core machine; sixteen workers reach `1m36s`, which is why
  the default is eight rather than everything. `--jobs` sets it and
  `ICO_SIM_JOBS` sets it for a machine.
  The property to protect is that `--jobs` changes the speed and never
  a number, and `sim/README.md` carries the two-line diff that checks
  it. Shopping is safe for free, being arithmetic over the die's faces
  rather than rolls of it. Duels are Monte Carlo and are safe because
  each one now seeds itself from its own name rather than drawing from
  one stream in sequence -- which also retires the oldest wart in this
  file, that the ORDER of the duels was part of the answer and adding
  an archetype re-rolled every pairing after it. It cost a one-off
  renumbering when it landed: the count stayed at nine, but
  `L10 duellist vs berserker` left the failing set and
  `L1 berserker vs commander` joined it, both of them pairings sitting
  within a tenth of the three-round bound.
