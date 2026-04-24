"""
EXTRACCIÓN DE DATOS DE UN SITIO WEB


"""
import requests
from bs4 import BeautifulSoup

# Web target
url: str = 'https://www.youtube.com/'

# Fetch the web page content
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
else:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Search headings
    headings: list = soup.find_all('h1')
    if headings:
        print('Headings:')
        for heading in headings:
            print(f'- {heading.text.strip()}')

    # Search links
    links: list = soup.find_all('a')
    if links:
        print('Links:')
        for link in links:
            href = link.get('href')
            if href is not None:
                print(f'- {href.strip()}')

# End message
input('\nPress any key to continue . . . ')
