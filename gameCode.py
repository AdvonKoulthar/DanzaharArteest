import random
import math
import racedata as rd

#RandomName
def roll_3d62():
    random.seed()
    roll1 = random.randint(1,6)
    random.seed()
    roll2 = random.randint(1,6)
    random.seed()
    roll3 = random.randint(1,6)
    return roll1+roll2+roll3
vowels = ["a","ae","i","e","ie","ee","ao","au","ai","oo","ou","u"]
vlen = len(vowels)
s_consonant = ["b","c","d","f","ph","g","h","j","k","l","ll","m","n","p","qu","r","s","ss","t","v","w","x","z","y"]
sclen = len(s_consonant)
d_consonant = ["ck","ch","kr"]
def rand_vowel():
    random.seed()
    v = vowels[random.randint(0,vlen-1)]
    return v
def rand_scons():
    random.seed()
    c = s_consonant[random.randint(0,sclen-1)]
    return c
def rand_name():
    random.seed()
    nleng = math.floor(roll_3d62()/3+1)
    cname = ""
    lv = 0
    for i in range (nleng):
        pick = random.randint(0,2)
        if pick == 0 or lv == 2:
            cname = cname + rand_vowel()
            lv = 0
        else:
            cname = cname + rand_scons()
            lv += 1
    return cname.capitalize()
#LocDefs
terrain_data = {
    0: {"name" : "grassland",
        "creatureTps" : ["human","goblin","ghol"]
        },
    
    1: {"name" : "forest",
        "creatureTps" : ["human","firbolg","elf"]
        },
    
    2: {"name" : "mountain",
        "creatureTps" : ["dwarf","orc","ghol"]
        },
    
    3: {"name" : "hills",
        "creatureTps" : ["dwarf","ghol","human","halfling"]
        },
    
    4: {"name" : "desert",
        "creatureTps" : ["human","ghol","orc"]
        },
    
    5: {"name" : "jungle",
        "creatureTps" : ["human","firbolg","elf","orc"]
        },
    
    6: {"name" : "lake",
        "creatureTps" : ["human","firbolg","elf","halfling"]
        }


    }

    

#end terrain Data
#creature type from dictionary    
def ctfd(ttype):
    try:
        miniarray = terrain_data[ttype]["creatureTps"]
        pickC = random.randint(0,len(miniarray)-1)
        return miniarray[pickC]
    except KeyError:
        print("It's NOT REAL!")
#minicreaturetype or random?
def randOrNot(ttype,who):
    for i in range(len(place_types)):
        if place_types[i] == ttype:
            ttype = i
    randn = random.randint(1,5)
    if randn == 1:
        randRace(who)
    else:
        rtxt = ctfd(ttype)
        who.race = rtxt
        rd.adaptMe(who,who.race)
        
        
#Location stuff
place_types = ["grassland","forest","mountain","hills","desert","jungle","lake"]
allZones = []

class Zone:
    def __init__(self):
        self.neighborNorth = None
        self.neighborSouth = None
        self.neighborWest = None
        self.neighborEast = None
        self.places = []
        self.zx = None
        self.zy = None
        
        create_places_for_zone(self)
        allZones.append(self)
        
class Place:
    def __init__(self):
        self.type = random.choice(place_types)
        meVillage(self)
        self.x = None
        self.y = None
        self.zone = None
        self.name = None
        self.feature = None
        if self.type == "village":
            self.name = rand_name()
            villageFeature(self)

def create_places_for_zone(zone):
    for y in range(10):
        for x in range(10):
            newPlace = Place()
            newPlace.x = x
            newPlace.y = y
            newPlace.zone = zone
            zone.places.append(newPlace)

def searchforzone(looker,nsew):
    #1324
    size = len(allZones)
    lookx = looker.zx
    looky = looker.zy
    if nsew == 1:
        looky += 1
    if nsew == 3:
        looky -= 1
    if nsew == 2:
        lookx += 1
    if nsew == 4:
        lookx -= 1
    for i in range(size):
        if allZones[i].zx == lookx:
            if allZones[i].zy == looky:
                return allZones[i]
    return None
def meVillage(who):
    chance = 5
    randInt = random.randint(1,100)
    if randInt <= chance:
        who.type = "village"
town_features = ["potion seller","fancy inn","training ground","temple", "weaponsmith"]
def villageFeature(where):
    where.feature = town_features[random.randint(0,len(town_features)-1)]
    
def buyPotion(who):
    #txt = "\"Naturally you want to buy one of my potions. I'll give you one of the watered down ones. You couldn't handle my masterpieces.\""
    #fprint(txt)
    if who.money > 9:
        who.money -= 10
        who.inventory.append("potion")
        #txt = "\"Here you are.\""
        #fprint(txt)
        #txt = "The potion seller hands you a potion, and you hand over the coins."
        #fprint(txt)
    #else:
        #txt = "\"Hold one moment! Though this is hardly fit to be called a potion, I'm not running a charity! Come back when you have money!\""
        #fprint(txt)
        #txt = "You don't have enough money."
        #fprint(txt)
        
    

def matchLoc(creature):
    where = creature.location
    creature.x = where.x
    creature.y = where.y
    creature.zone = where.zone

def go_north(who):
    if who.y != 0:
        arrayCur = (who.y*10)+(who.x)
        who.location = who.zone.places[arrayCur-10]
        matchLoc(who)       
    else:
        if who.zone.neighborNorth == None:
            loopypath = searchforzone(who.zone,1)
            if loopypath == None:
                newZ = Zone()
                who.zone.neighborNorth = newZ
                newZ.neighborSouth = who.zone
                newZ.zx = who.zone.zx
                newZ.zy = who.zone.zy+1
            else:
                who.zone.neighborNorth = loopypath
                loopypath.neighborSouth = who.zone
        who.zone = who.zone.neighborNorth
        arrayLoc = 90+(who.x)
        who.location = who.zone.places[arrayLoc]
        matchLoc(who)
        
def go_south(who):
    if who.y != 9:
        arrayCur = (who.y*10)+(who.x)
        who.location = who.zone.places[arrayCur+10]
        matchLoc(who)       
    else:
        if who.zone.neighborSouth == None:
            loopypath = searchforzone(who.zone,3)
            if loopypath == None:
                newZ = Zone()
                who.zone.neighborSouth = newZ
                newZ.neighborNorth = who.zone
                newZ.zx = who.zone.zx
                newZ.zy = who.zone.zy-1
            else:
                who.zone.neighborSouth = loopypath
                loopypath.neighborNorth = who.zone
        who.zone = who.zone.neighborSouth
        arrayLoc = (who.x)
        who.location = who.zone.places[arrayLoc]
        matchLoc(who)
def go_west(who):
    if who.x != 0:
        arrayCur = (who.y*10)+(who.x)
        who.location = who.zone.places[arrayCur-1]
        matchLoc(who)       
    else:
        if who.zone.neighborWest == None:
            loopypath = searchforzone(who.zone,4)
            if loopypath == None:
                newZ = Zone()
                who.zone.neighborWest = newZ
                newZ.neighborEast = who.zone
                newZ.zx = who.zone.zx-1
                newZ.zy = who.zone.zy
            else:
                who.zone.neighborWest = loopypath
                loopypath.neighborEast = who.zone
        who.zone = who.zone.neighborWest
        arrayLoc = (who.y*10)+9
        who.location = who.zone.places[arrayLoc]
        matchLoc(who)
def go_east(who):
    if who.x != 9:
        arrayCur = (who.y*10)+(who.x)
        who.location = who.zone.places[arrayCur+1]
        matchLoc(who)       
    else:
        if who.zone.neighborEast == None:
            loopypath = searchforzone(who.zone,2)
            if loopypath == None:
                newZ = Zone()
                who.zone.neighborEast = newZ
                newZ.neighborWest = who.zone
                newZ.zx = who.zone.zx+1
                newZ.zy = who.zone.zy
            else:
                who.zone.neighborEast = loopypath
                loopypath.neighborWest = who.zone
        who.zone = who.zone.neighborEast
        arrayLoc = (who.y*10)
        who.location = who.zone.places[arrayLoc]
        matchLoc(who)


#CREATURE STUFF
p_races = ["human","dwarf","ghol","goblin","orc","thrall","firbolg","elf","halfling"]

def randRace(who):
    rrti= random.randint(0,len(p_races)-1)
    wr = p_races[rrti]
    who.race = wr
    

#Random stuff
def itemSearch(who,what):
    irepeat = len(who.inventory)
    for i in range(irepeat):
            if who.inventory[i] == what:
                return True
