from tkinter import *
import tkinter.messagebox
import os

class login():

    def __init__():

        def __start__():
            root  = Tk()
            root.title('Savings Tracker')
            root.geometry("800x500") # orig window 700x350
            root.resizable(False, False) # set to true to make window resizable
            getbg = PhotoImage(file="app/res/login.png")
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)

            print(' LOGIN FOUND')

            root.mainloop()
        
        __start__()