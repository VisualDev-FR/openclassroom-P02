from turtle import bk
from bs4 import BeautifulSoup
import requests
from Page import Page

class Category(Page):

    def __init__(self, url, category) -> None:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.__url = url
        self.__category = category
        self.__resultsCount = int(soup.find(class_="form-horizontal").find("strong").get_text())
        self.__booksURL = []

    def readBooks(cls, url):   

        page = requests.get(url) 
        soup = BeautifulSoup(page.content, 'html.parser')        

        ls = soup.find('ol', class_='row').find_all("li")

        for i in range(len(ls)):            
            subSoup = BeautifulSoup(str(ls[i]), 'html.parser')
            cls.__booksURL.append(subSoup.find('a').get("href"))

        print("len = " + str(len(cls.__booksURL)))
        
    def printResults(cls):
        print(cls.__resultsCount)