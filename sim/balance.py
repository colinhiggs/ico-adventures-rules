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
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import model as m

# --- design targets -------------------------------------------------
# These encode the goals in ch-overview: a fight should be decisive but
# not a grind, no build should be strictly better, and no weapon should
# be inert against any armour.
TARGET_ROUNDS = (3.0, 12.0)      # rounds for an even duel
MAX_CONTRIBUTION_SPREAD = 2.5    # best archetype / worst, offence x survival
MIN_DAMAGE_VS_ANY_ARMOUR = 1.0   # expected damage per swing, level 5+
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
        "weapon": "sword", "armour": "chain_shirt", "shield": "shield",
        "stance": "block",
    },
    "berserker": {
        "disciplines": [("martial", "adept"), ("athletic", "adept")],
        "attributes": {"strength": 18, "dexterity": 12, "constitution": 16,
                       "intelligence": 8, "willpower": 12, "charisma": 14},
        "weapon": "two_handed_sword", "armour": "leather", "shield": None,
        "stance": "dodge",
    },
    "skirmisher": {
        "disciplines": [("athletic", "master"), ("martial", "initiate")],
        "attributes": {"strength": 12, "dexterity": 18, "constitution": 12,
                       "intelligence": 12, "willpower": 12, "charisma": 14},
        "weapon": "short_sword", "armour": "studded_leather", "shield": None,
        "stance": "dodge",
    },
    "sentinel": {
        "disciplines": [("martial", "adept"), ("awareness", "adept")],
        "attributes": {"strength": 16, "dexterity": 10, "constitution": 16,
                       "intelligence": 10, "willpower": 14, "charisma": 14},
        "weapon": "sword", "armour": "full_plate", "shield": "great_shield",
        "stance": "block",
    },
    "evoker": {
        "disciplines": [("magical", "master"), ("awareness", "initiate")],
        "attributes": {"strength": 10, "dexterity": 12, "constitution": 12,
                       "intelligence": 16, "willpower": 16, "charisma": 14},
        "weapon": "staff", "armour": "leather", "shield": None,
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
        "weapon": "two_handed_sword", "armour": "full_plate", "shield": None,
        "stance": "dodge",
    },
    "generalist": {
        "disciplines": [("martial", "initiate"), ("athletic", "initiate"),
                        ("awareness", "initiate"), ("spiritual", "initiate")],
        "attributes": {"strength": 13, "dexterity": 13, "constitution": 14,
                       "intelligence": 13, "willpower": 13, "charisma": 14},
        "weapon": "sword", "armour": "scale_mail", "shield": "buckler",
        "stance": "dodge",
    },
}

# The yardstick every build is measured against, so the numbers are
# comparable across builds and levels.
STANDARD_FOE = {
    "disciplines": [("martial", "initiate"), ("athletic", "initiate")],
    "attributes": {"strength": 14, "dexterity": 14, "constitution": 14,
                   "intelligence": 10, "willpower": 12, "charisma": 12},
    "weapon": "sword", "armour": "scale_mail", "shield": None,
    "stance": "dodge",
}


def standard_foe(level, M):
    return m.build_character("standard", STANDARD_FOE, level, M)


def hr(title):
    print("\n" + title)
    print("-" * len(title))


def build_all(level, M):
    out = {}
    for name, spec in ARCHETYPES.items():
        char = m.build_character(name, spec, level, M)
        if char is not None:
            out[name] = char
    return out


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
    for name, spec in ARCHETYPES.items():
        d_dodge = m.build_character(name, dict(spec, stance="dodge"), level, M)
        d_block = m.build_character(name, dict(spec, stance="block"), level, M)
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


def report_duels(level, chars, M, trials):
    hr("Even duels at level %d (%d trials each)" % (level, trials))
    names = list(chars)
    print("%-12s %-12s %-9s %s" % ("attacker", "defender", "rounds", "win rate"))
    rounds_seen = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            rounds, winrate, capped = m.duel(chars[a], chars[b], M, trials=trials)
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


def run_gates(levels, M, trials):
    hr("Gates")
    failures = []

    for level in levels:
        chars = build_all(level, M)
        if not chars:
            continue

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

        names = list(chars)
        for i, a in enumerate(names):
            for b in names[i + 1:]:
                rounds, _, capped = m.duel(chars[a], chars[b], M, trials=trials)
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


def contributions(chars, level, M):
    """Offence alone is a bad measure: a defensive signature scores zero
    on it. Contribution is damage dealt per round MULTIPLIED by how many
    rounds the build survives the standard foe, so trading damage for
    staying power comes out even."""
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
        offence = m.expected_offence(c, foe, M)
        control = m.expected_control(c, foe, M)
        out[name] = (offence + control) * survival
    return out


def main():
    ap = argparse.ArgumentParser(description="Measure the Ico rules.")
    ap.add_argument("--levels", default="1,5,10")
    ap.add_argument("--trials", type=int, default=3000)
    ap.add_argument("--swarm-trials", type=int, default=1200)
    ap.add_argument("--check", action="store_true",
                    help="gates only; exit 1 on failure")
    ap.add_argument("--seed", type=int, default=12345)
    args = ap.parse_args()

    import random
    random.seed(args.seed)

    levels = [int(x) for x in args.levels.split(",")]
    global TRIALS_SWARM
    TRIALS_SWARM = args.swarm_trials
    M = m.Mechanics()

    print("Ico balance report")
    print("source: %s" % M.path)

    if args.check:
        return 1 if run_gates(levels, M, args.trials) else 0

    for level in levels:
        chars = build_all(level, M)
        if not chars:
            print("\n(no affordable builds at level %d)" % level)
            continue
        report_sheets(level, chars, M)
        report_dpr(level, chars, M)
        report_swarm(level, chars, M)
        report_fields(level, chars, M)
        free_bands(level, chars, M)
        report_attrition(level, chars, M)
        report_powers(level, chars, M)
        report_stances(level, chars, M)
        report_duels(level, chars, M, args.trials)

    report_weapon_matrix(levels[-1], build_all(levels[-1], M), M)
    failures = run_gates(levels, M, args.trials)

    hr("Simulation assumptions")
    for a in m.ASSUMPTIONS:
        print("  - " + a)

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
