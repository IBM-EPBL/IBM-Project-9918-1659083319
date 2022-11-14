import os
from tkinter import *


tk = Tk()                                                 # preparing a Tkinter instance
tk.title('Data Visualization of Natural Disasters')       # adding Title
tk.geometry("325x195")                                    # window-size



def earthquake():
    # function to view earthquake data
    os.system('python3 earthquakes.py')

def flood():
    # function to view flood data
    os.system('python3 floods.py')

def cyclone():
    # function to view cyclone data
    os.system('python3 cyclone.py')

def wildfire():
    # function to view wildfire data
    os.system('python3 wildfire.py')


# Buttons to call each function

ear_btn = Button(tk,text="Earthquakes", command = earthquake, pady=5, width=8, bg="grey")
flo_btn = Button(tk,text="Floods", command = flood, pady=5, width=8, bg="brown")
cyl_btn = Button(tk,text="Cyclones", command= cyclone, pady=5, width=8, bg="darkblue")
wfr_btn = Button(tk,text="Wildfires", command= wildfire, pady=5, width=8, bg="orange")

# positioning the buttons

flo_btn.pack(side = RIGHT)
cyl_btn.pack(side = LEFT)
wfr_btn.pack(side = TOP)
ear_btn.pack(side = BOTTOM)

# running the mainloop
tk.mainloop()