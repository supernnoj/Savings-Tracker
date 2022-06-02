from msilib.schema import AdminExecuteSequence
from tkinter import *
import tkinter.messagebox
import os
from query import *

# global var
isProcessDone = False
this_user = f''
this_pw = False

class home():

    """def usernotfound_msgbox():
        tkinter.messagebox.showinfo(f'Error', f'User not found')
"""
    def __init__(user, pw):

        def errormsg():
            tkinter.messagebox.showinfo(f'Error Login', f'User not found')
        
        def okmsg():
            tkinter.messagebox.showinfo(f'Login Success', f'User found!')
            global isProcessDone
            isProcessDone = True

        def __start__():
            root = Tk()
            root.title('Savings Tracker')
            root.geometry("800x500") # orig window 700x350
            root.resizable(False, False) # set to true to make window resizable
            getbg = PhotoImage(file="app/res/home.png")
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)

            print(' HOME LOADED')

            # ============= create account button ui =============
            getcreate = PhotoImage(file='app/res/createacc.png')
            setcreate = Label(image=getcreate)

            # create account hover effects
            def entercreate(e):
                gethover = PhotoImage(file="app/res/createacchover.png")
                createbutton['image'] = gethover
                createbutton.image = gethover
            def leavecreate(e):
                getdefault = PhotoImage(file="app/res/createacc.png")
                createbutton['image'] = getdefault
                createbutton.image = getdefault
            
            createbutton = Button(root, image=getcreate, borderwidth=0, bg='#4152B3')
                #command=lambda: onClick("You accepted Terms of Service"))
            createbutton.place(y=217, x=60)

            createbutton.bind("<Enter>", entercreate)
            createbutton.bind("<Leave>", leavecreate)
            # ============= end create account button ui =============
            
            # ============= login button ui =============
            getlogin = PhotoImage(file='app/res/loginacc.png')
            setlogin = Label(image=getlogin)

            # login hover effects
            def enterlogin(e):
                gethover = PhotoImage(file="app/res/loginacchover.png")
                login_account_button['image'] = gethover
                login_account_button.image = gethover
            def leavelogin(e):
                getdefault = PhotoImage(file="app/res/loginacc.png")
                login_account_button['image'] = getdefault
                login_account_button.image = getdefault

            # login popup window
            def clickLogin():
                login = Toplevel(root)
                login.title(f'User Login')
                login.geometry('350x500')
                login.resizable(False, False)
                #login.configure(bg=f'#7B96D4')
                getloginbg = PhotoImage(file="app/res/login.png")
                setloginbg = Label(login, image=getbg).place(x=0, y=0)

                # username label
                space1 = Label(login,text='',bg='white').pack(side=TOP, pady=20)
                usertext=Label(login,text='u s e r n a m e',bg='white')
                usertextfont=('Calibri',10, 'bold')
                usertext.config(font=usertextfont)
                usertext.pack(side=TOP)

                # field for username entry
                userfield=Entry(login,width=20,border=0)
                userfieldfont=('Calibri',13)
                userfield.config(font=userfieldfont)
                userfield.pack(side=TOP)

                # password label
                space2 = Label(login,text='',bg='white').pack(side=TOP)
                pwtext=Label(login,text='p a s s w o r d',bg='white')
                pwtextfont=('Calibri',10, 'bold')
                pwtext.config(font=pwtextfont)
                pwtext.pack(side=TOP)

                # field for password entry
                pwfield=Entry(login,width=20,border=0, show='*')
                pwfieldfont=('Calibri',13)
                pwfield.config(font=pwfieldfont)
                pwfield.pack(side=TOP)

                # login button
                def confirm_log():
                    global this_user, this_pw

                    this_user = Q.verify_user(userfield.get())

                    print(f'')
                    print(f' user: {userfield.get()}')

                    if this_user == False:
                        print(f' USER NOT FOUND')
                        login.destroy()
                        errormsg()
                    else:
                        this_pw = Q.verify_pw(userfield.get(), pwfield.get())
                        print(f' password: {this_pw}')
                        if this_pw:
                            print(f' USER FOUND')
                            okmsg()
                            root.destroy()
                        else:
                            this_user = False
                            print(f' USER NOT FOUND')
                            login.destroy()
                            errormsg()

                login_button = Button(login, text=f'LOGIN', borderwidth=2,
                command=lambda: confirm_log())
                login_button.pack(side=TOP, pady=10)

            login_account_button = Button(root, image=getlogin, borderwidth=0, bg='#4152B3',
                command=lambda: clickLogin())
            login_account_button.place(y=281, x=60)

            login_account_button.bind("<Enter>", enterlogin)
            login_account_button.bind("<Leave>", leavelogin)
            # ============= end login button ui =============

            # #4152B3

            root.mainloop()
        
        __start__()
        print(f'\n PROCEED WITH USER PROFILE: {isProcessDone}')

            
            
                
            
            

        
            