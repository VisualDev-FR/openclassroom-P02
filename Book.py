from typing_extensions import Self
from bs4 import BeautifulSoup

class Book:

    soup:BeautifulSoup = None
    productInfos = []
    url = ""

    def __init__(self, url, soup:BeautifulSoup) -> None:
        self.url = url
        self.soup = soup
        self.productInfos = soup.find(class_="table table-striped").find_all("td")

    @classmethod
    def getProductPageUrl(cls):
        return cls.url

    @classmethod
    def getUPC(cls):
        return cls.productInfos[0]

    @classmethod
    def getBookTitle(cls):
        return cls.soup.find("li", class_="active").string

    @classmethod
    def getPriceInclude(cls):
        return cls.productInfos[3]

    @classmethod
    def getPriceExclude(cls):
        return cls.productInfos[2]

    @classmethod
    def getAvailableCount(cls):
        return cls.productInfos[5]

    @classmethod
    def getDescription(cls):
        return        

    @classmethod
    def getCategory(cls):
        return

    @classmethod
    def getReviewRating(cls):
        return

    @classmethod
    def getImageUrl(cls):
        return