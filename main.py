
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import csv
import tkinter as tk
from tkinter.ttk import *

csvUsers_data=open('users_data.csv','w')
csvUWriter = csv.writer(csvUsers_data)
csvUWriter.writerow(["user name","location","Reviews"])

csvRestaurant_data=open('restaurant_data.csv','w')
csvRWriter = csv.writer(csvRestaurant_data) 





def show_entry_fields():
    # a funciton that returns all the users that reveiwed the given retaurant
    def search_for_R(R_link):
        users_name=[]
        html = urlopen(R_link)
        html_soup = BeautifulSoup(html, 'html.parser')
        #extracting the div containing the review from only the first review page
        div= html_soup.findAll("div",{"class":"info_text pointer_cursor"})
        for i in div:
            #text manipulation to extract exactly the name of the user
            text= str(i)[106:]
            text=text.replace('</div></div>','')
            users_name.append(text)
            print(text)
        #we store the first user name 
        cond=users_name[0]
        c=1
        index = R_link.find('Reviews')
        #R_link is a model to generate all the rest of review pages
        R_link = R_link[:index+7] +"-or"+ str(c*10)+"-" + R_link[index+7:]

        while True:
            #creating the next  review page
            R_link = R_link[:index+7] +"-or"+ str(c*10)+"-" + R_link[index+7:]
            #extracting the reviews from the html page
            html = urlopen(R_link)
            html_soup = BeautifulSoup(html, 'html.parser')
            div= html_soup.findAll("div",{"class":"info_text pointer_cursor"})
            #extracting the reviwers names
            for i in div:
                text= str(i)[106:]
                text=text.replace('</div></div>','')
                #if text == cond then we went back to the first review page so we stop the extraction
                if text == cond:
                    return users_name
                users_name.append(text)
                print(text)
            c=c+1
    # fonction qui retourne les reviews faites par un user
    def user_info(user_name):
        # if there is a space in the user's name we can't extract his reviwes 
        if " " in user_name:
            return [user_name,"can't determine location ","can't determine username reviews"]
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
        print("searching for reviwes done by ",user_name)
        return [user_name,location,user_reviews]
    #putting the users names in a list 
    users_name = search_for_R(str(e1.get()))
    
    l=len(users_name)
    for name in users_name:
        #saving the names in a csv file
        csvRWriter.writerow([str(name).encode('utf8')])
        #us_in is user_information 
        us_in=user_info(name)
        #remove the name from the list to keep track of the number of names left 
        users_name.remove(name)

        print(l-len(users_name),"/",l,"done")
        #save the informations into the another csv file
        csvUWriter.writerow([us_in[0].encode('utf8'),us_in[1],str(us_in[2]).encode('utf8')])
        
    


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


