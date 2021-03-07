import math
import random

class Quest:
    def __init__(self):
        #quest types:[kill,fetch]
        self.type = 0
        self.objective = None
        self.goal = 5
        self.progress = 0
        RandomizeQuest(self)
        print(self.objective)

def RandomizeQuest(quest):
    qtype = 0
    if qtype == 0:
        t_races = ["human","dwarf","ghol","goblin","orc","thrall","firbolg","elf","halfling"]
        rrti= random.randint(0,len(t_races)-1)
        wr = t_races[rrti]
        quest.objective = wr
        quest.goal = random.randint(3,5)

def progressQuest(quest,mag):
    quest.progress += mag

def questComplete(who,quest):
    who.experience += quest.goal*3
    who.money += quest.goal+5
    who.MyQuests.remove(quest)
    del quest
