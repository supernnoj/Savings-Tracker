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

# to create label
_login = Label(root,text="login window",font=("Arial",17,"bold"),).pack(side=TOP,pady=12)

# to run in loop
root.mainloop()