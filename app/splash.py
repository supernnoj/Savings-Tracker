from tkinter.ttk import Progressbar
from tkinter import *
from tkinter import ttk
from customtkinter import *
import customtkinter

# >>> global var <<< 
splash_proccess_done = False

class splash():

    def __init__():

        w=Tk()

        width_of_window = 427
        height_of_window = 250
        screen_width = w.winfo_screenwidth()
        screen_height = w.winfo_screenheight()
        x_coordinate = (screen_width/2)-(width_of_window/2)
        y_coordinate = (screen_height/2)-(height_of_window/2)
        w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

        w.wm_overrideredirect(True)
        w.wm_attributes("-topmost",True)
        # w.lift()


        s = ttk.Style()
        s.theme_use('clam')
        s.configure("red.Horizontal.TProgressbar", foreground='white', background='#69D567')
                                         # #69D567 GREEN / #B5C9FD LIGHT BLUE / #273272 DARK BLUE
        progress=Progressbar(w,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=500,mode='determinate',)


        def new_win():
            global splash_proccess_done
            splash_proccess_done = True

        def bar():

            l4=Label(w,text='Savings Tracker is starting...',fg='white',bg=a)
            lst4=('Calibri (Body)',10)
            l4.config(font=lst4)
            l4.place(x=12,y=215)
            
            import time
            r=0
            for i in range(100):
                progress['value']=r
                w.update_idletasks()
                time.sleep(0.03)
                r=r+1
            
            w.destroy()
            new_win()
                
        progress.place(x=-10,y=235)

        a='#4152B3'
        Frame(w,width=427,height=241,bg=a).place(x=0,y=0)  #249794
        b1=customtkinter.CTkButton(  
                                    w,
                                    command=bar,
                                    #border_width=2,
                                    #border_color=f'white',
                                    text='Get Started',
                                    text_font=('Calibri', 10, 'bold'),
                                    text_color=f'#4152B3',
                                    fg_color='white',
                                    hover_color=f'#6595D4',
                                    bg_color=f'#4152B3',
                                    corner_radius=25,
                                    width=10  )
        #b1.place(x=170,y=195)
        b1.place(x=275,y=198)

        l4=Label(w,text='student\'s',fg='white',bg=a)
        lst4=('Calibri (Body)',10)
        l4.config(font=lst4)
        l4.place(x=50,y=62)

        l1=Label(w,text='SAVINGS',fg='white',bg=a)
        lst1=('Calibri (Body)',18,'bold')
        l1.config(font=lst1)
        l1.place(x=50,y=80)

        l2=Label(w,text='TRACKER',fg='white',bg=a)
        lst2=('Calibri (Body)',18)
        l2.config(font=lst2)
        l2.place(x=162,y=82)

        l3=Label(w,text='YOUR NO. 1 SAVING BUDDY FOR YOUR SAVING NEEDS',fg='white',bg=a)
        lst3=('Calibri (Body)',8)
        l3.config(font=lst3)
        l3.place(x=50,y=110)

        w.mainloop()
    
        if splash_proccess_done:
            return True


