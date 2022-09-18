import requests
from tkinter import filedialog
from bs4 import BeautifulSoup as bs
from Category import Category

bookScrappingURL = "https://books.toscrape.com/index.html"  # home page, from wich we read all catagories
blankCategories = bs(requests.get(bookScrappingURL).content, 'html.parser').find('ul', class_='nav nav-list').find_all('li') # first step of categories parsing

csvDirectory = filedialog.askdirectory()

for blankCat in blankCategories:
    
    strCat = bs(str(blankCat), 'html.parser').find('a').get_text().replace("    ","").replace("\n","") # parsing 
    urlCat = "https://books.toscrape.com/" + bs(str(blankCat), 'html.parser').find('a').get('href')

    if strCat != "Books":

        category = Category(urlCat, strCat)
        category.writeCSV(csvDirectory)