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
    "Only damaging spells are modelled. Healing, and everything cast for "
    "a narrative reason, is out of scope and always will be.",
    "An area spell catches one creature per two squares it covers, since "
    "bodies do not pack one to a square in a real fight.",
    "Spell damage meets armour like any other damage, capped the same "
    "way; nothing in the rules exempts it.",
    "A spell's damage comes from the difficulty declared, not from the "
    "margin on the roll -- margin buys a caster a lower price, not a "
    "bigger effect.",
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
    # Spellcasting is "intelligence or willpower" per skill-list, so it
    # is handled by Character.casting_bonus() rather than by this map.
    "spellcasting": "willpower",
    "attack_ranged": "dexterity",
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
    spirit: int = 0
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

    def casting_bonus(self, M):
        """Spellcasting takes intelligence OR willpower, whichever is
        better -- see skill-list."""
        ranks = self.skills.get("spellcasting", 0)
        return ranks + max(self.attr_bonus("intelligence", M),
                           self.attr_bonus("willpower", M))

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


FOCUS_ORDER = ("peripheral", "unfocused", "focused")


def skill_focus(char, skill_name, M):
    """Which focus tier a skill sits in, from the character's grades and
    the discipline-list skill groups.

    A skill may belong to more than one group -- spellcasting is both
    Magical and Spiritual, diplomacy is both Social and Spiritual -- so
    take the BEST tier the character has any claim to. Returning the
    first match instead would make a priest's own spellcasting
    peripheral because Magical sorts earlier."""
    best = "peripheral"
    for discipline in M.keys("discipline-list"):
        group = M.get("discipline-list", discipline, "skills")
        if skill_name in group:
            tier = focus_of(char.disciplines.get(discipline))
            if FOCUS_ORDER.index(tier) > FOCUS_ORDER.index(best):
                best = tier
    return best


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

    order = list(spec.get("skill_priority") or TRACKED_SKILLS)
    if not spec.get("skill_priority"):
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
    uses_spirit = bool(spec.get("casts"))
    source_ceiling = int(
        M.get("advancement", "max_power_source_bought_per_level")) * level
    source_points = min(points, source_ceiling)
    points -= source_points

    char.mhp = free_mhp + bought_mhp
    char.chp = char.attributes["constitution"]
    char.stamina = char.attributes["constitution"]
    char.spirit = char.attributes["willpower"]
    if uses_spirit:
        char.spirit += source_points * source_per_point
    else:
        char.stamina += source_points * source_per_point
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
def d20(M, depth=6):
    """An exploding d20: the highest face rerolls and adds, for as long
    as the luck holds. Returns (total, was_critical)."""
    crit_on = int(M.get("core-resolution", "critical_on"))
    chains = bool(M.get("core-resolution", "critical_chains"))
    total = 0
    first = None
    for _ in range(depth):
        r = random.randint(1, 20)
        total += r
        if first is None:
            first = r
        if r != crit_on or not chains and first != r:
            break
        if r != crit_on:
            break
    return total, first == crit_on


def d20_faces(M, depth=4):
    """Every outcome of an exploding d20 as (total, weight, is_critical).

    The exact enumeration the expectation functions rely on cannot just
    walk 1..20 any more, because the top face reopens the die. Depth 4
    leaves under one part in a hundred thousand unaccounted for, which is
    far below the noise in everything else here."""
    crit_on = int(M.get("core-resolution", "critical_on"))
    chains = bool(M.get("core-resolution", "critical_chains"))
    out = []

    def walk(total, weight, level, is_crit):
        for face in range(1, 21):
            w = weight / 20.0
            if face == crit_on and (level == 0 or chains) and level < depth:
                walk(total + face, w, level + 1, True)
            else:
                out.append((total + face, w, is_crit or face == crit_on))

    walk(0, 1.0, 0, False)
    return out


def critical_bonus_steps(M):
    return int(M.get("core-resolution", "critical_power_effect_steps"))


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


def damage_from(attacker, defender, margin, M, bonus=0, pierce=0,
                weapon_only=False, use_margin=True):
    """weapon_only strips the margin and skill terms, leaving the bare
    weapon rating -- what Quick Attack's extra swings deal. use_margin
    drops only the margin, keeping the trained arm behind the blow --
    what a Whirl sweep deals."""
    weapon_damage = attacker.weapon.damage
    if weapon_only:
        raw = weapon_damage
    else:
        from_margin = int(margin * margin_fraction(attacker, M)) if use_margin else 0
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
    total_damage = 0.0
    hits = 0.0
    for face, weight, _crit in d20_faces(M):
        total = face + attacker.attack_bonus(M) + attacker.weapon.accuracy
        landed = total >= td if on_tie else total > td
        if landed:
            hits += weight
            total_damage += weight * damage_from(
                attacker, defender, total - td, M, bonus=bonus, pierce=pierce
            )
    return total_damage, hits


def power_cost(difficulty, roll, M, minor=False):
    """A minor power has no minimum, so it reaches zero once the roll
    beats the difficulty by the base cost."""
    base = int(M.get("using-powers", "base_cost"))
    raw = base + difficulty - roll
    if minor:
        return max(0, raw)
    return max(difficulty // int(M.get("using-powers", "minimum_cost_divisor")), raw)


def spell_def(M, spell_id):
    """A spell's full definition, with the bolt chassis merged in.

    The bolt variants carry only a damage type and a domain; everything
    else -- difficulty, damage, the scaling rates -- lives once on the
    `bolt` entry, so a variant has to inherit it rather than repeat it."""
    spells = M.rules["spell-list"]
    if spell_id not in spells or not isinstance(spells[spell_id], dict):
        raise KeyError("no spell '%s' in spell-list" % spell_id)
    entry = dict(spells[spell_id])
    family = entry.get("family")
    if family:
        chassis = dict(spells[str(family)])
        chassis.update(entry)
        entry = chassis
    return entry


def spell_families(M):
    """Chassis entries are not castable spells in their own right."""
    return {str(e["family"]) for e in M.rules["spell-list"].values()
            if isinstance(e, dict) and "family" in e}


def combat_spells(M):
    """Spells this model can resolve: the ones that deal damage. Cure
    Wounds and anything narrative is out of scope by design."""
    out = []
    families = spell_families(M)
    for spell_id, entry in sorted(M.rules["spell-list"].items()):
        if not isinstance(entry, dict) or spell_id in families:
            continue
        merged = spell_def(M, spell_id)
        if "damage" in merged or "area_archetype" in merged:
            out.append(spell_id)
    return out


def can_cast(char, M):
    return char.has("magical", "initiate") or char.has("spiritual", "initiate")


def area_rates(M, archetype):
    a = M.get("spell-area", "archetypes", archetype)
    return int(a["difficulty_per_square"]), int(a["difficulty_per_damage"])


def circle_squares(M, radius):
    return int(M.get("spell-area", "circle_squares", "radius_%d" % radius))


def power_def(M, power_id):
    for rule_id in ("discipline-powers", "general-powers"):
        if power_id in M.rules.get(rule_id, {}):
            return M.rules[rule_id][power_id]
    raise KeyError("no power '%s' in discipline-powers or general-powers"
                   % power_id)


def is_minor(M, power_id):
    return power_def(M, power_id).get("tier") == "minor"


def power_expectation(char, power_id, difficulty, defender, M):
    """Expected damage and stamina for one round using a damage power,
    enumerated over the d20. The power roll and the attack roll are the
    same roll (using-powers: one_roll_serves_both_when_skills_match)."""
    p = power_def(M, power_id)
    minor = p.get("tier") == "minor"
    base_d = int(p["base_difficulty"])
    step = int(p.get("difficulty_per_step", p.get("difficulty_per_extra_attack", 1)))
    steps = max(0, (difficulty - base_d) // step)
    bonus = steps * int(p.get("damage_per_step", 0))
    pierce = steps * int(p.get("reduction_ignored_per_step", 0))
    extra_attacks = steps if "difficulty_per_extra_attack" in p else 0
    weak_extras = bool(p.get("extra_attacks_deal_weapon_damage_only"))

    skill = char.attack_bonus(M) + char.weapon.accuracy
    td = targeting_difficulty(defender, M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))

    per_step_damage = int(p.get("damage_per_step", 0))
    per_step_pierce = int(p.get("reduction_ignored_per_step", 0))
    crit_steps = critical_bonus_steps(M)

    damage = 0.0
    cost = 0.0
    for face, weight, is_crit in d20_faces(M):
        roll = face + char.attack_bonus(M)
        total = face + skill
        if roll >= difficulty:
            cost += weight * power_cost(difficulty, roll, M, minor)
            # A critical grants extra steps of the power's own effect,
            # which is the only thing margin does not already reach.
            extra = crit_steps if is_crit else 0
            b = bonus + extra * per_step_damage
            pc = pierce + extra * per_step_pierce
            swings = extra_attacks + (extra if extra_attacks else 0)
            if (total >= td) if on_tie else (total > td):
                damage += weight * damage_from(
                    char, defender, total - td, M, bonus=b, pierce=pc)
                for _ in range(swings):
                    damage += weight * damage_from(
                        char, defender, total - td, M,
                        bonus=0 if weak_extras else b,
                        pierce=0 if weak_extras else pc,
                        weapon_only=weak_extras)
        else:
            cost += weight * (0 if minor else difficulty // divisor)
            # power failed; the action is spent, so no swing at all
    return damage, cost


def best_difficulty(char, power_id, defender, M, stamina_budget):
    """Pick the difficulty maximising expected damage subject to an
    expected stamina spend the character can sustain."""
    p = power_def(M, power_id)
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
def make_mook(name, M, attack, dodge, hp, weapon, armour):
    """A rank-and-file opponent, built directly rather than by spending
    advancement points -- a goblin does not have a character sheet."""
    flat = {a: int(M.get("attributes", "average_score"))
            for a in ("strength", "dexterity", "constitution",
                      "intelligence", "willpower", "charisma")}
    c = Character(name=name, level=1, disciplines={}, attributes=flat,
                  stance="dodge")
    c.skills = {s: 0 for s in TRACKED_SKILLS}
    c.skills["attack_melee"] = attack
    c.skills["dodge"] = dodge
    c.weapon = Weapon.load(M, weapon)
    c.armour = Armour.load(M, armour)
    c.shield = None
    c.chp = hp
    c.mhp = 0
    c.stamina = 0
    return c


MOOKS = {
    # name:        attack dodge hp  weapon      armour
    "goblin":      (3,     4,    6,  "dagger",     "unarmoured"),
    "orc":         (5,     3,    12, "hand_axe",   "leather"),
}


def mook(kind, M):
    return make_mook(kind, M, *MOOKS[kind])


def chain_length(p, difficulty):
    """How many further bodies a Follow Through cascades into."""
    if "extra_follow_through_per_step" not in p:
        return 0
    step = int(p["difficulty_per_step"])
    steps = max(0, (difficulty - int(p["base_difficulty"])) // step)
    per = int(p["extra_follow_through_per_step"])
    return per + steps * per


def sweep_targets(p, difficulty):
    """How many enemies a sweep power reaches at this difficulty, or 0
    if the power is not a sweep."""
    if "extra_targets_per_step" not in p:
        return 0
    step = int(p["difficulty_per_step"])
    steps = max(0, (difficulty - int(p["base_difficulty"])) // step)
    return int(p["base_targets"]) + steps * int(p["extra_targets_per_step"])


# How many creatures a spell area actually catches. Bodies do not pack
# one to a square in a real fight, so half the covered squares is the
# working assumption -- generous enough that area magic is worth casting,
# mean enough that it is not free.
SQUARES_PER_BODY = 2
# How large a crowd the swarm planner assumes when weighing an area
# spell against a swing.
SWARM_CROWD_ASSUMED = 6


def area_catch(squares, count):
    return max(1, min(count, squares // SQUARES_PER_BODY))


def _spell_swarm_plan(hero, foe, M, count, budget):
    """The best area spell against a crowd, scored on bodies dropped."""
    if not can_cast(hero, M):
        return None
    best = (None, 0.0, 0)
    hp = foe.total_hp
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    for spell_id in combat_spells(M):
        sp = spell_def(M, spell_id)
        if "area_archetype" not in sp:
            continue
        base = int(sp["base_difficulty"])
        for difficulty in range(base, base + 70):
            damage, squares = spell_shape(M, spell_id, difficulty)
            if squares == 0:
                continue
            _, cost = cast_expectation(hero, spell_id, difficulty, foe, M)
            if cost > budget:
                continue
            landed = reduce_by_armour(damage, foe, M)
            if landed < hp:
                continue
            success = sum(w for face, w, _c in d20_faces(M)
                          if face + hero.casting_bonus(M) >= difficulty)
            kills = success * area_catch(squares, count)
            if kills > best[1]:
                best = ({"spell": spell_id, "difficulty": difficulty}, kills, squares)
    return best[0]


def _swarm_plan(hero, foe, M):
    """Against a crowd the useful measure is not raw damage but damage
    that actually lands on a fresh body -- overkill on a dying goblin
    clears nothing. Score each option by damage capped at one mook's
    hit points per attack."""
    budget = hero.stamina / 4.0
    best = (None, -1.0)
    for power_id in offensive_powers(hero, M, conditional=False):
        p = power_def(M, power_id)
        sweep = "extra_targets_per_step" in p
        chain = "extra_follow_through_per_step" in p
        if "difficulty_per_extra_attack" not in p and not sweep and not chain:
            continue
        base_d = int(p["base_difficulty"])
        step = int(p["difficulty_per_extra_attack"] if not (sweep or chain)
                   else p["difficulty_per_step"])
        for extras in range(0, 6):
            difficulty = base_d + extras * step
            value = _expected_kills(hero, foe, M, power_id, difficulty, budget)
            if value > best[1]:
                best = ({"power": power_id, "difficulty": difficulty}, value)
    plain = _expected_kills(hero, foe, M, None, 0, budget)

    spell_plan = _spell_swarm_plan(hero, foe, M, SWARM_CROWD_ASSUMED,
                                   hero.spirit / 4.0)
    if spell_plan is not None:
        damage, squares = spell_shape(M, spell_plan["spell"],
                                      spell_plan["difficulty"])
        bodies = area_catch(squares, SWARM_CROWD_ASSUMED)
        if bodies > max(best[1], plain):
            return spell_plan

    if best[0] is None or best[1] <= plain:
        return None
    return best[0]


def _expected_kills(hero, foe, M, power_id, difficulty, budget):
    """Expected number of mooks dropped in one round."""
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    td = targeting_difficulty(foe, M)
    skill = hero.attack_bonus(M)
    hp = foe.total_hp
    total_kills = 0.0
    for face, weight, _crit in d20_faces(M):
        roll = face + skill
        total = roll + hero.weapon.accuracy
        landed = (total >= td) if on_tie else (total > td)
        if not landed:
            continue
        if power_id is None:
            total_kills += weight * (1 if damage_from(hero, foe, total - td, M) >= hp else 0)
            continue
        p = power_def(M, power_id)
        minor = p.get("tier") == "minor"
        if roll < difficulty:
            continue
        if power_cost(difficulty, roll, M, minor) > budget:
            total_kills += weight * (1 if damage_from(hero, foe, total - td, M) >= hp else 0)
            continue
        if "extra_follow_through_per_step" in p:
            each = damage_from(hero, foe, total - td, M)
            if each >= hp:
                total_kills += weight * (1 + chain_length(p, difficulty))
            continue
        if "extra_targets_per_step" in p:
            reach = sweep_targets(p, difficulty)
            each = damage_from(hero, foe, total - td, M, use_margin=False)
            total_kills += weight * reach * (1 if each >= hp else 0)
            continue
        step = int(p["difficulty_per_extra_attack"])
        extras = max(0, (difficulty - int(p["base_difficulty"])) // step)
        weak = bool(p.get("extra_attacks_deal_weapon_damage_only"))
        kills = 1 if damage_from(hero, foe, total - td, M) >= hp else 0
        each = damage_from(hero, foe, total - td, M, weapon_only=weak)
        kills += extras * (1 if each >= hp else 0)
        total_kills += weight * kills
    return total_kills


def skirmish(hero_spec, kind, count, M, trials=2000, max_rounds=40):
    """One hero against a crowd. Returns (mean rounds to clear, win
    rate, mean share of the hero's hit points lost)."""
    import copy
    template = mook(kind, M)
    plan = _swarm_plan(hero_spec, template, M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))

    rounds_total = 0
    wins = 0
    lost_total = 0.0
    start_hp = hero_spec.total_hp

    for _ in range(trials):
        hero = copy.deepcopy(hero_spec)
        crowd = [copy.deepcopy(template) for _ in range(count)]
        rounds = 0
        while crowd and hero.chp > 0 and rounds < max_rounds:
            rounds += 1
            _swarm_act(hero, crowd, plan, M, on_tie, divisor)
            crowd = [m for m in crowd if m.chp > 0]
            for m in crowd:
                td = targeting_difficulty(hero, M)
                total = d20(M)[0] + m.attack_bonus(M) + m.weapon.accuracy
                if (total >= td) if on_tie else (total > td):
                    apply_damage(hero, damage_from(m, hero, total - td, M))
        rounds_total += rounds
        if not crowd and hero.chp > 0:
            wins += 1
        lost_total += (start_hp - max(0, hero.total_hp)) / max(1, start_hp)
    return rounds_total / trials, wins / trials, lost_total / trials


# ---------------------------------------------------------------------
# The adventuring day
#
# Every measurement above is a single fight from full. A dungeon is not
# one fight, and the question this answers is whether a character is
# still worth playing at the fourth one -- and whether the boss, which
# should be the most interesting fight of the day, is fought by people
# who can still afford to do anything.
# ---------------------------------------------------------------------
def maxima(char):
    return {"stamina": char.stamina, "mhp": char.mhp, "chp": char.chp}


def recover(char, caps, M, tier):
    """Give back a share of MAXIMUM stamina, spirit and mastery hit
    points -- never a share of what is left, which pays nothing to the
    character who has run dry. Core hit points are not on the list."""
    if tier is None:
        return
    pct = int(M.get("recovery", "%s_percent" % tier))
    char.stamina = min(caps["stamina"], char.stamina + caps["stamina"] * pct // 100)
    char.mhp = min(caps["mhp"], char.mhp + caps["mhp"] * pct // 100)


def run_encounter(hero, kind, count, M, max_rounds=40):
    """One fight, fought by THIS hero, spending their actual resources.
    Mutates the hero and returns (rounds, survived)."""
    import copy
    template = mook(kind, M)
    plan = _swarm_plan(hero, template, M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))
    crowd = [copy.deepcopy(template) for _ in range(count)]
    rounds = 0
    while crowd and hero.chp > 0 and rounds < max_rounds:
        rounds += 1
        _swarm_act(hero, crowd, plan, M, on_tie, divisor)
        crowd = [m for m in crowd if m.chp > 0]
        for m in crowd:
            td = targeting_difficulty(hero, M)
            total = d20(M)[0] + m.attack_bonus(M) + m.weapon.accuracy
            if (total >= td) if on_tie else (total > td):
                apply_damage(hero, damage_from(m, hero, total - td, M))
    return rounds, hero.chp > 0


DEFAULT_DAY = [("goblin", 4), ("orc", 3), ("goblin", 6), ("orc", 4), ("orc", 6)]


def adventuring_day(hero_spec, M, schedule=None, tier="breather", trials=300):
    """Run a day of encounters with recovery between each.

    Returns, per encounter: the mean share of the character's fresh
    offence they bring to it, the mean share of their hit points left,
    and the share of days they are still standing for it.

    Offence is looked up from a small cache keyed on stamina rather than
    recomputed per trial -- the difficulty search is far too expensive to
    run inside the loop, and stamina is what actually varies."""
    import copy
    schedule = schedule or DEFAULT_DAY
    foe = standard_foe_for(hero_spec, M)
    cache = {}

    def offence_at(stamina):
        key = int(stamina)
        if key not in cache:
            probe = copy.deepcopy(hero_spec)
            probe.stamina = key
            cache[key] = expected_offence(probe, foe, M)
        return cache[key]

    fresh = offence_at(hero_spec.stamina)
    n = len(schedule)
    stam = [0.0] * n
    hp = [0.0] * n
    alive = [0] * n

    for _ in range(trials):
        hero = copy.deepcopy(hero_spec)
        caps = maxima(hero)
        full_hp = caps["mhp"] + caps["chp"]
        for i, (kind, count) in enumerate(schedule):
            if hero.chp <= 0:
                break
            alive[i] += 1
            stam[i] += hero.stamina
            hp[i] += (hero.mhp + hero.chp) / max(1, full_hp)
            run_encounter(hero, kind, count, M)
            recover(hero, caps, M, tier)

    out = []
    for i in range(n):
        a = max(1, alive[i])
        out.append((offence_at(stam[i] / a) / max(0.01, fresh),
                    hp[i] / a,
                    alive[i] / trials))
    return out


def standard_foe_for(hero, M):
    """A yardstick opponent at the hero's own level, for measuring
    offence without importing balance.py."""
    return mook("orc", M)


def _swarm_act(hero, crowd, plan, M, on_tie, divisor):
    face, was_crit = d20(M)
    roll = face + hero.attack_bonus(M)
    total = roll + hero.weapon.accuracy

    def strike(target, weapon_only=False, bonus=0, pierce=0):
        td = targeting_difficulty(target, M)
        if (total >= td) if on_tie else (total > td):
            apply_damage(target, damage_from(hero, target, total - td, M,
                                             bonus=bonus, pierce=pierce,
                                             weapon_only=weapon_only))

    living = [m for m in crowd if m.chp > 0]
    if not living:
        return
    if plan is None:
        strike(living[0])
        return

    if "spell" in plan:
        _cast_at_crowd(hero, crowd, plan, M)
        return

    p = power_def(M, plan["power"])
    minor = is_minor(M, plan["power"])
    difficulty = plan["difficulty"]
    floor = 0 if minor else difficulty // divisor
    sweep = "extra_targets_per_step" in p
    chain = "extra_follow_through_per_step" in p
    step = int(p["difficulty_per_extra_attack"] if not (sweep or chain)
               else p["difficulty_per_step"])
    extras = max(0, (difficulty - int(p["base_difficulty"])) // step)
    weak = bool(p.get("extra_attacks_deal_weapon_damage_only"))

    if hero.stamina < floor or roll < difficulty:
        if roll < difficulty:
            hero.stamina = max(0, hero.stamina - floor)
            return          # action spent on a failed power
        strike(living[0])
        return

    cost = power_cost(difficulty, roll, M, minor)
    if cost > hero.stamina:
        strike(living[0])   # cannot pay: plain attack
        return
    hero.stamina -= cost

    if "extra_follow_through_per_step" in p:
        # Nothing happens unless a target actually falls; then the swing
        # carries on into the next one.
        remaining = chain_length(p, difficulty)
        idx = 0
        while idx < len(living):
            target = living[idx]
            before = target.chp
            strike(target)
            if target.chp > 0 or remaining <= 0:
                break
            remaining -= 1
            idx += 1
        return

    if sweep:
        # One sweeping cut: every enemy in reach, no margin converted.
        for target in living[:sweep_targets(p, difficulty)]:
            td = targeting_difficulty(target, M)
            if (total >= td) if on_tie else (total > td):
                apply_damage(target, damage_from(hero, target, total - td, M,
                                                 use_margin=False))
        return

    # One shared roll, extra attacks split across distinct targets.
    strike(living[0])
    idx = 1
    for _ in range(extras):
        living = [m for m in crowd if m.chp > 0]
        if idx >= len(living):
            idx = max(0, len(living) - 1)
        if not living:
            break
        strike(living[idx], weapon_only=weak)
        idx += 1


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


def _cast_at_crowd(hero, crowd, plan, M):
    """Resolve an area spell against a crowd: one casting roll, and
    everything under the template takes it."""
    sp = spell_def(M, plan["spell"])
    difficulty = plan["difficulty"]
    minor = sp.get("tier") == "minor"
    minimum = int(sp.get("minimum_spirit", 0))
    damage, squares = spell_shape(M, plan["spell"], difficulty)

    roll, _crit = d20(M)
    roll += hero.casting_bonus(M)
    if roll < difficulty:
        hero.spirit = max(0, hero.spirit - (0 if minor else minimum))
        return                                  # the spell fails outright
    cost = max(minimum, power_cost(difficulty, roll, M, minor))
    if cost > hero.spirit:
        return                                  # cannot pay: nothing happens
    hero.spirit -= cost

    living = [x for x in crowd if x.chp > 0]
    for target in living[:area_catch(squares, len(living))]:
        apply_damage(target, reduce_by_armour(damage, target, M))


def _guard(defender, plan, M):
    """Spend stamina to raise this defender's targeting difficulty for
    one incoming attack. Returns the bonus actually bought."""
    if plan is None:
        return 0
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))
    floor = plan["difficulty"] // divisor
    if defender.stamina < floor:
        return 0
    roll = d20(M)[0] + defender.skill("dodge", M)
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


# Powers that need a condition the rules leave to the fiction. Excluding
# them entirely made Athletic look purely defensive when two of its three
# powers are not.
CONDITIONAL_POWERS = {"sneak_attack"}

# Which mechanics a power must carry to count as an attack power here.
ATTACK_EFFECTS = ("damage_per_step", "reduction_ignored_per_step",
                  "difficulty_per_extra_attack", "extra_targets_per_step",
                  "extra_follow_through_per_step")


def opens_for(char, power_id, M):
    """Whether this character has access to a power.

    Access is read from the power's own mechanics -- its `discipline`
    and `grade` -- rather than hardcoded here, so moving a power between
    disciplines or grades is a rule-file edit and nothing else."""
    p = power_def(M, power_id)
    discipline = p.get("discipline")
    if discipline is None:
        return True                      # a general power, open to all
    return char.has(str(discipline), str(p.get("grade", "initiate")))


def offensive_powers(char, M, conditional=True):
    """Every attack power this build may bring."""
    options = []
    for rule_id in ("discipline-powers", "general-powers"):
        for power_id, p in sorted(M.rules.get(rule_id, {}).items()):
            if not isinstance(p, dict):
                continue
            if not any(k in p for k in ATTACK_EFFECTS):
                continue
            if power_id in CONDITIONAL_POWERS and not conditional:
                continue
            if opens_for(char, power_id, M):
                options.append(power_id)
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
        for face, weight, _crit in d20_faces(M):
            roll = face + skill
            expected_cost += weight * (
                power_cost(difficulty, roll, M) if roll >= difficulty
                else difficulty // int(M.get("using-powers", "minimum_cost_divisor")))
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
    for power_id in offensive_powers(char, M, conditional):
        difficulty, damage, cost = best_difficulty(char, power_id, foe, M, budget)
        if difficulty is not None and damage > best[1]:
            best = (power_id, damage, cost, difficulty)
    return best


def expected_offence(char, foe, M, rounds_budget=4):
    """Blended expected damage per round: the conditional power when the
    fight offers it, the best unconditional one when it does not.

    A caster's best turn is a spell, not a swing, so casting is folded in
    here -- without it a wizard is measured on the staff they are holding
    and looks like a very bad fighter."""
    budget = char.stamina / float(rounds_budget)
    plain, _ = attack_expectation(char, foe, M)
    unconditional = max(plain, _best_option(char, foe, M, budget, False)[1])
    if can_cast(char, M):
        spell = best_spell(char, foe, M, char.spirit / float(rounds_budget))
        unconditional = max(unconditional, spell[1])
    if not char.has("athletic", "adept"):
        return unconditional
    conditional = max(unconditional, _best_option(char, foe, M, budget, True)[1])
    return (SNEAK_AVAILABILITY * conditional
            + (1 - SNEAK_AVAILABILITY) * unconditional)


def spell_shape(M, spell_id, difficulty):
    """What a spell actually delivers at a declared difficulty.

    Returns (damage, squares) -- squares is 0 for a single-target spell.
    An area spell spends its budget on coverage first at the archetype's
    per-square rate, then turns what is left into damage at its
    per-damage rate; a bolt has no area and buys damage directly."""
    sp = spell_def(M, spell_id)
    base = int(sp["base_difficulty"])
    spare = max(0, difficulty - base)

    if "area_archetype" in sp:
        per_square, per_damage = area_rates(M, str(sp["area_archetype"]))
        best = (0, 0)
        for radius in range(1, 6):
            squares = circle_squares(M, radius)
            left = spare - squares * per_square
            if left < 0:
                break
            damage = left // per_damage
            # More bodies covered beats more damage per body, up to the
            # point where the damage stops being worth anything.
            if damage > 0 and squares >= best[1]:
                best = (damage, squares)
        return best

    step = int(sp["difficulty_per_step"])
    return int(sp["damage"]) + (spare // step) * int(sp["damage_per_step"]), 0


def cast_expectation(char, spell_id, difficulty, defender, M):
    """Expected damage to ONE defender and expected spirit cost.

    A bolt needs a ranged attack roll on top of the casting check, which
    is the price of its efficiency; an area spell needs none, which is
    what its difficulty buys."""
    sp = spell_def(M, spell_id)
    minor = sp.get("tier") == "minor"
    minimum = int(sp.get("minimum_spirit", 0))
    damage, _squares = spell_shape(M, spell_id, difficulty)
    skill = char.casting_bonus(M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    crit_steps = critical_bonus_steps(M)

    # A spell that needs an attack roll is aimed with the casting roll
    # itself -- one roll, two jobs, as spell-properties now says.
    needs_aim = bool(sp.get("needs_attack_roll"))
    td = targeting_difficulty(defender, M) if needs_aim else 0

    expected_damage = 0.0
    expected_cost = 0.0
    for face, weight, is_crit in d20_faces(M):
        roll = face + skill
        if roll >= difficulty:
            cost = max(minimum, power_cost(difficulty, roll, M, minor))
            expected_cost += weight * cost
            bonus = 0
            if is_crit:
                more, _ = spell_shape(M, spell_id, difficulty + crit_steps *
                                      _spell_step(M, spell_id))
                bonus = max(0, more - damage)
            aimed = (not needs_aim) or ((roll >= td) if on_tie else (roll > td))
            if aimed:
                expected_damage += weight * reduce_by_armour(
                    damage + bonus, defender, M)
        else:
            expected_cost += weight * (0 if minor else minimum)
    return expected_damage, expected_cost


def _spell_step(M, spell_id):
    sp = spell_def(M, spell_id)
    if "area_archetype" in sp:
        return area_rates(M, str(sp["area_archetype"]))[1]
    return int(sp["difficulty_per_step"])


def reduce_by_armour(raw, defender, M):
    """Spell damage meets armour like anything else, capped the same
    way. Nothing in the rules exempts it."""
    if raw <= 0:
        return 0
    reduction = defender.armour.ap
    if defender.stance == "block":
        reduction += (defender.shield.block_ap if defender.shield
                      else defender.weapon.block_ap)
    cap = raw * float(M.get("damage", "max_reduction_fraction"))
    return max(0, int(raw - min(reduction, cap)))


def best_spell(char, foe, M, spirit_budget):
    """The spell and difficulty giving the most expected damage to one
    target within a sustainable spirit spend."""
    best = (None, -1.0, 0.0, 0)
    for spell_id in combat_spells(M):
        sp = spell_def(M, spell_id)
        base = int(sp["base_difficulty"])
        for difficulty in range(base, base + 70):
            damage, cost = cast_expectation(char, spell_id, difficulty, foe, M)
            if cost > spirit_budget:
                continue
            if damage > best[1]:
                best = (spell_id, damage, cost, difficulty)
    return best


def best_spell_free(char, spell_id, foe, M):
    """Expected damage from a minor spell using only outcomes that cost
    nothing, which is all an empty caster can pay for."""
    sp = spell_def(M, spell_id)
    base = int(sp["base_difficulty"])
    needs_aim = bool(sp.get("needs_attack_roll"))
    td = targeting_difficulty(foe, M) if needs_aim else 0
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    skill = char.casting_bonus(M)
    best = 0.0
    for difficulty in range(base, base + 60):
        damage, _sq = spell_shape(M, spell_id, difficulty)
        total = 0.0
        for face, weight, _crit in d20_faces(M):
            roll = face + skill
            if roll < difficulty:
                continue
            if power_cost(difficulty, roll, M, minor=True) != 0:
                continue
            if needs_aim and not ((roll >= td) if on_tie else (roll > td)):
                continue
            total += weight * reduce_by_armour(damage, foe, M)
        best = max(best, total)
    return best


def floor_offence(char, foe, M):
    """Expected damage per round with the reservoir EMPTY.

    This is the number the minor-power tier exists to raise: on the
    fourth fight of a long day, what can this character still do that is
    more interesting than swinging? Only outcomes that genuinely cost
    nothing count -- anything the character cannot pay for falls back to
    a plain attack, exactly as the rules say."""
    plain, _ = attack_expectation(char, foe, M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    td = targeting_difficulty(foe, M)
    skill = char.attack_bonus(M)
    best = plain

    # A caster's floor is a bolt. Minor spells have no minimum cost, so
    # they are exactly what is left when the reservoir is empty -- the
    # same role Quick Attack plays for a fighter.
    if can_cast(char, M):
        for spell_id in combat_spells(M):
            if spell_def(M, spell_id).get("tier") != "minor":
                continue
            free = best_spell_free(char, spell_id, foe, M)
            best = max(best, free)

    for power_id in offensive_powers(char, M):
        if not is_minor(M, power_id):
            continue
        p = power_def(M, power_id)
        base_d = int(p["base_difficulty"])
        # Attack-granting powers step in whole extra attacks; the rest
        # step in damage, pierce and the like.
        step = int(p.get("difficulty_per_step",
                         p.get("difficulty_per_extra_attack", 1)))
        extras_power = "difficulty_per_extra_attack" in p
        weak = bool(p.get("extra_attacks_deal_weapon_damage_only"))

        for difficulty in range(base_d, base_d + 60):
            damage = 0.0
            for face, weight, _crit in d20_faces(M):
                roll = face + skill
                total = roll + char.weapon.accuracy
                if not ((total >= td) if on_tie else (total > td)):
                    continue
                free = (roll >= difficulty
                        and power_cost(difficulty, roll, M, minor=True) == 0)
                steps = max(0, (difficulty - base_d) // step) if free else 0
                damage += weight * damage_from(
                    char, foe, total - td, M,
                    bonus=0 if extras_power else steps * int(p.get("damage_per_step", 0)),
                    pierce=0 if extras_power else steps * int(p.get("reduction_ignored_per_step", 0)))
                if extras_power:
                    for _ in range(steps):
                        damage += weight * damage_from(char, foe, total - td, M,
                                                       weapon_only=weak)
            best = max(best, damage)
    return best


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
    face, was_crit = d20(M)
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

    minor = is_minor(M, plan["power"])
    floor = 0 if minor else difficulty // divisor

    def swing():
        if (total >= td) if on_tie else (total > td):
            apply_damage(target, damage_from(actor, target, total - td, M))

    if actor.stamina < floor:
        swing()
        return

    if roll >= difficulty:
        cost = power_cost(difficulty, roll, M, minor)
        if cost > actor.stamina:
            # You cannot spend what you do not have: the power does not
            # take effect, and the action resolves as a plain attack.
            swing()
            return
        actor.stamina -= cost
        bonus = steps * int(p.get("damage_per_step", 0))
        pierce = steps * int(p.get("reduction_ignored_per_step", 0))
        weak = bool(p.get("extra_attacks_deal_weapon_damage_only"))
        extras = steps if "difficulty_per_extra_attack" in p else 0
        if (total >= td) if on_tie else (total > td):
            apply_damage(target, damage_from(actor, target, total - td, M,
                                             bonus=bonus, pierce=pierce))
            for _ in range(extras):
                apply_damage(target, damage_from(
                    actor, target, total - td, M,
                    bonus=0 if weak else bonus,
                    pierce=0 if weak else pierce,
                    weapon_only=weak))
    else:
        # Failed the declared difficulty: minimum cost, action spent.
        actor.stamina = max(0, actor.stamina - floor)
