import combatCode as cc
def adaptMe(who,race):
    if race == "dwarf":
        who.hp_max += 4
        who.hp_cur += 4
        who.dexterity -= 1
        who.axe += 1
    if race == "goblin":
        who.hp_max -= 2
        who.hp_cur -= 2
        who.dexterity += 1
        who.dagger += 1
    if race == "halfling":
        who.dexterity += 1
    if race == "ghol":
        who.hp_max -= 2
        who.hp_cur -= 2
        who.dexterity += 1
        who.dagger += 1
        del who.weapon
        NewWeap = cc.weapon()
        cc.isStandard(NewWeap,7)
        who.weapon = NewWeap
    if race == "thrall":
        who.hp_max += 5
        who.hp_cur += 5
        who.dexterity -= 1
        who.strength += 1
        who.level = 2
    if race == "orc":
        who.hp_max += 5
        who.hp_cur += 5
        who.strength += 1
        who.level = 2
        who.learning = 0.6
    if race == "human":
        who.learning = 1.3
    if race == "elf":
        who.hp_max -= 2
        who.hp_cur -= 2
        who.dexterity -= 1
    if race == "firbolg":
        who.dexterity += 1
        who.strength += 1
    
