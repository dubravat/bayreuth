"""
Wikipedia's Table into pandas's dataframe
Taras Dubrava
21.05.2020
"""

# imports
import requests
from bs4 import BeautifulSoup

# wikipedia article parameters
url = "https://en.wikipedia.org/wiki/List_of_deadly_earthquakes_since_1900"
url_content_text = requests.get(url).text

# initiating BeautifulSoup library
soup = BeautifulSoup(url_content_text, 'lxml')

# getting data
wikipedia_table = soup.find('table', class_="sortable wikitable")
table_rows = wikipedia_table.find_all('td')

data = []
for row in table_rows:
    try:
        data.append(row.text.strip().strip('\n'))
    except:
        data.append(row.text)

# extracting columns
list_columns = []
for th in soup.find_all('th'):
    if th.parent.name == 'tr':
        list_columns.append(th.text.strip())

it = [iter(data)] * len(list_columns)
data_new = list(zip(*it))

print(data_new)