import os
import pandas as pd


def getTitle(book):
    return book['title']


def sortCatalogByTitle(catalog):
    catalog.sort(key=getTitle)


# Bool file name
filename = 'book_catalog_10.csv'

if not os.path.exists(filename):
    raise FileNotFoundError(f'File "{filename}" dont exists.')

# Load the book catalog from the CSV
bookCatalogDf = pd.read_csv(filename)

# Convert the DataFrame to a list to dictionaries
book_catalog = bookCatalogDf.to_dict(orient='records')
print(book_catalog)
