from tkinter import *
import tkinter.messagebox
import customtkinter

# >>> global var <<<
tos_process_done = False

class tos():

    def __init__():

        def main():
            WIDTH = 740
            HEIGHT = 390

            # ========= >>> main window <<< ========= 
            root  = Tk()
            root.title(f'Savings Tracker')
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x_coordinate = (screen_width/2)-(WIDTH/2)
            y_coordinate = (screen_height/2)-(HEIGHT/2)
            root.geometry("%dx%d+%d+%d" %(WIDTH,HEIGHT,x_coordinate,y_coordinate))
            root.resizable(False, False)
           
            # ========= >>> set background <<< =========
            getbg = PhotoImage(file=f'app/res/tos.png')
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)

            def onClick(text):
                tkinter.messagebox.showinfo(f'Terms of Service', text)
                global tos_process_done 
                tos_process_done = True
                root.destroy()

            btn = customtkinter.CTkButton(  root,
                                            text="Accept Terms of Service",
                                            corner_radius=10,
                                            border_width=0,
                                            text_font=(f'Calibri', 11, f'bold'),
                                            text_color=f'white',
                                            fg_color=f'#6595D4',
                                            bg_color=f'white',
                                            hover_color=f'#69D567',
                                            command=lambda: onClick(f'You accepted Terms of Service'),
                                            width=200     )
            btn.pack(side=BOTTOM, pady=68)
            
            print(f' WAIT ACCEPT TOS')

            root.mainloop()

        main()

        if tos_process_done:
            return True