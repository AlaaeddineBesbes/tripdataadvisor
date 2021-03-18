
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd


def search_for_R(R_name):
    html = urlopen("https://www.tripadvisor.com/Search?q="+R_name)
    html_soup = BeautifulSoup(html, 'html.parser')
    link = html_soup.find_all(class_="rebrand_2017 js_logging desktop_web Search")
    print(link)
    
search_for_R("majid")

#page=requests.get("https://www.tripadvisor.com/")
#print(page.text)


