import tkinter as tk
from tkinter import *  
from PIL import ImageTk,Image  
from tkinter.ttk import *
from tkinter import messagebox
import os, os.path, sys
import json
import types
import gm_config as gmc
import webbrowser
from pyshortcuts import make_shortcut
from gm_resources import resource_path, retrieve_file, download_file

# global frame_sportsetup
current = 0
frames_function = {}
config = config = {"name": None, "version": 2, "unit": None, "ct": None, "times": {"hours": None, "minutes": None, "seconds": None}, "scores": {}, "vars": [], "players": None, "settings": {"hours": False,"minutes": True,"seconds": True,"on top": False, "alarm": True}}

# make_shortcut(os.path.abspath(os.getcwd())+'\gamemaster.exe', name='GameMaster', icon=resource_path('icon.ico'))

def setup():
    frames_setup = {}
    

    window_setup = tk.Toplevel()
    window_setup.title("GameMaster Setup")
    window_setup.geometry("600x400")
    window_setup.resizable(False, False)
    window_setup.lift()
    window_setup.attributes("-topmost", True)
    window_setup.iconbitmap(resource_path("icon.ico"))

    window_setup.rowconfigure(index=0, weight=0)
    window_setup.rowconfigure(index=1, weight=1)
    window_setup.rowconfigure(index=2, weight=0)
    window_setup.columnconfigure(index=0, weight=0)
    window_setup.columnconfigure(index=1, weight=1)
    window_setup.columnconfigure(index=2, weight=0)

    bar = Progressbar(window_setup, orient=HORIZONTAL, length=500, mode='determinate')
    bar.grid(row=2, column=1, sticky=NSEW, padx=10, pady=10)
    bar['value'] = current*100/(len(frames_setup)-1) 

    frames_function[0] = lambda: None
    frames_function[1] = lambda: None
    frames_function[2] = lambda: None
    frames_function[3] = lambda: None
    frames_function[4] = lambda: None
    frames_function[5] = lambda: None
    frames_function[6] = lambda: None

    def next_frame():
        global current
        global frames_function
        frames_setup[current].grid_forget()
        frames_function[current]()
        print(cb_sportselect.get())
        if cb_sportselect.get() == "":
            print("none")
            if current+1 == 2:
                print(2)
                btn_setupfw['state'] = "disabled"
                current += 1
            else:
                btn_setupfw['state'] = "normal"
                current += 1
        else:
            if current == 2:
                if cb_sportselect.get() == "Football" or cb_sportselect.get() == "Basketball" or cb_sportselect.get() == "Soccer":
                    current = len(frames_setup)-2
                else:
                    current += 1
            else:
                current += 1
        print("continue")
        bar['value'] = current*100/(len(frames_setup)-1)
        print("continue")
        frames_setup[current].grid(row=1, column=0,columnspan=3, sticky=NSEW, padx=10, pady=10)
        if current == 0:
            btn_setupbw['state'] = "disabled"
        else:
            btn_setupbw['state'] = "normal"
        if current == len(frames_setup)-1:
            btn_setupfw['text'] = "Finish"
            btn_setupfw['command'] = lambda: os.execv(sys.executable, ["python"] + sys.argv)
        else:
            btn_setupfw['text'] = "Next"
            btn_setupfw['command'] = lambda: next_frame()

    def prev_frame():
        global current
        try:
            frames_setup[current].grid_forget()
        except:
            None
        if cb_sportselect.get() == "":
            print("none")
            if current+1 == 2:
                print(2)
                btn_setupfw['state'] = "normal"
                current -= 1
            else:
                btn_setupfw['state'] = "normal"
                current -= 1
        else:
            if current == 5:
                if cb_sportselect.get() == "Football" or cb_sportselect.get() == "Basketball" or cb_sportselect.get() == "Soccer":
                    current = 2
                else:
                    current -= 1
            else:
                current -= 1
        bar['value'] = current*100/(len(frames_setup)-1)
        frames_setup[current].grid(row=1, column=0,columnspan=3, sticky=NSEW, padx=10, pady=10)
        if current == 0:
            btn_setupbw['state'] = "disabled"
        else:
            btn_setupbw['state'] = "normal"
        if current == len(frames_setup)-1:
            btn_setupfw['text'] = "Finish"
            btn_setupfw['command'] = lambda: os.execv(sys.executable, ["python"] + sys.argv)
        else:
            btn_setupfw['text'] = "Next"
            btn_setupfw['command'] = lambda: next_frame()
        


    btn_setupfw = Button(window_setup, text="Next", command=lambda: next_frame())
    btn_setupfw.grid(row=2, column=2, sticky=NSEW, padx=10, pady=10)
    btn_setupbw = Button(window_setup, text="Back", state=DISABLED,command=lambda: prev_frame())
    btn_setupbw.grid(row=2, column=0, sticky=NSEW, padx=10, pady=10)

    header = tk.Frame(master=window_setup,width=40, height=10)
    header.grid(column=0, row=0, sticky=tk.EW, columnspan=3, rowspan=1, padx=0, pady=0)
    canvas = Canvas(master=header,width = 700, height = 96)
    canvas.grid(column=0, columnspan=3,row=0, rowspan=2, sticky=tk.NSEW)
    img = ImageTk.PhotoImage(Image.open(resource_path("header_alt.png")))  
    canvas.create_image(0, 0, anchor=NW, image=img)

    body = Frame(master=window_setup,width=40, height=10)
    body.grid(column=0, row=1, sticky=tk.NSEW, columnspan=3, rowspan=1, padx=5, pady=5)
    body.rowconfigure(index=0, weight=0)
    body.rowconfigure(index=1, weight=1)
    body.columnconfigure(index=0, weight=1)



    frames_setup[0] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)
    frames_setup[0].grid(column=0, row=1, sticky=tk.NSEW, columnspan=3, rowspan=1, padx=10, pady=10)
    frames_setup[0].rowconfigure(index=0, weight=0)
    frames_setup[0].rowconfigure(index=1, weight=1)
    frames_setup[0].columnconfigure(index=0, weight=1)

    lbl_setup = Label(master=frames_setup[0], text="Welcome to GameMaster!", font=("Arial", 18))
    lbl_setup.grid(column=0, row=0, sticky=tk.NSEW)
    lbl_intro = Label(master=frames_setup[0], wraplength=560, justify=LEFT, text="Let’s get you started. In this setup dialog, we’ll walk you through the basics of setting up and using GameMaster, as well as delving into the setup involved with displaying your values inside of OBS. \n\nGameMaster is constantly being updated and maintained by Bears Broadcast Group with help from TheLittleDoctor. Feel free to contact us through any of the channels in the “About” tab following setup.", font=("Arial", 10))
    lbl_intro.grid(column=0, row=1, sticky=tk.NW)

    frames_setup[1] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)
    frames_setup[1].rowconfigure(index=0, weight=0)
    frames_setup[1].rowconfigure(index=1, weight=1)
    frames_setup[1].columnconfigure(index=0, weight=1)

    lbl_configsetup = Label(master=frames_setup[1], text="Config Setup", font=("Arial", 18))
    lbl_configsetup.grid(column=0, row=0, sticky=tk.NSEW)
    lbl_configsetup_intro = Label(master=frames_setup[1], wraplength=560, justify=LEFT, text="One of GameMaster's unique features is the ability to change the sport it can score, which includes preset score values, default period durations, and how many periods can be played.\n\nIn theses next few pages, we will set up your GameMaster configuration to be ready to score the sport you need.", font=("Arial", 10))
    lbl_configsetup_intro.grid(column=0, row=1, sticky=tk.NW)

    frames_setup[2] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)
    frames_setup[2].rowconfigure(index=0, weight=0)
    frames_setup[2].rowconfigure(index=1, weight=0)
    frames_setup[2].rowconfigure(index=2, weight=0)
    frames_setup[2].columnconfigure(index=0, weight=0)
    frames_setup[2].columnconfigure(index=1, weight=0)
    frames_setup[2].columnconfigure(index=2, weight=1)

    lbl_configsetup_ = Label(master=frames_setup[2], text="Config Setup", font=("Arial", 18))
    lbl_configsetup_.grid(column=0, row=0, sticky=tk.NSEW,columnspan=3)
    lbl_sportselect = Label(master=frames_setup[2], text="Select sport: ", font=("Arial", 12))
    lbl_sportselect.grid(column=0, row=1, sticky=tk.NSEW)
    cb_sportselect = Combobox(frames_setup[2], state="readonly", values=("Custom", "Soccer", "Football", "Basketball"),width=15)
    lbl_sportname = Label(frames_setup[2], text="Sport name: ", font=("Arial", 12))
    sportname = StringVar()
    sportname.trace("w", lambda name, index,mode: edit_config("name", str(sportname.get())))
    ent_sportname = Entry(frames_setup[2], textvariable=sportname, width=15)
    lbl_namehelp = Label(frames_setup[2], wraplength=560, justify=LEFT, text="Name of your sport. Ex: Football, Soccer, Basketball", font=("Arial", 10))
    unit = StringVar()
    unit.trace("w", lambda name, index,mode: edit_config("unit", str(unit.get())))
    lbl_unit = Label(frames_setup[2], text="Sections: ", font=("Arial", 12))
    ent_unit = Entry(frames_setup[2], textvariable=unit, width=15)
    lbl_unithelp = Label(frames_setup[2], wraplength=560, justify=LEFT, text="What the time is broken into. Ex: Quarter, Half, Period", font=("Arial", 10))
    lbl_periods = Label(frames_setup[2], text="# of sections: ", font=("Arial", 12))
    periods = StringVar()
    periods.trace("w", lambda name, index,mode: edit_config("ct", str(periods.get())))
    
    ent_periods = Entry(frames_setup[2], textvariable=periods, width=15)
    def set_config():
        print(config)
        with open("gamemaster.json", "w") as f:
            json.dump(config, f, indent=4)
    def edit_config(property, value):
        config[property] = value
        # print(config[property])
        set_config()

    def sportselect(*args):
        # print(cb_sportselect.get())
        
        btn_setupfw['state'] = "normal"
        global sport
        sport = cb_sportselect.get()
        print(sport)
        if sport == "Custom":
            print("custom uwu")
            lbl_sportname.grid(column=0, row=2, sticky=tk.NSEW, pady=5)
            
            ent_sportname.grid(column=1, row=2, sticky=tk.NSEW, pady=5)
            lbl_namehelp.grid(column=2, row=2, sticky=tk.NSEW, pady=5,padx=5)
            lbl_unit.grid(column=0, row=3, sticky=tk.NSEW, pady=5)
            ent_unit.grid(column=1, row=3, sticky=tk.NSEW, pady=5)
            lbl_unithelp.grid(column=2, row=3, sticky=tk.NW, pady=5, padx=5)
            lbl_periods.grid(column=0, row=4, sticky=tk.NSEW, pady=5)
            ent_periods.grid(column=1, row=4, sticky=tk.NSEW, pady=5)
            # frame_sportsetup.grid_forget()
        elif sport == "Football" or sport == "Soccer" or sport == "Basketball":
            print("not custom")
            lbl_sportname.grid_forget()
            ent_sportname.grid_forget()
            lbl_namehelp.grid_forget()
            lbl_unit.grid_forget()
            ent_unit.grid_forget()
            lbl_unithelp.grid_forget()
            lbl_periods.grid_forget()
            ent_periods.grid_forget()

    cb_sportselect.bind("<<ComboboxSelected>>", sportselect)
    cb_sportselect.grid(column=1, row=1, sticky=tk.NSEW,pady=5)

    frames_setup[3] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)
    frames_setup[3].rowconfigure(index=0, weight=0)
    frames_setup[3].rowconfigure(index=1, weight=0)
    frames_setup[3].rowconfigure(index=2, weight=0)
    frames_setup[3].columnconfigure(index=0, weight=0)
    frames_setup[3].columnconfigure(index=1, weight=0)
    frames_setup[3].columnconfigure(index=2, weight=1)

    frames_setup[4] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)


    frames_setup[5] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)
    frames_setup[5].rowconfigure(index=0, weight=0)
    frames_setup[5].rowconfigure(index=1, weight=0)
    frames_setup[5].rowconfigure(index=2, weight=0)
    frames_setup[5].columnconfigure(index=0, weight=0)
    frames_setup[5].columnconfigure(index=1, weight=0)
    frames_setup[5].columnconfigure(index=2, weight=1)

    lbl_five = Label(master=frames_setup[5], text="Five lol", font=("Arial", 18))
    lbl_five.grid(column=0, row=0, sticky=tk.NSEW,columnspan=3)

    frames_setup[6] = Frame(master=window_setup,width=40, height=10, relief=GROOVE, borderwidth=5)
    frames_setup[6].rowconfigure(index=0, weight=0)
    frames_setup[6].rowconfigure(index=1, weight=0)
    frames_setup[6].rowconfigure(index=2, weight=0)
    frames_setup[6].columnconfigure(index=0, weight=0)
    frames_setup[6].columnconfigure(index=1, weight=0)
    frames_setup[6].columnconfigure(index=2, weight=1)

    lbl_finish = Label(master=frames_setup[6], text="Setup Completed", font=("Arial", 18))
    lbl_finish.grid(column=0, row=0, sticky=tk.NSEW,columnspan=3)
    lbl_closingremarks = Label(master=frames_setup[6], wraplength=560, justify=LEFT, text="Thank you for choosing GameMaster!\n\n", font=("Arial", 10))
    lbl_closingremarks.grid(column=0, row=1, sticky=tk.NW)


    window_setup.mainloop()