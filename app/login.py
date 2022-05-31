from operator import is_
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import json
import os


# create window
root  = Tk()
# window title
root.title('Savings Tracker')
# window size
root.geometry("800x500") # orig window 700x350
# window non-resizable
root.resizable(False, False) # set to true to make window resizable
# define background image
bg = PhotoImage(file="app/res/login.png")

print(' LOGIN PAGE LOADED')

# create label
_bg = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)
root.entry = Entry (root, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
#_login = Label(root,text="login window",font=("Arial",17,"bold"),).pack(side=TOP,pady=12)

# to run in loop
root.mainloop()