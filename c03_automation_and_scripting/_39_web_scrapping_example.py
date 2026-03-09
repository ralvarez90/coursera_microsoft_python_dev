"""
EJEMPLO DE ANÁLISIS DE DATOS
"""
import requests
from bs4 import BeautifulSoup

# Target a sports web page
url = 'https://www.fangraphs.com/'

# Fetch the website content
soup: BeautifulSoup | None = None
try:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)
    exit(1)
else:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

# Get data information
menu_items = soup.find_all('div', class_='menu-item-label')
for item in menu_items:
    print(item.text.strip())

# End application
input('\nPress ENTER to quit . . . ')
