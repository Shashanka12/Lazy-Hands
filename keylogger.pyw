import pythoncom, pyHook
import news as nw
import fb1 as f1
import alarm as al
import choice as cht1
import alle as a12
open("op.txt","w").close()
open("op2.txt","w").close()
s_key="zxy"
ct=-1
kw=["nws1","sm2","tr3","gn6","sc8","ck9","jk11","sv5"]

def nf(s):
    f=open("op2.txt","a")
    global ct
    if(ct>=0):
        f.write(s)
    f.close()
    f=open("op2.txt","r")
    buf=f.read()
    f.close()
    for i in kw:
        if(buf.find(i.upper())!=-1):
            if(i=="nws1"):
                print("#")
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                nw.rd()
            if(i=="sm2"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                f1.f1()
            if(i=="tr3"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                al.tm()
            if(i=="gn6"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                a12.gaana()
            if(i=="sv5"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                import speech as sp
            if(i=="sc8"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                a12.score()
            if(i=="ck9"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                cht1.own()
            if(i=="jk11"):
                open("op2.txt",'w').close()
                open("op.txt",'w').close()
                a12.joke()
    ct+=1
    if(ct>=5):
        open("op2.txt",'w').close()
        open("op.txt",'w').close()

def OnKeyboardEvent(event):

    f=open("op.txt","a")
    f.write(event.Key)
    f.close()
    f = open("op.txt", "r+")
    buf = f.read()
    f.close()
    global s_key
    if (buf.lower().find(s_key)!=-1):
        nf(event.Key)
    return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
