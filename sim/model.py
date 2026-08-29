# model.py -- the Ico combat model.
#
# This is the rules LOGIC that mechanics.json deliberately cannot hold.
# mechanics.json carries the VALUES (weapon damage, armour points, the
# cost formula's constants); this file carries the procedure that
# consumes them: who rolls what, in which order, and how a margin turns
# into a wound.
#
# The one hard rule, inherited from the rest of the pipeline: NO GAME
# NUMBER IS WRITTEN HERE. Every constant comes from build/mechanics.json
# and a missing key raises rather than defaulting, exactly as
# rules_runtime.py does for the server. If a rule file changes, this
# model changes with it or it stops running -- which is the point.
#
# Simulation-only assumptions (choices the rules do not make for us) are
# marked ASSUMPTION and collected by balance.py so they are reported
# rather than hidden.

import json
import random
from dataclasses import dataclass, field
from pathlib import Path

BUILD_DIR = Path(__file__).parent.parent / "build"
MECHANICS_PATH = BUILD_DIR / "mechanics.json"

ASSUMPTIONS = [
    "Both sides fight to the death with no morale, terrain or positioning.",
    "A character takes every mastery hit point allowed first, then "
    "raises tracked combat skills, then widens its power source.",
    "Chargen budgets and level budgets are treated as one pool, except "
    "that discipline spend is capped at the chargen budget plus levels.",
    "A power's difficulty is chosen once per build by expected-value "
    "search, then held fixed, rather than re-judged each round.",
    "Stamina and spirit do not recover during a fight.",
    "Sneak Attack's condition is met in half of all rounds; "
    "Redouble is sustained at a rate that lasts the whole fight.",
]


class RulesNotBuilt(Exception):
    pass


class Mechanics:
    """Fail-fast reader over build/mechanics.json."""

    def __init__(self, path=None):
        path = Path(path or MECHANICS_PATH)
        if not path.exists():
            raise RulesNotBuilt(
                "%s not found. Run:  python3 tools/build.py ico\n"
                "The simulator has no built-in game constants by design."
                % path
            )
        self.path = path
        self.rules = json.loads(path.read_text(encoding="utf-8"))["rules"]

    def get(self, rule_id, *keys):
        if rule_id not in self.rules:
            raise KeyError(
                "no rule '%s' in %s (have: %s)"
                % (rule_id, self.path.name, ", ".join(sorted(self.rules)))
            )
        cur = self.rules[rule_id]
        walked = [rule_id]
        for k in keys:
            if not isinstance(cur, dict) or k not in cur:
                have = ", ".join(sorted(cur)) if isinstance(cur, dict) else repr(cur)
                raise KeyError(
                    "'%s' has no mechanic '%s' (have: %s)"
                    % (".".join(walked), k, have)
                )
            cur = cur[k]
            walked.append(k)
        return cur

    def keys(self, rule_id):
        return sorted(self.rules.get(rule_id, {}))


# ---------------------------------------------------------------------
# Gear
# ---------------------------------------------------------------------
@dataclass
class Weapon:
    name: str
    accuracy: int
    damage: int
    size: str
    block_ap: int

    @classmethod
    def load(cls, M, key):
        return cls(
            name=key,
            accuracy=int(M.get("weapons", key, "accuracy")),
            damage=int(M.get("weapons", key, "damage")),
            size=str(M.get("weapons", key, "size")),
            block_ap=int(M.get("weapons", key, "block_ap")),
        )


@dataclass
class Armour:
    name: str
    ap: int
    skill_penalty: int

    @classmethod
    def load(cls, M, key):
        return cls(
            name=key,
            ap=int(M.get("armour", key, "ap")),
            skill_penalty=int(M.get("armour", key, "skill_penalty")),
        )


@dataclass
class Shield:
    name: str
    block_td_bonus: int
    block_ap: int
    skill_penalty: int

    @classmethod
    def load(cls, M, key):
        if key is None:
            return None
        return cls(
            name=key,
            block_td_bonus=int(M.get("armour", key, "block_td_bonus")),
            block_ap=int(M.get("armour", key, "block_ap")),
            skill_penalty=int(M.get("armour", key, "skill_penalty")),
        )


def _entries(M, rule_id):
    """Only the dict-valued mechanics are gear; scalars alongside them
    (weapons.finesse_size, say) are rules about the gear, not items."""
    return {k: v for k, v in M.rules.get(rule_id, {}).items()
            if isinstance(v, dict)}


def weapon_keys(M):
    return sorted(_entries(M, "weapons"))


def armour_keys(M):
    return sorted(k for k, v in _entries(M, "armour").items() if "ap" in v)


def shield_keys(M):
    return sorted(k for k, v in _entries(M, "armour").items() if "block_ap" in v)


# ---------------------------------------------------------------------
# Characters
# ---------------------------------------------------------------------
GRADE_ORDER = ("initiate", "adept", "master")

# Which discipline's skill group each tracked skill belongs to. Read from
# discipline-list's `skills` lists so it cannot drift from the book.
TRACKED_SKILLS = ("attack_melee", "dodge", "block", "fortitude", "spot")

# Which attribute governs each tracked skill, per skill-list.md prose.
# ASSUMPTION: skill-list.md states these in prose, not mechanics, so the
# mapping is duplicated here. Moving it into mechanics would remove this.
SKILL_ATTRIBUTE = {
    "attack_melee": "strength",
    "dodge": "dexterity",
    "block": "strength",
    "fortitude": "constitution",
    "spot": "willpower",
}


@dataclass
class Character:
    name: str
    level: int
    disciplines: dict           # {discipline: grade}
    attributes: dict
    skills: dict = field(default_factory=dict)
    weapon: Weapon = None
    armour: Armour = None
    shield: Shield = None
    stance: str = "dodge"
    mhp: int = 0
    chp: int = 0
    stamina: int = 0
    power_plan: dict = field(default_factory=dict)
    spent: dict = field(default_factory=dict)

    def attr_bonus(self, attribute, M):
        step = int(M.get("attributes", "points_per_bonus_step"))
        avg = int(M.get("attributes", "average_score"))
        return (self.attributes[attribute] - avg) // step

    def skill(self, name, M):
        return self.skills.get(name, 0) + self.attr_bonus(
            SKILL_ATTRIBUTE[name], M
        )

    def attack_bonus(self, M):
        """Attack skill plus the governing attribute -- dexterity rather
        than strength if the weapon is finesse (weapons.finesse_size)."""
        ranks = self.skills.get("attack_melee", 0)
        best = self.attr_bonus("strength", M)
        if self.weapon and self.weapon.size == str(M.get("weapons", "finesse_size")):
            best = max(best, self.attr_bonus("dexterity", M))
        return ranks + best

    def has(self, discipline, grade):
        held = self.disciplines.get(discipline)
        if held is None:
            return False
        return GRADE_ORDER.index(held) >= GRADE_ORDER.index(grade)

    @property
    def total_hp(self):
        return self.mhp + self.chp


def focus_of(discipline_grade):
    """Focus tier derived from the grade held, per disciplines.md."""
    if discipline_grade is None:
        return "peripheral"
    return {"initiate": "unfocused", "adept": "focused", "master": "focused"}[
        discipline_grade
    ]


def skill_focus(char, skill_name, M):
    """Which focus tier a skill sits in, from the character's grades and
    the discipline-list skill groups."""
    for discipline in M.keys("discipline-list"):
        group = M.get("discipline-list", discipline, "skills")
        if skill_name in group:
            return focus_of(char.disciplines.get(discipline))
    return "peripheral"


def skill_cap(focus, level, M):
    base = int(M.get("skills", "cap_base_%s" % focus))
    return base + int(M.get("skills", "cap_per_level")) * level


def rank_cost(focus, M):
    return int(M.get("skills", "rank_cost_%s" % focus))


def grade_costs(M):
    return {
        "initiate": int(M.get("disciplines", "initiate_cost")),
        "adept": int(M.get("disciplines", "adept_cost")),
        "master": int(M.get("disciplines", "master_cost")),
    }


def discipline_cost(grade, M):
    costs = grade_costs(M)
    total = 0
    for g in GRADE_ORDER:
        total += costs[g]
        if g == grade:
            break
    return total


def buy_disciplines(priorities, budget, M):
    """Spend a discipline budget depth-first down a priority list.

    `priorities` is [(discipline, target_grade), ...] in the order the
    character cares about them, so a specialist reaches Master in their
    first discipline before touching the second. Returns (held, spent)."""
    costs = grade_costs(M)
    held = {}
    spent = 0
    for discipline, target in priorities:
        for grade in GRADE_ORDER:
            if GRADE_ORDER.index(grade) > GRADE_ORDER.index(target):
                break
            if spent + costs[grade] > budget:
                break
            spent += costs[grade]
            held[discipline] = grade
    return held, spent


def build_character(name, spec, level, M):
    """Spend a level's worth of points into a playable sheet.

    Priority order is the ASSUMPTION listed at the top: disciplines
    first (they are the build), then the tracked combat skills to their
    caps in stance-relevant order, then everything left into mastery
    hit points."""
    chargen_disc = int(M.get("character-creation", "starting_discipline_budget"))
    chargen_pool = int(M.get("character-creation", "skill_point_pool"))
    per_level = int(M.get("advancement", "points_per_level"))

    disc_budget = chargen_disc + (level - 1) * per_level
    held, disc_spend = buy_disciplines(spec["disciplines"], disc_budget, M)

    char = Character(
        name=name,
        level=level,
        disciplines=held,
        attributes=dict(spec["attributes"]),
        stance=spec.get("stance", "dodge"),
    )
    char.weapon = Weapon.load(M, spec["weapon"])
    char.armour = Armour.load(M, spec["armour"])
    char.shield = Shield.load(M, spec.get("shield"))

    points = chargen_disc + chargen_pool + (level - 1) * per_level - disc_spend

    # Survivability first: a player almost always takes the mastery hit
    # points they are allowed before pushing the last ranks of a skill,
    # so reserve that budget before spending on skills.
    per_point = int(M.get("advancement", "mastery_hp_per_point"))
    mhp_ceiling = (
        int(M.get("character-creation", "max_starting_mastery_hp"))
        + int(M.get("advancement", "max_mastery_hp_bought_per_level")) * (level - 1)
    )
    mhp_points = min(points, -(-mhp_ceiling // per_point))
    points -= mhp_points

    order = list(TRACKED_SKILLS)
    lead = "block" if char.stance == "block" else "dodge"
    order.sort(key=lambda s: (s != "attack_melee", s != lead))

    for skill_name in order:
        focus = skill_focus(char, skill_name, M)
        cap = skill_cap(focus, level, M)
        cost = rank_cost(focus, M)
        ranks = max(0, min(cap, points // cost))
        char.skills[skill_name] = ranks
        points -= ranks * cost

    # Leftover points: mastery hit points up to the per-level ceiling,
    # then everything else widens the power source.
    free_mhp = int(M.get("advancement", "free_mastery_hp_per_level")) * level
    bought_mhp = min(mhp_ceiling, mhp_points * per_point)

    source_per_point = int(M.get("advancement", "power_source_per_point"))
    source_ceiling = int(
        M.get("advancement", "max_power_source_bought_per_level")) * level
    source_points = min(points, source_ceiling)
    points -= source_points

    char.mhp = free_mhp + bought_mhp
    char.chp = char.attributes["constitution"]
    char.stamina = char.attributes["constitution"] + source_points * source_per_point
    char.spent = {
        "disciplines": disc_spend,
        "mhp_points": mhp_points,
        "power_source_points": source_points,
        "unspent": points,
    }
    return char


# ---------------------------------------------------------------------
# Resolution
# ---------------------------------------------------------------------
def d20():
    return random.randint(1, 20)


def targeting_difficulty(defender, M, dodge_bonus=0):
    """TD the attacker must beat, per hitting.md."""
    if defender.stance == "block":
        td = defender.skill("block", M)
        if defender.shield:
            td += defender.shield.block_td_bonus
        return td
    td = int(M.get("hitting", "dodge_targeting_base")) + defender.skill("dodge", M)
    penalty = defender.armour.skill_penalty
    if defender.shield:
        penalty += defender.shield.skill_penalty
    # Untouchable (Athletic master) cancels armour's penalty when dodging.
    if not defender.has("athletic", "master"):
        td += penalty
    return td + dodge_bonus


def margin_fraction(attacker, M):
    """Half by default; Killing Blow makes it whole."""
    if attacker.has("martial", "master"):
        return float(M.get("discipline-powers", "killing_blow",
                           "margin_to_damage_fraction"))
    return float(M.get("damage", "margin_to_damage_fraction"))


def damage_from(attacker, defender, margin, M, bonus=0, pierce=0):
    weapon_damage = attacker.weapon.damage
    from_margin = int(margin * margin_fraction(attacker, M))
    step = int(M.get("damage", "damage_per_attack_skill_step"))
    from_skill = attacker.attack_bonus(M) // step if step else 0
    raw = weapon_damage + from_margin + from_skill + bonus
    reduction = defender.armour.ap
    if defender.stance == "block":
        reduction += (defender.shield.block_ap if defender.shield
                      else defender.weapon.block_ap)
    # Find the Gap ignores total reduction, shield included.
    reduction = max(0, reduction - pierce)
    # Reduction can never take more than its share of the raw blow.
    cap = raw * float(M.get("damage", "max_reduction_fraction"))
    return max(0, int(raw - min(reduction, cap)))


def attack_expectation(attacker, defender, M, bonus=0, pierce=0, dodge_bonus=0):
    """Exact expected damage of one swing, enumerated over the d20."""
    td = targeting_difficulty(defender, M, dodge_bonus)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    total_damage = 0
    hits = 0
    for face in range(1, 21):
        total = face + attacker.attack_bonus(M) + attacker.weapon.accuracy
        landed = total >= td if on_tie else total > td
        if landed:
            hits += 1
            total_damage += damage_from(
                attacker, defender, total - td, M, bonus=bonus, pierce=pierce
            )
    return total_damage / 20.0, hits / 20.0


def power_cost(difficulty, roll, M):
    base = int(M.get("using-powers", "base_cost"))
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))
    return max(difficulty // divisor, base + difficulty - roll)


def power_expectation(char, power_id, difficulty, defender, M):
    """Expected damage and stamina for one round using a damage power,
    enumerated over the d20. The power roll and the attack roll are the
    same roll (using-powers: one_roll_serves_both_when_skills_match)."""
    p = M.rules["discipline-powers"].get(power_id) or M.rules["general-powers"][power_id]
    base_d = int(p["base_difficulty"])
    step = int(p.get("difficulty_per_step", p.get("difficulty_per_extra_attack", 1)))
    steps = max(0, (difficulty - base_d) // step)
    bonus = steps * int(p.get("damage_per_step", 0))
    pierce = steps * int(p.get("reduction_ignored_per_step", 0))
    extra_attacks = steps if "difficulty_per_extra_attack" in p else 0

    skill = char.attack_bonus(M) + char.weapon.accuracy
    td = targeting_difficulty(defender, M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))

    damage = 0.0
    cost = 0.0
    for face in range(1, 21):
        roll = face + char.attack_bonus(M)
        total = face + skill
        if roll >= difficulty:
            cost += power_cost(difficulty, roll, M)
            swings = 1 + extra_attacks
            for _ in range(swings):
                if (total >= td) if on_tie else (total > td):
                    damage += damage_from(
                        char, defender, total - td, M, bonus=bonus, pierce=pierce
                    )
        else:
            cost += difficulty // divisor
            # power failed; the action is spent, so no swing at all
    return damage / 20.0, cost / 20.0


def best_difficulty(char, power_id, defender, M, stamina_budget):
    """Pick the difficulty maximising expected damage subject to an
    expected stamina spend the character can sustain."""
    p = M.rules["discipline-powers"].get(power_id) or M.rules["general-powers"][power_id]
    base_d = int(p["base_difficulty"])
    best = (None, -1.0, 0.0)
    for difficulty in range(base_d, base_d + 60):
        damage, cost = power_expectation(char, power_id, difficulty, defender, M)
        if cost > stamina_budget:
            continue
        if damage > best[1]:
            best = (difficulty, damage, cost)
    return best


# ---------------------------------------------------------------------
# Duels
# ---------------------------------------------------------------------
def apply_damage(target, amount):
    """Mastery hit points first, then core -- hit-points.md."""
    from_mhp = min(target.mhp, amount)
    target.mhp -= from_mhp
    target.chp -= amount - from_mhp


def duel(spec_a, spec_b, M, trials=4000, max_rounds=100, rounds_budget=4):
    """Monte Carlo. Returns (mean rounds, a's win rate, mean rounds
    where a was the one who fell)."""
    rounds_total = 0
    a_wins = 0
    capped = 0

    plan_a = _plan(spec_a, spec_b, M, rounds_budget)
    plan_b = _plan(spec_b, spec_a, M, rounds_budget)
    guard_a = redouble_plan(spec_a, M)
    guard_b = redouble_plan(spec_b, M)

    for _ in range(trials):
        a = _fresh(spec_a)
        b = _fresh(spec_b)
        rounds = 0
        while a.chp > 0 and b.chp > 0 and rounds < max_rounds:
            rounds += 1
            _act(a, b, _pick(plan_a), M, dodge_bonus=_guard(b, guard_b, M))
            if b.chp <= 0:
                break
            _act(b, a, _pick(plan_b), M, dodge_bonus=_guard(a, guard_a, M))
        rounds_total += rounds
        if rounds >= max_rounds:
            capped += 1
        elif b.chp <= 0:
            a_wins += 1
    return rounds_total / trials, a_wins / trials, capped / trials


def _guard(defender, plan, M):
    """Spend stamina to raise this defender's targeting difficulty for
    one incoming attack. Returns the bonus actually bought."""
    if plan is None:
        return 0
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))
    floor = plan["difficulty"] // divisor
    if defender.stamina < floor:
        return 0
    roll = d20() + defender.skill("dodge", M)
    if roll >= plan["difficulty"]:
        defender.stamina -= min(power_cost(plan["difficulty"], roll, M),
                                defender.stamina)
        return plan["bonus"]
    defender.stamina = max(0, defender.stamina - floor)
    return 0


def _pick(plans):
    return plans["flank" if random.random() < SNEAK_AVAILABILITY else "open"]


def _fresh(char):
    import copy
    return copy.deepcopy(char)


# How often a fight offers the flank or the distracted target that
# Sneak Attack needs. The rules do not say -- this is a table
# assumption, and the skirmisher's whole offence hangs off it.
SNEAK_AVAILABILITY = 0.5


def offensive_powers(char, conditional=True):
    """Every attack power this build may bring. Sneak Attack is listed
    separately because it needs a condition the rules leave to the
    fiction; excluding it entirely made Athletic look purely defensive
    when two of its three powers are not."""
    options = []
    if char.has("martial", "initiate"):
        options.append("power_attack")
    if char.has("martial", "adept"):
        options.append("find_the_gap")
    if conditional and char.has("athletic", "adept"):
        options.append("sneak_attack")
    options.append("fast_attack")
    return options


def redouble_plan(char, M):
    """The difficulty a dodger should declare for Redouble, and what it
    costs. Returns None if the build cannot use it."""
    if char.stance != "dodge" or not char.has("athletic", "initiate"):
        return None
    p = M.rules["discipline-powers"]["redouble"]
    base = int(p["base_difficulty"])
    step = int(p["difficulty_per_step"])
    per_step = int(p["dodge_bonus_per_step"])
    skill = char.skill("dodge", M)
    best = None
    for difficulty in range(base, base + 40):
        chance = max(0.0, min(1.0, (20 - (difficulty - skill) + 1) / 20.0))
        if chance <= 0:
            break
        bonus = ((difficulty - base) // step) * per_step
        expected_cost = 0.0
        for face in range(1, 21):
            roll = face + skill
            expected_cost += (power_cost(difficulty, roll, M) if roll >= difficulty
                              else difficulty // int(M.get("using-powers",
                                                           "minimum_cost_divisor")))
        expected_cost /= 20.0
        value = chance * bonus
        if best is None or value > best["value"]:
            best = {"difficulty": difficulty, "bonus": bonus,
                    "value": value, "cost": expected_cost}
    return best


# Roughly how long a fight runs, used to work out how much of one a
# character can afford to spend a per-attack power on.
TYPICAL_FIGHT_ROUNDS = 6


def sustained_dodge_bonus(char, M):
    """Redouble is paid for EVERY attack it answers, so a build can only
    keep it up for as many rounds as its stamina lasts. This returns the
    average bonus per incoming attack across a whole fight -- not the
    bonus it could manage for one glorious round."""
    plan = redouble_plan(char, M)
    if plan is None or plan["cost"] <= 0:
        return 0
    affordable_rounds = char.stamina / plan["cost"]
    covered = min(1.0, affordable_rounds / TYPICAL_FIGHT_ROUNDS)
    return int(plan["value"] * covered)


def _best_option(char, foe, M, budget, conditional=True):
    best = (None, -1.0, 0.0, 0)
    for power_id in offensive_powers(char, conditional):
        difficulty, damage, cost = best_difficulty(char, power_id, foe, M, budget)
        if difficulty is not None and damage > best[1]:
            best = (power_id, damage, cost, difficulty)
    return best


def expected_offence(char, foe, M, rounds_budget=4):
    """Blended expected damage per round: the conditional power when the
    fight offers it, the best unconditional one when it does not."""
    budget = char.stamina / float(rounds_budget)
    plain, _ = attack_expectation(char, foe, M)
    unconditional = max(plain, _best_option(char, foe, M, budget, False)[1])
    if not char.has("athletic", "adept"):
        return unconditional
    conditional = max(unconditional, _best_option(char, foe, M, budget, True)[1])
    return (SNEAK_AVAILABILITY * conditional
            + (1 - SNEAK_AVAILABILITY) * unconditional)


def _plan(char, foe, M, rounds_budget):
    budget = char.stamina / float(rounds_budget)
    plain, _ = attack_expectation(char, foe, M)
    plans = {}
    for label, conditional in (("open", False), ("flank", True)):
        best = _best_option(char, foe, M, budget, conditional)
        plans[label] = (None if best[0] is None or best[1] <= plain
                        else {"power": best[0], "difficulty": best[3]})
    return plans


def _act(actor, target, plan, M, dodge_bonus=0):
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    td = targeting_difficulty(target, M, dodge_bonus)
    face = d20()
    total = face + actor.attack_bonus(M) + actor.weapon.accuracy

    if plan is None:
        if (total >= td) if on_tie else (total > td):
            apply_damage(target, damage_from(actor, target, total - td, M))
        return

    p = (M.rules["discipline-powers"].get(plan["power"])
         or M.rules["general-powers"][plan["power"]])
    difficulty = plan["difficulty"]
    step = int(p.get("difficulty_per_step", p.get("difficulty_per_extra_attack", 1)))
    steps = max(0, (difficulty - int(p["base_difficulty"])) // step)
    roll = face + actor.attack_bonus(M)
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))

    # Out of stamina: the character simply swings, they do not stand
    # there failing. Attempting a power you cannot pay for is not a
    # thing the rules make you do.
    if actor.stamina < difficulty // divisor:
        if (total >= td) if on_tie else (total > td):
            apply_damage(target, damage_from(actor, target, total - td, M))
        return

    if roll >= difficulty:
        actor.stamina -= min(power_cost(difficulty, roll, M), actor.stamina)
        bonus = steps * int(p.get("damage_per_step", 0))
        pierce = steps * int(p.get("reduction_ignored_per_step", 0))
        swings = 1 + (steps if "difficulty_per_extra_attack" in p else 0)
        for _ in range(swings):
            if (total >= td) if on_tie else (total > td):
                apply_damage(
                    target,
                    damage_from(actor, target, total - td, M,
                                bonus=bonus, pierce=pierce),
                )
    else:
        # Failed the declared difficulty: minimum cost, action spent.
        actor.stamina = max(0, actor.stamina - difficulty // divisor)
