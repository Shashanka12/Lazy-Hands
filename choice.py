import webbrowser
from tkinter import *

def own():
    gui=Tk()
    gui.title("OC")
    def next():
        ab=Tk()
        l1=Label(ab,text="Enter the website to be saved for fast accessing:")
        l2=Label(ab,text="Enter the short cut key:")
        V1=StringVar()
        V2=StringVar()
        e1=Entry(ab,textvariable=V1)
        e2=Entry(ab,textvariable=V2)
        def save():
            fav=str(V1.get())
            key=str(V2.get())
            with open('pref.txt','a') as f:
                f.write("\n"+key+"|"+fav)
        l1.grid(row=0,column=0)
        e1.grid(row=0,column=1)
        l2.grid(row=1,column=0)
        e2.grid(row=1,column=1)
        b1=Button(ab,text="Press Me",command=save)
        b1.grid(row=2)
        ab.mainloop()
    def st():
        with open('pref.txt','r') as f:
            for line in f:
                temp=line.split("|")
                if (temp[0]==key.get()): 
                    webbrowser.open(temp[1])
                    return
        gui.withdraw()
        next()
    l1=Label(gui,text="Enter the key:")
    key=StringVar()
    e1=Entry(gui,textvariable=key)
    l1.grid(row=0,column=0)
    e1.grid(row=0,column=1)
    b1=Button(gui,text="Submit",command=st)
    b1.grid(row=1)
    
    
    gui.mainloop()



