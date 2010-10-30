# This program basically exists to give a sample implementation using the
# framework that's been developed, and to allow me to test and debug my
# calculations as I go along.  At some point a more formal/organized test
# framework should be written - particularly if anyone else ever wants to build
# off this - but for the moment, this will suffice.

from calcs.rogue.Aldriana import AldrianasRogueDamageCalculator
from calcs.rogue.Aldriana import settings

from objects import buffs
from objects import stats
from objects.rogue import rogue_talents
from objects.rogue import rogue_glyphs


# Set up buffs and make sure things at least vaguely work.
test_buffs = buffs.Buffs('stat_multiplier_buff',
    'crit_chance_buff',
    'melee_haste_buff',
    'attack_power_buff',
    'str_and_agi_buff',
    'armor_debuff',
    'spell_damage_debuff',
    'spell_crit_debuff'
    )

assert test_buffs.crit_chance_buff
assert not test_buffs.bleed_damage_debuff


# Set up weapons and make sure things at least vaguely work.
test_mh = stats.Weapon(737, 1.8, is_dagger=True)
test_oh = stats.Weapon(573, 1.4, is_dagger=True)
test_ranged = stats.Weapon(1104, 2.0, is_thrown=True)

assert test_mh._normalization_speed == 1.7
assert test_oh._normalization_speed == 1.7
assert test_ranged._normalization_speed == 2.1


# Set up procs and make sure things at least vaguely work.
test_procs = stats.Procs('chaotic_metagem', 'heroic_deaths_verdict')

assert test_procs.chaotic_metagem
assert not test_procs.heroic_sharpened_twilight_scale


# Set up a calcs object and make sure things at least vaguely work.  Stat
# values are currently pulled from a level 80 gear set, which I will fix as
# soon as I can find or put together a decent estimate of stats for, say, level
# 85 heroic dungeon gear.

test_stats = stats.Stats(20, 3485, 190, 1517, 1086, 641, 899, 666, test_mh, test_oh, test_ranged, test_procs)

assert test_stats.mastery == 666


# Initialize talents and test.

test_talents = rogue_talents.RogueTalents('0333230113022110321', '0020000000000000000', '33')

assert test_talents.assassination.master_poisoner == 1
assert test_talents.combat.killing_spree == 0
assert test_talents.subtlety.opportunity == 3


# Set up glyphs and test.
glyph_list = ['backstab', 'mutilate', 'rupture']
test_glyphs = rogue_glyphs.RogueGlyphs(*glyph_list)

assert test_glyphs.backstab
assert not test_glyphs.vendetta


# Set up settings.
test_cycle = settings.AssassinationCycle()
test_settings = settings.Settings(test_cycle, response_time=1)

# Build a DPS object, and test some functions.
calculator = AldrianasRogueDamageCalculator(test_stats, test_talents, test_glyphs, test_buffs, test_settings)

assert calculator.oh_penalty() == .5
assert calculator.assassins_resolve()

print calculator.backstab_damage(9001)
print calculator.mutilate_damage(9001)

calculator.init_assassination()
