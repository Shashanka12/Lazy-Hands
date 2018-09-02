count=0
from tkinter import *

def rd():
    gui=Tk()
    gui.title("News")
    gui.config(background='alice blue')
    import feedparser

    def parseRSS( rss_url ):
        return feedparser.parse( rss_url ) 
    

    def getHeadlines( rss_url ):
        global count
        headlines = []
    
        feed = parseRSS( rss_url )
        for newsitem in feed['items']:
            count+=1
            if(count<=5):
                headlines.append(newsitem['title'])
        count=0
        return headlines
 

    allheadlines = []
 

    newsurls = {
    't_s':           'http://feeds.feedburner.com/ndtvnews-top-stories',
    'sport': 'http://feeds.feedburner.com/ndtvsports-latest',
    'world':'http://feeds.feedburner.com/ndtvnews-world-news',
    'india':'http://feeds.feedburner.com/ndtvnews-india-news'
    }
 
    for key,url in newsurls.items():
        allheadlines.extend( getHeadlines( url ) )
    p_nws=[]
    p_nws=allheadlines.copy()
    #if(p_nws[0]!=allheadlines[0]):
    #    pass
    a_nws=[]
    for hl in allheadlines:
        a_nws.append(chr(7)+" "+hl)
    l=Label(gui,text="Headlines",bg='alice blue')
    l1=Label(gui,text=a_nws[0],bg='alice blue')
    l2=Label(gui,text=a_nws[1],bg='alice blue')
    l3=Label(gui,text=a_nws[2],bg='alice blue')
    l4=Label(gui,text=a_nws[3],bg='alice blue')
    l5=Label(gui,text=a_nws[4],bg='alice blue')
    l6=Label(gui,text=a_nws[5],bg='alice blue')
    l7=Label(gui,text=a_nws[6],bg='alice blue')
    l8=Label(gui,text=a_nws[7],bg='alice blue')
    l9=Label(gui,text=a_nws[8],bg='alice blue')
    l10=Label(gui,text=a_nws[9],bg='alice blue')
    l11=Label(gui,text=a_nws[10],bg='alice blue')
    l12=Label(gui,text=a_nws[11],bg='alice blue')
    l13=Label(gui,text=a_nws[12],bg='alice blue')
    l14=Label(gui,text=a_nws[13],bg='alice blue')
    l15=Label(gui,text=a_nws[14],bg='alice blue')
    l16=Label(gui,text=a_nws[15],bg='alice blue')
    n_t1=Label(gui,text="\nTop Stories\n",bg='alice blue')
    n_t2=Label(gui,text="\nSport\n",bg='alice blue')
    n_t3=Label(gui,text="\nWorld\n",bg='alice blue')
    n_t4=Label(gui,text="\nIndia\n",bg='alice blue')
    l.pack()
    n_t1.pack()
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    n_t2.pack()
    l5.pack()
    l6.pack()
    l7.pack()
    l8.pack()
    n_t3.pack()
    l9.pack()
    
    l10.pack()
    l11.pack()
    l12.pack()
    
    n_t4.pack()
    l13.pack()
    l14.pack()
    l15.pack()
    l16.pack()
    gui.mainloop()

