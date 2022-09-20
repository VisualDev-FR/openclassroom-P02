# Project description :

Data extraction with python from https://books.toscrape.com/

This app will download all book datas from the previously mentionned website.

For each book category, the app will create on directory (with the name of the category) containing :

* One .csv file with one line per book containing all his datas
* All book cover picture, named with the book name

# Configure the required virtual env :

First, clone the repository and open a terminal in the directory where you cloned.

* Then create your virtual env with the command : 
  
```python.exe -m venv env ```

1) install needed packages with the command : 
   
```.\env\Scripts\pip.exe install -r .\requirements.txt ```

# Launch the app :

Once you have configure your virtual env, launch the following command in your terminal :

```.\env\Scripts\python.exe .\src\main.py ```

Then a window will open, and asking you to select a directory where to download all the scrapped datas.