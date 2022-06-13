''' a module for building a map'''
from argparse import ArgumentParser
from math import cos, asin, sqrt
from pandas import DataFrame, read_csv, errors

from folium import Map, features, FeatureGroup, Marker, CircleMarker, Icon, LayerControl
from geopy.geocoders import Nominatim



parser = ArgumentParser(description="Creating a map")
parser.add_argument('year', type=str, help='a year of the film production')
parser.add_argument('latitude', type=float, help='a geographic coordinate that\
specifies the north–south position')
parser.add_argument('longtitude', type=float, help='a geographic coordinate that\
specifies the east–west position')
parser.add_argument('path_to_dataset', type=str, help='Path to the file with data')
args = parser.parse_args()

input_year = args.year
input_latit = args.latitude
input_longit = args.longtitude
input_path_to_file = args.path_to_dataset
my_coords = [input_latit, input_longit]

def read_file(path):
    '''
    A function to read a dataset.
    Return list of lists with: film name, year, address.
    >>> print(len(read_file(input_path_to_file)[0]))
    3
    '''
    with open(path, 'r', encoding='utf8') as file:
        file_list = file.readlines()
    films_list = []
    for line in file_list:
        if not line.startswith('"'):
            continue
        else:
            films_list.append(line.rstrip().split("\t"))
    new_films = []
    for line in films_list:
        filter_object = filter(lambda x: x != "" and not x.startswith('('), line)
        lin = list(filter_object)
        new_films.append(lin)
    for line in new_films:
        inx  = line[0].find("(")
        film = line[0][:inx-1]
        year = line[0][inx+1:inx+5]
        del line[0]
        line.insert(0, film)
        line.insert(1, year)
    return new_films


def coordinates(l_films, year):
    '''
    A function to find coordinates with geopy.geocoder module.
    Return a dictionary with addresses as keys and
    lists with latitudes and longtitudes as values.
    >>> print(type(coordinates(read_file(input_path_to_file), input_year)))
    <class 'dict'>
    '''
    geolocator = Nominatim(user_agent="locationfind")
    addresses_dictionary = {}
    films_set = set(el[2] for el in l_films if year == el[1])
    for address in list(films_set):
        location = geolocator.geocode(address)
        if location is None:
            temp = address.split(',')
            if len(temp) == 1:
                continue
            address1 = temp[1][1:] + ', '.join(temp[2:])
            location1 = geolocator.geocode(address1)
            if location1 is None:
                continue
            else:
                if address1 not in addresses_dictionary:
                    addresses_dictionary[address1] = [location1.latitude, location1.longitude]
        else:
            if address not in addresses_dictionary:
                addresses_dictionary[address] = [location.latitude, location.longitude]
    return addresses_dictionary


def write_csv(l_films, coords, year):
    '''
    A function to write list of lists as a csv file.
    Return the name of the file.
    >>> print(write_csv(read_file(input_path_to_file), coordinates(read_file(input_path_to_file), input_year), input_year))
    csv_for_map.csv
    '''
    films_list = []
    for film in l_films:
        for key, value in coords.items():
            if film[1] == year:
                under_film = []
                if key in film[2]:
                    under_film.append(film[0])
                    under_film.append(key)
                    under_film.append(value[0])
                    under_film.append(value[1])
                    films_list.append(under_film)
    my_df = DataFrame(films_list)
    name = 'csv_for_map.csv'
    my_df.to_csv(name, index=False)
    return name


try:
    df = read_csv(write_csv(read_file(input_path_to_file),\
    coordinates(read_file(input_path_to_file), input_year), input_year))
except errors.EmptyDataError:
    quit('File with such path is empty. Choose another one!')
except FileNotFoundError:
    quit('There is no file or directory with such path. Try again!')


def haversine_distance(my_cords, place_cords):
    '''
    A function to find distances between two points on the Earth with the haversine formula.
    Return a distance as a float number.
    >>> print(haversine_distance([53.483959, -2.244644], [40.730610, -73.935242]))
    5363.581249324559
    '''
    dlat = my_cords[0] - place_cords[0]
    dlong = my_cords[1] - place_cords[1]
    p_rad = 0.017453292519943295
    rad = 6371.0
    under_root = (1 - cos(dlat*p_rad))/2 +\
    cos(my_cords[0]*p_rad)*cos(place_cords[0]*p_rad)*(1-cos(dlong*p_rad))/2
    asin_root = 2*rad*asin(sqrt(under_root))
    return asin_root


def dataframe_opening(d_frame):
    '''
    A function to form a list of lists with latitudes and longtitudes.
    Return a list of lists.
    >>> print(type(dataframe_opening(df)))
    <class 'list'>
    '''
    csv_list = []
    for i in range(len(d_frame['2'])):
        dt_list = [d_frame['2'][i], d_frame['3'][i]]
        csv_list.append(dt_list)
    return csv_list


def find_distances(cords, my_place):
    '''
    A function to find distances between
    input coordinates and addresses coordinates.
    Return a dictionary with distances as keys and lists of coordinates as values.
    >>> print(len(find_distances(dataframe_opening(df), my_coords)))
    10
    '''
    distance_dict = {}
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


def data_converter(add_dict, data_fr):
    '''
    A function to gather all the needed information.
    Return a set of tuples with the data.
    >>> print(len(data_converter(find_distances(dataframe_opening(df), my_coords), df)))
    10
    '''
    general = data_fr.values.tolist()
    new_gen = set()
    for under_gen in general:
        if [under_gen[2], under_gen[3]] in add_dict.values():
            inx = list(add_dict.values()).index([under_gen[2], under_gen[3]])
            key = list(add_dict.keys())[inx]
            under_gen.append(key)
            new_gen.add(tuple(under_gen))
    return new_gen


map_of_films = Map(location = my_coords, zoom_start = 4)
addreses = list(data_converter(find_distances(dataframe_opening(df), my_coords), df))
films = [addreses[i][0] for i in range(len(addreses))]
addresses = [addreses[i][1] for i in range(len(addreses))]
lat = [addreses[i][2] for i in range(len(addreses))]
long = [addreses[i][3] for i in range(len(addreses))]
distances = [addreses[i][4] for i in range(len(addreses))]

cat_icon = features.CustomIcon('/Users/kvitoslava/2semestr/lab1/lab1_2/cat-clip-art-104.png', icon_size=(40, 40))

fg_1 = FeatureGroup(name="Films_and_addresses")
fg_2 = FeatureGroup("Distances")
for lt, lg, fl, ad in zip(lat, long, films, addresses):
    Marker(location=[lt, lg], popup=f'<strong>{fl}</strong>\n{ad}', icon=Icon()).add_to(fg_1)

for lt, lg, dis in zip(lat, long, distances):
    CircleMarker(location=[lt, lg], radius=10,
    popup=f'<strong>Distance:</strong>\n{round(dis, 2)}km',
    fill_color='green', color='pink', fill_opacity=0.5).add_to(fg_2)

Marker(location=my_coords, popup='<strong>This is you!</strong>',
icon=cat_icon).add_to(map_of_films)

map_of_films.add_child(fg_1)
map_of_films.add_child(fg_2)
map_of_films.add_child(LayerControl())
map_name = 'map_of_films_product.html'
map_of_films.save(map_name)
print('Your map is created!')
