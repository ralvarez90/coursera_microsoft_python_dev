"""
EJEMPLO DE AUTOMATIZACIÓN
"""
from pprint import pprint

import pandas as pd
import requests

from bs4 import BeautifulSoup


def extractFromWebsite(url: str) -> pd.DataFrame | None:
    try:
        # Make a request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Create soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find table element
        table = soup.find('table')
        if table:
            pprint(table.string)
        else:
            print('Data not found!')

    except Exception as e:
        print(f'Error fetching url: {url}')
        print(e)


def gatherDataFromResources():
    pass


def processAndFormatData():
    pass


def generateReport():
    pass


if __name__ == '__main__':
    extractFromWebsite('https://webscraper.io/test-sites/tables/tables-without-thead')
