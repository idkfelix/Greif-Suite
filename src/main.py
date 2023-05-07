from wrapper import *
from tools import *

import tkinter as tk
from tkinter import ttk
import sv_ttk

import threading

# Create config if it dosent exist
if not os.path.exists(os.getenv("LOCALAPPDATA")+"\GreifSuite\config.yaml"):
    Tools.SetConfig("ap","ap")

# Create Tk Window
window = tk.Tk()
window.geometry("285x300")
window.title("Greif Suite")

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

### CHAT SPAMMER ###

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Chat")

l1 = ttk.Label(tab1, font=('Helvetica', 12, 'bold'), text="Chat Spammer")
l1.pack(pady=10, padx=10, anchor="center")

# Chat Spammer
e1 = ttk.Entry(tab1, font=('Helvetica', 12), width=20)
e1.pack(pady=10, padx=10, ipady=5)

sl1 = ttk.Label(tab1, text="Count: 1")
sl1.pack(pady=0)

sv1 = tk.StringVar()
s1 = ttk.Scale(tab1, from_=1, to=1000, variable=sv1, orient=tk.HORIZONTAL, length=200)
s1.pack(pady=10)

def on_slider_move(event):
    value = int(s1.get())
    sl1.config(text=f"Count: {value}")

s1.bind("<ButtonRelease-1>", on_slider_move)

spam_mode = tk.StringVar()
spam_mode.set("party")  # default value
spam_mode_frame = ttk.Frame(tab1)
spam_mode_frame.pack(pady=10)

partybutton = ttk.Radiobutton(spam_mode_frame, text="Party", variable=spam_mode, value="party")
teambutton = ttk.Radiobutton(spam_mode_frame, text="Team", variable=spam_mode, value="team")
gamebutton = ttk.Radiobutton(spam_mode_frame, text="Game", variable=spam_mode, value="game")
partybutton.pack(side="left", padx=5)
teambutton.pack(side="left", padx=5)
gamebutton.pack(side="left", padx=5)

def clickSpam():
    msg = e1.get()
    count = s1.get()
    if spam_mode.get() == "party":
        cid = Chat.getPartyCid()
    elif spam_mode.get() == "team":
        cid = Chat.getTeamCid()
    else:
        cid = Chat.getGameCid()
    Tools.Spammer((int(1+count)), msg, cid)

b1 = ttk.Button(tab1, text="Spam", width=20, command=threading.Thread(target=clickSpam).start)
b1.pack(pady=10, padx=10, ipadx=10)

### PREGAME ###

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Game")

l2 = ttk.Label(tab2,font=('Helvetica', 12, 'bold'), text="PreGame")
l2.pack(pady=10)

# Game Dodge
b2 = ttk.Button(tab2, text="Dodge", command=lambda: Match.Dodge(Get.PreMatchID()), width=20)
b2.pack(pady=10, padx=10, ipadx=10)

# Wheel of Fortune
def clickWheel():
    Tools.WheelOfFortune(Get.AgentIDs())

b4 = ttk.Button(tab2, text="Wheel Of Fortune", command=threading.Thread(target=clickWheel).start, width=20)
b4.pack(pady=10, padx=10, ipadx=10)

# Instalock
l3 = ttk.Label(tab2,font=('Helvetica', 12, 'bold'), text="Instalock")
l3.pack(pady=10)

dv1 = tk.StringVar()
dagents = Get.AgentLUT()
d1 = ttk.OptionMenu(tab2, dv1, *dagents,)
d1.config(width=20)
d1.pack()

b3 = ttk.Button(tab2, text="set", command=lambda: Tools.Instalock(dagents[dv1.get()]), width=20)
b3.pack(pady=10, padx=10, ipadx=10)

### TAB 3 ###

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Misc")

l4 = ttk.Label(tab3,font=('Helvetica', 12, 'bold'), text="Misc")
l4.pack(pady=10)

b5 = ttk.Button(tab3, text="Start Custom Game", command=lambda: Party.StartCustom(), width=20)
b5.pack(pady=10, padx=10, ipadx=10)

b6 = ttk.Button(tab3, text="Stop Queue", command=lambda: Party.LeaveMatchmaking, width=20)
b6.pack(pady=10, padx=10, ipadx=10)

# button6 = ttk.Button(tab3, text="Counter", command=threading.Thread(target=Tools.Counter()).start, width=20)
# button6.pack(pady=10, padx=10, ipadx=10)

### Tab 4 ###

tab4 = ttk.Frame(notebook)
notebook.add(tab4, text="Settings")

l5 = ttk.Label(tab4,font=('Helvetica', 12, 'bold'), text="Region")
l5.pack(pady=10)

dv2 = tk.StringVar()
Regions = ["ap","ap","na","kr","br","eu","latam"]
d2 = ttk.OptionMenu(tab4, dv2, *Regions,)
d2.config(width=20)
d2.pack()

l6 = ttk.Label(tab4,font=('Helvetica', 12, 'bold'), text="Shard")
l6.pack(pady=10)

dv3 = tk.StringVar()
Shards = ["ap","ap","na","kr","pbe","eu"]
d3 = ttk.OptionMenu(tab4, dv3, *Shards,)
d3.config(width=20)
d3.pack()

b7 = ttk.Button(tab4, text="Set Config", command=lambda: Tools.SetConfig(dv2.get(),dv3.get()), width=20)
b7.pack(pady=10, padx=10, ipadx=10)

sv_ttk.set_theme("dark")
window.mainloop()