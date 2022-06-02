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
            getbg = PhotoImage(file=f'app/res/tos.png')
            setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)
            # button ui
            getbutton = PhotoImage(file=f'app/res/accept.png')
            setbutton = Label(image=getbutton)

            def enter(e):
                gethover = PhotoImage(file=f'app/res/accepthover.png')
                button[f'image'] = gethover
                button.image = gethover
            
            def leave(e):
                getdefault = PhotoImage(file=f'app/res/accept.png')
                button[f'image'] = getdefault
                button.image = getdefault

            def onClick(text):
                tkinter.messagebox.showinfo(f'Terms of Service', text)
                global isOK 
                isOK = True
                root.destroy()

            button = Button(root, image=getbutton, borderwidth=0, bg='white',
                command=lambda: onClick(f'You accepted Terms of Service'))
            button.image = getbutton
            button.pack(side=BOTTOM, pady=60)

            button.bind(f'<Enter>', enter)
            button.bind(f'<Leave>', leave)

            print(f' WAIT ACCEPT TOS')

            root.mainloop()

        main()

        if isOK:
            return True