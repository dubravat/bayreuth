import geopandas as gpd

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
list = world.name.to_list()
for i in list:
    if i.startswith("Si"):
        print(i)
singapore = world[world.name == 'Singapore']
boundaries = singapore['geometry']