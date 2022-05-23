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
root.geometry("700x350")

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
    _title = Label(root,text=x_tos['title'],font=("Arial",17,"bold"),).pack(side=TOP,pady=12)
    _tos = Label(root,text=x_tos['tos'],font=("Arial",10),).pack(side=TOP,pady=1)
    _tos = Label(root,text=x_tos['tos_text'],font=("Arial",8),).pack(side=TOP,pady=0)
    _accept = Button(root,text="ACCEPT TERMS OF SERVICE",font=("Arial", 9),command=lambda m="You accepted terms of service": destroy(m)).pack(side=TOP,pady=25) 
except:
    for x in range(0,5):
        print(" ERROR: TOS.JSON COULDN'T BE FOUND. PLEASE CHECK IF EXIST IN APP FOLDER")

# to run in loop
root.mainloop()