
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd


def search_for_R(R_name):
    #html = urlopen("https://www.tripadvisor.com/Search?q="+R_name)
    page=requests.get("https://www.tripadvisor.com/"+R_name)
    print(page.text)
#search_for_R("majid")
#html_soup = BeautifulSoup(html, 'html.parser')
#page=requests.get("https://www.tripadvisor.com/")
#print(page.text)


