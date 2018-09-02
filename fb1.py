import os
import json
import facebook
import requests
from tkinter import *

def f1():
        gui=Tk()
        gui.title("FB")
        gui.config(background='alice blue')
        open("my_posts.jsonl","w").close()
        def sub1():
                global name,dob,loc,n_f,token
                token="EAAPEtxZBLvaoBAKZBxkeoZAZBZApY6hJrLqrL7zYOZCmzYxZBPAK8Ha2dbyZCMzwmSugEUezw7CsDNTqEhjyPwaw9vEq3OEqg6HR4nvOr26UfNOzVwR5d5jRkIerLrDmnO2jBZCYGE4rPH94oUJ7Y0CwymZAjbCJgnB7liU4DwbJgAuRqvpgIJ0OmwE9YHN0hyhDMvzTswZBveTvwZDZD"
                graph=facebook.GraphAPI(token)
                profile=graph.get_object("me",fields="name")
                st=str(json.dumps(profile,indent=4))
                st=st.replace("{","")
                st=st.replace("}","")
                st=st.replace("\n","")
                st=st.split(",")
                st[0]=st[0].strip()
                st[1]=st[1].strip()
                x=st[0].split(":")
                name=x[1].strip().lstrip('"').rstrip('"')
                profile=graph.get_object("me",fields="location")
                st=str(json.dumps(profile,indent=4))
                num=st.find('"name"')
                num_f=num+len('"name"')
                a=[]
                while(st[num_f]!='}'):
                        a.append(st[num_f])
                        num_f+=1
                loc=""
                for i in a:
                    loc+=i
                loc=loc[2:]
                loc=loc.strip().strip('"')

                profile=graph.get_object("me",fields="birthday")
                st=str(json.dumps(profile,indent=4))
                num=st.find('"birthday"')
                num_f=num+len('"birthday"')
                a=[]
                while(st[num_f]!=','):
                        a.append(st[num_f])
                        num_f+=1
                dob=""
                for i in a:
                        dob+=i
                dob=dob[2:]
                dob=dob.strip().strip('"')

                user=graph.get_object("me")
                friends = graph.get_connections(user["id"], "friends")
                st=str(json.dumps(friends, indent=4))
                num=st.find('"total_count"')
                num_f=num+len('"total_count"')
                a=[]
                while(st[num_f]!='}'):
                        a.append(st[num_f])
                        num_f+=1
                n_f=""
                for i in a:
                    n_f+=i
                n_f=n_f.strip(':')
                n_f=int(n_f)
        def sub2():
                graph=facebook.GraphAPI(token)
                posts=graph.get_connections('me','posts')

                while True:
                        try:
                                with open('my_posts.jsonl','a') as f:
                                        for post in posts['data']:
                                                f.write(json.dumps(post)+"\n")
                                        posts=requests.get(posts['paging']['next']).json()
                        except KeyError:
                                break
        def sub3():
                with open('my_posts.jsonl','r') as f:
                        for line in f:
                                if('"message"' in line):
                                        pos=line.find('"message"')
                                        pos_end=pos+len('"message"')
                                        a = []
                                        count=0
                                        while (1):
                                                if(line[pos_end]=='"'):
                                                        count+=1
                                                if(count==2):
                                                        break
                                                a.append(line[pos_end])
                                                pos_end += 1

                                        loc = ""
                                        for i in a:
                                                loc += i
                                        loc=loc.lstrip(":").strip()
                                        loc=loc[1:]
                                        loc="->"+loc
                                        lt=Label(gui,text=loc,bg='alice blue')
                                        lt.pack()
        sub1()
        sub2()
        sub3()
        gui.mainloop()

