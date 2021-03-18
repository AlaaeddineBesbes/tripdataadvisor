
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd


def search_for_R(R_name):
    html = urlopen("https://www.tripadvisor.com/Restaurant_Review-g609074-d4064823-Reviews-Pizzahut-Coatbridge_North_Lanarkshire_Scotland.html")
    html_soup = BeautifulSoup(html, 'html.parser')
    link = html_soup.find_all(class_="review-container")
    print(link)
    
search_for_R("majid")

#page=requests.get("https://www.tripadvisor.com/")
#print(page.text)


