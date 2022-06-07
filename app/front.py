from tkinter import *
from database import *
from customtkinter import *
from system import *
import customtkinter

# >>> global var <<<
app_landing_process_done = False


class app:
    def __init__():
        def __start__():

            print(f" FOUND HOME")

            WIDTH = 500
            HEIGHT = 500

            root = Tk()
            root.title(f"Savings Tracker")
            root.config(bg="#2A2D2E")
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_coordinate = (screen_width / 2) - (WIDTH / 2)
            y_coordinate = (screen_height / 2) - (HEIGHT / 2)
            root.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, x_coordinate, y_coordinate))
            root.resizable(False, False)

            getbg = PhotoImage(file="app/res/home.png")
            setbg = Label(image=getbg, border=0).place(
                x=0, y=0, relheight=1, relwidth=1
            )

            # ========= >>> create account pop up window <<< =========
            def clickCreate():

                WIDTH = 350
                HEIGHT = 500

                create = Toplevel(root)
                create.title(f"Create Account")

                screen_width = create.winfo_screenwidth()
                screen_height = create.winfo_screenheight()
                x_coordinate = (screen_width / 2) - (WIDTH / 2)
                y_coordinate = (screen_height / 2) - (HEIGHT / 2)
                create.geometry(
                    "%dx%d+%d+%d" % (WIDTH, HEIGHT, x_coordinate, y_coordinate)
                )
                create.resizable(False, False)
                getcreatebg = PhotoImage(file=f"app/res/createbg.png")
                setcreatebg = Label(create, image=getcreatebg).place(
                    x=0, y=0, relwidth=1, relheight=1
                )
                # ========= >>> username label <<< =========
                space1 = Label(create, text="", bg="#4152B3").pack(side=TOP, pady=15)
                usertext = Label(
                    create, text="u s e r n a m e", bg="#4152B3", fg="white"
                )
                usertextfont = ("Calibri", 10, "bold")
                usertext.config(font=usertextfont)
                usertext.pack(side=TOP)
                # ========= >>> field for username entry <<< =========
                userfield = Entry(create, width=20, border=0, bg="#485AB7", fg="white")
                userfieldfont = ("Calibri", 13)
                userfield.config(font=userfieldfont)
                userfield.pack(side=TOP, pady=10)
                # ========= >>> email label <<< =========
                space2 = Label(create, text="", bg="#4152B3").pack(side=TOP)
                emailtext = Label(create, text="e m a i l", bg="#4152B3", fg="white")
                emailtextfont = ("Calibri", 10, "bold")
                emailtext.config(font=emailtextfont)
                emailtext.pack(side=TOP)
                # ========= >>> field for email entry <<< =========
                emailfield = Entry(create, width=20, border=0, bg="#485AB7", fg="white")
                emailfieldfont = ("Calibri", 13)
                emailfield.config(font=emailfieldfont)
                emailfield.pack(side=TOP, pady=10)
                # ========= >>> password label <<< =========
                space2 = Label(create, text="", bg="#4152B3").pack(side=TOP)
                pwtext = Label(create, text="p a s s w o r d", bg="#4152B3", fg="white")
                pwtextfont = ("Calibri", 10, "bold")
                pwtext.config(font=pwtextfont)
                pwtext.pack(side=TOP)
                # field for password entry <<< =========
                pwfield = Entry(
                    create, width=20, border=0, bg="#485AB7", fg="white", show="*"
                )
                pwfieldfont = ("Calibri", 13)
                pwfield.config(font=pwfieldfont)
                pwfield.pack(side=TOP, pady=10)
                # ========= >>> confirm password label <<< =========
                space2 = Label(create, text="", bg="#4152B3").pack(side=TOP)
                cpwtext = Label(
                    create,
                    text="c o n f i r m   p a s s w o r d",
                    bg="#4152B3",
                    fg="white",
                )
                cpwtextfont = ("Calibri", 10, "bold")
                cpwtext.config(font=cpwtextfont)
                cpwtext.pack(side=TOP)
                # ========= >>> confirm field for password entry <<< =========
                cpwfield = Entry(
                    create, width=20, border=0, bg="#485AB7", fg="white", show="*"
                )
                cpwfieldfont = ("Calibri", 13)
                cpwfield.config(font=cpwfieldfont)
                cpwfield.pack(side=TOP, pady=10)

                # ========= >>> confirm button <<< =========
                def confirm():
                    if (
                        validate.fields(userfield.get())
                        or validate.fields(emailfield.get())
                        or validate.fields(pwfield.get())
                        or validate.fields(cpwfield.get())
                    ):
                        error.empty()
                    else:
                        if Q.verify_user(userfield.get()) or Q.verify_email(
                            emailfield.get()
                        ):
                            if Q.verify_user(userfield.get()):
                                error.user_exist()
                            if Q.verify_email(emailfield.get()):
                                error.email_exist()
                        else:
                            if pwfield.get() == cpwfield.get():
                                if Q.create_user(
                                    emailfield.get(), userfield.get(), pwfield.get()
                                ):
                                    create.destroy()
                                    success.user_added()
                            else:
                                error.password()

                btn = customtkinter.CTkButton(
                    create,
                    text="CREATE",
                    corner_radius=10,
                    border_width=0,
                    text_font=(f"Calibri", 11, f"bold"),
                    text_color=f"white",
                    fg_color=f"#4152B3",
                    bg_color=f"white",
                    hover_color=f"#69D567",
                    command=lambda: confirm(),
                    width=80,
                )
                btn.place(x=246, y=430)

                create.mainloop()

            btn_create = customtkinter.CTkButton(
                root,
                text="SIGN UP",
                command=lambda: clickCreate(),
                border_width=1,
                border_color=f"white",
                text_font=("Calibri", 15, "bold"),
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=f"#4F5FB9",
                corner_radius=5,
                width=120,
            )
            btn_create.place(x=195, y=335)

            btn_new = customtkinter.CTkButton()

            # # ========= >>> login pop up window <<< =========
            def clickLogin():
                login = Toplevel(root)
                login.title(f"User Login")
                WIDTH = 350
                HEIGHT = 500
                screen_width = login.winfo_screenwidth()
                screen_height = login.winfo_screenheight()
                x_coordinate = (screen_width / 2) - (WIDTH / 2)
                y_coordinate = (screen_height / 2) - (HEIGHT / 2)
                login.geometry(
                    "%dx%d+%d+%d" % (WIDTH, HEIGHT, x_coordinate, y_coordinate)
                )
                login.resizable(False, False)
                getloginbg = PhotoImage(file=f"app/res/login.png")
                setloginbg = Label(login, image=getloginbg).place(
                    x=0, y=0, relwidth=1, relheight=1
                )
                # ========= >>>  username label <<< =========
                space1 = Label(login, text="", bg="#4152B3").pack(side=TOP, pady=15)
                usertext = Label(
                    login, text="u s e r n a m e", bg="#4152B3", fg="white"
                )
                usertextfont = ("Calibri", 10, "bold")
                usertext.config(font=usertextfont)
                usertext.pack(side=TOP)
                # ========= >>>  field for username entry <<< =========
                userfield = Entry(login, width=20, border=0, bg="#485AB7", fg="white")
                userfieldfont = ("Calibri", 13)
                userfield.config(font=userfieldfont)
                userfield.pack(side=TOP, pady=10)
                # ========= >>>  password label <<< =========
                space2 = Label(login, text="", bg="#4152B3").pack(side=TOP)
                pwtext = Label(login, text="p a s s w o r d", bg="#4152B3", fg="white")
                pwtextfont = ("Calibri", 10, "bold")
                pwtext.config(font=pwtextfont)
                pwtext.pack(side=TOP)
                # ========= >>>  field for password entry <<< =========
                pwfield = Entry(
                    login, width=20, border=0, bg="#485AB7", fg="white", show="*"
                )
                pwfieldfont = ("Calibri", 13)
                pwfield.config(font=pwfieldfont)
                pwfield.pack(side=TOP, pady=10)

                # ========= >>> login button function <<< =========
                def confirm_log():
                    if validate.fields(userfield.get()) or validate.fields(
                        pwfield.get()
                    ):
                        error.empty()
                    else:
                        print(f"")
                        print(f" user : {userfield.get()}")
                        if Q.verify_user(userfield.get()) == False:
                            print(f" USER NOT FOUND")
                            error.user_not_found()
                        else:
                            print(
                                f" password : {Q.verify_pw(userfield.get(), pwfield.get())}"
                            )
                            if Q.verify_pw(userfield.get(), pwfield.get()):
                                print(f" USER FOUND")
                                get_email = Q.get_email(userfield.get())
                                if Q.set_active(get_email):
                                    global app_landing_process_done
                                    app_landing_process_done = success.login()
                                    root.destroy()
                            else:
                                print(f" USER NOT FOUND")
                                error.user_not_found()

                def enterlogin(e):
                    gethover = PhotoImage(file="app/res/logohover.png")
                    login_button["image"] = gethover
                    login_button.image = gethover

                def leavelogin(e):
                    getdefault = PhotoImage(file="app/res/logo.png")
                    login_button["image"] = getdefault
                    login_button.image = getdefault

                clicktologin = Label(
                    login,
                    text=f"click logo below to log in",
                    fg=f"white",
                    bg=f"#4152B3",
                    font=("Calibri", 10, "bold"),
                ).pack(side=TOP, pady=15)

                # ========= >>> login button using logo <<< =========
                getlogo = PhotoImage(file=f"app/res/logo.png")
                login_button = Button(
                    login, image=getlogo, borderwidth=0, command=lambda: confirm_log()
                )
                login_button.pack(side=BOTTOM, pady=73)
                login_button.bind("<Enter>", enterlogin)
                login_button.bind("<Leave>", leavelogin)

                login.mainloop()

            # ========= >>> login button <<< =========
            btn_login = customtkinter.CTkButton(
                root,
                text="LOG IN",
                command=lambda: clickLogin(),
                border_width=1,
                border_color=f"white",
                text_font=("Calibri", 15, "bold"),
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=f"#4F5FB9",
                corner_radius=5,
                width=120,
            )
            btn_login.place(x=195, y=290)

            # ========= >>> about button <<< =========
            btn_reset_pw = customtkinter.CTkButton(
                root,
                text="ABOUT",
                command=lambda: clickCreate(),
                border_width=1,
                border_color=f"white",
                text_font=("Calibri", 15, "bold"),
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=f"#4F5FB9",
                corner_radius=5,
                width=120,
                state=DISABLED,
            )
            btn_reset_pw.place(x=195, y=380)

            # ========= >>> help button <<< =========
            btn_reset_pw = customtkinter.CTkButton(
                root,
                text="HELP",
                command=lambda: clickCreate(),
                border_width=1,
                border_color=f"white",
                text_font=("Calibri", 15, "bold"),
                text_color="white",
                fg_color=None,
                hover_color=f"#6595D4",
                bg_color=f"#4F5FB9",
                corner_radius=5,
                width=120,
                state=DISABLED,
            )
            btn_reset_pw.place(x=195, y=425)

            root.mainloop()

        __start__()

        print(f"\n PROCEED WITH USER : {app_landing_process_done}")

        if app_landing_process_done:
            return app_landing_process_done
