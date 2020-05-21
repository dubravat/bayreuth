"""
Wikipedia's Table into pandas's dataframe and some visualization
Taras Dubrava
18.05.2020
"""

# imports
import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

# wikipedia article parameters
url = "https://de.wikipedia.org/wiki/Liste_der_Gro%C3%9Fst%C3%A4dte_in_Deutschland"
url_content_text = requests.get(url).text

# initiating BeautifulSoup library
soup = BeautifulSoup(url_content_text, 'lxml')

# getting data
wikipedia_table = soup.find('table', class_="wikitable sortable zebra mw-datatable")
table_rows = wikipedia_table.find_all('td')
data = []
for row in table_rows:
    data.append(row.text.strip())

# extracting columns
wikipedia_columns = soup.find('tr', class_="hintergrundfarbe6").text.strip()
list_columns_1 = [i.replace('\xad', '') for i in wikipedia_columns.split('\n') if i != '']

list_columns_2 = []
for th in soup.find_all('th'):
    if th.parent.name == 'tr' and th.text.strip()[:2] in ('19', '20'):
        list_columns_2.append(th.text.strip()[:4])
list_columns_2 = list(dict.fromkeys(list_columns_2))
list_columns_2 = ['Bev' + str(i) for i in list_columns_2]

columns = list_columns_1[:2] + list_columns_2 + list_columns_1[3:]

# creating a list with tuples acceptable by pandas's DataFrame
it = [iter(data)] * len(columns)
data_new = list(zip(*it))

# inserting data into DataFrame and some data cleaning
df = pd.DataFrame(data_new, columns = columns)
df['Bundesland'] = df['Bundesland'].apply(lambda x: ''.join(set(x.split(' '))))

df['Name'] = df['Name'].str.replace(r'[\u00AD\d,-]+', '').str.strip()

# geocoding addresses with Nominatim
geolocator = Nominatim(user_agent='my-application', timeout=1)

def geocoding(add):
    try:
        adds_geocoded = geolocator.geocode(add)
        location = list((adds_geocoded.latitude, adds_geocoded.longitude))
        return location
    except:
        return None

df['lat'] = df['Name'].apply(lambda x: geocoding(x)[0])
df['lon'] = df['Name'].apply(lambda x: geocoding(x)[1])

df['Bev2018'] = df['Bev2018'].str.replace('.', '').apply(pd.to_numeric)

# visualization of data
df[df['Bev2018'] > 500000].plot(kind="scatter", x="lon", y="lat", s=df['Bev2018']/100000, color='DarkBlue', marker="o", alpha=0.6)
plt.title('Germany cities with population > 500.000')
plt.axis('off')
plt.show()