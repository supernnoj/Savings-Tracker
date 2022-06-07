from tkinter import *
from database import *
from database import *
from system import *
from new_user import *

class user():
    
    def welcome():

        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        root = customtkinter.CTk()
        root.title(f'Hi, {Q.get_user(Q.get_active())}!')
        root.geometry("780x520") 
        root.resizable(False, False)

        # ============ create two frames ============

        # configure grid layout (2x1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        frame_left = customtkinter.CTkFrame(master=root,
                                                 width=180,
                                                 corner_radius=0)
        frame_left.grid(row=0, column=0, sticky="nswe")

        frame_right = customtkinter.CTkFrame(master=root)
        frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        label_1 = customtkinter.CTkLabel(master=frame_left,
                                              text=f"{Q.get_user(Q.get_active())}",
                                              text_font=("Roboto Medium", 25))  # font name and size in px
        label_1.grid(row=1, column=0, pady=10, padx=10)

        button_1 = customtkinter.CTkButton(master=frame_left,
                                                text="CTkButton 1",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                                #command=root.button_event
                                                )
        button_1.grid(row=2, column=0, pady=10, padx=20)

        button_2 = customtkinter.CTkButton(master=frame_left,
                                                text="CTkButton 2",
                                                fg_color=("gray75", "gray30"),  # <- custom tuple-color
                                            )
                                                #command=root.button_event)
        button_2.grid(row=3, column=0, pady=10, padx=20)

        button_3 = customtkinter.CTkButton(master=frame_left,
                                                text="CTkButton 3",
                                                fg_color=("gray75", "gray30"),)  # <- custom tuple-color
                                                #command=root.button_event)
        button_3.grid(row=4, column=0, pady=10, padx=20)

        switch_1 = customtkinter.CTkSwitch(master=frame_left)
        switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")

        switch_2 = customtkinter.CTkSwitch(master=frame_left,
                                                text="Dark Mode",)
                                                #command=root.change_mode)
        switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")
        

        root.mainloop()