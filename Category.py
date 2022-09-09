from fileinput import filename
from Book import Book
from Page import Page
import csv

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

    def writeCSV(cls, fileLocation):

        fileName = fileLocation + cls.__category + ".csv"

        fichier = open(fileName, "wb")
        fichier.write(str(cls.__getHeaders()).encode('utf8'))

        for urlBook in cls.__booksURL:
            book = Book(urlBook, cls.__category)
            fichier.write(book.toString())

        fichier.close()

        print("printing csv : '" + cls.__category + "' done.")

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

    def __getHeaders(cls):

        headers = [None] * 10

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

        return ";".join(headers) + "\n"

    def print(cls):

        print(cls.__category, ": nb Results =", len(cls.__booksURL))
        index = 0

        for urlBook in cls.__booksURL:
            index += 1
            #book = Book(urlBook, cls.__category)
            #print("     " + "%02d" % index, book.getTitle())

            print("     " + "%02d" % index, urlBook)
        
        print(" ")            
    