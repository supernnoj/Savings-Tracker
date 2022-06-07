from tkinter import *
import customtkinter
from system import *
from database import *

new_user_process_done = False


class new_user:
    def true():
        def __init__():
            w = 450
            h = 600

            customtkinter.set_appearance_mode(
                "Dark"
            )  # Modes: "System" (standard), "Dark", "Light"
            customtkinter.set_default_color_theme(
                "blue"
            )  # Themes: "blue" (standard), "green", "dark-blue"

            root = customtkinter.CTk()
            root.geometry(f"{w}x{h}")
            root.title("Personal Info")
            root.resizable(False, False)

            # main frame
            main = customtkinter.CTkFrame(
                root, width=450, height=600, corner_radius=0, fg_color=f"#4152B3"
            )

            # center frame

            center = customtkinter.CTkFrame(
                main, width=350, height=500, corner_radius=25, fg_color="white"
            )

            # config
            # labels
            lfont = ("Calibri", 14, "bold")
            lbg = f"#FFFFFF"
            lfg = f"black"
            # entry
            efont = ("Calibri", 15)
            ebg = f"white"
            efg = f"black"
            ewidth = 200
            eborder = 2
            ebordercolor = f"#4152B3"
            eradius = 10
            egfcolor = ebg

            # ========= >>> last name label <<< =========
            space1 = Label(center, text="", bg=lbg).pack(side=TOP, pady=1)
            lfn = Label(center, text="First name", bg=lbg, fg=lfg, font=lfont)
            lfn.pack(side=TOP)
            # ========= >>> last name entry <<< =========
            efn = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            efn.pack(side=TOP, pady=5)
            # ========= >>> middle initial label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lmi = Label(center, text="Middle initials", bg=lbg, fg=lfg, font=lfont)
            lmi.pack(side=TOP)
            # ========= >>> field for middle initial entry <<< =========
            emi = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            emi.pack(side=TOP, pady=5)
            # ========= >>> last name label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lln = Label(center, text="Last name", bg=lbg, fg=lfg, font=lfont)
            lln.pack(side=TOP)
            #  ========= >>> field for last name entry <<< =========
            eln = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            eln.pack(side=TOP, pady=5)
            # ========= >>> date of birth label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            ldob = Label(
                center, text="Date of Birth (MM-DD-YYYY)", bg=lbg, fg=lfg, font=lfont
            )
            ldob.pack(side=TOP)
            # ========= >>> field for date of birth entry <<< =========
            edob = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            edob.pack(side=TOP, pady=5)
            # ========= >>> security question label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            lsq = Label(center, text="Security Question", bg=lbg, fg=lfg, font=lfont)
            lsq.pack(side=TOP)
            # ========= >>> field for security entry <<< =========
            esq = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            esq.pack(side=TOP, pady=5)
            # ========= >>> answer question label <<< =========
            space2 = Label(center, text="", bg=lbg, font=("Calibri", 3)).pack(side=TOP)
            laq = Label(
                center, text="Answer to Security Question", bg=lbg, fg=lfg, font=lfont
            )
            laq.pack(side=TOP)
            # ========= >>> field for answer entry <<< =========
            eaq = customtkinter.CTkEntry(
                center,
                width=ewidth,
                border_color=ebordercolor,
                border_width=eborder,
                bg_color=ebg,
                text_color=efg,
                fg_color=egfcolor,
                corner_radius=eradius,
            )
            eaq.pack(side=TOP, pady=5)

            # confirm function
            def confirm():
                if (
                    validate.fields(eln.get())
                    or validate.fields(efn.get())
                    or validate.fields(emi.get())
                    or validate.fields(edob.get())
                    or validate.fields(esq.get())
                    or validate.fields(eaq.get())
                ):
                    error.empty()
                else:
                    if Q.write_profile(
                        Q.get_active(),
                        efn.get(),
                        emi.get(),
                        eln.get(),
                        edob.get(),
                        esq.get(),
                        eaq.get(),
                    ):
                        root.destroy()
                        if success.personal_info_added():
                            global new_user_process_done
                            new_user_process_done = True

            btn = customtkinter.CTkButton(
                center,
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
            btn.place(x=230, y=445)

            center.pack(side=TOP, pady=45)
            center.pack_propagate(False)

            main.pack()
            main.pack_propagate(False)

            root.mainloop()

        __init__()

        if new_user_process_done:
            return True
