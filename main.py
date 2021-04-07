
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd
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
users_name=[]
def search_for_R(R_name):
    html = urlopen("https://www.tripadvisor.com/Restaurant_Review-g651707-d1137600-Reviews-La_Table_d_Heloise-Cluny_Saone_et_Loire_Bourgogne_Franche_Comte.html")
    html_soup = BeautifulSoup(html, 'html.parser')
    div= html_soup.findAll("div",{"class":"info_text pointer_cursor"})
    for i in div:
        text= str(i)[106:]
        text=text.replace('</div></div>','')
        users_name.append(text)
    


def user_location(user_name):
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
 

print(user_location("kimbrona"))
#search_for_R("z")
#print(users_name)
#page=requests.get("https://www.tripadvisor.com/")
#print(page.text)


