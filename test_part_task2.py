import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

df = pd.read_csv('TEST_geocoded.csv', sep=';', encoding='utf-8')

# visualization of data
df[df['Bev2018'] > 500000].plot(kind="scatter", x="lon", y="lat", s=df['Bev2018']/100000, color='DarkBlue', marker="o", alpha=0.6)
plt.title('Germany cities with population > 500.000')
plt.axis('off')
plt.show()

# df.to_csv('TEST22.csv', sep=';', index=False, encoding='utf-8')