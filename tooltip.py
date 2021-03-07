import tkinter as tk
import math

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.l1 = tk.Label(self, text="Hover over me")
        self.l2 = tk.Label(self, text="", width=40)
        self.l1.pack(side="top")
        self.l2.pack(side="top", fill="x")

        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.l2.configure(text="Hello world")

    def on_leave(self, enter):
        self.l2.configure(text="")

##if __name__ == "__main__":
##    root = tk.Tk()
##    Example(root).pack(side="top", fill="both", expand="true")
##    root.mainloop()

def showStats(who):
    statReadout = tk.Tk()
    statReadout.title('Player Stats')
    statReadout.geometry('400x600-50+50')
    txt = who.name + " the " + who.race 
    name = tk.Label(statReadout,text=txt,background="red")
    name.grid(column=0,columnspan=20,sticky='N')
    txt = math.floor(who.hp_cur)
    txt2 = math.floor(who.hp_max)
    txt = str(txt) + "/" + str(txt2)
    health = tk.Label(statReadout,text="Health",background="red")
    health.grid(column = 0,row=2,columnspan=2,sticky="W")
    healthc = tk.Label(statReadout,text=txt)
    healthc.grid(column = 0,row=3,columnspan=2,sticky="W")
    txt = math.floor(who.experience)
    txt2 = who.level*100
    txt = str(txt) + "/" + str(txt2)
    exp = tk.Label(statReadout,text="Experience",background="Blue",fg="cyan")
    exp.grid(column = 2,row=2,columnspan=2,sticky="W")
    expc = tk.Label(statReadout,text=txt)
    expc.grid(column = 2,row=3,columnspan=2,sticky="W")

    attsh = tk.Label(statReadout,text="Attributes",background="cyan")
    attsh.grid(column=5,row=2,columnspan=2,sticky="W")
    skl = (who.strength-math.floor(who.strength))*10
    float(skl)
    txt = "Strength " + str(math.floor(who.strength)) + "/%0.2f%%" % (skl)
    attstr = tk.Label(statReadout,text=txt)
    attstr.grid(column=5,row=3,columnspan=2,sticky="W")
    skl = (who.dexterity-math.floor(who.dexterity))*10
    float(skl)
    txt = "Dexterity " + str(math.floor(who.dexterity)) + "/%0.2f%%" % (skl)
    attdex = tk.Label(statReadout,text=txt)
    attdex.grid(column=5,row=4,columnspan=2,sticky="W")

    skillh =tk.Label(statReadout,text="Skills",background="orange")
    skillh.grid(column=0,row=5,columnspan=2,sticky="W")
    txt = "Unarmed " + str(math.floor(who.unarmed))
    skun = tk.Label(statReadout,text=txt)
    skun.grid(column=0,row=6,columnspan=1,sticky="W")
    txt = "Dagger " + str(math.floor(who.dagger))
    skda = tk.Label(statReadout,text=txt)
    skda.grid(column=0,row=7,columnspan=1,sticky="W")
    txt = "Sword " + str(math.floor(who.sword))
    sksw = tk.Label(statReadout,text=txt)
    sksw.grid(column=0,row=8,columnspan=1,sticky="W")

    skl = (who.survivalist-math.floor(who.survivalist))*10
    float(skl)
    txt = "Survivalist " + str(math.floor(who.survivalist)) + "/%0.2f%%" % (skl)
    sksu = tk.Label(statReadout,text=txt)
    sksu.grid(column=2,row=6,columnspan=1,sticky="W")
    txt = "Block " + str(who.block)
    skbl = tk.Label(statReadout,text=txt)
    skbl.grid(column=2,row=7,columnspan=1,sticky="W")

