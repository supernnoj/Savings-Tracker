from operator import is_
from re import I
from tkinter import *
import tkinter.messagebox

# to create window
root  = Tk()
# to change window title
root.title('Savings Tracker')
# to set window size
root.geometry("740x390") # orig window 700x350
# to make window non-resizable
root.resizable(False, False) # set to true to make window resizable
# define background image
bg = PhotoImage(file="app/res/tos.png")
_bg = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)

def destroy(m):
    tkinter.messagebox.showinfo('Terms of Service', m)
    print(' TOS ACCEPTED')
    root.destroy()
    print('\n LOADING LOGIN PAGE')
    import login

# terms of service
get_accept_button = PhotoImage(file='app/res/accept.png')
bg_button = Label(image=get_accept_button)

print('\n RETRIEVING TOS')

# to create label
print(' WAITING FOR ACCEPT TOS')
_accept = Button(root,image=get_accept_button,font=("Arial", 10),borderwidth=0,bg='white',command=lambda m="You accepted terms of service": destroy(m)).pack(side=BOTTOM,pady=60) # orig font 9 : pady 30

# to run in loop
root.mainloop()