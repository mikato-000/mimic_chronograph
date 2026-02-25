from tkinter import *
chrono = Tk()

BLK = "#000000"
PANEL = "#1c1c1c"
WHITE = "#ffffff"

chrono.geometry("260x250")
chrono.title("Chronograph")
chrono.resizable(False, False)
chrono.configure(bg=BLK)

#UI dawwwwwwwwwwwwwwwwwwwwwwwwwwwwww
#info
info=Frame(chrono,bg=BLK)
info.pack(side=TOP,pady=(10,0))

jbox=LabelFrame(info, text="Joules",fg=WHITE,bg=BLK,padx=15,pady=12)
jbox.pack(side=LEFT,padx=10)
joules=Label(jbox,text="0.000",fg=WHITE,bg=BLK)
joules.pack()

jcbox=LabelFrame(info, text="J/cm^2",fg=WHITE,bg=BLK,padx=15,pady=12)
jcbox.pack(side=LEFT,padx=10)
jcm=Label(jcbox,text="0.000",fg=WHITE,bg=BLK)
jcm.pack()

ammo=LabelFrame(info, text="Ammo",fg=WHITE,bg=BLK,padx=11,pady=2)
ammo.pack(side=LEFT,padx=10)
mm=Label(ammo,text="6mm",fg=WHITE,bg=BLK)
mm.pack()
bbsweight=Label(ammo,text="0.2g",fg=WHITE,bg=BLK)
bbsweight.pack()

#bigboisinfotypeshit

biginfo=Frame(chrono,bg=BLK)
biginfo.pack(side=TOP)
number=Frame(biginfo)
number.pack(side=LEFT)
rof=Label(number,text="- - - -",fg=WHITE,bg=BLK,font=("Arial", 40))
rof.pack()
bar=Frame(number,bg=WHITE,width=40)
bar.pack(fill="x", pady=1)
fps=Label(number,text="- - - -",fg=WHITE,bg=BLK,font=("Arial", 40))
fps.pack()

rflabel=Frame(biginfo,bg=BLK)
rflabel.pack(side=RIGHT,padx=(35,0))
roftxt=Label(rflabel,text="ROF",fg=BLK,bg=WHITE,font=("Arial", 12))
roftxt.pack()
count=Label(rflabel,text="0",fg=WHITE,bg=BLK,font=("Arial", 30))
count.pack()
fpstxt=Label(rflabel,text="FPS",fg=BLK,bg=WHITE,font=("Arial", 12))
fpstxt.pack()

#big button mimic some typeshit trigger or something idk

trigger=Frame(chrono,bg=BLK)
trigger.pack()

semi=Button(trigger,text="SEMI",font=("Arial", 12),width=8,fg=WHITE,bg=PANEL)
##semi.config(command=)
semi.pack(side=LEFT,padx=(0,10))

full=Button(trigger,text="FULL",font=("Arial", 12),width=8,fg=WHITE,bg=PANEL)
##full.config(command=)
full.pack(side=LEFT)



chrono.mainloop()