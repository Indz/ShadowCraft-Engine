class Race(object):
    rogue_base_stats = {80:(113,189,105,43,67),
                        85:(122,206,114,46,73)}
    racial_stat_offset = {  "human":        (0,0,0,0,0),
                "night elf":    (-4,4,0,0,0),
                "dwarf":        (5,-4,1,-1,-1),
                "gnome":        (-5,2,0,3,0),
                "draenei":      (1,-3,0,0,2),
                "worgen":       (3,2,0,-4,-1),
                "orc":          (3,-3,1,-3,2),
                "undead":       (-1,-2,0,-2,5),
                "tauren":       (5,-4,1,-4,2),
                "troll":        (1,2,0,-4,1),
                "blood elf":    (-3,2,0,3,-2),
                "goblin":       (-3,2,0,3,-2),
    }

    allowed_racials = frozenset([
        "axe_specialization",       #Orc
        "fist_specialization",      #Orc
        "mace_specialization",      #Human, Dwarf
        "stoneform",                #Dwarf
        "expansive_mind",           #Gnome
        "dagger_specialization",    #Gnome
        "sword_1h_specialization",  #Gnome, Human
        "human_spirit",             #Human
        "sword_2h_specialization",  #Human
        "quickness",                #Night Elf
        "heroic_presence",          #Draenei
        "viciousness",              #Worgen
        "blood_fury",               #Orc
        "command",                  #Orc
        "endurance",                #Tauren
        "berserking",               #Troll
        "regeneration",             #Troll
        "beast_slaying",            #Troll
        "throwing_specialization",  #Troll
        "bow_specialization",       #Troll
        "gun_specialization",       #Dwarf
        "arcane_torrent",           #Blood Elf
        "rocket_barrage",           #Goblin
        "time_is_money"             #Goblin
    ])

    racials_by_race = {
                "human":        ["mace_expertise_racial","sword_1h_expertise_racial","sword_2h_specialization","human_spirit"],
                "night elf":    ["quickness"],
                "dwarf":        ["stoneform","gun_specialization","mace_specialization"],
                "gnome":        ["expansive_mind","dagger_specialization","sword_1h_specialization"],
                "draenei":      ["heroic_presence"],
                "worgen":       ["viciousness"],
                "orc":          ["blood_fury","mace_specialization","axe_specialization"],
                "undead":       [],
                "tauren":       ["endurance"],
                "troll":        ["regeneration","beast_slaying","throwing_specialization","bow_specialization"],
                "blood elf":    ["arcane_torrent"],
                "goblin":       ["rocket_barrage","time_is_money"],
    }

    #Note this allows invalid class-race combos
    def __init__(self, race, clas="Rogue", level=85):
        self.clas = str.lower(clas)
        self.race_name = str.lower(race)
        if self.clas == "rogue":
            self.stat_set = Race.rogue_base_stats
        else:
            #Unsupported class, throw error
            assert False, "Unsupported class %{class}s" % {'class': clas}
        if level in self.stat_set:
            self.stats = self.stat_set[level]
        else:
            #Unsupported level, throw error
            assert False, "Unsupported class/level combination %{class}s/%{level}d" \
            % {'class': self.clas, 'level':level}
        if self.race_name in Race.racial_stat_offset:
            self.stats = map(sum,zip(self.stats, Race.racial_stat_offset[race]))
        else:
            #Non-existant race
            assert False, "Unsupported race %{race}s" % {'race':self.race_name}
        self.set_racials()

    def set_racials(self):
        racials = Race.racials_by_race[self.race_name]
        for racial in racials:
            setattr(self, racial, True)

    def __getattr__(self, name):
        # Any racial we haven't assigned a value to, we don't have.
        if name in self.allowed_racials:
            return False
        object.__getattribute__(self, name)

    #3 to expertise
    def axe_specialization(self):
        if self.axe_specialization:
            return 3
        return 0

    #3 to expertise
    def sword_1h_specialization(self):
        if self.sword_1h_specialization:
            return 3
        return 0

    #3 to expertise
    def sword_2h_specialization(self):
        if self.sword_2h_specialization:
            return 3
        return 0

    #3 to expertise
    def mace_specialization(self):
        if self.mace_specialization:
            return 3
        return 0

    #3 to expertise
    def dagger_specialization(self):
        if self.dagger_specialization:
            return 3
        return 0

    #1% to crit
    def throwing_specialization(self):
        if self.throwing_specialization:
            return 1
        return 0

    #1% to crit
    def gun_specialization(self):
        if self.gun_specialization:
            return 1
        return 0

    #1% to crit
    def bow_specialization(self):
        if self.bow_specialization:
            return 1
        return 0

if __name__ == "__main__":
    race = Race("night elf");
    print race.stats
    print race.quickness
    print race.blood_fury
    race2 = Race("undead");
    print race2.stats
    print race2.quickness
    print race2.blood_fury
