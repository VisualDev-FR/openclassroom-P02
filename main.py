import requests
import Book as bk
from bs4 import BeautifulSoup

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


book = bk.Book("https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")

print(book.url)
print(book.upc)
print(book.title)
print(book.priceInclude)
print(book.reviewRating)



