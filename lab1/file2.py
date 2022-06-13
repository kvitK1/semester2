# import file1
import pandas as pd
from math import cos, asin, sqrt
import folium
from geopy.geocoders import Nominatim
file_path = 'my_csv.csv'
my_coords = [49.83826, 24.02324]
df = pd.read_csv(file_path)

def haversine_distance(my_cords, place_cords):
    dlat = my_cords[0] - place_cords[0]
    dlong = my_cords[1] - place_cords[1]
    p = 0.017453292519943295
    rad = 6371.0
    under_root = (1 - cos(dlat*p))/2 + cos(my_cords[0]*p)*cos(place_cords[0]*p)*(1-cos(dlong*p))/2
    asin_root = 2*rad*asin(sqrt(under_root))
    return asin_root


def opening(d_frame):
    csv_list = []
    for i in range(len(d_frame['2'])):
        dt_list = [d_frame['2'][i], d_frame['3'][i]]
        csv_list.append(dt_list)
    return csv_list
# print(opening(df))


def find_distances(cords, my_place):
    distance_dict = {}
    # distance = haversine_distance(my_place, cords[0])
    # distance_dict[distance] = cords[0]
    for i in range(len(cords)):
        distance = haversine_distance(my_place, cords[i])
        if distance not in distance_dict:
            distance_dict[distance] = cords[i]
    keys = sorted(list(distance_dict.keys()))[:10]
    new_dict = {}
    for key in keys:
        new_value = distance_dict[key]
        new_dict[key] = new_value
    return new_dict
# find_distances(opening(df), my_coords)


def data_converter(add_dict, data_fr):
    general = data_fr.values.tolist()
    new_gen = set()
    for under_gen in general:
        if [under_gen[2], under_gen[3]] in add_dict.values():
            inx = list(add_dict.values()).index([under_gen[2], under_gen[3]])
            key = list(add_dict.keys())[inx]
            under_gen.append(key)
            new_gen.add(tuple(under_gen))
    return new_gen
# data_converter(find_distances(opening(df), my_coords), df)


map_of_films = folium.Map(location = my_coords, zoom_start = 4)
addreses = list(data_converter(find_distances(opening(df), my_coords), df))
films = [addreses[i][0] for i in range(len(addreses))]
addresses = [addreses[i][1] for i in range(len(addreses))]
lat = [addreses[i][2] for i in range(len(addreses))]
long = [addreses[i][3] for i in range(len(addreses))]
distances = [addreses[i][4] for i in range(len(addreses))]

cat_icon = folium.features.CustomIcon('cat-clip-art-104.png', icon_size=(40, 40))

fg_1 = folium.FeatureGroup(name="Films_and_addresses")
fg_2 = folium.FeatureGroup("Distances")
for lt, lg, fl, ad in zip(lat, long, films, addresses):
    folium.Marker(location=[lt, lg], popup=f'<strong>{fl}</strong>\n{ad}', icon=folium.Icon()).add_to(fg_1)

for lt, lg, dis in zip(lat, long, distances):
    folium.CircleMarker(location=[lt, lg], radius=10, popup=f'<strong>Distance:</strong>\n{round(dis, 2)}km', fill_color='green', color='pink', fill_opacity=0.5).add_to(fg_2)

folium.Marker(location=my_coords, popup='<strong>This is you!</strong>', icon=cat_icon).add_to(map_of_films)

map_of_films.add_child(fg_1)
map_of_films.add_child(fg_2)
map_of_films.add_child(folium.LayerControl())
map_of_films.save('map_of_films.html')