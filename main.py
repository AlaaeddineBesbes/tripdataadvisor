
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv


csvUsers_data=open('users_data.csv','w')
csvUWriter = csv.writer(csvUsers_data)
csvUWriter.writerow(["user name","location","Reviews"])

csvRestaurant_data=open('restaurant_data.csv','w')
csvRWriter = csv.writer(csvRestaurant_data) 


'''
def generate_reve_link():
    i=1
    html = urlopen("https://www.tripadvisor.com/Restaurant_Review-g609074-d4064823-Reviews-Pizzahut-Coatbridge_North_Lanarkshire_Scotland.html")

    
    links=["https://www.tripadvisor.com/Restaurant_Review-g609074-d4064823-Reviews-Pizzahut-Coatbridge_North_Lanarkshire_Scotland.html"]
    html_soup = BeautifulSoup(html, 'html.parser')
    reviews1 = html_soup.find(class_="review-container")
    while True:
        link="https://www.tripadvisor.com/Restaurant_Review-g609074-d4064823-Reviews-or"+str(i*10)+"-Pizzahut-Coatbridge_North_Lanarkshire_Scotland.html"
        html1 = urlopen(link)
        html1_soup = BeautifulSoup(html1, 'html.parser')
        reviews= html1_soup.find(class_="review-container")
        if reviews.text == reviews1 :
            return links
        else:links.append(link)
        i+=1
print(generate_reve_link())
'''

def search_for_R(R_name):
    users_name=[]
    html = urlopen("https://www.tripadvisor.com/Restaurant_Review-g651707-d1137600-Reviews-La_Table_d_Heloise-Cluny_Saone_et_Loire_Bourgogne_Franche_Comte.html")
    html_soup = BeautifulSoup(html, 'html.parser')
    div= html_soup.findAll("div",{"class":"info_text pointer_cursor"})
    for i in div:
        text= str(i)[106:]
        text=text.replace('</div></div>','')
        users_name.append(text)
    cond=users_name[0]
    c=1
    while True:
        html = urlopen("https://www.tripadvisor.com/Restaurant_Review-g651707-d1137600-Reviews-or"+str(c*10)+"-La_Table_d_Heloise-Cluny_Saone_et_Loire_Bourgogne_Franche_Comte.html")
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

users_name = search_for_R("")


for i in users_name:
    csvRWriter.writerow([i])


for name in users_name:
    us_in=user_info(name)
    csvUWriter.writerow([us_in[0],us_in[1],us_in[2]])

#print(search_for_R("z"))
print(user_info("jjdcan"))
#for name in users_name:
   #
#print(users_name)
#page=requests.get("https://www.tripadvisor.com/")
#print(page.text)


