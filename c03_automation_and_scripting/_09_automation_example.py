"""
EJEMPLO DE AUTOMATIZACIÓN
"""
from pprint import pprint

import pandas as pd
import requests

from bs4 import BeautifulSoup


def extract_from_website(url: str) -> pd.DataFrame | None:
    try:
        # Make a request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Create soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find table element
        table = soup.find('table')
        pprint(table.string)

    except Exception as e:
        print(f'Error fetching url: {url}')
        print(e)
        return None


def gather_data_from_resources():
    pass


def process_anf_format_data():
    pass


def generate_report():
    pass


if __name__ == '__main__':
    extract_from_website('https://webscraper.io/test-sites/tables/tables-without-thead')
