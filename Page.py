#from dataclasses import replace
import requests
from bs4 import BeautifulSoup as bs

class Page:

    def __init__(self, url) -> None:
        self._url = url
        self._content = requests.get(url).content

    def hasNextPage(cls):
        # does the page has a 'next' button ?
        soup = bs(cls._content, 'html.parser')
        return len(soup.find_all(class_='next')) > 0

    def _getNextURL(cls):

        # Find the index of the next page
        nextIndex = bs(cls._content, 'html.parser').find(class_='next').find('a').get('href')

        # Split the url in order to concatenate it with the next index
        nextURL = str(cls._url).split("//")[1].split("/")
        nextURL[len(nextURL) - 1] = nextIndex

        # concatenate the full url
        return "https://" + "/".join(nextURL)

    def _setPage(cls, url):
        cls._url = url
        cls._content = requests.get(url).content

    def _getHtmlParser(cls, strContent):
        return bs(strContent, 'html.parser')

    @staticmethod
    def _parsBookURL(strBookUrl):
        return "https://books.toscrape.com/catalogue/" + strBookUrl.replace("../", "")

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