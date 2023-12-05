# https://en.wikipedia.org/wiki/Programmer

import bs4
import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    tag = soup.find_all("a")
    for t in tag:
        url2 = t.get("href")
        print(url2)
    #print(tag)

    #print(soup.title.string)
    #var = soup.find(id = "Count")
    #print(var.string)
    #print(var)


get_page(input("What url would you like to scrape?"))
