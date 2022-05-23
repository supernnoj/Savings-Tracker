from operator import is_
from tkinter import *
import tkinter.messagebox
import json
import os

# to create window
root  = Tk()
# to change window title
root.title('Savings Tracker')
# to set window size
root.geometry("740x390") # orig window 700x350
#to make window unresizeable
root.resizable(False, False)

def destroy(m):
    tkinter.messagebox.showinfo('Terms of Service', m)
    root.destroy()
    import login

# terms of service
try:
    to_file = os.getcwd() + "\\app\\" # to get current directory and set path to app folder
    with open(to_file + "tos.json", "r") as open_tos: # to open json file
        get_tos = json.load(open_tos)
        for x in get_tos:
            x_tos = x['tos']
    # to create label
    _w_s_01 = Label(root,text="").pack(side=TOP,pady=20) # blank label to serve as divider
    _title = Label(root,text=x_tos['title'],font=("Arial",18,"bold"),).pack(side=TOP,pady=12) # orig font 17
    _tos = Label(root,text=x_tos['tos'],font=("Arial",10),).pack(side=TOP,pady=1) # orig font 10
    _tos = Label(root,text=x_tos['tos_text'],font=("Arial",10),).pack(side=TOP,pady=1) # orig font 8 : pady 0
    _accept = Button(root,text="ACCEPT TERMS OF SERVICE",font=("Arial", 10),command=lambda m="You accepted terms of service": destroy(m)).pack(side=TOP,pady=30) # orig font 9 : pady 30
except:
    for x in range(0,5):
        print(" ERROR: TOS.JSON COULDN'T BE FOUND. PLEASE CHECK IF EXIST IN APP FOLDER")

# to run in loop
root.mainloop()