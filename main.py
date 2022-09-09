from opcode import hasname
import requests
from bs4 import BeautifulSoup as bs

from Book import Book
from Category import Category
from Page import Page

bookScrappingURL = "https://books.toscrape.com/index.html"

blankCategories = bs(requests.get(bookScrappingURL).content, 'html.parser').find('ul', class_='nav nav-list').find_all('li')

# cd .\Desktop\OpenClassrooms\P02\openclassroom-P02\

for blankCat in blankCategories:
    
    strCat = bs(str(blankCat), 'html.parser').find('a').get_text().replace("    ","").replace("\n","")
    urlCat = "https://books.toscrape.com/" + bs(str(blankCat), 'html.parser').find('a').get('href')

    if strCat != "Books":

        category = Category(urlCat, strCat)        

        print(strCat, ": nb Results =", len(category.getBookURLs()))
        index = 0

        for urlBook in category.getBookURLs():
            index += 1
            book = Book(urlBook, strCat)
            print("     " + "%02d" % index, book.getTitle())
        
        print(" ")
