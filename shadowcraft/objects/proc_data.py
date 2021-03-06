# None should be used to indicate unknown values
# The Proc class takes these parameters:
# stat, value, duration, proc_name, default_behaviour, max_stacks=1, can_crit=True, spell_behaviour=None
# Assumed heroic trinkets have the same behaviour as the non-heroic kin.
# behaviours must have a 'default' key so that the proc is properly initialized.
allowed_procs = {
    #generic
    'rogue_poison': {
        'stat': 'weird_proc',
        'value': 0,
        'duration': 0,
        'proc_name': 'rogue_poison',
        'type': 'perc',
        'icd': 0,
        'proc_rate': 1,
        'trigger': 'all_attacks'
    },
    #potions
    'draenic_agi_pot': {
        'stat': 'stats',
        'value': {'agi':1000},
        'duration': 25,
        'proc_name': 'Draenic Agi Potion',
        'item_level': 100,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'draenic_agi_prepot': {
        'stat': 'stats',
        'value': {'agi':1000},
        'duration': 23,
        'proc_name': 'Draenic Agi Prepot',
        'item_level': 100,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'virmens_bite': {
        'stat': 'stats',
        'value': {'agi':456},
        'duration': 25,
        'proc_name': 'Virmens Bite',
        'item_level': 90,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'virmens_bite_prepot': {
        'stat': 'stats',
        'value': {'agi':456},
        'duration': 23,
        'proc_name': 'Virmens Bite',
        'item_level': 90,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    #weapon enchant support
    'mark_of_the_shattered_hand_dot': {
        'stat': 'physical_dot',
        'value': 750,
        'duration': 6,
        'proc_name': 'Mark of the Shattered Hand DOT',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 3.5,
        'haste_scales': True,
        'trigger': 'all_attacks',
    },
    #racials
    'touch_of_the_grave': {
        'stat': 'spell_damage',
        'value': 0,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Touch of the Grave',
        'type': 'icd',
        'icd': 15,
        'proc_rate': .20,
        'trigger': 'all_attacks'
    },
    'rocket_barrage': {
        'stat': 'spell_damage',
        'value': 0,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Rocket Barrage',
        'type': 'icd',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    #gear procs
    'fury_of_xuen': {
        'stat':'physical_damage',
        'value': 1,
        'duration': 0,
        'proc_name': 'Fury of Xuen',
        'scaling': 0.0,
        'item_level': 0,
        'type': 'rppm',
        'source': 'unique',
        'icd': 3,
        'proc_rate': 1.74, #1.55 mut, 1.15 com, 1.0 sub
        'haste_scales': True,
        'trigger': 'all_attacks'
    },
    'legendary_capacitive_meta': {
        'stat':'spell_damage',
        'value': 280,
        'duration': 0,
        'max_stacks': 5,
        'proc_name': 'Lightning Strike (meta)',
        'scaling': 0.0,
        'item_level': 541,
        'type': 'rppm',
        'source': 'unique',
        'icd': 1,
        'proc_rate': 19.27, #1.789 mut, 1.136 com, 1.114 sub
        'haste_scales': True,
        'trigger': 'all_attacks'
    },
    'archmages_incandescence': {
        'stat':'stats_modifier',
        'value': {'agi':.10},
        'duration': 10,
        'proc_name': 'Archmages Incandescence',
        'scaling': 0.0,
        'item_level': 541,
        'type': 'rppm',
        'source': 'unique',
        'icd': 1,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'archmages_greater_incandescence': {
        'stat':'stats_modifier',
        'value': {'agi':.15},
        'duration': 10,
        'proc_name': 'Archmages Greater Incandescence',
        'scaling': 0.0,
        'item_level': 541,
        'type': 'rppm',
        'source': 'unique',
        'icd': 1,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    #6.0 procs
    'humming_blackiron_trigger': {
        'stat': 'stats',
        'value': {'crit':131},
        'duration': 10,
        'proc_name': 'Humming Blackiron Trigger',
        'upgradable': True,
        'scaling': 0.2969999909 * 10.5,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'meaty_dragonspine_trophy': {
        'stat': 'stats',
        'value': {'haste':1913},
        'duration': 10,
        'proc_name': 'Meaty Dragonspine Trophy',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'formidable_jar_of_doom': {
        'stat': 'stats',
        'value': {'mastery':1743},
        'duration': 10,
        'proc_name': 'Formidable Jar of Doom',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'scales_of_doom': {
        'stat': 'stats',
        'value': {'multistrike':1743},
        'duration': 10,
        'proc_name': 'Scales of Doom',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'blackheart_enforcers_medallion': {
        'stat': 'stats',
        'value': {'multistrike':1665},
        'duration': 10,
        'proc_name': 'Blackheart Enforcers Medallion',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'lucky_doublesided_coin': {
        'stat': 'stats',
        'value': {'agi':1467},
        'duration': 20,
        'proc_name': 'Lucky Double-sided Coin',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 665,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'beating_heart_of_the_mountain': {
        'stat': 'stats',
        'value': {'multistrike':1467},
        'duration': 20,
        'proc_name': 'Beating Heart of the Mountain',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 665,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'skull_of_war': {
        'stat': 'stats',
        'value': {'crit':1396},
        'duration': 20,
        'proc_name': 'Skull of War',
        'upgradable': True,
        'scaling': 4.0000000000,
        'item_level': 640,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'primal_combatants_ioc': {
        'stat': 'stats',
        'value': {'agi':505},
        'duration': 20,
        'proc_name': 'Primal Combatants Insignia of Conquest',
        'upgradable': True,
        'scaling': 1.7480000257,
        'item_level': 620,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'primal_combatants_boc': {
        'stat': 'stats',
        'value': {'versatility':358},
        'duration': 20,
        'proc_name': 'Primal Combatants Badge of Conquest',
        'upgradable': True,
        'scaling': 1.2384999990,
        'item_level': 620,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'gorashans_lodestone_spike': {
        'stat': 'stats',
        'value': {'multistrike':1060},
        'duration': 15,
        'proc_name': 'Gorashans Lodestone Spike',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 630,
        'type': 'icd',
        'source': 'trinket',
        'icd': 90,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'turbulent_vial_of_toxin': {
        'stat': 'stats',
        'value': {'mastery':1060},
        'duration': 15,
        'proc_name': 'Turbulent Vial of Toxin',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 630,
        'type': 'icd',
        'source': 'trinket',
        'icd': 90,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'kihras_adrenaline_injector': {
        'stat': 'stats',
        'value': {'mastery':1060},
        'duration': 20,
        'proc_name': 'Kihras Adrenaline Injector',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 630,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'witherbarks_branch': {
        'stat': 'stats',
        'value': {'haste':1383},
        'duration': 10,
        'proc_name': 'Witherbarks Branch',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 630,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'munificent_emblem_of_terror': {
        'stat': 'stats',
        'value': {'crit':1200},
        'duration': 10,
        'proc_name': 'Munificent Emblem of Terror',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 615,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'void-touched_totem': {
        'stat': 'stats',
        'value': {'mastery':540},
        'duration': 20,
        'proc_name': 'Void-Touched Totem',
        'upgradable': True,
        'scaling': 2.3333330154,
        'item_level': 604,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115, #correct?
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'smoldering_heart_of_hyperious': {
        'stat': 'stats',
        'value': {'mastery':540},
        'duration': 20,
        'proc_name': 'Smoldering Heart of Hyperious',
        'upgradable': True,
        'scaling': 2.3333330154,
        'item_level': 607,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115, #correct?
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'draenic_philosophers_stone': {
        'stat': 'stats',
        'value': {'agi':771},
        'duration': 15,
        'proc_name': 'Draenic Philosophers Stone',
        'upgradable': True,
        'scaling': 2.6670000553,
        'item_level': 620,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55, #correct?
        'proc_rate': 0.35,
        'trigger': 'all_attacks'
    },
    'rabid_talbuk_horn': {
        'stat': 'stats',
        'value': {'agi':430},
        'duration': 20,
        'proc_name': 'Rabid Talbuk Horn',
        'upgradable': True,
        'scaling': 2.0000000000,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'excavated_highmaul_knicknack': {
        'stat': 'stats',
        'value': {'agi':430},
        'duration': 20,
        'proc_name': 'Excavated Highmaul Knicknack',
        'upgradable': True,
        'scaling': 2.0000000000,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'springrain_stone_of_rage': {
        'stat': 'stats',
        'value': {'mastery':572},
        'duration': 20,
        'proc_name': 'Springrain Stone of Rage',
        'upgradable': True,
        'scaling': 2.3333330154,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55, #correct?
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'tormented_tooth_of_ferocity': {
        'stat': 'stats',
        'value': {'haste':800},
        'duration': 20,
        'proc_name': 'Tormented Tooth of Ferocity',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    #5.4 procs
    'assurance_of_consequence': { #DBC - 197491
        'stat': 'stats',
        'value': {'agi':268},
        'duration': 20,
        'proc_name': 'Assurance of Consequence',
        'upgradable': True,
        'scaling': 4.000,
        'item_level': 572,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'haromms_talisman': { #DBC - 203539
        'stat': 'stats',
        'value': {'agi':14037},
        'duration': 10,
        'proc_name': 'Haromms Talisman',
        'upgradable': True,
        'scaling': 2.9730000496,
        'item_level': 572,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 10,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'sigil_of_rampage': {
        'stat': 'stats',
        'value': {'agi':14037},
        'duration': 15,
        'proc_name': 'Sigil of Rampage',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 572,
        'type': 'icd',
        'source': 'trinket',
        'icd': 85,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'ticking_ebon_detonator': {
        'stat': 'stats',
        'value': {'agi':1275 * 10.5},
        'duration': 10,
        'proc_name': 'Ticking Ebon Detonator',
        'upgradable': True,
        'scaling': 0.2703000009 * 10.5,
        'item_level': 572,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 10,
        'proc_rate': 1.00,
        'trigger': 'all_attacks'
    },
    'thoks_tail_tip': {
        'stat': 'stats',
        'value': {'str':14037},
        'duration': 20,
        'proc_name': 'Thoks Tail Tip',
        'upgradable': True,
        'scaling': 2.9730000496,
        'item_level': 572,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'discipline_of_xuen': {
        'stat': 'stats',
        'value': {'mastery':9943},
        'duration': 20,
        'proc_name': 'Discipline of Xuen',
        'upgradable': True,
        'scaling': 2.9730000496,
        'item_level': 535,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    # Old Enchants
    'bad_juju': {
        'stat': 'stats',
        'value': {'agi':8756},
        'duration': 10,
        'proc_name': 'Bad Juju',
        'upgradable': True,
        'scaling': 2.4749999046,
        'item_level': 541,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 10,
        'proc_rate': 1.1,
        'trigger': 'all_attacks'
    },
    'talisman_of_bloodlust': {
        'stat': 'stats',
        'value': {'haste':1836},
        'duration': 10,
        'proc_name': 'Talisman of Bloodlust',
        'upgradable': True,
        'scaling': 0.5189999938,
        'max_stacks': 5,
        'item_level': 541,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 3.5,
        'trigger': 'all_attacks'
    },
    'renatakis_soul_charm': {
        'stat': 'stats',
        'value': {'agi':8756},
        'duration': 10,
        'proc_name': 'Renataki\'s Soul Charm',
        'upgradable': True,
        'scaling': 0.4499999881*5.5,
        'item_level': 541,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 10,
        'proc_rate': 1.21,
        'trigger': 'all_attacks'
    },
    'vicious_talisman_of_the_shado-pan_assault': {
        'stat': 'stats',
        'value': {'agi':8800},
        'duration': 20,
        'proc_name': 'Talisman of the Shado-pan Assault',
        'upgradable': True,
        'scaling': 2.9700000286,
        'item_level': 522,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'terror_in_the_mists': {
        'stat': 'stats',
        'value': {'crit':6808},
        'duration': 20,
        'proc_name': 'Terror in the Mists',
        'upgradable': True,
        'scaling': 4.000,
        'item_level': 496,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'bottle_of_infinite_stars': {
        'stat': 'stats',
        'value': {'agi':3653},
        'duration': 20,
        'proc_name': 'Bottle of Infinite Stars',
        'upgradable': True,
        'scaling': 2.000,
        'item_level': 496,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'relic_of_xuen': {
        'stat': 'stats',
        'value': {'agi':3027},
        'duration': 15,
        'proc_name': 'Relic of Xuen',
        'upgradable': True,
        'scaling': 1.5684000254,
        'item_level': 476,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.2,
        'trigger': 'all_attacks',
        'on_crit': True
    },
    'corens_cold_chromium_coaster': {
        'stat': 'stats',
        'value': {'agi':3027},
        'duration': 15,
        'proc_name': 'Corens Cold Chromium Coaster',
        'upgradable': True,
        'scaling': 2.9719998837,
        'item_level': 476,
        'type': 'icd',
        'source': 'trinket',
        'icd': 50,
        'proc_rate': 0.10,
        'trigger': 'all_attacks',
        'on_crit': True
    },
    'searing_words': {
        'stat': 'stats',
        'value': {'agi':3386},
        'duration': 25,
        'proc_name': 'Searing Words',
        'upgradable': True,
        'scaling': 2.2666659355,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 85,
        'proc_rate': 0.45,
        'trigger': 'all_attacks',
        'on_crit': True
    },
    'windswept_pages': {
        'stat': 'stats',
        'value': {'haste':3386},
        'duration': 20,
        'proc_name': 'Windswept Pages',
        'upgradable': True,
        'scaling': 2.1666660309,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 65,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'kiroptyric_sigil': {
        'stat': 'stats',
        'value': {'agi':2029},
        'duration': 15,
        'proc_name': 'Kiroptyric Sigil',
        'upgradable': True,
        'scaling': 2.4760000706,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 90,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'rickets_magnetic_fireball': {
        'stat': 'stats',
        'value': {'crit':1700},
        'duration': 20,
        'proc_name': 'Rickets Magnetic Fireball',
        'upgradable': True,
        'scaling': 2.4779999256,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'ancient_petrified_seed': {
        'stat': 'stats',
        'value': {'agi':1277},
        'duration': 15,
        'proc_name': 'Ancient Petrified Seed',
        'upgradable': True,
        'scaling': 1.6480000019,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'gerps_perfect_arrow': {
        'stat': 'stats',
        'value': {'agi':3480},
        'duration': 20,
        'proc_name': 'Gerps Perfect Arrow',
        'upgradable': True,
        'scaling': 2.4749999046,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'woundripper_medallion': {
        'stat': 'stats',
        'value': {'crit':3838},
        'duration': 15,
        'proc_name': 'Woundripper Medallion',
        'upgradable': True,
        'scaling': 1.6499999762,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'flashing_steel_talisman': {
        'stat': 'stats',
        'value': {'agi':4232},
        'duration': 15,
        'proc_name': 'Flashing Steel Talisman',
        'upgradable': True,
        'scaling': 2.4749999046,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 90,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'hawkmasters_talon': {
        'stat': 'stats',
        'value': {'haste':3595},
        'duration': 15,
        'proc_name': 'Hawkmasters Talon',
        'upgradable': True,
        'scaling': 1.6499999762,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'jade_bandit_figurine': {
        'stat': 'stats',
        'value': {'haste':3595},
        'duration': 15,
        'proc_name': 'Jade Bandit Figurine',
        'upgradable': True,
        'scaling': 1.6499999762,
        'item_level': 463,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
}

allowed_melee_enchants = {
    #6.0
    'mark_of_the_frostwolf': {
        'stat': 'stats',
        'value': {'multistrike':500},
        'duration': 6,
        'max_stacks': 2,
        'proc_name': 'Mark of the Frostwolf',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 3.0,
        'trigger': 'all_melee_attacks'
    },
    'mark_of_the_shattered_hand': {
        'stat': 'bleed_damage',
        'value': 1500, #triggers mark_of_the_shattered_hand_dot
        'duration': 0,
        'proc_name': 'Mark of the Shattered Hand',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 3.5,
        'haste_scales': True,
        'trigger': 'all_attacks',
    },
    'mark_of_the_thunderlord': {
        'stat': 'stats',
        'value': {'crit':500},
        'duration': 12,
        'proc_name': 'Mark of the Thunderlord',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 2.5,
        'trigger': 'all_melee_attacks'
    },
    'mark_of_the_bleeding_hollow': {
        'stat': 'stats',
        'value': {'mastery':500},
        'duration': 12,
        'proc_name': 'Mark of the Bleeding Hollow',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 2.3,
        'trigger': 'all_melee_attacks'
    },
    'mark_of_warsong': {
        'stat': 'stats',
        'value': {'haste':5.5*100},
        'duration': 20,
        'proc_name': 'Mark of the Bleeding Hollow',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 1.15,
        'trigger': 'all_melee_attacks'
    },
    #5.0
    'windsong': {
        'stat': 'random',
        'value': {'haste':75, 'mastery':75, 'crit':75},
        'duration': 12,
        'proc_name': 'Windsong',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 90,
        'icd': 0,
        'proc_rate': 2.2,
        'trigger': 'all_attacks'
    },
    'dancing_steel': {
        'stat': 'stats',
        'value': {'agi':103},
        'duration': 12,
        'proc_name': 'Dancing Steel',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 90,
        'icd': 0,
        'proc_rate': 2.53,
        'trigger': 'all_melee_attacks'
    },
    'elemental_force': {
        'stat': 'spell_damage',
        'value': 188,
        'duration': 0,
        'proc_name': 'Elemental Force',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 90,
        'icd': 0,
        'proc_rate': 9.17,
        'haste_scales': True,
        'trigger': 'all_attacks'
    },
}