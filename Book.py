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
        self.__description = soup.find("meta", attrs={'name':'description'}).get('content') 
        self.__category = category
        self.__reviewRating = self._parseRate(soup.find(class_="icon-star").parent.attrs.get('class')[1])
        self.__imageUrl = self._parseImageURL(soup.find(class_="item active").find("img").get('src'))



    def printDescription(cls):
        print(cls.__description)

    def getTitle(cls):
        return cls.__title

    def toString(cls):

        strContent = [None] * 10

        strContent[0] = cls._url
        strContent[1] = cls.__upc
        strContent[2] = cls.__title
        strContent[3] = cls.__priceInclude
        strContent[4] = cls.__priceExclude
        strContent[5] = cls.__availableCount
        strContent[6] = cls.__description
        strContent[7] = cls.__category
        strContent[8] = str(cls.__reviewRating)
        strContent[9] = cls.__imageUrl

        return "\n".join(strContent)