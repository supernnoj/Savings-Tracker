from tkinter import *
import tkinter.messagebox
from init_db import Q

# global var
isProcessDone = False
this_user = f'' # login
this_pw = False # login

emailError = False
userError = False

class home():

    def __init__(user, pw):

        def errormsg():
            tkinter.messagebox.showinfo(f'Login Error', f'User not found')
        
        def errorempty():
            tkinter.messagebox.showinfo(f'Fields Empty', f'Fields can\'t be empty. Please check and try again')
        
        def errorpass():
            tkinter.messagebox.showinfo(f'Password Error', f'Passwords do not match. Please check and try again.')

        def dupemail():
            tkinter.messagebox.showinfo(f'Email Error', f'Email already exist. Please check and try again.')
        
        def dupuser():
            tkinter.messagebox.showinfo(f'Username Error', f'Username already exist. Please check and try again.')
        
        def useradded():
            tkinter.messagebox.showinfo(f'Account Created', f'Account created successfully!')
        
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

            print(' FOUND HOME')

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

            # create account pop up window
            def clickCreate():
                create = Toplevel(root)
                create.title(f'Create Account')
                create.geometry('350x500')
                create.resizable(False, False)
                #create.configure(bg=f'#7B96D4')
                getcreatebg = PhotoImage(file = f'app/res/createbg.png')
                setcreatebg = Label(create, image = getcreatebg).place(x=0, y=0, relwidth=1, relheight=1)
                # username label
                space1 = Label(create,text='',bg='#4152B3').pack(side=TOP, pady=15)
                usertext=Label(create,text='u s e r n a m e',bg='#4152B3', fg='white')
                usertextfont=('Calibri',10, 'bold')
                usertext.config(font=usertextfont)
                usertext.pack(side=TOP)
                # field for username entry
                userfield=Entry(create,width=20,border=0, bg='#485AB7', fg='white')
                userfieldfont=('Calibri',13)
                userfield.config(font=userfieldfont)
                userfield.pack(side=TOP, pady=10)
                # email label
                space2 = Label(create,text='',bg='#4152B3').pack(side=TOP)
                emailtext=Label(create,text='e m a i l',bg='#4152B3',fg='white')
                emailtextfont=('Calibri',10, 'bold')
                emailtext.config(font=emailtextfont)
                emailtext.pack(side=TOP)
                # field for email entry
                emailfield=Entry(create,width=20,border=0, bg='#485AB7', fg='white')
                emailfieldfont=('Calibri',13)
                emailfield.config(font=emailfieldfont)
                emailfield.pack(side=TOP, pady=10)
                # password label
                space2 = Label(create,text='',bg='#4152B3').pack(side=TOP)
                pwtext=Label(create,text='p a s s w o r d',bg='#4152B3',fg='white')
                pwtextfont=('Calibri',10, 'bold')
                pwtext.config(font=pwtextfont)
                pwtext.pack(side=TOP)
                # field for password entry
                pwfield=Entry(create,width=20,border=0, bg='#485AB7', fg='white', show='*')
                pwfieldfont=('Calibri',13)
                pwfield.config(font=pwfieldfont)
                pwfield.pack(side=TOP, pady=10)
                 # confirm password label
                space2 = Label(create,text='',bg='#4152B3').pack(side=TOP)
                cpwtext=Label(create,text='c o n f i r m   p a s s w o r d',bg='#4152B3',fg='white')
                cpwtextfont=('Calibri',10, 'bold')
                cpwtext.config(font=cpwtextfont)
                cpwtext.pack(side=TOP)
                # confirm field for password entry
                cpwfield=Entry(create,width=20,border=0, bg='#485AB7', fg='white', show='*')
                cpwfieldfont=('Calibri',13)
                cpwfield.config(font=cpwfieldfont)
                cpwfield.pack(side=TOP, pady=10)
                # confirm button
                def confirmh(e):
                    gethover = PhotoImage(file="app/res/confirmhover.png")
                    confirmb['image'] = gethover
                    confirmb.image = gethover
                def confirml(e):
                    getdefault = PhotoImage(file="app/res/confirm.png")
                    confirmb['image'] = getdefault
                    confirmb.image = getdefault
                def confirm():
                    cuser = userfield.get()
                    cemail = emailfield.get()
                    cpw = pwfield.get()
                    ccpw = cpwfield.get()
                    if len(cuser) == 0 or len(cemail) == 0 or len(cpw) == 0 or len(ccpw) == 0:
                        errorempty()
                    else:
                        global emailError, userError
                        userError = Q.verify_user(cuser)
                        emailError = Q.verify_email(cemail)
                        if userError or emailError:
                            if userError:
                                dupuser()
                            if emailError:
                                dupemail()
                        else:
                            if cpw == ccpw:
                                isAdded = Q.write_user(cemail, cuser, cpw)
                                if isAdded:
                                    userError = False
                                    emailError = False
                                    create.destroy()
                                    useradded()
                            else:
                                errorpass()
                getconfirm = PhotoImage(file=f'app/res/confirm.png')
                confirmb = Button(create, image=getconfirm, borderwidth=0, bg=f'#4152B3',
                command=lambda: confirm())
                confirmb.place(x=229, y=410)
                confirmb.bind("<Enter>", confirmh)
                confirmb.bind("<Leave>", confirml)

                create.mainloop()
            
            createbutton = Button(root, image=getcreate, borderwidth=0, bg=f'#4152B3',
                command=lambda: clickCreate())
            #createbutton.place(y=217, x=60)
            createbutton.place(y=281, x=60)

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
                getloginbg = PhotoImage(file = f'app/res/login.png')
                setloginbg = Label(login, image = getloginbg).place(x=0, y=0, relwidth=1, relheight=1)
                # username label
                space1 = Label(login,text='',bg='#4152B3').pack(side=TOP, pady=15)
                usertext=Label(login,text='u s e r n a m e',bg='#4152B3', fg='white')
                usertextfont=('Calibri',10, 'bold')
                usertext.config(font=usertextfont)
                usertext.pack(side=TOP)
                # field for username entry
                userfield=Entry(login,width=20,border=0, bg='#485AB7', fg='white')
                userfieldfont=('Calibri',13)
                userfield.config(font=userfieldfont)
                userfield.pack(side=TOP, pady=10)
                # password label
                space2 = Label(login,text='',bg='#4152B3').pack(side=TOP)
                pwtext=Label(login,text='p a s s w o r d',bg='#4152B3',fg='white')
                pwtextfont=('Calibri',10, 'bold')
                pwtext.config(font=pwtextfont)
                pwtext.pack(side=TOP)
                # field for password entry
                pwfield=Entry(login,width=20,border=0, bg='#485AB7', fg='white', show='*')
                pwfieldfont=('Calibri',13)
                pwfield.config(font=pwfieldfont)
                pwfield.pack(side=TOP, pady=10)
                # login button
                def confirm_log():
                    global this_user, this_pw
                    loguser = userfield.get()
                    logpw = pwfield.get()
                    if len(loguser) == 0 or len(logpw) == 0:
                        errorempty()
                    else:
                        this_user = Q.verify_user(userfield.get())
                        print(f'')
                        print(f' user : {userfield.get()}')
                        if this_user == False:
                            print(f' USER NOT FOUND')
                            #login.destroy()
                            errormsg()
                        else:
                            this_pw = Q.verify_pw(userfield.get(), pwfield.get())
                            print(f' password : {this_pw}')
                            if this_pw:
                                print(f' USER FOUND')
                                get_email = Q.get_email(userfield.get())
                                set_active = Q.set_active(get_email)
                                if set_active:
                                    okmsg()
                                    root.destroy()
                            else:
                                this_user = False
                                print(f' USER NOT FOUND')
                                #login.destroy()
                                errormsg()

                """login_button = Button(login, text=f'LOGIN', borderwidth=2,
                command=lambda: confirm_log())
                login_button.pack(side=TOP, pady=10)"""

                def enterlogin(e):
                    gethover = PhotoImage(file="app/res/logohover.png")
                    login_button['image'] = gethover
                    login_button.image = gethover
                def leavelogin(e):
                    getdefault = PhotoImage(file="app/res/logo.png")
                    login_button['image'] = getdefault
                    login_button.image = getdefault

                clicktologin = Label(login, text=f'click logo below to log in', fg=f'white', bg=f'#4152B3', font=('Calibri',10, 'bold')).pack(side=TOP, pady=15)
                
                getlogo = PhotoImage(file=f'app/res/logo.png')
                login_button = Button(login, image=getlogo, borderwidth=0,
                command=lambda: confirm_log())
                login_button.pack(side=BOTTOM, pady=73)
                login_button.bind("<Enter>", enterlogin)
                login_button.bind("<Leave>", leavelogin)

                login.mainloop()
            # end login pop up window

            login_account_button = Button(root, image=getlogin, borderwidth=0, bg='#4152B3',
                command=lambda: clickLogin())
            #login_account_button.place(y=281, x=60)
            login_account_button.place(y=217, x=60)

            login_account_button.bind("<Enter>", enterlogin)
            login_account_button.bind("<Leave>", leavelogin)
            # ============= end login button ui =============

            root.mainloop()
        
        __start__()

        print(f'\n PROCEED WITH USER : {isProcessDone}')

        if isProcessDone:
            return isProcessDone

       

            
            
                
            
            

        
            