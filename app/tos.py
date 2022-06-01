from tkinter import *
import tkinter.messagebox

isOK = False

class tos():

    def __init__():

        def main():

            root  = Tk()
            root.title(f'Savings Tracker')
            root.geometry(f'740x390')
            root.resizable(False, False)
            getbg = PhotoImage(file="app/res/tos.png")
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)
            getbutton = PhotoImage(file='app/res/accept.png')
            setbutton = Label(image=getbutton)

            """def on_click(text):
                tkinter.messagebox.OK("Button label", text)
                global isOK 
                isOK = True"""

            def onClick(text):
                tkinter.messagebox.showinfo("Terms of Service", text)
                global isOK 
                isOK = True
                root.destroy()

            #-! button = Button(root,image=getbutton,borderwidth=0,bg='white',command=lambda: on_click("Hi")).pack(side=BOTTOM, pady=60)

            button = Button(root, image=getbutton, borderwidth=0,
                command=lambda: onClick("You accepted Terms of Service"))
            button.pack(side=BOTTOM, pady=60)

            root.mainloop()

        main()

        if isOK:
            return True