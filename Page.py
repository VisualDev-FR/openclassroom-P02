import sys
import math
import requests
from bs4 import BeautifulSoup as bs

class Page:

    def __init__(self, url) -> None:
        self._url = url
        self._content = requests.get(url).content

    def hasNextPage(cls):
        soup = bs(cls._content, 'html.parser')
        return len(soup.find_all('a', class_='next')) > 0

    def getNextURL(cls):
        
        # https://books.toscrape.com/catalogue/category/books/mystery_3/index.html

        nextIndex = bs(cls._content, 'html.parser').find(class_='next').find('a').get('href')
        nextURL = str(cls._url).split("//")[1].split("/")
        nextURL[len(nextURL) - 1] = nextIndex
        return "https://" + "/".join(nextURL)

    @staticmethod
    def _parseImageURL(strImageUrl):
        return "https://books.toscrape.com/" + strImageUrl.replace("../", "")

    @staticmethod
    def _parseRate(strRate):
        if strRate.lower() == "one":
            return 1
        elif strRate.lower() == "two":
            return 2
        elif strRate.lower() == "three":
            return 3
        elif strRate.lower() == "four":
            return 4
        elif strRate.lower() == "five":
            return 5
        else:
            return 0