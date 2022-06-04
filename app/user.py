from tkinter import *
import tkinter.messagebox
from database import *

class user():
    
    def welcome():
        
        print(f' FOUND USER APP')

        print(f'\n user : {Q.get_user(Q.get_active())}')
        print(f' new user : {Q.verify_new(Q.get_active())}')

        def main():

            root = Tk()
            root.title(f'Hi, {Q.get_user(Q.get_active())}!')
            root.geometry("800x500") 
            root.resizable(False, False)
            #getbg = PhotoImage(file="app/res/home.png")
            #setbg = Label(root, image=getbg).place(x=0, y=0, relwidth=1, relheight=1)

            root.mainloop()

        def hello_user():
            tkinter.messagebox.showinfo(f'Hi, {Q.get_user(Q.get_active())}!', f'The system recognized that you are a new user of this app.\nLet us help you run a quick setup.')
            return True

        def setup():
            tkinter.messagebox.showinfo(f'Personal Info', f'Let us start with your personal information.')
            
            setup = Tk()
            setup.title(f'Personal Info')
            width_of_window = 350
            height_of_window = 500
            screen_width = setup.winfo_screenwidth()
            screen_height = setup.winfo_screenheight()
            x_coordinate = (screen_width/2)-(width_of_window/2)
            y_coordinate = (screen_height/2)-(height_of_window/2)
            setup.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
            setup.resizable(False, False)
            getcreatebg = PhotoImage(file = f'app/res/form.png')
            setcreatebg = Label(setup, image = getcreatebg).place(x=0, y=0, relwidth=1, relheight=1)
            
            setup.mainloop()

        if Q.verify_new(Q.get_active()):
            if hello_user():
                setup()
        else:
            main()