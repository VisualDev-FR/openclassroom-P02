from opcode import hasname
import requests
from bs4 import BeautifulSoup as bs

from Book import Book
from Category import Category
from Page import Page

bookScrappingURL = "https://books.toscrape.com/index.html"
blankCategories = bs(requests.get(bookScrappingURL).content, 'html.parser').find('ul', class_='nav nav-list').find_all('li')

#csvDirectory = input("Please specifie a valid path, to generate csv files : ")
#csvDirectory = "C:\Users\menan\Desktop\OpenClassrooms\P02\openclassroom-P02\csv"

csvDirectory = "C:/Users/menan/Desktop/OpenClassrooms/P02/openclassroom-P02/csv/"

for blankCat in blankCategories:
    
    strCat = bs(str(blankCat), 'html.parser').find('a').get_text().replace("    ","").replace("\n","")
    urlCat = "https://books.toscrape.com/" + bs(str(blankCat), 'html.parser').find('a').get('href')

    if strCat != "Books":

        category = Category(urlCat, strCat)
        category.writeCSV(csvDirectory)
        #category.print()
