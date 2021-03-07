import random
import sys
import tkinter as tk

class weapon:
    def __init__(self):
        self.name = "weapon of void"
        self.count = 1
        self.size = 6
        self.skill = None
        self.description = "This is an undefined weapon."
        self.price = 10
        self.enchants = []
#    def __del__(self):
#        print("why must I die")
        
def isStandard(what,which):
        what.name = weaponStandard[which]["name"]
        what.count = weaponStandard[which]["count"]
        what.size = weaponStandard[which]["size"]
        what.skill = weaponStandard[which]["skill"]
        what.price = weaponStandard[which]["price"]

def getWSkillN(who):
    wpn = who.weapon.skill
    num = "who.%s" % (wpn)
    retnum = eval(num)
    return retnum


def getWSkill(who):
    ws = who.weapon.skill
    return ws

weaponStandard = {
    0: {"name" : "unarmed",
        "count" : 1,
        "size" : 3,
        "desc" : "You'll tear apart your opponent with YOUR BARE HANDS! \nIt'll take a while though.\nDoes 1d3 damage.",
        "price" : 0,
        "skill" : "unarmed",
        },
    1: {"name" : "dagger",
        "count" : 1,
        "size" : 4,
        "desc" : "Slightly better than nothing. Poke, poke. \nDoes 1d4 damage.",
        "price" : 10,
        "skill" : "dagger",
        },
    2: {"name" : "longsword",
        "count" : 1,
        "size" : 8,
        "desc" : "Now this is something meant for killing. Have at thee, foul beast! \nDoes 1d8 damage.",
        "price" : 25,
        "skill" : "sword",
        },
    3: {"name" : "hand axe",
        "count" : 1,
        "size" : 6,
        "desc" : "Chop chop! Let's get to work! Effective on flesh AND wood. \nDoes 1d6 damage.",
        "price" : 15,
        "skill" : "axe",
        },
    4: {"name" : "greataxe",
        "count" : 1,
        "size" : 12,
        "desc" : "Good for killing elves. Also killing in general, but it's best used on elves. \nDoes 1d12 damage.",
        "price" : 30,
        "skill" : "axe",
        },
    5: {"name" : "shortspear",
        "count" : 1,
        "size" : 6,
        "desc" : "A small pokey stick. You could roast some marshmallows on this. \nDoes 1d6 damage.",
        "price" : 10,
        "skill" : "spear",
        },
    6: {"name" : "trident",
        "count" : 1,
        "size" : 8,
        "desc" : "A three-pronged weapon, good for disarming...ah who are we kidding. It's a giant fork. \nDoes 1d8 damage.",
        "price" : 25,
        "skill" : "spear",
        },
    7: {"name" : "sickle",
        "count" : 2,
        "size" : 2,
        "desc" : "A tool for reaping wheat, now used to reap lives. Small, but ever so slightly more effective than a dagger. \nDoes 2d2 damage.",
        "price" : 15,
        "skill" : "dagger",
        },
    99: {"name" : "katana",
        "count" : 2,
        "size" : 10,
        "desc" : "None of that 'masterwork bastard sword' crap, this is what katanas deserve. \nDoes 2d10 damage.",
        "price" : 25,
        "skill" : "sword",
        },




    }
