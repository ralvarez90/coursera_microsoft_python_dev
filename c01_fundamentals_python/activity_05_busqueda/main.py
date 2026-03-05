import os
import pandas as pd


def get_title(book):
    return book['title']


def sort_catalog_by_title(catalog):
    catalog.sort(key=get_title)


# Bool file name
filename = 'book_catalog_10.csv'

if not os.path.exists(filename):
    raise FileNotFoundError(f'File "{filename}" dont exists.')

# Load the book catalog from the CSV
book_catalog_df = pd.read_csv(filename)

# Convert the DataFrame to a list to dictionaries
book_catalog = book_catalog_df.to_dict(orient='records')
print(book_catalog)
