import string
import re
import requests

from Page import Page

class Book(Page):

    def __init__(self, url, category) -> None:

        super().__init__(url)
        soup = self._getHtmlParser(self._content)
        
        productInfos = soup.find(class_="table table-striped").find_all('td')        

        self.__upc = productInfos[0].get_text()
        self.__title = soup.find("li", class_="active").string
        self.__priceInclude = productInfos[3].get_text()
        self.__priceExclude = productInfos[2].get_text()
        self.__availableCount = productInfos[5].get_text()
        self.__description = soup.find("meta", attrs={'name':'description'}).get('content').replace("\n", " ").replace(';', ',')
        self.__category = category
        self.__reviewRating = self._parseRate(soup.find(class_="icon-star").parent.attrs.get('class')[1])
        self.__imageUrl = self._parseImageURL(soup.find(class_="item active").find("img").get('src'))

    def __parseTitle(cls):
        return re.sub("[^a-zA-Z0-9]", "_", cls.__title) # regex removing all charachters differents from letters / numbers

    def printImage(cls, directoryPath:string):

        filename = directoryPath + "/" + cls.__parseTitle() + ".png"
        image = requests.get(cls.__imageUrl)

        file = open(filename, "wb")
        file.write(image.content)
        file.close

    def printDescription(cls):
        print(cls.__description)

    def getTitle(cls):
        return cls.__title

    def toString(cls):

        strContent = [None] * 10

        strContent[0] = str(cls._url)
        strContent[1] = str(cls.__upc)
        strContent[2] = str(cls.__title)
        strContent[3] = str(cls.__priceInclude)
        strContent[4] = str(cls.__priceExclude)
        strContent[5] = str(cls.__availableCount)
        strContent[6] = str(cls.__description)
        strContent[7] = str(cls.__category)
        strContent[8] = str(cls.__reviewRating)
        strContent[9] = str(cls.__imageUrl)

        return str(";".join(strContent) + "\n").encode('utf8')