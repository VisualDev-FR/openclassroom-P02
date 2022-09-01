from bs4 import BeautifulSoup
import requests

class Book:

    url = ""
    upc  = ""
    title = ""
    priceInclude = ""
    priceExclude = ""
    availableCount = ""
    description = ""
    category = ""
    reviewRating = ""
    imageUrl = ""

    def __init__(self, url) -> None:

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        productInfos = soup.find(class_="table table-striped").find_all('td')

        self.url = url
        self.upc = productInfos[0].get_text()
        self.title = soup.find("li", class_="active").string
        self.priceInclude = productInfos[3].get_text()
        self.priceExclude = productInfos[2].get_text()
        self.availableCount = productInfos[5].get_text()
        self.description = ""
        self.category = ""
        self.reviewRating = self.__parseRate(soup.find(class_="icon-star").parent.attrs.get('class')[1])
        self.imageUrl = ""

    @staticmethod
    def __parseRate(strRate):
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