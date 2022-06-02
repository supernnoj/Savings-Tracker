from inspect import getcallargs
from tkinter import *
import tkinter.messagebox
from init_db import Q

print(f' FOUND USER APP')
get_active = Q.get_active()

class app():
    
    def welcomepage():
        
        global get_active

        root = Tk()
        root.title(f'{Q.get_user(get_active)}')
        root.geometry("800x500") 
        root.resizable(False, False)
        #getbg = PhotoImage(file="app/res/home.png")
        #setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)

        root.mainloop()