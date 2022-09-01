from ntpath import join
from tokenize import String
from typing_extensions import Self
from unittest.util import strclass
from bs4 import BeautifulSoup

class Book:

    url = ""
    upc  = ""
    title = ""
    priceInclude = 0
    priceExclude = 0
    availableCount = 0
    description = ""
    category = ""
    reviewRating = 0
    imageUrl = ""

    def __init__(self, url, soup:BeautifulSoup) -> None:
        
        productInfos = soup.find(class_="table table-striped").find_all("td")

        self.url = url
        self.upc = productInfos[0]
        self.title = soup.find("li", class_="active").string
        self.priceInclude = productInfos[3]
        self.priceExclude = productInfos[2]
        self.availableCount = productInfos[5]
        self.description = ""
        self.category = ""
        self.reviewRating = 0
        self.imageUrl = ""

    def toString(cls):

        strContent = [None] * 10

        strContent[0] = cls.url
        strContent[1] = cls.upc
        strContent[2] = cls.title
        strContent[3] = cls.priceInclude
        strContent[4] = cls.priceExclude
        strContent[5] = cls.availableCount
        strContent[6] = cls.description
        strContent[7] = cls.category
        strContent[8] = cls.reviewRating
        strContent[9] = cls.imageUrl

        return "\n".join(strContent)