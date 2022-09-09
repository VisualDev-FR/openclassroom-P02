from Page import Page

""" Headers :

    headers[0] = "product_page_url"
    headers[1] = "universal_ product_code (upc)"
    headers[2] = "title"
    headers[3] = "price_including_tax"
    headers[4] = "price_excluding_tax"
    headers[5] = "number_available"
    headers[6] = "product_description"
    headers[7] = "category"
    headers[8] = "review_rating"
    headers[9] = "image_url"
"""

class Category(Page):

    def __init__(self, url, category) -> None:

        super().__init__(url)

        self.__category = category
        self.__booksURL = []
        self.__readBookURLs()

    def __readBookURLs(cls):

        # we keep the category url + 1st page content in memory

        currentPage = cls._url
        currentContent = cls._content

        while True:

            pageBooks = cls._getHtmlParser(cls._content).find('ol', class_='row').find_all("li")

            for i in range(len(pageBooks)):            
                bookUrl = cls._getHtmlParser(str(pageBooks[i])).find('a').get("href")
                cls.__booksURL.append(cls._parsBookURL(bookUrl))

            if cls.hasNextPage():
                cls._setPage(cls._getNextURL())
            else:
                break
        
        # we set back the category url + 1st page content before exiting the function

        cls._url = currentPage
        cls._content = currentContent        

    def getCategory(cls):
        return cls.__category

    def getBookURLs(cls):
        return cls.__booksURL
    