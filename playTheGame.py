import tkinter as tk
import random
import gameCode as gc
import combatCode as cc
import math
import racedata as rd
import tooltip

        
class Creature:
    def __init__(self):
        self.hp_cur = 10
        self.hp_max = 10
        self.x = 0
        self.y = 0
        self.race = "human"
        self.name = "Nevets"
        self.strength = 1
        self.dexterity = 1
        self.armor = 0
        self.experience = 0
        self.learning = 1
        self.level = 1
        self.location = None
        self.zone = None
        self.money = 0
        #Skills
        self.survivalist = 1
        self.unarmed = 0
        self.dagger = 0
        self.sword = 0
        self.block = 1
        self.axe = 0
        self.inventory = ["potion"]

        #Items
        NewWeap = cc.weapon()
        cc.isStandard(NewWeap,0)
        self.weapon = NewWeap

    def skillUp(me,skil2,mag):
        new = getattr(me,skil2,0)+(((mag*random.randint(1,3)*me.learning)+math.ceil(me.learning-1))/1000)
        setattr(me,skil2,new)

    def __del__(self):
        del self.weapon

#Random Stuff
def roll_3d6():
    random.seed()
    roll1 = random.randint(1,6)
    random.seed()
    roll2 = random.randint(1,6)
    random.seed()
    roll3 = random.randint(1,6)
    return roll1+roll2+roll3
def qDe(q,e):
    random.seed()
    qq = int(q)
    ee = int(e)
    total = 0
    for i in range(qq):
        total += random.randint(1,ee)
    return int(total)
#TownStuff
def RemoveTownButts():
    print("no")
    if player.location.feature == "potion seller":
        txt = "You walk up to the doors of the potion seller. Smoke billows out, and you see an arrogant fellow behind the counter with a potion in one hand."
        fprint(txt)
        txt = "\"Hmm, what can I do for you traveller?\""
        fprint(txt)
    #haha
def buyPotBut(event):
    if player.location.feature == "potion seller":
        gc.buyPotion(player)
    else:
        txt = "No one sells potions here."
        fprint(txt)
def weaponEnter(event):
    if player.location.feature == "weaponsmith":
        print("yeos buy wea-pon")

def noTownNoButt():
    if player.location.type == "village":
        if player.location.feature == "potion seller":
            shopButt.grid(row=17,column=2,sticky="W")        
    else:
        shopButt.forget()

def generalStoreButt(event):
    print("makebutt")

#Combat stuff
def randomEncounter():
    encounterChance = 25
    if encounterChance < 5:
        encounterChance = 5
    if player.location.type == "village":
        encounterChance = 0
    randroll = random.randint(1,100)
    if randroll <= encounterChance:
        popeye = Creature()
        popeye.money += qDe(2,5)
#        gc.randRace(popeye)
#        rd.adaptMe(popeye,popeye.race)
        gc.randOrNot(player.location.type,popeye)
        global CurPopeye
        CurPopeye = popeye
        global Fighting
        Fighting = True
        makeCombatButtons()
        removement()
        enemyHp.config(image=health10)


def makeCombatButtons():
    attackButt.grid(row=3,column=1,sticky="W")
    attackButt.bind('<Button-1>', attackregBE)
    chargeButt.grid(row=2,column=1,sticky="W")
    chargeButt.bind('<Button-1>', attackchaBE)
    defendButt.grid(row=4,column=1,sticky="W")
    defendButt.bind('<Button-1>', attackdefBE)
    potionButt.grid(row=2,column=2,sticky="W")
    potionButt.bind('<Button-1>', healpotBE)
    blockButt.grid(row=5,column=1,sticky="W")
    blockButt.bind('<Button-1>', attackblockBE)
    fleeButt.grid(row=6,column=1,sticky="W")
    fleeButt.bind('<Button-1>', fleeFightBE)
def removement():
    goNorthButt.grid_forget()
    goSouthButt.grid_forget()
    goWestButt.grid_forget()
    goEastButt.grid_forget()
    restButt.grid_forget()

def removeCombatButtons():
    attackButt.grid_forget()
    fleeButt.grid_forget()
    chargeButt.grid_forget()
    defendButt.grid_forget()
    potionButt.grid_forget()
    blockButt.grid_forget()
def recoverMovementButtons():
    restButt.grid(row=17,column=0,sticky="W")
    goNorthButt.grid(row=17,column=1,sticky="W")
    goWestButt.grid(row=18,column=0,sticky="E")
    goSouthButt.grid(row=18,column=1,sticky="W")
    goEastButt.grid(row=18,column=2,sticky="W")
    
def endFightFunc():
    global Fighting
    Fighting = False
    global CurPopeye
    del CurPopeye
    CurPopeye = None
    removeCombatButtons()
    recoverMovementButtons()
    playHpImg()
    counter_label(label)
    enemyVisual.config(image=camp)
    enemyHp.config(image=healthnot)
    amDed()
    
    
def fleeFightBE(event):
    if Fighting == True:
        opponent = CurPopeye
        pdef = roll_3d6()+player.dexterity-2
        ene_atk = roll_3d6()
        sb = cc.getWSkillN(opponent)
        ene_atk += math.floor(sb)+2
        if ene_atk > pdef:
            odamc = opponent.weapon.count
            odams = opponent.weapon.size
            odam = math.floor(qDe(odamc,odams)+opponent.strength*1.5)
            odam -= player.armor
            if odam < 0:
                odam = 0
            player.hp_cur -= odam
            player.skillUp("hp_max",odam)
            text = ("As you run away the %s strikes you in the back, dealing %i damage!" % (opponent.race,odam))
            #~32 chars
            fprint(text)
        else:
            fprint("They miss!")
        endFightFunc()


def attackregBE(event):
    if Fighting == True:
        patk = roll_3d6()
        pdef = roll_3d6()
        oppResponse(CurPopeye,patk,pdef,1)
def attackdefBE(event):
    if Fighting == True:
        patk = roll_3d6()-2
        pdef = roll_3d6()+2
        oppResponse(CurPopeye,patk,pdef,2)
def attackchaBE(event):
    if Fighting == True:
        patk = roll_3d6()
        pdef = roll_3d6()
        oppResponse(CurPopeye,patk,pdef,3)
def healpotBE(event):
    if Fighting == True:
        if gc.itemSearch(player,"potion") == True:
            player.inventory.remove("potion")
            patk = -5
            pdef = roll_3d6()
            heal = qDe(1,6)
            player.hp_cur += heal
            if player.hp_cur > player.hp_max:
                heal -= (player.hp_cur - math.floor(player.hp_max))
                player.hp_cur = math.floor(player.hp_max)
            txt = "You quaff a potion, healing by %i" % (heal)
            playHpImg()
            oppResponse(CurPopeye,patk,pdef,4)
        else:
            txt = "You don't have one of those!"
        fprint(txt)
def attackblockBE(event):
    if Fighting == True:
        patk = roll_3d6()-4
        pdef = roll_3d6()+2
        player.armor = math.floor(player.block)
        print(player.armor)
        oppResponse(CurPopeye,patk,pdef,5)

def oppResponse(opponent,patk,pdef,origin):
    ene_def = roll_3d6()+opponent.block+opponent.dexterity
    sb = cc.getWSkillN(player)
    if origin != 4:
        patk += math.floor(sb)
    pdef += player.block+player.dexterity
    if patk > ene_def:
        pdamc = player.weapon.count
        pdams = player.weapon.size
        pdam = math.floor(qDe(pdamc,pdams)+player.strength)
        pdam -= opponent.armor
        if pdam < 0:
            pdam = 0
        opponent.hp_cur -= pdam
        text = ("You strike the %s, dealing %i damage!" % (opponent.race,pdam))
        yos = cc.getWSkill(player)
        player.skillUp(yos,2)
        if origin == 2:
            player.skillUp("block",1)
        if origin == 3:
            player.skillUp("strength",1)
        fprint(text)
        oppHpImg(opponent)
    else:
        if origin != 4:
            fprint("You swing, but miss...")
    if opponent.hp_cur < 1:
        player.experience += math.floor(player.learning*opponent.level*10)
        playXpImg()
        player.money += opponent.money
        endFightFunc()
    ene_atk = roll_3d6()
    sb = cc.getWSkillN(opponent)
    ene_atk += math.floor(sb)
    if ene_atk > pdef:
        odamc = opponent.weapon.count
        odams = opponent.weapon.size
        odam = math.floor(qDe(odamc,odams)+opponent.strength)
        odam -= player.armor
        if odam < 0:
            odam = 0
        player.hp_cur -= odam
        player.skillUp("hp_max",odam)
        text = ("The %s slips past your guard, dealing %i damage!" % (opponent.race,odam))
        #~32 chars
        fprint(text)
    else:
        fprint("They miss!")
    if origin == 5:
        player.armor -= math.floor(player.block)
    counter_label(label)
    playHpImg()
    amDed()
def oppHpImg(who):
    perc = (who.hp_cur/who.hp_max)*10
    perfl = math.floor(perc)
    if perfl == 0:
        enemyHp.config(image=health0)
    if perfl == 1:
        enemyHp.config(image=health1)
    if perfl == 2:
        enemyHp.config(image=health2)
    if perfl == 3:
        enemyHp.config(image=health3)
    if perfl == 4:
        enemyHp.config(image=health4)
    if perfl == 5:
        enemyHp.config(image=health5)
    if perfl == 6:
        enemyHp.config(image=health6)
    if perfl == 7:
        enemyHp.config(image=health7)
    if perfl == 8:
        enemyHp.config(image=health8)
    if perfl == 9:
        enemyHp.config(image=health9)
    if perc > 9.5:
        enemyHp.config(image=health10)

def playHpImg():
    perc = (player.hp_cur/math.floor(player.hp_max))*10
    perfl = math.floor(perc)
    if perfl == 0:
        playerHp.config(image=health0)
    if perfl == 1:
        playerHp.config(image=health1)
    if perfl == 2:
        playerHp.config(image=health2)
    if perfl == 3:
        playerHp.config(image=health3)
    if perfl == 4:
        playerHp.config(image=health4)
    if perfl == 5:
        playerHp.config(image=health5)
    if perfl == 6:
        playerHp.config(image=health6)
    if perfl == 7:
        playerHp.config(image=health7)
    if perfl == 8:
        playerHp.config(image=health8)
    if perfl == 9:
        playerHp.config(image=health9)
    if perc > 9.5:
        playerHp.config(image=health10)

def playXpImg():
    perc = (player.experience/player.level/100)*10
    perfl = math.floor(perc)
    if perfl == 0:
        playerXp.config(image=exp0)
    if perfl == 1:
        playerXp.config(image=exp1)
    if perfl == 2:
        playerXp.config(image=exp2)
    if perfl == 3:
        playerXp.config(image=exp3)
    if perfl == 4:
        playerXp.config(image=exp4)
    if perfl == 5:
        playerXp.config(image=exp5)
    if perfl == 6:
        playerXp.config(image=exp6)
    if perfl == 7:
        playerXp.config(image=exp7)
    if perfl == 8:
        playerXp.config(image=exp8)
    if perfl == 9:
        playerXp.config(image=exp9)
    if perc > 9.5:
        playerXp.config(image=exp10)

def amDed():
    if player.hp_cur < 1 - player.survivalist:
        fprint("Omae wa mou shindeiru")
        fprint("Nani?!?!")
        mainScreen.destroy()
        print("You died.")
def gpUpdate():
    gpt = "Gold:%i" % (player.money)
    playerGp.config(text=gpt)
        
#Level Up Stuff
def levelUpP():
    player.experience -= player.level*100
    player.level += 1
    player.hp_max += 2
    player.hp_cur = math.floor(player.hp_max)

#OOC Stuff
def restEvent(event):
    amDed()
    interrupted = False
    if Fighting == False:
        for i in range(8):
            if Fighting == False:
                timePasses()              
                refreshImage()
            else:
                if interrupted == False:
                    text = "After %i hours, a %s interrupts your rest!" % (i,CurPopeye.race)
                    fprint(text)
                    heal = math.floor(((math.floor(player.survivalist)*2)+(player.level))*i/8)+1
                    player.hp_cur += heal
                    if player.hp_cur > player.hp_max:
                        heal -= (player.hp_cur - math.floor(player.hp_max))
                        player.hp_cur = math.floor(player.hp_max)
                    text = "You were interrupted and only heal by %i. Hopefully that is enough." % (heal)
                    fprint(text)
                    interrupted = True
    if Fighting == False:
        heal = player.level+(math.floor(player.survivalist)*2)
        player.hp_cur += heal
        if player.hp_cur > player.hp_max:
            heal -= (player.hp_cur - math.floor(player.hp_max))
            player.hp_cur = math.floor(player.hp_max)
        text = "You rest up, healing for %i health" % (heal)
        fprint(text)

        
    playHpImg()
    if player.location.type == "village":
        player.skillUp("survivalist",1)
    else:
        player.skillUp("survivalist",2)

        
#End OOC stuff

#Change positions
def fakeLoop():
    counter_label(label)
    gpUpdate()
    playHpImg()
    timePasses()
    refreshTime()
    refreshImage()
    noTownNoButt()
    mainScreen.update()
    if Fighting == False:
        if player.experience > player.level*100:
            levelUpP()
    amDed()
def refreshTime():
    global time
    if time < 13:
        hour = time
        apm = "AM"
    if time > 12:
        hour = time-12
        apm = "PM"
    if time == 0:
        hour = 12
        apm = "AM"
    newT = str(hour)+ ":00"+str(apm)
    clock.config(text=newT)
def refreshImage():
    newImg = ghol
    if player.location.type == "forest":
        newImg = ti_forest
    if player.location.type == "hills":
        newImg = ti_hills
    if player.location.type == "desert":
        newImg = ti_desert
    if player.location.type == "grassland":
        newImg = ti_grassland
    if player.location.type == "mountain":
        newImg = ti_mountain
    if player.location.type == "jungle":
        newImg = ti_jungle
    if player.location.type == "lake":
        newImg = ti_lake
    if player.location.type == "village":
        newImg = ti_village
        text = "You are in %s" % (player.location.name)
        fprint(text)
    locationVisual.config(image=newImg)
    newImg = camp
    if CurPopeye != None:
        if CurPopeye.race == "ghol":
            newImg = ghol
        if CurPopeye.race == "dwarf":
            newImg = dwarf
        if CurPopeye.race == "human":
            newImg = human
        if CurPopeye.race == "goblin":
            newImg = goblin
        if CurPopeye.race == "orc":
            newImg = orc
        if CurPopeye.race == "thrall":
            newImg = thrall
        if CurPopeye.race == "firbolg":
            newImg = firbolg
        if CurPopeye.race == "elf":
            newImg = elf
        if CurPopeye.race == "halfling":
            newImg = halfling
    else:
        if player.location.feature == "potion seller":
            newImg = potioneer
        if player.location.feature == "weaponsmith":
            newImg = blacksmith
        if player.location.feature == "temple":
            newImg = priestess
        if player.location.feature == "fancy inn":
            newImg = bartender
    enemyVisual.config(image=newImg)
def fprint(newT):
    text_display.config(text=text_display2.cget("text"))
    text_display2.config(text=text_display3.cget("text"))
    text_display3.config(text=text_display4.cget("text"))
    text_display4.config(text=text_display5.cget("text"))
    #text_display5.config(text=text_display6.cget("text"))
    #text_display6.config(text=text_display7.cget("text"))
    text_display5.config(text=newT)

def increaseHealth(event):
    player.hp_cur = player.hp_cur+1
    counter_label(label)
    fakeLoop()

def northButt(event):
    if Fighting == False:
        gc.go_north(player)
        fprint("You travel.")
        fakeLoop()
def southButt(event):
    if Fighting == False:
        gc.go_south(player)
        fprint("You travel.")
        fakeLoop()
def westButt(event):
    if Fighting == False:
        gc.go_west(player)
        fprint("You travel.")
        fakeLoop()
def eastButt(event):
    if Fighting == False:
        gc.go_east(player)
        fprint("You travel.")
        fakeLoop()
def showStats(event):
    tooltip.showStats(player)


def decreaseHealth(event):
    player.hp_cur = player.hp_cur-1
    counter_label(label)

def counter_label(label):
  def count():
    newT = "Player Health:" + str(player.hp_cur)
    label.config(text=newT)
  count()

#setups
player = Creature()
rd.adaptMe(player,player.race)
player.MyQuests = []
startZ = gc.Zone()
startZ.zx =0
startZ.zy =0
player.location = startZ.places[54]
gc.matchLoc(player)
player.shopping = "False"
global Fighting
Fighting = False
global CurPopeye
CurPopeye = None
CombatActed = False



global time
global day
time = 0
day = 0

def timePasses():
    global time
    global day
    time += 1
    if time == 24:
        time = 0
        day += 1
    randomEncounter()

mainScreen = tk.Tk()
mainScreen.title('Danzahar Adventure')
mainScreen.geometry('800x600-50+50')
#setup Images 170x170
ghol = tk.PhotoImage(file="images/ghol.png")
dwarf = tk.PhotoImage(file="images/jari.png")
human = tk.PhotoImage(file="images/fighter.png")
goblin = tk.PhotoImage(file="images/goblin.png")
thrall = tk.PhotoImage(file="images/thrall.png")
elf = tk.PhotoImage(file="images/elf.png")
firbolg = tk.PhotoImage(file="images/firbolg.png")
orc = tk.PhotoImage(file="images/orc.png")
halfling = tk.PhotoImage(file="images/halfling.png")
camp = tk.PhotoImage(file="images/campfire.png")
potioneer = tk.PhotoImage(file="images/potionseller.png")
blacksmith = tk.PhotoImage(file="images/blacksmith.png")
priestess = tk.PhotoImage(file="images/priestess.png")
bartender = tk.PhotoImage(file="images/bartender.png")

health10 = tk.PhotoImage(file="images/health10.png")
health9 = tk.PhotoImage(file="images/health9.png")
health8 = tk.PhotoImage(file="images/health8.png")
health7 = tk.PhotoImage(file="images/health7.png")
health6 = tk.PhotoImage(file="images/health6.png")
health5 = tk.PhotoImage(file="images/health5.png")
health4 = tk.PhotoImage(file="images/health4.png")
health3 = tk.PhotoImage(file="images/health3.png")
health2 = tk.PhotoImage(file="images/health2.png")
health1 = tk.PhotoImage(file="images/health1.png")
health0 = tk.PhotoImage(file="images/health0.png")
healthnot = tk.PhotoImage(file="images/healthnot.png")

exp0 = tk.PhotoImage(file="images/experience0.gif")
exp1 = tk.PhotoImage(file="images/experience1.gif")
exp2 = tk.PhotoImage(file="images/experience2.gif")
exp3 = tk.PhotoImage(file="images/experience3.gif")
exp4 = tk.PhotoImage(file="images/experience4.gif")
exp5 = tk.PhotoImage(file="images/experience5.gif")
exp6 = tk.PhotoImage(file="images/experience6.gif")
exp7 = tk.PhotoImage(file="images/experience7.gif")
exp8 = tk.PhotoImage(file="images/experience8.gif")
exp9 = tk.PhotoImage(file="images/experience9.gif")
exp10 = tk.PhotoImage(file="images/experience10.gif")



moneybag = tk.PhotoImage(file="images/moneybag.gif")

ti_forest = tk.PhotoImage(file="images/forest2.gif")
ti_desert = tk.PhotoImage(file="images/desert.gif")
ti_hills = tk.PhotoImage(file="images/hills.gif")
ti_grassland = tk.PhotoImage(file="images/grassland.gif")
ti_mountain = tk.PhotoImage(file="images/mountain.gif")
ti_jungle = tk.PhotoImage(file="images/jungle.png")
ti_lake = tk.PhotoImage(file="images/lake.png")
ti_village = tk.PhotoImage(file="images/village.png")
#end Images

#General Gui
locationVisual = tk.Label(image=ti_forest)
locationVisual.grid(columnspan=20)
enemyVisual = tk.Label(image=dwarf)
enemyVisual.grid(column=17,row=2,columnspan=3,rowspan=12,sticky="NW")
enemyHp = tk.Label(image=healthnot)
enemyHp.grid(column=16,row=2,columnspan=1,rowspan=12,sticky="NW")

playerHp = tk.Label(image=health10)
playerHp.grid(column=0,row=2,columnspan=1,rowspan=12,sticky="NW")
playerXp = tk.Label(image=exp0)
playerXp.grid(column=0,row=30,columnspan=10,rowspan=1,sticky="NW")
playerGpi = tk.Label(image=moneybag)
playerGpi.grid(column=10,row=30,columnspan=2,rowspan=1,sticky="NW")
playerGp = tk.Label(text="Gold")
playerGp.grid(column=12,row=30,columnspan=2,rowspan=1,sticky="NW")
gpUpdate()





clock = tk.Label(mainScreen,text="12:00am",borderwidth=2, relief="groove")
clock.grid(row=14,column=0,columnspan=20,sticky="W")
label = tk.Label(mainScreen, fg="dark green",borderwidth=2, relief="groove")
label.grid(row=15,column=0,columnspan=4,sticky="W")
counter_label(label)
log_width = tk.Label(mainScreen,text="oO0OooO0Oo Combat Log oO0OooO0Oo")
log_width.grid(row=2, column=5,columnspan=11,rowspan=1,sticky="N")
text_display = tk.Label(mainScreen,text="Nothing interesting",wraplength=300,fg="grey",borderwidth=2, relief="groove",width=30)
text_display.grid(row=3, column=5,columnspan=11,rowspan=1,sticky="N")
text_display2 = tk.Label(mainScreen,text="Nothing interesting",wraplength=300,fg="darkgrey",borderwidth=2, relief="groove",width=30)
text_display2.grid(row=4, column=5,columnspan=11,rowspan=1,sticky="N")
text_display3 = tk.Label(mainScreen,text="Nothing interesting",wraplength=300,fg="darkgrey",borderwidth=2, relief="groove",width=30)
text_display3.grid(row=5, column=5,columnspan=11,rowspan=1,sticky="N")
text_display4 = tk.Label(mainScreen,text="Nothing interesting",wraplength=300,borderwidth=2, relief="groove",width=30)
text_display4.grid(row=6, column=5,columnspan=11,rowspan=1,sticky="N")
text_display5 = tk.Label(mainScreen,text="Nothing interesting",wraplength=300,borderwidth=2, relief="groove",width=30)
text_display5.grid(row=7, column=5,columnspan=11,rowspan=1,sticky="N")
#text_display6 = tk.Label(mainScreen,text="Nothing interesting",wraplength=300)
#text_display6.grid(row=8, column=5,columnspan=11,rowspan=1,sticky="N")
#text_display7 = tk.Label(mainScreen,text="Nothing interesting",wraplength=300)
#text_display7.grid(row=9, column=5,columnspan=11,rowspan=1,sticky="N")
#End GGUI
refreshImage()

#movement
goNorthButt = tk.Button(mainScreen,text="⇧")
goNorthButt.grid(row=17,column=1,sticky="W")
goNorthButt.bind('<Button-1>', northButt)
goWestButt = tk.Button(mainScreen,text="⇦")
goWestButt.grid(row=18,column=0,sticky="E")
goWestButt.bind('<Button-1>', westButt)
goSouthButt = tk.Button(mainScreen,text="⇩")
goSouthButt.grid(row=18,column=1,sticky="W")
goSouthButt.bind('<Button-1>', southButt)
goEastButt = tk.Button(mainScreen,text="⇨")
goEastButt.grid(row=18,column=2,sticky="W")
goEastButt.bind('<Button-1>', eastButt)
mainScreen.bind('<Up>', northButt,add='+')
mainScreen.bind('<Down>', southButt,add='+')
mainScreen.bind('<Left>', westButt,add='+')
mainScreen.bind('<Right>', eastButt,add='+')
#end movement

#Out of Combat
restButt = tk.Button(mainScreen,text="Rest")
restButt.grid(row=17,column=0,sticky="W")
restButt.bind('<Button-1>', restEvent)
shopButt = tk.Button(mainScreen,text="Buy potion-10g")
#shopButt.grid(row=17,column=2,sticky="W")
shopButt.bind('<Button-1>', buyPotBut)

mainScreen.bind('r',restEvent,add='+')
mainScreen.bind('b',buyPotBut,add='+')
#end OOC

#combat
attackButt = tk.Button(mainScreen, text="Attack",borderwidth=2, relief="raised")
fleeButt = tk.Button(mainScreen, text="Flee",borderwidth=2, relief="raised")
chargeButt = tk.Button(mainScreen, text="Charge",borderwidth=2, relief="raised")
defendButt = tk.Button(mainScreen, text="Defensive",borderwidth=2, relief="raised")
potionButt = tk.Button(mainScreen, text="Heal Potion",borderwidth=2, relief="raised")
blockButt = tk.Button(mainScreen, text="Block",borderwidth=2, relief="raised")

mainScreen.bind('a', attackregBE,add='+')
mainScreen.bind('c', attackchaBE,add='+')
mainScreen.bind('d', attackdefBE,add='+')
mainScreen.bind('f', fleeFightBE,add='+')
mainScreen.bind('p', healpotBE,add='+')
mainScreen.bind('b', attackblockBE,add='+')
#end combat

statButt = tk.Button(mainScreen,text="Player Stats")
statButt.bind('<Button-1>', showStats)
statButt.grid(row=19,column=0,columnspan=3,sticky="W")

leaveBut = tk.Button(mainScreen,text="Exit",command=mainScreen.destroy) 
leaveBut.grid(column=0,row=25)




