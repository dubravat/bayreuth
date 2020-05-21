import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

"""
#df.to_csv('TEST.csv', sep=';', index=False, encoding='utf-8')

df = pd.read_csv('TEST.csv', sep=';', encoding='utf-8')

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

df.to_csv('TEST_geocoded.csv', sep=';', index=False, encoding='utf-8')
"""

df = pd.read_csv('TEST_geocoded.csv', sep=';', encoding='utf-8')

# visualization of data
df[df['Bev2018'] > 500000].plot(kind="scatter", x="lon", y="lat", s=df['Bev2018']/100000, color='DarkBlue', marker="o", alpha=0.6)
plt.title('Germany cities with population > 500.000')
plt.axis('off')
plt.show()

# df.to_csv('TEST22.csv', sep=';', index=False, encoding='utf-8')