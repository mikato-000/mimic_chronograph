from tkinter import *
import math, random
chrono = Tk()

BLK = "#000000"
PANEL = "#1c1c1c"
WHITE = "#ffffff"

chrono.geometry("260x250")
chrono.title("Chronograph")
chrono.resizable(False, False)
chrono.configure(bg=BLK)

#variables that can manipulate
psi = 100
ib_length = 470
bbs = 0.2
rof = 30

#staph, don't manipulate these
rng = random.uniform(1, 15)
bbcount = 0
#def func
def semi_fire():
    global psi,ib_length,bbs,rof,rng,bbcount
    #fps
    base_fps = 115 * math.sqrt(psi) - 750
    length = math.sqrt(ib_length / 470)
    weight = math.sqrt(0.20/bbs)
    fps = round(rng + base_fps * length * weight, 2)
    
    #joules
    v = fps * 0.3048
    m = bbs / 1000
    joules = round(0.5 * m * v **2, 2)

    #j/cm^2
    area = math.pi * (0.3)**2
    jcm2 = round(joules/ area, 3)

    bbcount = bbcount + 1

    fpsnum.config(text=fps,font=("Arial", 33))
    rofnum.config(text="1",font=("Arial", 33))
    joulesnum.config(text=joules)
    jcm.config(text=jcm2)
    count.config(text=bbcount)
    rng = random.uniform(1, 15)
    return

def full_fire():
    global psi,ib_length,bbs,rof,rng,bbcount
    #fps
    base_fps = 115 * math.sqrt(psi) - 750
    length = math.sqrt(ib_length / 470)
    weight = math.sqrt(0.20/bbs)
    fps = round(rng + base_fps * length * weight, 2)
    
    #joules
    v = fps * 0.3048
    m = bbs / 1000
    joules = round(0.5 * m * v **2, 2)

    #j/cm^2
    area = math.pi * (0.3)**2
    jcm2 = round(joules/ area, 3)

    bbcount = bbcount + rof

    fpsnum.config(text=fps,font=("Arial", 33))
    rofnum.config(text=rof,font=("Arial", 33))
    joulesnum.config(text=joules)
    jcm.config(text=jcm2)
    if bbcount >= 100:
        count.config(font=("Arial", 20))
    count.config(text=bbcount)
    rng = random.uniform(1, 15)
    return bbcount

#UI dawwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#info
info=Frame(chrono,bg=BLK,)
info.pack(side=TOP,pady=(10,0))

jbox=LabelFrame(info, text="Joules",fg=WHITE,bg=BLK,padx=15,pady=12)
jbox.pack(side=LEFT,padx=10)

joulesnum=Label(jbox,text="0.00",fg=WHITE,bg=BLK)
joulesnum.pack()

jcbox=LabelFrame(info, text="J/cm^2",fg=WHITE,bg=BLK,padx=15,pady=12)
jcbox.pack(side=LEFT,padx=10)
jcm=Label(jcbox,text="0.000",fg=WHITE,bg=BLK)
jcm.pack()

ammo=LabelFrame(info, text="Ammo",fg=WHITE,bg=BLK,padx=11,pady=2)
ammo.pack(side=LEFT,padx=10)
mm=Label(ammo,text="6mm",fg=WHITE,bg=BLK)
mm.pack()
bbsweight=Label(ammo,text=str(bbs) + "g",fg=WHITE,bg=BLK)
bbsweight.pack()

#bigboisinfotypeshit

biginfo=Frame(chrono,bg=BLK,width=220, height=120)
biginfo.pack(side=TOP)
biginfo.pack_propagate(False)
             
number=Frame(biginfo, bg= BLK)
number.pack(side=LEFT)
rofnum=Label(number,text="------",fg=WHITE,bg=BLK,font=("Arial", 40))
rofnum.pack()
bar=Frame(number,bg=WHITE,width=40)
bar.pack(fill="x", pady=1)
fpsnum=Label(number,text="------",fg=WHITE,bg=BLK,font=("Arial", 40))
fpsnum.pack()

rflabel=Frame(biginfo,bg=BLK)
rflabel.pack(side=RIGHT,padx=(35,0))
roftxtlabel=Label(rflabel,text="ROF",fg=BLK,bg=WHITE,font=("Arial", 12))
roftxtlabel.pack()
count=Label(rflabel,text="0",fg=WHITE,bg=BLK,font=("Arial", 30))
count.pack()
fpstxt=Label(rflabel,text="FPS",fg=BLK,bg=WHITE,font=("Arial", 12))
fpstxt.pack()

#big button mimic some typeshit trigger or something idk

trigger=Frame(chrono,bg=BLK)
trigger.pack(pady=(5, 0))

semi=Button(trigger,text="SEMI",font=("Arial", 12),width=8,fg=WHITE,bg=PANEL, command=semi_fire)
semi.pack(side=LEFT,padx=(0,10))

full=Button(trigger,text="FULL",font=("Arial", 12),width=8,fg=WHITE,bg=PANEL, command=full_fire)
full.pack(side=LEFT)



chrono.mainloop()