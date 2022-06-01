from msilib.schema import AdminExecuteSequence
from tkinter import *
import tkinter.messagebox
import os

isLogged = True

class login():

    def __init__(user, pw):

        def __start__():
            root = Tk()
            root.title('Savings Tracker')
            root.geometry("800x500") # orig window 700x350
            root.resizable(False, False) # set to true to make window resizable
            getbg = PhotoImage(file="app/res/login.png")
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)

            print(' LOGIN FOUND')

            # create account button ui
            getcreate = PhotoImage(file='app/res/createacc.png')
            setcreate = Label(image=getcreate)
            """def clickCreate(text):
                tkinter.messagebox.showinfo("Terms of Service", text)
                global isLogin 
                isLogin = True"""
            createbutton = Button(root, image=getcreate, borderwidth=0, bg='#4152B3')
                #command=lambda: onClick("You accepted Terms of Service"))
            createbutton.place(y=217, x=60)
            
            # ============= create login button ui =============
            getlogin = PhotoImage(file='app/res/loginacc.png')
            setlogin = Label(image=getlogin)
            
            # login popup window
            def clickLogin():
                login = Toplevel(root)
                login.title(f'User Login')
                login.geometry('350x500')
                login.resizable(False, False)
                login.configure(bg=f'#7B96D4')

                l1=Label(login,text='Username',bg='white')
                l=('Consolas',13)
                l1.config(font=l)
                l1.place(x=80,y=200)

                #e1 entry for username entry
                e1=Entry(login,width=20,border=0)
                l=('Consolas',13)
                e1.config(font=l)
                e1.place(x=80,y=230)

            createbutton = Button(root, image=getlogin, borderwidth=0, bg='#4152B3',
                command=lambda: clickLogin())
            createbutton.place(y=281, x=60)
            # ============= end create login button ui =============

            # #4152B3

            root.mainloop()
        
        __start__()

        if isLogged:
            return True
            

        
            