from operator import is_
from tkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox
import json
import os

# to create window
root  = Tk()
# to change window title
root.title('Savings Tracker')
# to set window size
root.geometry("740x390") # orig window 700x350
# to make window non-resizable
root.resizable(False, False) # set to true to make window resizable
# define background image
_file = Image.open("app/res/tos.png").resize((740, 390), Image.ANTIALIAS)
_bg = ImageTk.PhotoImage(_file)
_set = tkinter.Label(image=_bg)
_set.image = _bg
_set.place(x=0, y=0)

def destroy(m):
    tkinter.messagebox.showinfo('Terms of Service', m)
    print(' TOS ACCEPTED')
    root.destroy()
    print('\n LOADING LOGIN PAGE')
    import login

# terms of service
get_accept_button = PhotoImage(file='app/res/accept.png')
bg_button = Label(image=get_accept_button)

try:
    print('\n RETRIEVING TOS')
    to_file = os.getcwd() + "\\app\\" # to get current directory and set path to app folder
    with open(to_file + "script.json", "r") as open_tos: # to open json file
        get_tos = json.load(open_tos)
        for x in get_tos:
            x_tos = x['tos']
    # to create label
    print(' WAITING FOR ACCEPT TOS')
    _w_s_01 = Label(root,text="").pack(side=TOP,pady=20) # blank label to serve as divider
    _title = Label(root,text=x_tos['title'],font=("Arial",18,"bold"),bg='white',fg='#7B96D4').pack(side=TOP,pady=12) # orig font 17
    _tos = Label(root,text=x_tos['tos'],font=("Arial",10),bg='white',fg='#4152B3').pack(side=TOP,pady=1) # orig font 10
    _tos = Label(root,text=x_tos['tos_text'],font=("Arial",10),bg='white',fg='#4152B3').pack(side=TOP,pady=1) # orig font 8 : pady 0
    _accept = Button(root,image=get_accept_button,font=("Arial", 10),borderwidth=0,bg='white',command=lambda m="You accepted terms of service": destroy(m)).pack(side=TOP,pady=30) # orig font 9 : pady 30

except:
    for x in range(0,5):
        print("\n ERROR: TOS.JSON COULDN'T BE FOUND. PLEASE CHECK IF EXIST IN APP FOLDER")

# to run in loop
root.mainloop()