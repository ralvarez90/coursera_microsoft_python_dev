import pandas as pd
import requests

from bs4 import BeautifulSoup

# Create soup with content
url: str = 'http://localhost:5500/baseball_stats.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get headers
headers_table = soup.find_all('th')
headers_table = [h.text for h in headers_table]

# Create dataframe
data_rows = []
table_body_rows = soup.select('tbody tr')
for row in table_body_rows:
    data_rows.append([item.text for item in row.find_all('td')])

# Create dataframe
df = pd.DataFrame(
    data=data_rows,
    columns=headers_table
)

# Save data in csv file
df.to_csv('sports_statistics.csv', index=False)
