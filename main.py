
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import tkinter as tk
from tkinter.ttk import *

csvUsers_data=open('users_data.csv','w')
csvUWriter = csv.writer(csvUsers_data)
csvUWriter.writerow(["user name","location","Reviews"])

csvRestaurant_data=open('restaurant_data.csv','w')
csvRWriter = csv.writer(csvRestaurant_data) 





def show_entry_fields():
    print("Le lien est : %s" % (e1.get()))
    def search_for_R(R_link):
        users_name=[]
        html = urlopen(R_link)
        html_soup = BeautifulSoup(html, 'html.parser')
        div= html_soup.findAll("div",{"class":"info_text pointer_cursor"})
        for i in div:
            text= str(i)[106:]
            text=text.replace('</div></div>','')
            users_name.append(text)
        cond=users_name[0]
        c=1
        index = R_link.find('Reviews')
        R_link = R_link[:index+7] + str(c*10) + R_link[index+7:]
        while True:
            html = urlopen(R_link)
            html_soup = BeautifulSoup(html, 'html.parser')
            div= html_soup.findAll("div",{"class":"info_text pointer_cursor"})
            for i in div:
                text= str(i)[106:]
                text=text.replace('</div></div>','')
                if text == cond:
                    return users_name
                users_name.append(text)
            c=c+1

    def user_info(user_name):
        if " " in user_name:
            return ["can't determine username ","can't determine location ","can't determine username reviews"]
        html = urlopen("https://www.tripadvisor.com/Profile/"+user_name)
        html_soup = BeautifulSoup(html, 'html.parser')
        location = html_soup.find("span",{"class":"_2VknwlEe _3J15flPT default"})
        location = str(location)[94:]
        location = location[:-7]
        review=html_soup.find_all("div",{"class","_133ThCYf"})
        user_reviews=[]
        for i in review:
            rev=str(i)[43:]
            rev=rev[:-10]
            user_reviews.append(rev)
        return [user_name,location,user_reviews]

    users_name = search_for_R(str(e1.get()))

    for name in users_name:
        us_in=user_info(name)
        csvUWriter.writerow([us_in[0],us_in[1],str(us_in[2]).encode('utf8')])
        
    for i in users_name:
        csvRWriter.writerow([i])


interface = tk.Tk()

interface.title("Trip Advisor")
interface.geometry("400x200")
tk.Label(interface, 
         text="Web scraping!").grid(row=0)
tk.Label(interface, 
         text="Coller ici le lien du restaurant").grid(row=1)




e1 = tk.Entry(interface)


e1.grid(row=1, column=1)




tk.Button(interface, 
          text='Valider', command=show_entry_fields).place(x=200,y=150)



tk.mainloop()


