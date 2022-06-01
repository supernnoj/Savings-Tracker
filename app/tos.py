from email.mime import image
from tkinter import *
import tkinter.messagebox

isOK = False

class tos():

    def __init__():

        def main():

            # create window
            root  = Tk()
            root.title(f'Savings Tracker')
            root.geometry(f'740x390')
            root.resizable(False, False)
            # set background
            getbg = PhotoImage(file="app/res/tos.png")
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)
            # button ui
            getbutton = PhotoImage(file='app/res/accept.png')
            setbutton = Label(image=getbutton)

            def enter(e):
                gethover = PhotoImage(file="app/res/accepthover.png")
                button['image'] = gethover
                button.image = gethover
            
            def leave(e):
                getdefault = PhotoImage(file="app/res/accept.png")
                button['image'] = getdefault
                button.image = getdefault

            def onClick(text):
                tkinter.messagebox.showinfo("Terms of Service", text)
                global isOK 
                isOK = True
                root.destroy()

            button = Button(root, image=getbutton, borderwidth=0, bg='white',
                command=lambda: onClick("You accepted Terms of Service"))
            button.image = getbutton
            button.pack(side=BOTTOM, pady=60)

            button.bind("<Enter>", enter)
            button.bind("<Leave>", leave)

            print(' WAIT ACCEPT TOS')

            root.mainloop()

        main()

        if isOK:
            return True