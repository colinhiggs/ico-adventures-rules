# balance.py -- what the Ico rules actually do, measured.
#
# The book proves the prose and the server agree on every NUMBER. It
# proves nothing about whether those numbers make a good game. This does
# the second job: it reads the same build/mechanics.json the server
# reads, plays the rules out, and reports where they misbehave.
#
# Usage, from rules/ico/:
#   python3 sim/balance.py              full report
#   python3 sim/balance.py --check      gates only; exit 1 if any fail
#   python3 sim/balance.py --levels 1,5,10,15
#
# Change a rule file, rebuild, re-run. The gates at the bottom are
# design TARGETS, not rules -- edit them when the intent changes, and
# treat a failure as a question rather than a verdict.

import argparse
import copy
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import model as m
import parallel

# --- design targets -------------------------------------------------
# These encode the goals in ch-overview: a fight should be decisive but
# not a grind, no build should be strictly better, and no weapon should
# be inert against any armour.
# The base every duel's own seed is derived from -- see
# parallel.duel_seed. Set from --seed in main(); the default matters
# because sweep.py and the tests reach these functions without going
# through the command line.
SEED = 12345

TARGET_ROUNDS = (3.0, 12.0)      # rounds for an even duel
MAX_CONTRIBUTION_SPREAD = 2.5    # best archetype / worst, offence x survival
MIN_DAMAGE_VS_ANY_ARMOUR = 1.0   # expected damage per swing, level 5+

# How much the weapon in your hand may decide about your character. The
# median build's gap between its best weapon and its worst, as a
# fraction of its best. Some gap is the point -- a weapon that changed
# nothing would not be worth choosing -- but past a certain width the
# choice stops being yours and starts being arithmetic's.
#
# The median rather than the worst case, deliberately. One or two builds
# have a legitimately large gap: an evoker's staff is not really
# competing with the axes, it is a piece of casting equipment that can
# also hit people. Gating on the worst case would be gating on those.
MAX_WEAPON_SPREAD = 0.20

# The same question inside one class, where it is asked harder. Two
# weapons that cost the same hands and sit in the same weight are meant
# to be a choice about the character rather than about the numbers, so
# the gap between the best and worst of them -- as a share of the best
# IN THAT CLASS, not of the whole table -- should be small enough that
# a player can pick on taste and not be wrong.
MAX_CLASS_SPREAD = 0.30
MIN_POWER_COST = 1.0             # expected stamina per use, at any level
SURVIVAL_CLAMP_ROUNDS = 25.0     # beyond this a fight is a stalemate
# What a character can still do on the fourth fight of a long day, as a
# fraction of what they manage fresh. Too low and an empty reservoir
# means sitting the fight out; too high and the reservoir never mattered.
FLOOR_RATIO_BAND = (0.35, 0.85)
RESERVOIR_MATTERS_FROM_LEVEL = 5
# A mid-level character should be able to deal with rank-and-file
# opposition briskly and without it costing much.
SWARM_SIZE = 6
SWARM_MOOK = "goblin"
TRIALS_SWARM = 1200
SWARM_ROUNDS_BY_LEVEL_10 = 4.0
SWARM_HP_COST_BY_LEVEL_10 = 0.25
# A damaging field is area denial, and denial only denies if crossing
# costs something worth avoiding. One tick must take at least this much
# of a rank-and-file creature's hit points through its armour -- a field
# nobody minds walking through is not doing the job the spell exists for.
MIN_FIELD_BITE_FRACTION = 0.25
# A field the caster cannot land is not a field. Only spells they make
# at least this often count towards the test.
MIN_FIELD_SUCCESS = 0.5
# The smallest area worth calling denial: anything narrower is a blast
# that happens to linger.
MIN_FIELD_SQUARES = 13
# Healing must not outrun harm, or a fight with a healer in it does not
# end. The comparison is against what ONE comparable attacker deals per
# round, not against what the healer's own build happens to take, which
# depends far too much on the armour it is standing in.
MAX_HEAL_FRACTION_OF_ATTACK = 0.5
# Opening every fight with a self-buff should not be the right play. A
# blessing is for making somebody ELSE formidable; if it beats a
# character's own best round spent on itself, the spell has become a
# compulsory opener and the choice has gone out of the game.
MAX_SELF_BLESSING_RATIO = 1.0
# The same question for the guards. Damage prevented and damage dealt
# are quoted in one currency for the same reason control is: a point the
# enemy never takes off you is worth a point you never had to put back.
MAX_SELF_GUARD_RATIO = 1.0

# Every minor power is a weaker twin of a standard one. If a minor twin
# ever matches its counterpart at the same difficulty, the standard
# version is dead: same effect, lower floor. The pairing is a design
# fact rather than something derivable, so it is written down here.
MINOR_TWINS = {
    "quick_attack": "fast_attack",
    "precise_strike": "power_attack",
    "sidestep": "redouble",
    "weak_point": "find_the_gap",
}

# Each build lists its disciplines in PRIORITY order with the grade it
# is aiming at. At low level it holds whatever the budget reached, so
# the same build can be followed from level 1 upward.
ARCHETYPES = {
    "duellist": {
        "disciplines": [("martial", "master"), ("athletic", "initiate")],
        "attributes": {"strength": 16, "dexterity": 12, "constitution": 14,
                       "intelligence": 10, "willpower": 14, "charisma": 14},
        "stance": "block",
    },
    "berserker": {
        "disciplines": [("martial", "adept"), ("athletic", "adept")],
        "attributes": {"strength": 18, "dexterity": 12, "constitution": 16,
                       "intelligence": 8, "willpower": 12, "charisma": 14},
        "stance": "dodge",
    },
    "skirmisher": {
        "disciplines": [("athletic", "master"), ("martial", "initiate")],
        "attributes": {"strength": 12, "dexterity": 18, "constitution": 12,
                       "intelligence": 12, "willpower": 12, "charisma": 14},
        "stance": "dodge",
    },
    "sentinel": {
        "disciplines": [("martial", "adept"), ("awareness", "adept")],
        "attributes": {"strength": 16, "dexterity": 10, "constitution": 16,
                       "intelligence": 10, "willpower": 14, "charisma": 14},
        "stance": "block",
    },
    "evoker": {
        "disciplines": [("magical", "master"), ("awareness", "initiate")],
        "attributes": {"strength": 10, "dexterity": 12, "constitution": 12,
                       "intelligence": 16, "willpower": 16, "charisma": 14},
        "stance": "dodge", "casts": True,
        # A caster buys none of the melee skills; spellcasting is the
        # only one that pays them back every round.
        "skill_priority": ["spellcasting", "attack_ranged", "dodge", "spot"],
    },
    # The breadth stress test: the only pairing whose BOTH signatures
    # this model implements, and the sharpest one in the game -- Killing
    # Blow doubles what margin is worth, Untouchable cancels armour's
    # dodge penalty. Contribution is offence times survival, so this
    # build multiplies on both halves of the metric at once, and it
    # wears the heaviest armour in the game while dodging in it.
    # Attribute total is 80, as every archetype here has.
    "paragon": {
        "disciplines": [("martial", "master"), ("athletic", "master")],
        "attributes": {"strength": 16, "dexterity": 16, "constitution": 12,
                       "intelligence": 8, "willpower": 14, "charisma": 14},
        "stance": "dodge",
    },
    # A commander: a real fighter with a dip into Social, spending some
    # of its actions on other people's rolls. NOTHING it bought that dip
    # for can be scored here -- Rally and Hold the Line buff allies and
    # there are no allies -- so it appears in the report as a duellist
    # that paid five points for nothing. That is the measurement being
    # wrong, not the build.
    "commander": {
        "disciplines": [("martial", "master"), ("social", "initiate")],
        "attributes": {"strength": 16, "dexterity": 12, "constitution": 14,
                       "intelligence": 10, "willpower": 12, "charisma": 16},
        "stance": "block",
    },
    # A priest: spells come from a god rather than a book, so the build
    # casts only what it was granted and casts its major domain with the
    # god's favour. War is the domain with combat spells in it today.
    "priest": {
        "disciplines": [("spiritual", "master"), ("martial", "initiate")],
        "attributes": {"strength": 12, "dexterity": 12, "constitution": 14,
                       "intelligence": 10, "willpower": 18, "charisma": 14},
        "stance": "dodge", "casts": True,
        "major_domain": "war", "minor_domains": ("healing", "nature"),
        "armour_relief": 3,
        "skill_priority": ["spellcasting", "dodge", "attack_melee", "spot"],
    },
    # The build the free-hands penalty exists to permit: fights and
    # casts, and is second-rate at both by choice. If it never picks a
    # real weapon the penalty is too steep; if a pure caster starts
    # picking one, it is too shallow.
    "spellblade": {
        "disciplines": [("martial", "adept"), ("magical", "adept")],
        "attributes": {"strength": 14, "dexterity": 12, "constitution": 14,
                       "intelligence": 14, "willpower": 12, "charisma": 14},
        "stance": "dodge", "casts": True,
        "skill_priority": ["attack_melee", "spellcasting", "dodge", "spot"],
    },
    "generalist": {
        "disciplines": [("martial", "initiate"), ("athletic", "initiate"),
                        ("awareness", "initiate"), ("spiritual", "initiate")],
        "attributes": {"strength": 13, "dexterity": 13, "constitution": 14,
                       "intelligence": 13, "willpower": 13, "charisma": 14},
        "stance": "dodge",
    },
}

# The yardstick every build is measured against, so the numbers are
# comparable across builds and levels.
# The one build whose kit stays pinned. Everybody else shops against it,
# so it has to be the same opponent whatever anybody buys -- and a
# standard of comparison that re-equips itself in response to what it is
# being compared with is no standard at all.
STANDARD_FOE = {
    "disciplines": [("martial", "initiate"), ("athletic", "initiate")],
    "attributes": {"strength": 14, "dexterity": 14, "constitution": 14,
                   "intelligence": 10, "willpower": 12, "charisma": 12},
    "weapon": "sword", "armour": "scale_mail", "shield": None,
    "stance": "dodge",
}


# The armour grant from domains.md is a span, not a value: a god gives
# its priests somewhere between nothing and full relief from armour on
# the casting roll. One priest can only ever sit at one point on that
# span, so these two sit at the others.
#
# They are kept OUT of ARCHETYPES deliberately. They differ from the
# priest in one number and in nothing else, so in the panel they would
# be one build voting three times -- which is not a small thing: with
# all three in, the median build's weapon spread read 0.238 against the
# 0.180 the same ruleset gives with them out, and a gate calibrated on
# the panel duly failed. That was the panel changing shape, not the
# rules changing behaviour.
#
# They are also given the SAME domains as the priest, because only
# damaging spells are modelled and a healing god's priest therefore
# scores a third of a war god's -- a fact about what the simulator can
# see rather than about the god. Domain held still, grant moving, so
# the difference between the three is the grant's doing.
ARMOUR_PANEL = {
    "temple_priest": dict(ARCHETYPES["priest"], armour_relief=2),
    "ascetic": dict(ARCHETYPES["priest"], armour_relief=0),
}


def report_armour_grants(level, chars, M):
    """What a god's opinion of armour is worth to its priests."""
    hr("What a god grants against armour, at level %d" % level)
    print("%-14s %-7s %-16s %-8s %s"
          % ("priest of", "grant", "wears", "casting", "contribution"))
    panel = shopping_panel(level, M)
    builds = {"priest": chars["priest"]}
    for name, spec in ARMOUR_PANEL.items():
        built = m.build_character(name, spec, level, M, shopping_foe=panel)
        if built is not None:
            builds[name] = built
    scored = contributions(builds, level, M)
    for name, c in builds.items():
        print("%-14s %-7d %-16s %-8d %.0f"
              % (name, c.armour_relief, c.armour.name,
                 c.casting_bonus(M), scored.get(name, 0.0)))


# The panel a build shops against. Quickness is worth nothing except
# against a weapon longer than your own and reach is worth nothing
# except against a shorter one, so a single opponent cannot price
# either: one sword-armed yardstick makes quickness look worthless, and
# one spear-armed yardstick makes it look compulsory.
REACH_FOE = dict(STANDARD_FOE, weapon="two_handed_sword")


def standard_foe(level, M):
    return m.build_character("standard", STANDARD_FOE, level, M)


def shopping_panel(level, M):
    return [m.build_character("standard", STANDARD_FOE, level, M),
            m.build_character("reachy", REACH_FOE, level, M)]


def hr(title):
    print("\n" + title)
    print("-" * len(title))


def _shop(M, task):
    """One archetype, built and sent shopping. Top-level and taking its
    own `Mechanics` so that it runs identically in a worker process and
    in this one."""
    level, name = task
    panel = shopping_panel(level, M)
    return name, m.build_character(name, ARCHETYPES[name], level, M,
                                   shopping_foe=panel)


def build_all(level, M, pool=None):
    """Build every archetype, each of them shopping for its own kit
    against the standard foe of its level.

    This is the expensive half of a run -- a profile of `--check` put
    56% of its time here, because every build weighs a few hundred kits
    against the panel -- and every archetype's shopping is independent
    of every other's, so it is handed to `pool`.

    It is also pure arithmetic: `choose_gear` enumerates the faces of
    the die rather than rolling any, so nothing here touches the random
    stream and the answer is identical however many workers there are.

    Each worker rebuilds the panel for itself. That looks wasteful and
    is not: the panel's two opponents carry pinned gear, so building one
    does no shopping at all."""
    tasks = [(level, name) for name in ARCHETYPES]
    if pool is None:
        built = [_shop(M, task) for task in tasks]
    else:
        built = pool.map(_shop, tasks)
    return {name: char for name, char in built if char is not None}


def report_sheets(level, chars, M):
    hr("Character sheets at level %d" % level)
    print("%-12s %-5s %-5s %-5s %-5s %-6s %-6s %-6s %s"
          % ("build", "atk", "dodge", "block", "stam", "mhp", "chp",
             "disc", "unspent points"))
    for name, c in chars.items():
        print("%-12s %-5d %-5d %-5d %-5d %-6d %-6d %-6d %d"
              % (name, c.skill("attack_melee", M), c.skill("dodge", M),
                 c.skill("block", M), c.stamina, c.mhp, c.chp,
                 c.spent["disciplines"], c.spent["unspent"]))

    hr("What each build bought, on %dgp (level %d)"
       % (m.gear_budget(level, M), level))
    print("%-12s %-18s %-16s %-14s %s"
          % ("build", "weapon", "armour", "shield", "spent"))
    for name, c in chars.items():
        spend = (c.weapon.cost_gp + c.armour.cost_gp
                 + (c.shield.cost_gp if c.shield else 0))
        print("%-12s %-18s %-16s %-14s %dgp"
              % (name, c.weapon.name, c.armour.name,
                 c.shield.name if c.shield else "-", spend))

    # Letting builds shop is only worth doing if the answers are read.
    # A weapon nobody buys is dead content the same way a weapon that
    # cannot hurt anybody is, and one that EVERYBODY buys is the more
    # expensive problem: it means the rest of the table is decoration.
    taken = [c.weapon.name for c in chars.values()]
    unbought = [w for w in m.weapon_keys(M) if w not in taken]
    if unbought:
        print("not chosen by anybody: " + ", ".join(unbought))
    if len(set(taken)) == 1:
        print("every build chose the same weapon (%s)" % taken[0])


# Every axis a weapon can be better on, and which direction is better.
# A weapon beaten on all of them and beating on none is a mistake in the
# table; a weapon merely NOT CHOSEN is usually just a tie, and telling
# those two apart is the whole reason this exists.
WEAPON_AXES = (
    ("damage", 1), ("accuracy", 1), ("block_ap", 1), ("reach_bonus", 1),
    ("thrown_range", 1), ("cost_gp", -1),
    ("quick", 1), ("aids_spellcasting", 1), ("unwieldy", -1),
)
SIZE_ORDER = {"S": 0, "M": 1, "L": 2}


def _axis(M, key, field):
    entry = M.get("weapons", key)
    value = entry.get(field, 0)
    return float(value) if not isinstance(value, bool) else float(value)


def dominated_weapons(M):
    """Weapons with nothing whatever to offer over some other weapon.

    Being smaller counts as an advantage in its own right, because size
    buys finesse and a free hand, and being cheaper counts too. So this
    only fires on a weapon that is beaten or matched on every axis there
    is and wins on none -- which no amount of play or taste can rescue,
    and which is a different complaint from a weapon that simply loses a
    close race."""
    keys = weapon_keys_sorted(M)
    out = []
    for loser in keys:
        for winner in keys:
            if winner == loser:
                continue
            better_anywhere = False
            beaten_everywhere = True
            for field, direction in WEAPON_AXES:
                a = _axis(M, loser, field) * direction
                b = _axis(M, winner, field) * direction
                if a > b:
                    beaten_everywhere = False
                    break
                if b > a:
                    better_anywhere = True
            if not beaten_everywhere:
                continue
            a = -SIZE_ORDER.get(str(M.get("weapons", loser, "size")), 1)
            b = -SIZE_ORDER.get(str(M.get("weapons", winner, "size")), 1)
            if a > b:
                continue
            if b > a:
                better_anywhere = True
            if better_anywhere:
                out.append((loser, winner))
                break
    return out


def weapon_keys_sorted(M):
    return sorted(m.weapon_keys(M))


# A weapon's class, taken from the size the rules already give it
# rather than from a new mechanic: S is the light one-handed group that
# finesse reaches, M the one-handed rest, L the two-handed pair. The
# question the class gate asks is the one a player asks -- "of the
# weapons I could reasonably carry, does it matter much which?" -- and
# that comparison is only fair within a group that costs the same
# hands.
WEAPON_CLASS_NAMES = {"S": "light", "M": "one-handed", "L": "two-handed"}


def weapon_class(M, key):
    return WEAPON_CLASS_NAMES.get(str(M.get("weapons", key, "size")), "other")


def weapon_spreads(chars):
    """For each build, how much better its best weapon is than its worst,
    as a share of its best.

    This is the number the old dead-weapon gate was groping for. It says
    how much of a character the weapon decides -- zero would mean the
    choice is pure decoration, and one would mean the character is
    whatever it is holding."""
    out = []
    for name, c in chars.items():
        values = c.weapon_values
        if len(values) < 2:
            continue
        top = max(values.values())
        if top <= 0:
            continue
        out.append((1.0 - min(values.values()) / top, c.level, name))
    return out


def class_weapon_spreads(chars, M):
    """The same, inside one class, as a share of the best weapon IN THAT
    CLASS.

    In that class matters. Measured against the whole table's best, the
    figure moves whenever the top of the table moves, and a change that
    narrowed every class would still read as though the classes had
    widened."""
    out = []
    for name, c in chars.items():
        values = c.weapon_values
        if len(values) < 2:
            continue
        for size, label in WEAPON_CLASS_NAMES.items():
            group = [v for k, v in values.items()
                     if str(M.get("weapons", k, "size")) == size]
            if len(group) < 2 or max(group) <= 0:
                continue
            out.append(((max(group) - min(group)) / max(group),
                        c.level, name, label))
    return out


def weapon_utility(chars):
    """How close each weapon comes to being the right answer, for the
    build that likes it most.

    `choose_gear` scores every weapon for every build and then keeps the
    winner. Reading only the winner turns a continuous quantity into a
    yes or no: a weapon `2%` behind the best and a weapon `40%` behind
    both come out as "not chosen", which says the table is broken in
    both cases and is wrong in the first. This keeps the quantity.

    Each build's scores are divided by its own best, because the builds
    are not on the same scale -- a paragon out-scores a priest at
    everything, and dividing lets the two of them vote on WEAPONS rather
    than on who is stronger. What comes back for a weapon is then the
    best of those relative scores across all builds, which is the right
    reduction: a weapon exists to suit somebody. A dagger that is `94%`
    for a duellist and `60%` for a berserker is doing its job. Only a
    weapon that is nobody's near-miss is really weak."""
    out = {}
    for c in chars.values():
        values = c.weapon_values
        if not values:
            continue
        top = max(values.values())
        if top <= 0:
            continue
        for key, value in values.items():
            share = value / top
            if share > out.get(key, 0.0):
                out[key] = share
    return out


def report_weapon_utility(level, chars, M):
    hr("What each weapon is worth at level %d" % level)
    utility = weapon_utility(chars)
    if not utility:
        return utility
    # Who likes it most, for reading alongside the number.
    champion = {}
    for name, c in chars.items():
        if not c.weapon_values:
            continue
        top = max(c.weapon_values.values())
        for key, value in c.weapon_values.items():
            share = value / top
            if share >= utility.get(key, 0.0) - 1e-9:
                champion.setdefault(key, name)
    print("%-18s %-12s %-8s %s"
          % ("weapon", "class", "utility", "best for"))
    for key in sorted(utility, key=lambda k: -utility[k]):
        print("%-18s %-12s %-8.3f %s"
              % (key, weapon_class(M, key), utility[key],
                 champion.get(key, "-")))
    for size in ("S", "M", "L"):
        group = [k for k in utility if str(M.get("weapons", k, "size")) == size]
        if len(group) < 2:
            continue
        lo = min(utility[k] for k in group)
        hi = max(utility[k] for k in group)
        print("  %-12s spread %.3f (%.3f-%.3f) across %s"
              % (WEAPON_CLASS_NAMES[size], hi - lo, lo, hi,
                 ", ".join(sorted(group))))
    return utility


def report_weapon_matrix(level, chars, M):
    hr("Expected damage per swing, by weapon and armour (level %d)" % level)
    armours = m.armour_keys(M)
    print("%-18s %s" % ("weapon", " ".join("%6s" % a[:6] for a in armours)))
    worst = []
    for wkey in m.weapon_keys(M):
        row = []
        for akey in armours:
            a = m.build_character("target", dict(
                STANDARD_FOE, armour=akey, stance="dodge"), level, M)
            atk = m.build_character("atk", dict(
                ARCHETYPES["duellist"], weapon=wkey), level, M)
            damage, _ = m.attack_expectation(atk, a, M)
            row.append(damage)
            worst.append((damage, wkey, akey))
        print("%-18s %s" % (wkey, " ".join("%6.1f" % d for d in row)))
    return worst


def report_stances(level, chars, M):
    hr("Stance check: is blocking ever the right choice? (level %d)" % level)
    attacker = chars["berserker"] if "berserker" in chars else list(chars.values())[0]
    print("%-12s %-14s %-14s %s" % ("defender", "dmg taken/dodge", "dmg taken/block", "better"))
    panel = shopping_panel(level, M)
    for name, spec in ARCHETYPES.items():
        # Each stance shops for itself: a blocker who cannot buy a shield
        # is not a fair test of blocking.
        d_dodge = m.build_character(name, dict(spec, stance="dodge"), level,
                                    M, shopping_foe=panel)
        d_block = m.build_character(name, dict(spec, stance="block"), level,
                                    M, shopping_foe=panel)
        if d_dodge is None or d_block is None:
            continue
        dd, _ = m.attack_expectation(attacker, d_dodge, M)
        db, _ = m.attack_expectation(attacker, d_block, M)
        better = "dodge" if dd <= db else "block"
        print("%-12s %-14.2f %-14.2f %s" % (name, dd, db, better))


def report_swarm(level, chars, M):
    """One character against a crowd of rank and file.

    Damage per creature was never the problem -- a goblin dies to one
    solid blow -- so this measures whether a build can REACH them all
    before being surrounded, and what clearing them costs."""
    hr("Rank and file at level %d -- one character against %d goblins"
       % (level, SWARM_SIZE))
    print("%-12s %-8s %-7s %-9s %-9s %s"
          % ("build", "rounds", "wins", "hp lost", "empty", "plan"))
    goblin = m.mook("goblin", M)
    for name, c in chars.items():
        rounds, win, lost = m.skirmish(c, "goblin", SWARM_SIZE, M, trials=TRIALS_SWARM)
        drained = copy.deepcopy(c)
        drained.stamina = 0
        e_rounds, e_win, _ = m.skirmish(drained, "goblin", SWARM_SIZE, M,
                                        trials=TRIALS_SWARM)
        plan = m._swarm_plan(c, goblin, M)
        if not plan:
            label = "plain attack"
        else:
            what = plan.get("power") or plan["spell"]
            label = "%s @%d" % (what, plan["difficulty"])
        print("%-12s %-8.1f %-7.0f%% %-9.0f%% %-9s %s"
              % (name, rounds, win * 100, lost * 100,
                 "%.1f rd" % e_rounds, label))


def free_bands(level, chars, M):
    """At what difficulty is a minor power certainly free, and how many
    extra attacks does that buy? This is the 'eventually costs nothing'
    promise, measured."""
    hr("Quick Attack free band at level %d" % level)
    p = m.power_def(M, "quick_attack")
    base = int(p["base_difficulty"])
    step = int(p["difficulty_per_extra_attack"])
    base_cost = int(M.get("using-powers", "base_cost"))
    print("%-12s %-7s %-14s %-14s %s"
          % ("build", "skill", "always free", "free half", "extra attacks free"))
    for name, c in chars.items():
        skill = c.attack_bonus(M)
        always = skill - base_cost + 1
        half = skill
        n = max(0, (always - base) // step)
        print("%-12s %-7d %-14s %-14s %d"
              % (name, skill, "diff <= %d" % always, "diff <= %d" % half, n))


def best_field(char, foe, M, budget):
    """The hardest-biting field this caster can actually land and pay
    for, over an area wide enough to be worth walking around.

    Affordability alone is not enough: expected cost FALLS as the
    declared difficulty runs away, because the spell simply stops going
    off, so a success floor has to be part of the question."""
    best = None
    for spell_id in m.combat_spells(M):
        if not m.persists(M, spell_id):
            continue
        base = int(m.spell_def(M, spell_id)["base_difficulty"])
        for extra in range(0, 5):
            for difficulty in range(base, base + 70):
                success = sum(w for face, w, _c in m.d20_faces(M)
                              if face + char.casting_bonus(M) >= difficulty)
                if success < MIN_FIELD_SUCCESS:
                    continue
                _dmg, cost, _ctl = m.cast_expectation(
                    char, spell_id, difficulty, foe, M, extra)
                if cost > budget:
                    continue
                for damage, squares in m.spell_options(M, spell_id,
                                                       difficulty, extra):
                    if squares < MIN_FIELD_SQUARES:
                        continue
                    bite = m.reduce_by_armour(damage, foe, M)
                    if bite <= 0:
                        continue        # a field that deals nothing is none
                    if best is None or bite > best["bite"]:
                        best = {"spell": spell_id, "difficulty": difficulty,
                                "bite": bite, "squares": squares,
                                "rounds": m.spell_rounds(M, spell_id, extra)}
    return best


def report_fields(level, chars, M):
    """Would anybody go round? Crossing a field costs about one tick
    plus whatever FIELD_LINGER keeps, so that is what gets compared to
    the creature's hit points."""
    hr("Area denial at level %d -- is a field worth walking around?" % level)
    casters = {n: c for n, c in chars.items() if m.can_cast(c, M)}
    if not casters:
        print("no caster at this level")
        return {}
    out = {}
    for name, c in sorted(casters.items()):
        for kind in sorted(m.MOOKS):
            foe = m.mook(kind, M)
            field = best_field(c, foe, M, c.spirit / 4.0)
            if field is None:
                print("%-12s vs %-7s no field it can both land and afford"
                      % (name, kind))
                out[(name, kind)] = None
                continue
            cross = field["bite"] * (1 + m.FIELD_LINGER)
            share = cross / foe.total_hp
            print("%-12s vs %-7s %s @%d: %d over %d squares for %d rounds; "
                  "crossing costs %.1f of %d hp (%.0f%%)"
                  % (name, kind, field["spell"], field["difficulty"],
                     field["bite"], field["squares"], field["rounds"],
                     cross, foe.total_hp, share * 100))
            out[(name, kind)] = share
    return out


def healing_picture(level, chars, M):
    """(per caster: sustainable heal, free heal), and the yardstick."""
    foe = standard_foe(level, M)
    attack = max([m.expected_offence(c, foe, M)
                  for n, c in chars.items() if not m.can_cast(c, M)]
                 or [1.0])
    out = {}
    for name, c in sorted(chars.items()):
        if not m.can_cast(c, M):
            continue
        out[name] = (m.best_heal(c, M, c.spirit / 4.0),
                     m.best_heal(c, M, 0, free_only=True))
    return out, attack


def report_healing(level, chars, M):
    hr("Healing at level %d -- does it outrun harm?" % level)
    picture, attack = healing_picture(level, chars, M)
    if not picture:
        print("no caster at this level")
        return
    print("one attacker deals %.1f per round; healing has to stay under it"
          % attack)
    print("%-12s %-26s %-22s %s"
          % ("build", "sustainable", "with nothing left", "share of an attack"))
    for name, (paid, free) in picture.items():
        print("%-12s %-26s %-22s %.0f%%"
              % (name,
                 "%s @%d = %.1f hp (%.1f sp)" % (paid[0], paid[3], paid[1],
                                                 paid[2]),
                 "%s @%d = %.1f hp" % (free[0], free[3], free[1]),
                 100 * paid[1] / attack))

    # Mend always wins on raw hit points, because it restores the pool
    # that costs least to restore. Cure Wounds is worth reporting on its
    # own terms: it is the only thing in the game that gives back a core
    # hit point, and a core hit point is a night's rest.
    print()
    print("%-12s %s" % ("", "core healing, which nothing else provides"))
    for name, c in sorted(chars.items()):
        if not m.can_cast(c, M):
            continue
        best = (0, 0.0, 0.0)
        for difficulty in range(16, 90):
            restored, cost = m.heal_expectation(c, "cure_wounds",
                                                difficulty, M)
            if cost <= c.spirit / 4.0 and restored > best[1]:
                best = (difficulty, restored, cost)
        print("%-12s cure_wounds @%d = %.1f core hp (%.1f sp), %.1f casts "
              "a fight" % (name, best[0], best[1], best[2],
                           c.spirit / max(0.1, best[2]) / 4))


def self_blessing_picture(level, chars, M):
    """Per caster: what a self-cast blessing is worth against spending
    those same rounds on whatever the build would otherwise do.

    Comparing against a plain swing is too kind -- an evoker's swing is
    worth almost nothing, so anything beats it. The fair comparison is
    the build's best round, which for a caster is a spell."""
    foe = standard_foe(level, M)
    rounds = float(m.TYPICAL_FIGHT_ROUNDS)
    out = {}
    for name, c in sorted(chars.items()):
        if not m.can_cast(c, M):
            continue
        spell, difficulty, buffed, _plain = m.best_self_blessing(c, foe, M)
        if spell is None:
            continue
        best_round = m.expected_offence(c, foe, M) * rounds
        out[name] = (spell, difficulty, buffed, best_round,
                     buffed / max(0.01, best_round))
    return out


def report_blessings(level, chars, M):
    hr("Self-blessing at level %d -- is opening with a buff the right play?"
       % level)
    picture = self_blessing_picture(level, chars, M)
    if not picture:
        print("no caster can reach a blessing at this level")
        return
    print("%-12s %-28s %9s %9s %s"
          % ("build", "best self-blessing", "buffed", "just act", "ratio"))
    for name, (spell, difficulty, buffed, best, ratio) in picture.items():
        print("%-12s %-28s %9.1f %9.1f %.2f"
              % (name, "%s @%d" % (spell, difficulty), buffed, best, ratio))
    print()
    print("A party buff cannot be measured here -- there is no party. This")
    print("is the one blessing question a single character can answer.")


def self_guard_picture(level, chars, M):
    foe = standard_foe(level, M)
    rounds = float(m.TYPICAL_FIGHT_ROUNDS)
    out = {}
    for name, c in sorted(chars.items()):
        if not m.can_cast(c, M):
            continue
        spell, difficulty, prevented = m.best_self_guard(c, foe, M)
        if spell is None:
            continue
        offence = m.expected_offence(c, foe, M)
        with_guard = prevented + offence * (rounds - 1)
        out[name] = (spell, difficulty, prevented, offence * rounds,
                     with_guard / max(0.01, offence * rounds))
    return out


def report_guards(level, chars, M):
    hr("Self-guarding at level %d -- is opening with a guard the right "
       "play?" % level)
    picture = self_guard_picture(level, chars, M)
    if not picture:
        print("no caster can reach a guard at this level")
        return
    print("%-12s %-24s %10s %10s %s"
          % ("build", "best self-guard", "prevented", "just act", "ratio"))
    for name, (spell, difficulty, prevented, best, ratio) in picture.items():
        print("%-12s %-24s %10.1f %10.1f %.2f"
              % (name, "%s @%d" % (spell, difficulty), prevented, best,
                 ratio))
    print()
    print("Only a pool of hit points and a change in reduction are scored.")
    print("Resistance to a damage type or a school cannot be: nothing here")
    print("tracks which type or school a blow came from.")


def report_attrition(level, chars, M):
    """Fresh versus empty. This is the minor-power tier's whole reason
    for existing: a long adventure should wear a character down, not
    switch them off."""
    hr("Attrition at level %d -- damage per round fresh vs empty" % level)
    foe = standard_foe(level, M)
    print("%-12s %-8s %-8s %-7s %s"
          % ("build", "fresh", "empty", "kept", "verdict"))
    for name, c in chars.items():
        fresh = m.expected_offence(c, foe, M)
        floor = m.floor_offence(c, foe, M)
        ratio = floor / max(0.01, fresh)
        verdict = "ok"
        if ratio < FLOOR_RATIO_BAND[0]:
            verdict = "switches off when empty"
        elif ratio > FLOOR_RATIO_BAND[1]:
            verdict = "reservoir barely matters"
        print("%-12s %-8.1f %-8.1f %-7.0f%% %s"
              % (name, fresh, floor, ratio * 100, verdict))


def report_powers(level, chars, M):
    hr("Power economy at level %d" % level)
    print("%-12s %-14s %-6s %-8s %-8s %s"
          % ("build", "power", "diff", "E[dmg]", "E[cost]", "uses/fight"))
    foe = standard_foe(level, M)
    rows = []
    for name, c in chars.items():
        for power_id in m.offensive_powers(c, M):
            difficulty, damage, cost = m.best_difficulty(
                c, power_id, foe, M, c.stamina / 4.0)
            if difficulty is None:
                continue
            uses = c.stamina / cost if cost > 0 else float("inf")
            print("%-12s %-14s %-6d %-8.2f %-8.2f %s"
                  % (name, power_id, difficulty, damage, cost,
                     "unlimited" if cost <= 0 else "%.1f" % uses))
            rows.append((name, power_id, cost))
    return rows


def _duel(M, task):
    """One pairing, seeded from its own name. See parallel.duel_seed."""
    level, a, b, spec_a, spec_b, trials = task
    rounds, winrate, capped = m.duel(
        spec_a, spec_b, M, trials=trials,
        seed=parallel.duel_seed(SEED, level, a, b))
    return a, b, rounds, winrate, capped


def duel_grid(level, chars, M, trials, pool=None):
    """Every pairing at this level, in a fixed order.

    The order is the order of the results and nothing else: each duel
    seeds itself, so which worker took which pairing cannot reach the
    numbers."""
    names = list(chars)
    tasks = [(level, a, b, chars[a], chars[b], trials)
             for i, a in enumerate(names) for b in names[i + 1:]]
    if pool is None:
        return [_duel(M, task) for task in tasks]
    return pool.map(_duel, tasks)


def report_duels(level, chars, M, trials, pool=None):
    hr("Even duels at level %d (%d trials each)" % (level, trials))
    print("%-12s %-12s %-9s %s" % ("attacker", "defender", "rounds", "win rate"))
    rounds_seen = []
    for a, b, rounds, winrate, capped in duel_grid(level, chars, M, trials,
                                                   pool):
        flag = "  (%.0f%% hit the round cap)" % (capped * 100) if capped else ""
        print("%-12s %-12s %-9.1f %.0f%%%s"
              % (a, b, rounds, winrate * 100, flag))
        rounds_seen.append((rounds, a, b))
    return rounds_seen


def report_dpr(level, chars, M):
    hr("Damage per round against a common target (level %d)" % level)
    foe = standard_foe(level, M)
    out = {}
    for name, c in chars.items():
        if c is foe:
            continue
        plain, hitrate = m.attack_expectation(c, foe, M)
        best = m.expected_offence(c, foe, M)
        control = m.expected_control(c, foe, M)
        out[name] = best
        print("%-12s plain %5.2f   best power %5.2f   control %5.2f   "
              "hit rate %.0f%%"
              % (name, plain, best, control, hitrate * 100))
    return out


def run_gates(levels, M, trials, pool=None):
    hr("Gates")
    failures = []
    ever_chosen = set()
    build_spreads = []          # (gap, level, build) over every build
    class_spreads = []          # (gap, level, build, class) within a class

    for level in levels:
        chars = build_all(level, M, pool)
        if not chars:
            continue
        ever_chosen.update(c.weapon.name for c in chars.values())
        build_spreads.extend(weapon_spreads(chars))
        class_spreads.extend(class_weapon_spreads(chars, M))

        if level >= 5:
            for wkey in m.weapon_keys(M):
                for akey in m.armour_keys(M):
                    atk = m.build_character("a", dict(ARCHETYPES["duellist"],
                                                      weapon=wkey), level, M)
                    target = m.build_character("d", dict(STANDARD_FOE,
                                                         armour=akey,
                                                         stance="dodge"), level, M)
                    damage, _ = m.attack_expectation(atk, target, M)
                    if damage < MIN_DAMAGE_VS_ANY_ARMOUR:
                        failures.append(
                            "L%d %s vs %s: %.2f expected damage per swing "
                            "(target >= %.1f)"
                            % (level, wkey, akey, damage, MIN_DAMAGE_VS_ANY_ARMOUR))

        # Area denial has to deny. A field a rank-and-file creature is
        # happy to stroll across is a spell with no job, so the test is
        # whether crossing costs a worthwhile share of its hit points.
        # Only a build with real magic behind it is asked this: an
        # Initiate dabbler has no business laying down a field, and the
        # test is measured against the same rank-and-file the swarm
        # gates use rather than against something out of its weight.
        for name, c in sorted(chars.items()):
            if not (c.has("magical", "adept") or c.has("spiritual", "adept")):
                continue
            foe = m.mook(SWARM_MOOK, M)
            field = best_field(c, foe, M, c.spirit / 4.0)
            if field is None:
                # Not a verdict on the field rates: this caster cannot
                # land or afford one at all, which is a question about
                # its reservoir.
                failures.append(
                    "L%d %s can neither land nor afford any field"
                    % (level, name))
                continue
            cross = field["bite"] * (1 + m.FIELD_LINGER) / foe.total_hp
            if cross < MIN_FIELD_BITE_FRACTION:
                failures.append(
                    "L%d %s's best field costs a %s %.0f%% of its hit "
                    "points to cross (target >= %.0f%%)"
                    % (level, name, SWARM_MOOK, cross * 100,
                       MIN_FIELD_BITE_FRACTION * 100))

        # A self-cast blessing must not beat getting on with it.
        blessings = self_blessing_picture(level, chars, M)
        for name, (spell, _d, _buffed, _best, ratio) in blessings.items():
            if ratio > MAX_SELF_BLESSING_RATIO:
                failures.append(
                    "L%d %s opens best with %s on itself (%.2fx its own "
                    "best round, target <= %.2fx)"
                    % (level, name, spell, ratio, MAX_SELF_BLESSING_RATIO))

        # Nor should a self-cast guard.
        guards = self_guard_picture(level, chars, M)
        for name, (spell, _d, _p, _b, ratio) in guards.items():
            if ratio > MAX_SELF_GUARD_RATIO:
                failures.append(
                    "L%d %s opens best with %s on itself (%.2fx its own "
                    "best round, target <= %.2fx)"
                    % (level, name, spell, ratio, MAX_SELF_GUARD_RATIO))

        # Healing must not outrun harm, or a fight with a healer in it
        # simply does not end.
        picture, attack = healing_picture(level, chars, M)
        for name, (paid, free) in picture.items():
            share = paid[1] / max(0.1, attack)
            if share > MAX_HEAL_FRACTION_OF_ATTACK:
                failures.append(
                    "L%d %s heals %.1f a round against an attack of %.1f "
                    "(%.0f%%, target <= %.0f%%)"
                    % (level, name, paid[1], attack, share * 100,
                       MAX_HEAL_FRACTION_OF_ATTACK * 100))

        contrib = contributions(chars, level, M)
        if len(contrib) > 1:
            spread = max(contrib.values()) / max(0.01, min(contrib.values()))
            if spread > MAX_CONTRIBUTION_SPREAD:
                best = max(contrib, key=contrib.get)
                worst = min(contrib, key=contrib.get)
                failures.append(
                    "L%d contribution spread %.1fx (%s %.0f vs %s %.0f, "
                    "target <= %.1fx)"
                    % (level, spread, best, contrib[best], worst, contrib[worst],
                       MAX_CONTRIBUTION_SPREAD))

        for a, b, rounds, _w, _capped in duel_grid(level, chars, M, trials,
                                                   pool):
            if not (TARGET_ROUNDS[0] <= rounds <= TARGET_ROUNDS[1]):
                failures.append(
                    "L%d %s vs %s: %.1f rounds (target %.0f-%.0f)"
                    % (level, a, b, rounds, *TARGET_ROUNDS))

        # A minor power must never match its standard twin at the same
        # difficulty, or the standard one is pointless.
        for minor_id, standard_id in MINOR_TWINS.items():
            worse = minor_beaten_by_twin(minor_id, standard_id, level, chars, M)
            if worse is False:
                failures.append(
                    "L%d %s matches or beats %s at equal difficulty -- the "
                    "standard power is dead" % (level, minor_id, standard_id))

        if level >= 10:
            for name, c in chars.items():
                rounds, win, lost = m.skirmish(c, "goblin", SWARM_SIZE, M,
                                               trials=TRIALS_SWARM)
                if rounds > SWARM_ROUNDS_BY_LEVEL_10 or lost > SWARM_HP_COST_BY_LEVEL_10:
                    failures.append(
                        "L%d %s takes %.1f rounds and %.0f%% of its hit points "
                        "to clear %d goblins (target <= %.0f rounds, <= %.0f%%)"
                        % (level, name, rounds, lost * 100, SWARM_SIZE,
                           SWARM_ROUNDS_BY_LEVEL_10, SWARM_HP_COST_BY_LEVEL_10 * 100))

        foe = standard_foe(level, M)
        for name, c in chars.items():
            fresh = m.expected_offence(c, foe, M)
            ratio = m.floor_offence(c, foe, M) / max(0.01, fresh)
            # The lower bound applies always -- nobody should ever be
            # switched off by an empty reservoir. The upper bound only
            # applies once a character HAS a reservoir worth the name;
            # below that, powers are rare enough that running dry
            # genuinely should not change much.
            floor_only = level < RESERVOIR_MATTERS_FROM_LEVEL
            low, high = FLOOR_RATIO_BAND
            if ratio < low or (not floor_only and ratio > high):
                failures.append(
                    "L%d %s keeps %.0f%% of its damage with an empty "
                    "reservoir (band %.0f-%.0f%%)"
                    % (level, name, ratio * 100, low * 100, high * 100))
        for name, c in chars.items():
            if not c.has("martial", "initiate"):
                continue
            difficulty, damage, cost = m.best_difficulty(
                c, "power_attack", foe, M, c.stamina / 4.0)
            if difficulty is not None and cost < MIN_POWER_COST:
                failures.append(
                    "L%d %s power_attack costs %.2f stamina (target >= %.1f) "
                    "-- the resource has stopped mattering"
                    % (level, name, cost, MIN_POWER_COST))

    # The mirror of MIN_DAMAGE_VS_ANY_ARMOUR. That gate asks whether any
    # weapon is useless; these ask whether the table is the right shape.
    #
    # This used to be "did anybody choose it", which turned a continuous
    # quantity into a yes or no and reported a weapon 2% off the pace
    # identically to one 40% off. Worse, two weapons that are exactly
    # equivalent produce a tie, the chooser takes one, and the other was
    # reported dead for ever through no fault of its own. What follows
    # asks the two questions that were really wanted.
    if dominated := dominated_weapons(M):
        for loser, winner in dominated:
            failures.append(
                "%s is beaten by %s on every axis and beats it on none "
                "-- no play or taste can rescue it" % (loser, winner))
    if build_spreads:
        worst, level, name = max(build_spreads)
        median = statistics.median(gap for gap, _l, _n in build_spreads)
        if median > MAX_WEAPON_SPREAD:
            failures.append(
                "the median build's best weapon beats its worst by %.0f%% "
                "(target <= %.0f%%) -- the weapon is deciding too much of "
                "the character; worst is %s at L%d, %.0f%%"
                % (median * 100, MAX_WEAPON_SPREAD * 100, name, level,
                   worst * 100))
    if class_spreads:
        gap, level, name, group = max(class_spreads)
        if gap > MAX_CLASS_SPREAD:
            failures.append(
                "L%d %s gains %.0f%% by picking the right %s weapon "
                "(target <= %.0f%%) -- within a class the choice should "
                "be about the character"
                % (level, name, gap * 100, group, MAX_CLASS_SPREAD * 100))

    if failures:
        for f in failures:
            print("  FAIL  " + f)
        print("\n%d gate failure(s)." % len(failures))
    else:
        print("  all gates pass")
    return failures


def minor_beaten_by_twin(minor_id, standard_id, level, chars, M):
    """True when the standard twin is better at the same difficulty.

    Attack-granting powers are compared by expected damage against the
    standard foe, because their extra swings are not the same unit as
    each other. The rest are compared on raw effect, since a point of
    dodge bonus is a point of dodge bonus either way."""
    minor = m.power_def(M, minor_id)
    standard = m.power_def(M, standard_id)
    char = chars.get("duellist") or list(chars.values())[0]
    foe = standard_foe(level, M)
    base = max(int(minor["base_difficulty"]), int(standard["base_difficulty"]))
    for difficulty in range(base, base + 60):
        # Only compare where the STANDARD power actually grants
        # something. Below its first step it delivers nothing at all,
        # and "the minor one is better than nothing" is not dominance.
        std_step = int(standard.get("difficulty_per_step",
                                    standard.get("difficulty_per_extra_attack", 1)))
        if (difficulty - int(standard["base_difficulty"])) // std_step < 1:
            continue
        if "difficulty_per_extra_attack" in minor:
            a, _ = m.power_expectation(char, minor_id, difficulty, foe, M)
            b, _ = m.power_expectation(char, standard_id, difficulty, foe, M)
        else:
            def effect(p):
                step = int(p.get("difficulty_per_step", 1))
                per = (int(p.get("damage_per_step", 0))
                       + int(p.get("dodge_bonus_per_step", 0))
                       + int(p.get("reduction_ignored_per_step", 0)))
                return max(0, (difficulty - int(p["base_difficulty"])) // step) * per
            a, b = effect(minor), effect(standard)
        if a > b:
            return False
    return True


def report_contributions(level, chars, M):
    """The gate's own arithmetic, shown rather than only asserted.

    `contributions` decides MAX_CONTRIBUTION_SPREAD and was for a long
    time the one figure in the report that could only be reproduced by
    writing a script against the model. Every column it multiplies is
    here so a failure can be read as offence, survival or the opening,
    rather than guessed at."""
    hr("Contribution at level %d -- (offence + control) x survival" % level)
    foe = standard_foe(level, M)
    contrib = contributions(chars, level, M)
    print("%-12s %8s %8s %8s %8s %6s %10s"
          % ("build", "offence", "control", "taken", "survival", "open",
             "contrib"))
    for name, c in chars.items():
        taken, _ = m.attack_expectation(
            foe, c, M, dodge_bonus=m.sustained_dodge_bonus(c, M))
        survival = min(SURVIVAL_CLAMP_ROUNDS, c.total_hp / max(0.1, taken))
        print("%-12s %8.2f %8.2f %8.2f %8.2f %6d %10.1f"
              % (name, m.expected_offence(c, foe, M),
                 m.expected_control(c, foe, M), taken, survival,
                 m.opening_rounds(c, foe, M), contrib[name]))
    if len(contrib) > 1:
        best = max(contrib, key=contrib.get)
        worst = min(contrib, key=contrib.get)
        print("spread %.2fx (%s vs %s), target <= %.1fx"
              % (contrib[best] / max(0.01, contrib[worst]), best, worst,
                 MAX_CONTRIBUTION_SPREAD))
    print("'open' is rounds acting before the foe arrives: zero for "
          "anything that cannot")
    print("act at a distance, and credited at the spell's worth rather "
          "than the build's best.")


AGGRESSION_STEPS = (0.0, 0.25, 0.5, 0.75, 1.0)


def _at_aggression(M, task):
    """One archetype built at one setting of the dial, shopping for its
    own kit like any other build. Top-level and taking its own
    `Mechanics` so that it runs the same in a worker as in here."""
    level, name, aggression = task
    panel = shopping_panel(level, M)
    char = m.build_character(name, ARCHETYPES[name], level, M,
                             shopping_foe=panel, aggression=aggression)
    return (name, aggression), char


def spectrum(level, M, pool=None, steps=AGGRESSION_STEPS):
    """Every archetype built across the tank-to-striker dial."""
    tasks = [(level, name, a) for name in ARCHETYPES for a in steps]
    built = (pool.map(_at_aggression, tasks) if pool is not None
             else [_at_aggression(M, task) for task in tasks])
    return {key: char for key, char in built if char is not None}


def report_spectrum(level, M, pool=None, steps=AGGRESSION_STEPS):
    """Contribution against the dial, which is the whole question.

    The advancement menu is only a menu if the ends of it are worth
    comparable amounts. Reading down a row: flat means a player choosing
    between hitting harder and lasting longer is making a real choice;
    rising or falling all the way across means one end is simply better
    and the other end is a trap for anybody who takes the fiction
    seriously.

    The dial is a measuring instrument and not a claim about how a
    character is built. Every other report in this file uses the
    model's own cascade, which is what `aggression=None` still does."""
    hr("The tank-to-striker spectrum at level %d" % level)
    chars = spectrum(level, M, pool, steps)
    print("contribution against how much of the discretionary budget "
          "goes to offence")
    print("%-12s %s %9s %8s" % (
        "build", "".join("%9s" % ("%d%%" % (a * 100)) for a in steps),
        "best at", "spread"))
    for name in sorted(ARCHETYPES):
        row = {a: chars[(name, a)] for a in steps if (name, a) in chars}
        if not row:
            continue
        scores = {a: contributions({name: c}, level, M)[name]
                  for a, c in row.items()}
        best = max(scores, key=scores.get)
        lo, hi = min(scores.values()), max(scores.values())
        print("%-12s %s %8d%% %7.2fx" % (
            name, "".join("%9.0f" % scores[a] for a in steps),
            best * 100, hi / max(0.01, lo)))
    print()
    print("A flat row is a real choice. A row that climbs or falls all "
          "the way across is a")
    print("dominant end, and the spread column says by how much.")


def contributions(chars, level, M):
    """Offence alone is a bad measure: a defensive signature scores zero
    on it. Contribution is damage dealt per round MULTIPLIED by how many
    rounds the build survives the standard foe, so trading damage for
    staying power comes out even -- plus whatever the build got done
    before the foe arrived, which is nothing at all unless it can act
    at a distance."""
    foe = standard_foe(level, M)
    out = {}
    for name, c in chars.items():
        taken, _ = m.attack_expectation(
            foe, c, M, dodge_bonus=m.sustained_dodge_bonus(c, M))
        # Clamped: past this many rounds the fight is a stalemate, not a
        # win, and an unclamped ratio lets one near-untouchable build
        # dominate the metric by dividing by almost zero.
        survival = min(SURVIVAL_CLAMP_ROUNDS, c.total_hp / max(0.1, taken))
        # expected_offence knows every power the build can bring AND
        # its spells. An earlier version of this function carried its
        # own hardcoded list of martial powers, which measured a wizard
        # on the staff it was holding and scored it near zero.
        #
        # Control is added to offence rather than to survival: a round
        # taken off the foe is a round of its damage that never happens,
        # and quoting it as damage is the only way a stun and a sword
        # swing can be compared at all. It is zero for every build that
        # applies no conditions, which is every martial build.
        # Scored over the whole arc rather than fresh only -- see
        # DEPLETED_FRACTION. This is what prices a hybrid's second
        # capability: fresh, `expected_offence` is a max and the weapon
        # under a better spell is worth nothing; empty, the spell is
        # gone and the weapon is all there is.
        offence = m.arc_offence(c, foe, M)
        control = m.expected_control(c, foe, M)
        # A fight does not begin with everyone in contact. The build
        # that reaches furthest opens the fight at its own range and
        # acts while the other one walks -- `crowd_geometry` has said so
        # since area spells were given a range, and this is the same
        # rule applied to the single-target measure.
        #
        # Those rounds are credited at what the SPELL is worth, not at
        # what the build's best turn is worth. The two differ for a
        # hybrid, and crediting the better of them would pay the
        # spellblade's axe at the range of a lance it is not casting.
        # A build with no spell opens in contact, so every martial in
        # the panel is untouched by this and the figures stay
        # comparable with the ones before it.
        free = m.opening_rounds(c, foe, M)
        approach = m.opening_value(c, foe, M) * free
        out[name] = approach + (offence + control) * survival
    return out


def main():
    ap = argparse.ArgumentParser(description="Measure the Ico rules.")
    ap.add_argument("--levels", default="1,5,10")
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--swarm-trials", type=int, default=1200)
    ap.add_argument("--check", action="store_true",
                    help="gates only; exit 1 on failure")
    ap.add_argument("--spectrum", action="store_true",
                    help="sweep the tank-to-striker dial and report "
                         "contribution across it, instead of the full report")
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--jobs", type=int, default=None,
                    help="worker processes (default %d, or ICO_SIM_JOBS); "
                         "changes the speed and never a number"
                         % parallel.DEFAULT_JOBS)
    ap.add_argument("--path", default=None,
                    help="Ruleset directory to measure (or a mechanics.json), "
                         "instead of this checkout's own build/.")
    args = ap.parse_args()

    import random
    random.seed(args.seed)
    global SEED
    SEED = args.seed

    levels = [int(x) for x in args.levels.split(",")]
    global TRIALS_SWARM
    TRIALS_SWARM = args.swarm_trials
    M = m.Mechanics(args.path)

    print("Ico balance report")
    print("source: %s" % M.path)

    with parallel.Pool(M, args.jobs) as pool:
        return _run(args, levels, M, pool)


def _run(args, levels, M, pool):
    if args.check:
        return 1 if run_gates(levels, M, args.trials, pool) else 0

    if args.spectrum:
        for level in levels:
            report_spectrum(level, M, pool)
        return 0

    for level in levels:
        chars = build_all(level, M, pool)
        if not chars:
            print("\n(no affordable builds at level %d)" % level)
            continue
        report_sheets(level, chars, M)
        report_dpr(level, chars, M)
        report_swarm(level, chars, M)
        report_fields(level, chars, M)
        report_healing(level, chars, M)
        report_blessings(level, chars, M)
        report_guards(level, chars, M)
        free_bands(level, chars, M)
        report_attrition(level, chars, M)
        report_powers(level, chars, M)
        report_stances(level, chars, M)
        report_contributions(level, chars, M)
        report_weapon_utility(level, chars, M)
        report_armour_grants(level, chars, M)
        report_duels(level, chars, M, args.trials, pool)

    report_weapon_matrix(levels[-1], build_all(levels[-1], M, pool), M)
    failures = run_gates(levels, M, args.trials, pool)

    hr("Simulation assumptions")
    for a in m.ASSUMPTIONS:
        print("  - " + a)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
