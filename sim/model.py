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
    "Halved movement costs a creature its action half the time it "
    "applies, since the model has no positions and cannot ask whether "
    "the creature could still reach anybody.",
    "A creature caught by a field is still standing in it at the start "
    "of its next turn half the time.",
    "A burn is counted for its full expected duration, as though the "
    "target lives long enough to take every tick.",
    "A burning creature smothers the flames when what the fire will "
    "still take off it is worth more than the turn it spends doing so.",
    "A round taken off an enemy is worth the damage that enemy would "
    "have dealt in it, which is how a stun and a sword swing are "
    "quoted in the same currency.",
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
    move_penalty: int = 0

    @classmethod
    def load(cls, M, key):
        return cls(
            name=key,
            ap=int(M.get("armour", key, "ap")),
            skill_penalty=int(M.get("armour", key, "skill_penalty")),
            move_penalty=int(M.get("armour", key, "move_penalty")),
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
    "resolve": "willpower",
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
    # {condition name: rounds left}, and the damage a burn repeats.
    conditions: dict = field(default_factory=dict)
    burning_damage: int = 0

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


def grade_minimum_level(M, grade):
    """The level a grade cannot be taken below. Only Master has one:
    depth is held back by time rather than by price, so that paying for
    it does not eat the skill ranks its powers need to be used."""
    key = "%s_minimum_level" % grade
    if key not in M.keys("disciplines"):
        return 1
    return int(M.get("disciplines", key))


def buy_disciplines(priorities, budget, M, level=1):
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
            if level < grade_minimum_level(M, grade):
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
    held, disc_spend = buy_disciplines(spec["disciplines"], disc_budget, M,
                                       level)

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
    cached = _FACES_CACHE.get(depth)
    if cached is not None:
        return cached
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
    _FACES_CACHE[depth] = out
    return out


_FACES_CACHE = {}


def critical_bonus_steps(M):
    return int(M.get("core-resolution", "critical_power_effect_steps"))


# ---------------------------------------------------------------------
# Conditions
#
# conditions.md gives every effect that does more than damage the same
# shape: an opposed roll against Fortitude or Resolve, and a duration
# read off the margin. What each one then DOES is read from its own
# mechanics entry rather than switched on its name, so a new condition
# needs no code here as long as it is described in the same vocabulary.
# ---------------------------------------------------------------------
def condition_def(M, name):
    return M.get("conditions", "conditions", name)


def resist_skill(M, name):
    return str(condition_def(M, name)["resisted_with"])


def margin_per_round(M, name):
    """How much margin buys another round. A condition may price itself
    above the general rate; stun does, and that is the whole reason it
    is not the only spell anyone ever casts."""
    c = condition_def(M, name)
    if "margin_per_extra_round" in c:
        return int(c["margin_per_extra_round"])
    return int(M.get("conditions", "margin_per_extra_round"))


def condition_duration(M, name, margin):
    return (int(M.get("conditions", "base_rounds"))
            + margin // margin_per_round(M, name))


_CONDITION_CACHE = {}


def condition_expectation(M, name, difficulty, resist_bonus):
    """(chance it lands, mean rounds it then lasts).

    The number to beat is the DECLARED DIFFICULTY, not the roll that was
    made against it -- conditions.md puts how hard an effect is to shrug
    off on the same lever as everything else a power's user pays for. A
    tie goes to the user, exactly as core-resolution gives ties to the
    actor."""
    key = (name, difficulty, resist_bonus)
    got = _CONDITION_CACHE.get(key)
    if got is not None:
        return got
    landed = 0.0
    rounds = 0.0
    for face, weight, _crit in d20_faces(M):
        total = face + resist_bonus
        if total > difficulty:
            continue
        landed += weight
        rounds += weight * condition_duration(M, name, difficulty - total)
    got = (landed, rounds / landed if landed else 0.0)
    _CONDITION_CACHE[key] = got
    return got


def try_condition(target, name, difficulty, M, damage=0):
    """Roll this defender's resistance for real. Returns the rounds the
    condition lasts, or 0 if it was shrugged off."""
    roll = d20(M)[0] + target.skill(resist_skill(M, name), M)
    if roll > difficulty:
        return 0
    rounds = condition_duration(M, name, difficulty - roll)
    target.conditions[name] = max(target.conditions.get(name, 0), rounds)
    if condition_def(M, name).get("repeats_damage"):
        target.burning_damage = max(target.burning_damage, damage)
    return rounds


def burn_schedule(M, name, damage, rounds):
    """What a burn deals on each of the turns it lasts. Each tick is a
    fraction of the one before, rounding down, and the fire is out when
    that reaches nothing -- so a burn adds up to about one more blow
    however long it burns."""
    frac = float(condition_def(M, name).get("damage_fraction_per_round", 1.0))
    out = []
    current = damage
    for _ in range(max(0, rounds)):
        current = int(current * frac)
        if current <= 0:
            break
        out.append(current)
    return out


def burn_remaining(char, M):
    """What the burn on this creature will still deal if it is left to
    run its course, before armour."""
    total = 0
    for name, left in char.conditions.items():
        if condition_def(M, name).get("repeats_damage"):
            total += sum(burn_schedule(M, name, char.burning_damage, left))
    return total


def would_smother(char, M, action_value):
    """Whether this creature should spend its action putting itself out.

    The rules give it the choice and say nothing about how to make it;
    the model weighs what the fire will still take off it against what
    it would have done with the turn."""
    if not any(condition_def(M, n).get("smothered_by_action")
               for n in char.conditions):
        return False
    left = burn_remaining(char, M)
    if left <= 0:
        return False
    return reduce_by_armour(left, char, M) > action_value


def smother(char, M):
    for name in list(char.conditions):
        if condition_def(M, name).get("smothered_by_action"):
            del char.conditions[name]
    char.burning_damage = 0


def condition_attack_penalty(char, M):
    """What every condition on this creature takes off its attack rolls
    -- and, by the same rule, off the difficulty of hitting it."""
    if not char.conditions:
        return 0
    return sum(int(condition_def(M, n).get("attack_penalty", 0))
               for n in char.conditions)


# How often reaching the target is what limits a crowd member's swing.
# The rules do not model position, so halved movement cannot be resolved
# literally; this is the share of a creature's rounds in which closing
# the distance, rather than the swing itself, is the binding constraint.
MOVEMENT_GATES_ATTACK = 0.5


def action_loss(M, name):
    """The share of a creature's actions this condition costs it. Stun
    takes the whole action; halved movement costs an action only when
    the creature needed that movement to reach anybody."""
    c = condition_def(M, name)
    if c.get("loses_action"):
        return 1.0
    if "movement_fraction" in c:
        return MOVEMENT_GATES_ATTACK * (1.0 - float(c["movement_fraction"]))
    if "attack_penalty" in c:
        # A flat penalty on a d20 removes exactly that many faces.
        return int(c["attack_penalty"]) / 20.0
    return 0.0


def tick_conditions(char, M):
    """Start of this creature's turn: a burn bites, then everything
    counts down. Returns True if the creature can still act."""
    if not char.conditions:
        return True
    for name in char.conditions:
        if not condition_def(M, name).get("repeats_damage"):
            continue
        if char.burning_damage:
            frac = float(condition_def(M, name)
                         .get("damage_fraction_per_round", 1.0))
            char.burning_damage = int(char.burning_damage * frac)
            if char.burning_damage <= 0:
                char.conditions[name] = 0     # the fire has gone out
            else:
                apply_damage(char,
                             reduce_by_armour(char.burning_damage, char, M))
        break
    acts = True
    for name in char.conditions:
        # A condition that works as a penalty on the roll is applied
        # there, by condition_attack_penalty, and must not also be
        # charged an action here. Only the ones that gate the action
        # outright -- stun, and movement that fails to close -- do this.
        if "attack_penalty" in condition_def(M, name):
            continue
        loss = action_loss(M, name)
        if loss >= 1.0 or random.random() < loss:
            acts = False
    for name in list(char.conditions):
        char.conditions[name] -= 1
        if char.conditions[name] <= 0:
            del char.conditions[name]
            if condition_def(M, name).get("repeats_damage"):
                char.burning_damage = 0
    return acts and char.chp > 0


def targeting_difficulty(defender, M, dodge_bonus=0):
    """TD the attacker must beat, per hitting.md. A condition that takes
    points off the defender's attacks takes the same off the difficulty
    of hitting them -- dazed says so explicitly."""
    slack = condition_attack_penalty(defender, M)
    if defender.stance == "block":
        td = defender.skill("block", M)
        if defender.shield:
            td += defender.shield.block_td_bonus
        return td - slack
    td = int(M.get("hitting", "dodge_targeting_base")) + defender.skill("dodge", M)
    td -= slack
    penalty = defender.armour.skill_penalty
    if defender.shield:
        penalty += defender.shield.skill_penalty
    # Untouchable (Athletic master) takes armour's dodge penalty off.
    # How much of it comes off is read from the power, so the shape of
    # the relief can be changed in the rule rather than here.
    td += penalty + untouchable_relief(defender, penalty, M)
    return td + dodge_bonus


def untouchable_relief(defender, penalty, M):
    """How many points of armour's dodge penalty Untouchable gives back.

    `penalty` is negative, and the relief is the positive number that
    cancels some or all of it. Three optional keys on the power shape
    it, and with none of them present it cancels the lot:

      untouchable_max_move_penalty   only armour this light qualifies
      untouchable_penalty_fraction   this share of the penalty comes off
      untouchable_max_points         at most this many points come off
    """
    if not defender.has("athletic", "master") or penalty >= 0:
        return 0
    p = M.get("discipline-powers", "untouchable")
    if "untouchable_max_move_penalty" in p:
        if defender.armour.move_penalty > int(p["untouchable_max_move_penalty"]):
            return 0
    relief = -penalty
    if "untouchable_penalty_fraction" in p:
        relief = int(relief * float(p["untouchable_penalty_fraction"]))
    if "untouchable_max_points" in p:
        relief = min(relief, int(p["untouchable_max_points"]))
    return relief


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


def area_rates(M, archetype, spell=None):
    """(squares covered per point of difficulty, difficulty per damage).

    A spell may override either rate. A field spreads at the diffuse
    rate but buys its damage at the blast rate, because a field nobody
    minds crossing denies nothing."""
    a = M.get("spell-area", "archetypes", archetype)
    per_square = int(a["squares_per_difficulty"])
    per_damage = int(a["difficulty_per_damage"])
    if spell:
        per_square = int(spell.get("squares_per_difficulty", per_square))
        per_damage = int(spell.get("difficulty_per_damage", per_damage))
    return per_square, per_damage


def area_cost(squares, per_point):
    """Squares divided by the coverage rate, rounded up."""
    return -(-squares // per_point)


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
def make_mook(name, M, attack, dodge, hp, weapon, armour, resist=0):
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
    c.skills["fortitude"] = resist
    c.skills["resolve"] = resist
    c.weapon = Weapon.load(M, weapon)
    c.armour = Armour.load(M, armour)
    c.shield = None
    c.chp = hp
    c.mhp = 0
    c.stamina = 0
    return c


MOOKS = {
    # name:        attack dodge hp  weapon      armour        resist
    "goblin":      (3,     4,    6,  "dagger",     "unarmoured", 2),
    "orc":         (5,     3,    12, "hand_axe",   "leather",    4),
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


def _hp_needed(foe, M, spell_id, difficulty, ticks=1.0):
    """How much raw damage per tick it takes to drop this creature
    through its armour, so the planner can tell a killing shape from a
    scratch. Armour bites every tick, so a field that lands three times
    is not the same as one blow of three times the size."""
    for raw in range(1, 200):
        if reduce_by_armour(raw, foe, M) * ticks >= foe.total_hp:
            return raw
    return 200


def _spell_swarm_plan(hero, foe, M, count, budget):
    """The best area spell against a crowd, scored on bodies neutralised.

    A body is neutralised by being killed, and partly neutralised by
    being stunned or slowed: a creature that loses two of the fight's
    rounds has been taken out of two thirds of a six-round fight. That
    is the only way a burst that stuns and a blast that kills can be
    compared without preferring one by definition."""
    if not can_cast(hero, M):
        return None
    best = (None, 0.0)
    skill = hero.casting_bonus(M)
    for spell_id in combat_spells(M):
        sp = spell_def(M, spell_id)
        if "area_archetype" not in sp:
            continue
        base = int(sp["base_difficulty"])
        durations = range(0, 5) if persists(M, spell_id) else (0,)
        cond = spell_condition(M, spell_id)
        resist = (foe.skill(resist_skill(M, cond), M) if cond else 0)
        loss = action_loss(M, cond) if cond else 0.0
        for extra in durations:
            rounds = spell_rounds(M, spell_id, extra)
            ticks = field_ticks(rounds) if persists(M, spell_id) else 1.0
            for difficulty in range(base, base + 70):
                # Pick the shape that kills, not the one that covers most.
                need = _hp_needed(foe, M, spell_id, difficulty, ticks)
                damage, squares, bodies = spell_best_for_crowd(
                    M, spell_id, difficulty, need, count, extra)
                if bodies <= 0:
                    continue
                _d, cost, _c = cast_expectation(hero, spell_id, difficulty,
                                                foe, M, extra)
                if cost > budget:
                    continue
                success = sum(w for face, w, _c in d20_faces(M)
                              if face + skill >= difficulty)
                value = success * bodies
                if cond is not None and loss > 0:
                    # Every body it catches also loses part of the fight.
                    chance, held = condition_expectation(M, cond, difficulty,
                                                         resist)
                    value += (success * bodies * chance * held * loss
                              / TYPICAL_FIGHT_ROUNDS)
                if value > best[1]:
                    best = ({"spell": spell_id, "difficulty": difficulty,
                             "squares": squares, "duration_points": extra},
                            value)
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
                                      spell_plan["difficulty"],
                                      spell_plan["duration_points"])
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
    # What one of these creatures gives up by stopping to put itself
    # out, which is the only thing it can weigh the fire against.
    action_value, _ = attack_expectation(template, hero_spec, M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    divisor = int(M.get("using-powers", "minimum_cost_divisor"))

    rounds_total = 0
    wins = 0
    lost_total = 0.0
    start_hp = hero_spec.total_hp

    for _ in range(trials):
        hero = copy.deepcopy(hero_spec)
        crowd = [copy.deepcopy(template) for _ in range(count)]
        fields = []             # persisting spells still on the ground
        rounds = 0
        while crowd and hero.chp > 0 and rounds < max_rounds:
            rounds += 1
            _swarm_act(hero, crowd, plan, M, on_tie, divisor, fields)
            crowd = [m for m in crowd if m.chp > 0]
            for m in crowd:
                if m.chp <= 0:
                    continue
                _stand_in_fields(m, fields, M)
                if m.chp <= 0:
                    continue
                # Burning bites and stun bites before the swing does.
                if not tick_conditions(m, M):
                    continue
                if would_smother(m, M, action_value):
                    smother(m, M)
                    continue        # the turn went on the flames
                td = targeting_difficulty(hero, M)
                total = (d20(M)[0] + m.attack_bonus(M) + m.weapon.accuracy
                         - condition_attack_penalty(m, M))
                if (total >= td) if on_tie else (total > td):
                    apply_damage(hero, damage_from(m, hero, total - td, M))
            crowd = [m for m in crowd if m.chp > 0]
            _age_fields(fields)
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
def _stand_in_fields(creature, fields, M):
    """A field damages anything inside it at the start of that
    creature's turn. With no positions to consult, a creature caught by
    a field stays in it with probability FIELD_LINGER and is out of it
    for good otherwise."""
    for f in fields:
        # Identity, not equality: Character is a dataclass, so two fresh
        # goblins compare equal and a membership test would burn the
        # wrong one.
        if id(creature) not in f["caught"]:
            continue
        apply_damage(creature, reduce_by_armour(f["damage"], creature, M))
        if random.random() >= FIELD_LINGER:
            f["caught"].discard(id(creature))


def _age_fields(fields):
    for f in fields:
        f["rounds"] -= 1
    fields[:] = [f for f in fields if f["rounds"] > 0 and f["caught"]]


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


def _swarm_act(hero, crowd, plan, M, on_tie, divisor, fields=None):
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
        _cast_at_crowd(hero, crowd, plan, M, fields)
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


def _cast_at_crowd(hero, crowd, plan, M, fields=None):
    """Resolve an area spell against a crowd: one casting roll, and
    everything under the template takes it -- damage now, a condition to
    resist, and, if the spell persists, a field left on the ground."""
    spell_id = plan["spell"]
    sp = spell_def(M, spell_id)
    difficulty = plan["difficulty"]
    extra = plan.get("duration_points", 0)
    minor = sp.get("tier") == "minor"
    minimum = int(sp.get("minimum_spirit", 0))
    lasting = persists(M, spell_id)
    ticks = field_ticks(spell_rounds(M, spell_id, extra)) if lasting else 1.0

    living0 = [x for x in crowd if x.chp > 0]
    if living0:
        need = _hp_needed(living0[0], M, spell_id, difficulty, ticks)
        damage, squares, _bodies = spell_best_for_crowd(
            M, spell_id, difficulty, need, len(living0), extra)
        if squares == 0:
            damage, squares = spell_shape(M, spell_id, difficulty, extra)
    else:
        damage, squares = spell_shape(M, spell_id, difficulty, extra)

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
    caught = living[:area_catch(squares, len(living))]
    cond = spell_condition(M, spell_id)
    for target in caught:
        landed = reduce_by_armour(damage, target, M)
        apply_damage(target, landed)
        if cond is not None and target.chp > 0:
            # The casting roll already made is the number to beat.
            try_condition(target, cond, roll, M, damage=damage)

    if lasting and fields is not None:
        fields.append({"damage": damage,
                       # The cast itself was the first tick, so what is
                       # left on the ground is one round shorter.
                       "rounds": spell_rounds(M, spell_id, extra) - 1,
                       "caught": {id(t) for t in caught if t.chp > 0}})


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


def expected_control(char, foe, M, rounds_budget=4):
    """Expected damage per round the foe never gets to deal, because a
    condition took the round away from it.

    Only casters produce any: no martial power in the list applies a
    condition. It is quoted in damage so that it can be added to
    offence, which is the only way a stun and a sword swing can be
    compared at all."""
    if not can_cast(char, M):
        return 0.0
    return best_spell(char, foe, M, char.spirit / float(rounds_budget))[4]


def spell_condition(M, spell_id):
    """The condition this spell tries to apply, or None."""
    sp = spell_def(M, spell_id)
    if not sp.get("applies_condition"):
        return None
    return str(sp["condition"])


def spell_rounds(M, spell_id, duration_points=0):
    """How many rounds a spell persists. Anything without a duration
    goes off once and is gone -- spell-duration calls that
    instantaneous, and one round is how the model counts it."""
    sp = spell_def(M, spell_id)
    if "duration_rounds" not in sp:
        return 1
    per = int(sp.get("rounds_per_difficulty", 0))
    return int(sp["duration_rounds"]) + per * duration_points


def persists(M, spell_id):
    return "duration_rounds" in spell_def(M, spell_id)


# The chance a creature caught in a field is still in it at the start of
# its next turn. The model has no positions, so it cannot ask; half is
# the midpoint between a crowd that must cross the field to reach the
# caster and one that simply walks around it.
FIELD_LINGER = 0.5


def field_ticks(rounds):
    """Expected number of times a field damages one creature it catches:
    the first tick is certain, each later one only if the creature is
    still standing in it."""
    total = 0.0
    live = 1.0
    for _ in range(max(1, rounds)):
        total += live
        live *= FIELD_LINGER
    return total


def spell_options(M, spell_id, difficulty, duration_points=0):
    """Every (damage, squares) a spell can be shaped into at this
    difficulty. An area spell trades coverage against damage, and which
    trade is right depends entirely on what is being shot at -- so the
    choice belongs to the caller, not to a heuristic buried here.

    `duration_points` is difficulty set aside for extra rounds before
    any of it is spent on area or damage."""
    sp = spell_def(M, spell_id)
    base = int(sp["base_difficulty"])
    spare = max(0, difficulty - base - duration_points)

    if "area_archetype" not in sp:
        step = int(sp["difficulty_per_step"])
        damage = int(sp["damage"]) + (spare // step) * int(sp["damage_per_step"])
        return [(damage, 0)]

    per_point, per_damage = area_rates(M, str(sp["area_archetype"]), sp)
    out = []
    for radius in range(1, 6):
        squares = circle_squares(M, radius)
        left = spare - area_cost(squares, per_point)
        if left < 0:
            break
        out.append((left // per_damage, squares))
    return out or [(0, 0)]


def spell_shape(M, spell_id, difficulty, duration_points=0):
    """The hardest-hitting shape, which is what a single target cares
    about."""
    return max(spell_options(M, spell_id, difficulty, duration_points),
               key=lambda o: o[0])


def spell_best_for_crowd(M, spell_id, difficulty, target_hp, count,
                         duration_points=0):
    """The shape that drops the most bodies: wide enough to reach them,
    still hard enough to kill them. `target_hp` is raw damage needed per
    tick, so a field that gets several ticks is allowed to be weaker."""
    best = (0, 0, 0.0)
    for damage, squares in spell_options(M, spell_id, difficulty,
                                         duration_points):
        if damage < target_hp:
            continue
        bodies = area_catch(squares, count)
        if bodies > best[2]:
            best = (damage, squares, bodies)
    return best


def cast_expectation(char, spell_id, difficulty, defender, M,
                     duration_points=0):
    """Expected damage, spirit cost and control against ONE defender.

    `damage` is everything the spell eventually deals to that creature:
    the hit itself, the further ticks of a field it stands in, and the
    burn a fire spell leaves on it. `control` is damage the defender
    never gets to deal back, because a condition took its action away --
    the only currency a stun and a sword swing can both be quoted in.

    A bolt needs a ranged attack roll on top of the casting check, which
    is the price of its efficiency; an area spell needs none, which is
    what its difficulty buys."""
    sp = spell_def(M, spell_id)
    minor = sp.get("tier") == "minor"
    minimum = int(sp.get("minimum_spirit", 0))
    damage, _squares = spell_shape(M, spell_id, difficulty, duration_points)
    skill = char.casting_bonus(M)
    on_tie = bool(M.get("core-resolution", "success_on_matching_target"))
    crit_steps = critical_bonus_steps(M)

    ticks = (field_ticks(spell_rounds(M, spell_id, duration_points))
             if persists(M, spell_id) else 1.0)

    # The condition is settled by the declared difficulty, so it does
    # not vary with the roll and is worked out once, up here.
    cond = spell_condition(M, spell_id)
    burn = 0.0
    control_each = 0.0
    if cond is not None:
        resist = defender.skill(resist_skill(M, cond), M)
        chance, held = condition_expectation(M, cond, difficulty, resist)
        if condition_def(M, cond).get("repeats_damage"):
            # A burn deals a shrinking share of the blow that started
            # it. Armour bites every tick, so the schedule is reduced
            # tick by tick rather than in one lump.
            burn_ticks = burn_schedule(M, cond, damage, int(round(held)))
            burn = chance * sum(reduce_by_armour(t, defender, M)
                                for t in burn_ticks)
        # What the defender would have done with the rounds it loses.
        foe_dpr, _ = attack_expectation(defender, char, M)
        control_each = chance * held * action_loss(M, cond) * foe_dpr

    # A spell that needs an attack roll is aimed with the casting roll
    # itself -- one roll, two jobs, as spell-properties now says.
    needs_aim = bool(sp.get("needs_attack_roll"))
    td = targeting_difficulty(defender, M) if needs_aim else 0

    expected_damage = 0.0
    expected_cost = 0.0
    expected_control = 0.0
    for face, weight, is_crit in d20_faces(M):
        roll = face + skill
        if roll >= difficulty:
            cost = max(minimum, power_cost(difficulty, roll, M, minor))
            expected_cost += weight * cost
            bonus = 0
            if is_crit:
                more, _ = spell_shape(M, spell_id, difficulty + crit_steps *
                                      _spell_step(M, spell_id),
                                      duration_points)
                bonus = max(0, more - damage)
            aimed = (not needs_aim) or ((roll >= td) if on_tie else (roll > td))
            if aimed:
                landed = reduce_by_armour(damage + bonus, defender, M)
                expected_damage += weight * (landed * ticks + burn)
                expected_control += weight * control_each
        else:
            expected_cost += weight * (0 if minor else minimum)
    return expected_damage, expected_cost, expected_control


def _spell_step(M, spell_id):
    sp = spell_def(M, spell_id)
    if "area_archetype" in sp:
        return area_rates(M, str(sp["area_archetype"]), sp)[1]
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


_BEST_SPELL_CACHE = {}


def best_spell(char, foe, M, spirit_budget):
    """The spell, difficulty and duration giving the best turn against
    one target within a sustainable spirit spend.

    Ranked on damage PLUS control, because a caster who stuns for two
    rounds has had a better turn than one who scratched for one more
    point, and the metric that could not see that was the reason a
    wizard read as a bad fighter.

    Returns (spell, damage, cost, difficulty, control, duration_points)."""
    key = (char.name, char.level, char.casting_bonus(M),
           round(spirit_budget, 3),
           foe.name, foe.total_hp, foe.armour.ap, foe.stance,
           foe.skills.get("fortitude", 0), foe.skills.get("resolve", 0))
    got = _BEST_SPELL_CACHE.get(key)
    if got is not None:
        return got
    best = (None, -1.0, 0.0, 0, 0.0, 0)
    for spell_id in combat_spells(M):
        sp = spell_def(M, spell_id)
        base = int(sp["base_difficulty"])
        durations = range(0, 5) if persists(M, spell_id) else (0,)
        for extra in durations:
            for difficulty in range(base, base + 70):
                damage, cost, control = cast_expectation(
                    char, spell_id, difficulty, foe, M, extra)
                if cost > spirit_budget:
                    continue
                if damage + control > best[1] + best[4]:
                    best = (spell_id, damage, cost, difficulty, control, extra)
    _BEST_SPELL_CACHE[key] = best
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
