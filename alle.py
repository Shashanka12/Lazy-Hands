from bs4 import BeautifulSoup
from urllib.request import urlopen
import pyjokes
import webbrowser
from tkinter import *
import sports

#print(bsobj.h1)

def joke():
    #----JOKE----
    window=Tk()
    var=StringVar()
    window.title("Joke of the day!")
    window.configure(background='white')
    #print('JOKE')
    j=pyjokes.get_joke()
    w=Label(window,text=j,relief='raised')
    w.pack();
    #print(pyjokes.get_joke())
    window.mainloop()

def gaana():
    #----GAANA----
    html=urlopen("https://gaana.com/playlist/gaana-dj-todays-top-5-hindi")
    bsobj=BeautifulSoup(html.read(),'lxml')
    webbrowser.open('https://gaana.com/playlist/gaana-dj-todays-top-5-hindi')

def score():
    #----SCORE----
    all_matches=sports.all_matches()
    football=all_matches['soccer']
    tennis=all_matches['tennis']
    print('FOOTBALL')
    for i in football:
        print(i)
        print()
    print('TENNIS')
    for i in tennis:
        print(i)
        print()
