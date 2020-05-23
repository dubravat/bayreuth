"""
Wikipedia's Table into pandas's dataframe
Taras Dubrava
21.05.2020
"""

# imports
import requests
import pandas as pd
from bs4 import BeautifulSoup

# wikipedia article parameters
url = "https://en.wikipedia.org/wiki/List_of_deadly_earthquakes_since_1900"
url_content_text = requests.get(url).text

# initiating BeautifulSoup library
soup = BeautifulSoup(url_content_text, 'lxml')

# extracting columns
list_columns = []
for th in soup.find_all('th'):
    if th.parent.name == 'tr':
        list_columns.append(th.text.strip())

# getting data
table = soup.find('table', class_="sortable wikitable")
rows = table.find_all('tr')

data = []

for row in rows[1:]:
    elements = row.find_all("td")
    for i in range(len(list_columns)):
        try:
            data.append(elements[i].get_text().strip())
        except:
            data.append('')

# creating a list with tuples acceptable by pandas's DataFrame
it = [iter(data)] * len(list_columns)
data_new = list(zip(*it))

# inserting data into DataFrame
df = pd.DataFrame(data_new, columns = list_columns)
df.index = df.index.rename('id')

# exporting data into csv-file
df.to_csv('earthquakes_since_1900.csv', sep=';', index=True, encoding='utf-8')