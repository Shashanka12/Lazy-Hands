from datetime import datetime
from threading import Timer
from tkinter import filedialog
from tkinter import *
import os
def tm():
    def sett():
        global f_n
        f_n="C:\\Users\\Sasanka\\PycharmProjects\\untitled14\\best_alarm_2014_ever.mp3"
        gui.withdraw()
        aday=int(a_day.get())
        amonth=int(a_month.get())
        ahour=int(a_hour.get())
        aminute=int(a_minutes.get())
        asec=int(a_seconds.get())
        y=x.replace(day=aday,month=amonth, hour=ahour, minute=aminute, second=asec)
        delta_t=y-x
        secs=delta_t.seconds+1
        def alarm():
            os.system("start "+f_n)
        def c1():
            root.withdraw()
        def c2():
            global f_n
            f_n= filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
            root.withdraw()
        root = Tk()
        L=Label(root,text="Is it an Alarm or do you want to open an app")
        B1=Button(root,text="Alarm",command=c1)
        B2=Button(root,text="App",command=c2)
        B1.grid(row=0,column=0)
        B2.grid(row=0,column=1)
        t = Timer(secs, alarm)
        t.start()
            
            
        
    gui=Tk()
    gui.title("FB")
    gui.config(background='alice blue')
    
    x=datetime.today()

    l=Label(gui,text="Date",bg='alice blue')
    l.grid(row=0,column=0)
    a_day=StringVar(gui)
    a_day.set(1)
    w1=OptionMenu(gui,a_day,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    w1.grid(row=0,column=1)



    l2=Label(gui,text="Month",bg='alice blue')
    l2.grid(row=1,column=0)
    a_month=StringVar(gui)
    a_month.set(1)
    w2=OptionMenu(gui,a_month,1,2,3,4,5,6,7,8,9,10,11,12)
    w2.grid(row=1,column=1)
    
    l3=Label(gui,text="Hour",bg='alice blue')
    l3.grid(row=2,column=0)
    a_hour=StringVar(gui)
    a_hour.set(1)
    w3=OptionMenu(gui,a_hour,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
    w3.grid(row=2,column=1)
    

    l4=Label(gui,text="Minutes",bg='alice blue')
    l4.grid(row=3,column=0)
    a_minutes=StringVar(gui)
    a_minutes.set(1)
    w4=OptionMenu(gui,a_minutes,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59)
    w4.grid(row=3,column=1)

    l5=Label(gui,text="Seconds",bg='alice blue')
    l5.grid(row=4,column=0)
    a_seconds=StringVar(gui)
    a_seconds.set(1)
    w5=OptionMenu(gui,a_seconds,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59)
    w5.grid(row=4,column=1)

    b1=Button(gui,text="Submit",command=sett)
    b1.grid(row=10,column=5,columnspan=2)
    gui.mainloop()
    

