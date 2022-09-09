from opcode import hasname
import requests
from bs4 import BeautifulSoup

from Book import Book
from Category import Category
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

# Main program

""" 
cat = ctg.Category("https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html", "Mystery")

#cat.readBooks("https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html")

book = bk.Book("https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html", "Mystery")

print(book.toString())
 """


page = Page("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")

print(page.getNextURL())
