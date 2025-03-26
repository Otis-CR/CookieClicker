import tkinter as tk 
import threading
import time
root = tk.Tk()
cpc = 3
cps = 0
cookies = 0
# First CPS Upgrade information 
cps_Cost = 1000
cps_num = 0
#Second CPS Upgrade information
cps2_Cost = 15000
cps2_num = 0
#Third Autoclicker Upgrade information
cps3_Cost = 150000
cps3_num = 0
#Grandma
grandma = 10
grandma_num = 0
#Windmill
Windmill = 1000
Windmill_num = 0
#Reactor
Reactor = 5000000
Reactor_num = 0
def Counter():
    global cpc
    global cookies
    global cps
    cookies += cpc
    lbl2["text"] = cookies
#Grandma
def Upgrade():
    global cpc
    global cookies
    global grandma
    global grandma_num
    if cookies >= grandma:
        cookies -= grandma
        grandma += 100
        grandma_num += 1
        cpc += 4
        upgrade_1["text"] = f"{grandma} cookies to Upgrade, you have {grandma_num} grandmas"
        cpc_Tracker["text"] = f"Cookies Per Click: {cpc}"
        lbl2["text"] = cookies
    return grandma
#windmill
def Upgrade_2():
    global cpc
    global cookies
    global Windmill
    global Windmill_num
    if cookies >= Windmill:
        cookies -= Windmill
        Windmill_num += 1
        Windmill *= 2
        cpc *= 2
        upgrade_2["text"] = f"{Windmill} cookies to Upgrade, you have {Windmill_num} windmills"
        cpc_Tracker["text"] = f"Cookies Per Click: {cpc}"
        lbl2["text"] = cookies
    return grandma
#CookieFusionReactor
def Upgrade_3():
    global cpc
    global cookies
    global Reactor
    global Reactor_num
    if cookies >= Reactor:
        cookies -= Reactor
        Reactor_num += 1
        Reactor *= 3
        cpc *= 5
        upgrade_3["text"] = f"{Reactor} cookies to Upgrade, you have {Reactor_num} reactors"
        cpc_Tracker["text"] = f"Cookies Per Click: {cpc}"
        lbl2["text"] = cookies
    return grandma
#AutoClicker upgrade the increases the autoclicker output NUMBER 1
def AutoClick_Upgrade():
    global cookies
    global cps
    global cps_Cost
    global cps_num
    if cookies >= cps_Cost:
        cookies -= cps_Cost
        cps_Cost *= 1.5
        cps += 2
        cps_num += 1
        upgrade_4["text"] = f"{cps_Cost} cookies to Upgrade, you have {cps_num} autoclickers"
        cps_tracker["text"] = f"Cookies Per Second: {cps}"
        lbl2["text"] = cookies
#Second Autoclicker Upgrade
def AutoClick_Upgrade_2():
    global cookies
    global cps
    global cps2_Cost
    global cps2_num
    if cookies >= cps2_Cost:
        cookies -= cps2_Cost
        cps2_Cost *= 1.5
        cps *= 2
        cps2_num += 1
        upgrade_5["text"] = f"{cps2_Cost} cookies to Upgrade, you have {cps2_num} autoclickers"
        cps_tracker["text"] = f"Cookies Per Second: {cps}"
        lbl2["text"] = cookies
#Third Autoclicker Upgrade
def AutoClick_Upgrade_3():
    global cookies
    global cps
    global cps3_Cost
    global cps3_num
    if cookies >= cps3_Cost:
        cookies -= cps3_Cost
        cps3_Cost *= 5
        cps *= 4
        cps3_num += 1
        upgrade_6["text"] = f"{cps3_Cost} cookies to Upgrade, you have {cps3_num} autoclickers"
        cps_tracker["text"] = f"Cookies Per Second: {cps}"
        lbl2["text"] = cookies
#Autoclicker runs in the background
def autoclicker():
    global cps
    global cookies
    while True:
        time.sleep(1)
        lbl2["text"] = lbl2["text"] + cps        

# Design
root.geometry("300x300")
root.title ("Cookie Clicker")
Img = tk.PhotoImage(file="./assets/cookie.png").subsample(4)
lbl = tk.Label(root, image = Img)
lbl.grid (row = 0, column = 0)
grandma_img = tk.PhotoImage(file="./assets/upgrade1.png").subsample(4)
Windmill_img = tk.PhotoImage(file= "./assets/upgrade2.png").subsample(4)
Reactor_img = tk.PhotoImage(file="./assets/upgrade3.png").subsample(4)
Autoclicker_img = tk.PhotoImage(file="./assets/upgrade4.png").subsample(4)
Tokamak_img = tk.PhotoImage(file="./assets/upgrade5.png").subsample(4)
Wormhole_img = tk.PhotoImage(file="./assets/upgrade6.png").subsample(4)
lbl2 = tk.Label(root, text = 0)
lbl2.grid(row = 2, column =0)
#Cookie Button
btn = tk.Button(root, image=Img, command = Counter )
btn.grid (row = 0, column = 0)
#Grandma Button/Upgrade
upgrade_1 = tk.Button(root, text= f"{grandma} cookies to Upgrade, you have {grandma_num} grandmas", command = Upgrade, image = grandma_img, compound= "right")
upgrade_1.grid (row=3, column=0)
#Windmill Button/Upgrade
upgrade_2 = tk.Button(root, text= f"{Windmill} cookies to Upgrade, you have {Windmill_num} windmills", command = Upgrade_2, image = Windmill_img, compound= "right")
upgrade_2.grid (row=4, column=0)
#Reactor Button/Upgrade
upgrade_3 = tk.Button(root, text= f"{Reactor} cookies to Upgrade, you have {Reactor_num} reactors", command = Upgrade_3, image = Reactor_img, compound= "right")
upgrade_3.grid (row=5, column=0)
#CPS Button/Upgrade
upgrade_4 = tk.Button(root, text= f"{cps_Cost} cookies to Upgrade, you have {cps_num} autoclickers",command = AutoClick_Upgrade, image = Autoclicker_img, compound = "right")
upgrade_4.grid (row= 6, column=0)
#Tokamak Button/Upgrade
upgrade_5 = tk.Button(root, text= f"{cps2_Cost} cookies to Upgrade, you have {cps2_num} autoclickers", command= AutoClick_Upgrade_2, image= Tokamak_img, compound= "right")
upgrade_5.grid (row=7, column=0)
# WormHole Button/Upgrade
upgrade_6 = tk.Button(root, text= f"{cps3_Cost} cookies to Upgrade, you have {cps3_num} autoclickers", command= AutoClick_Upgrade_3, image= Wormhole_img, compound= "right")
upgrade_6.grid (row=8, column=0)
#CPC Tracker
cpc_Tracker = tk.Label(root, text = f"Cookies Per Click: {cpc}")
cpc_Tracker.grid (row = 9, column = 0)
#cps Tracker
cps_tracker = tk.Label(root, text=f"Cookies persecond: {cps}")
cps_tracker.grid (row=10,column=0)
ent = tk.Entry()
#Calling My Threads

cps_1 = threading.Thread(target = autoclicker)
cps_1.start()


root.mainloop()


