from tkinter import *
from database import *
from database import *
from system import *
from new import *


class user:
    def welcome():

        customtkinter.set_appearance_mode(
            "System"
        )  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme(
            "blue"
        )  # Themes: "blue" (standard), "green", "dark-blue"

        root = customtkinter.CTk()
        root.title(f"Hi, {Q.get_user(Q.get_active())}!")
        root.geometry("780x520")
        root.resizable(False, False)

        # button functions
        """def button_event():
            print("Button pressed")

        def change_mode():
            if  switch_2.get() == 1:
                customtkinter.set_appearance_mode("dark")
            else:
                customtkinter.set_appearance_mode("light")

        def on_closing(root, event=0):
            root.destroy()"""

        # ============ create two frames ============

        # configure grid layout (2x1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_rowconfigure(0, weight=1)

        frame_left = customtkinter.CTkFrame(master=root, width=180, corner_radius=0)
        frame_left.grid(row=0, column=0, sticky="nswe")

        frame_right = customtkinter.CTkFrame(master=root)
        frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        label_1 = customtkinter.CTkLabel(
            master=frame_left,
            text=f"{Q.get_user(Q.get_active())}",
            text_font=("Roboto Medium", 25),
        )  # font name and size in px
        label_1.grid(row=1, column=0, pady=10, padx=10)

        button_1 = customtkinter.CTkButton(
            master=frame_left,
            text="VIEW PROFILE",
            fg_color=("gray75", "gray30"),  # <- custom tuple-color
            # command=root.button_event
        )
        button_1.grid(row=2, column=0, pady=10, padx=20)

        button_2 = customtkinter.CTkButton(
            master=frame_left,
            text="VIEW SETTINGS",
            fg_color=("gray75", "gray30"),  # <- custom tuple-color
        )
        # command=root.button_event)
        button_2.grid(row=3, column=0, pady=10, padx=20)

        button_3 = customtkinter.CTkButton(
            master=frame_left,
            text="SWITCH USER",
            fg_color=("gray75", "gray30"),
        )  # <- custom tuple-color
        # command=root.button_event)
        button_3.grid(row=4, column=0, pady=10, padx=20)

        """switch_1 = customtkinter.CTkSwitch(master=frame_left)
        switch_1.grid(row=9, column=0, pady=10, padx=20, sticky="w")"""

        switch_2 = customtkinter.CTkSwitch(
            master=frame_left,
            text="Dark Mode",
        )
        # command=root.change_mode)
        switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        frame_right.rowconfigure(7, weight=10)
        frame_right.columnconfigure((0, 1), weight=1)
        frame_right.columnconfigure(2, weight=0)

        frame_info = customtkinter.CTkFrame(master=frame_right)
        frame_info.grid(
            row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew"
        )

        # ============ frame_info ============

        # configure grid layout (1x1)
        frame_info.rowconfigure(0, weight=1)
        frame_info.columnconfigure(0, weight=1)

        label_info_1 = customtkinter.CTkLabel(
            master=frame_info,
            text="Current total balance: \n" + "00.000\n",
            # "Current balance:" ,
            height=100,
            fg_color=("white", "gray38"),  # <- custom tuple-color
            justify=tkinter.LEFT,
        )
        label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        progressbar = customtkinter.CTkProgressBar(master=frame_info)
        progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # ============ frame_right ============

        radio_var = tkinter.IntVar(value=0)

        label_radio_group = customtkinter.CTkLabel(
            master=frame_right, text="CTkRadioButton Group:"
        )
        label_radio_group.grid(
            row=0, column=2, columnspan=1, pady=20, padx=10, sticky=""
        )

        radio_button_1 = customtkinter.CTkRadioButton(
            master=frame_right, variable=radio_var, value=0
        )
        radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        radio_button_2 = customtkinter.CTkRadioButton(
            master=frame_right, variable=radio_var, value=1
        )
        radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        radio_button_3 = customtkinter.CTkRadioButton(
            master=frame_right, variable=radio_var, value=2
        )
        radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        slider_1 = customtkinter.CTkSlider(
            master=frame_right,
            from_=0,
            to=1,
            number_of_steps=3,
            command=progressbar.set,
        )
        slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        slider_2 = customtkinter.CTkSlider(master=frame_right, command=progressbar.set)
        slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        slider_button_1 = customtkinter.CTkButton(
            master=frame_right,
            height=25,
            text="CTkButton",
            # command=button_event
        )
        slider_button_1.grid(
            row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we"
        )

        slider_button_2 = customtkinter.CTkButton(
            master=frame_right,
            height=25,
            text="CTkButton",
            # command=button_event
        )
        slider_button_2.grid(
            row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we"
        )

        checkbox_button_1 = customtkinter.CTkButton(
            master=frame_right,
            height=25,
            text="CTkButton",
            border_width=3,  # <- custom border_width
            fg_color=None,  # <- no fg_color
            # command=self.button_event
        )
        checkbox_button_1.grid(
            row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we"
        )

        check_box_1 = customtkinter.CTkCheckBox(master=frame_right, text="CTkCheckBox")
        check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        check_box_2 = customtkinter.CTkCheckBox(master=frame_right, text="CTkCheckBox")
        check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        entry = customtkinter.CTkEntry(
            master=frame_right, width=120, placeholder_text="Search for available log"
        )
        entry.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        button_5 = customtkinter.CTkButton(
            master=frame_right,
            text="LOGOUT",
            # command=button_event
        )
        button_5.grid(row=8, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        radio_button_1.select()
        switch_2.select()
        slider_1.set(0.2)
        slider_2.set(0.7)
        progressbar.set(0.5)
        slider_button_1.configure(state=tkinter.DISABLED, text="Disabled Button")
        radio_button_3.configure(state=tkinter.DISABLED)
        check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        check_box_2.select()

        root.mainloop()
