from wrapper import *
from tools import *

import tkinter as tk
from tkinter import ttk
import sv_ttk

import threading

window = tk.Tk()
window.geometry("300x300")
window.title("Greif Suite")

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

### CHAT SPAMMER ###

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Chat Spammer")

label = ttk.Label(tab1, font=('Helvetica', 12, 'bold'), text="Chat Spammer")
label.pack(pady=10, padx=10, anchor="center")

entry = ttk.Entry(tab1, font=('Helvetica', 12), width=20)
entry.pack(pady=10, padx=10, ipady=5)

slider_label = ttk.Label(tab1, text="Count: 1")
slider_label.pack(pady=0)

sv = tk.StringVar()
slider = ttk.Scale(tab1, from_=1, to=1000, variable=sv, orient=tk.HORIZONTAL, length=200)
slider.pack(pady=10)

def on_slider_move(event):
    value = int(slider.get())
    slider_label.config(text=f"Count: {value}")

slider.bind("<ButtonRelease-1>", on_slider_move)

spam_mode = tk.StringVar()
spam_mode.set("party")  # default value
spam_mode_frame = ttk.Frame(tab1)
spam_mode_frame.pack(pady=10)

party_button = ttk.Radiobutton(spam_mode_frame, text="Party", variable=spam_mode, value="party")
team_button = ttk.Radiobutton(spam_mode_frame, text="Team", variable=spam_mode, value="team")
game_button = ttk.Radiobutton(spam_mode_frame, text="Game", variable=spam_mode, value="game")
party_button.pack(side="left", padx=5)
team_button.pack(side="left", padx=5)
game_button.pack(side="left", padx=5)

def clickSpam():
    msg = entry.get()
    count = slider.get()
    if spam_mode.get() == "party":
        cid = Chat.getPartyCid()
    elif spam_mode.get() == "team":
        cid = Chat.getTeamCid()
    else:
        cid = Chat.getGameCid()
    Tools.Spammer((int(1+count)), msg, cid)

button1 = ttk.Button(tab1, text="Spam", width=20, command=threading.Thread(target=clickSpam).start)
button1.pack(pady=10, padx=10, ipadx=10)

### PREGAME ###

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="PreGame")

label2 = ttk.Label(tab2,font=('Helvetica', 12, 'bold'), text="PreGame")
label2.pack(pady=10)

button2 = ttk.Button(tab2, text="Dodge", command=lambda: Match.Dodge(Get.PreMatchID()), width=20)
button2.pack(pady=10, padx=10, ipadx=10)

def clickWheel():
    Tools.WheelOfFortune(Get.AgentIDs())

button4 = ttk.Button(tab2, text="Wheel Of Fortune", command=threading.Thread(target=clickWheel).start, width=20)
button4.pack(pady=10, padx=10, ipadx=10)


label3 = ttk.Label(tab2,font=('Helvetica', 12, 'bold'), text="Instalock")
label3.pack(pady=10)

dv = tk.StringVar()
dagents = Get.AgentLUT()
dropdown = ttk.OptionMenu(tab2, dv, *dagents,)
dropdown.config(width=20)
dropdown.pack()

button3 = ttk.Button(tab2, text="set", command=lambda: Tools.Instalock(dagents[dv.get()]), width=20)
button3.pack(pady=10, padx=10, ipadx=10)

### TAB 3 ###

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Misc")

label4 = ttk.Label(tab3,font=('Helvetica', 12, 'bold'), text="Misc")
label4.pack(pady=10)

button5 = ttk.Button(tab3, text="Start Custom Game", command=lambda: Party.StartCustom(), width=20)
button5.pack(pady=10, padx=10, ipadx=10)

button6 = ttk.Button(tab3, text="Stop Queue", command=lambda: Party.LeaveMatchmaking, width=20)
button6.pack(pady=10, padx=10, ipadx=10)

button6 = ttk.Button(tab3, text="Counter", command=threading.Thread(target=Tools.Counter()).start, width=20)
button6.pack(pady=10, padx=10, ipadx=10)


sv_ttk.set_theme("dark")
window.mainloop()