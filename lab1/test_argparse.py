# import argparse
# parser = argparse.ArgumentParser(description="Creating a map")
# parser.add_argument('year', type=str, help='a year of the film production')
# parser.add_argument('latitude', type=float, help='a geographic coordinate that specifies the north–south position')
# parser.add_argument('longtitude', type=float, help='a geographic coordinate that specifies the east–west position')
# parser.add_argument('path_to_dataset', type=str, help='Path to the file with data')
# args = parser.parse_args()

# year = args.year
# latit = args.latitude
# longit = args.longtitude
# path_to_file = args.path_to_dataset
# import pandas as pd

# file_path = 'my_csv.csv'
# try:
#     df = pd.read_csv(file_path)
# except pd.errors.EmptyDataError:
#     quit(f'File with path: {file_path} is empty. Choose another one!')
# print('gwgw')


from pandas import DataFrame, read_csv, errors
from math import cos, asin, sqrt
from folium import Map, features, FeatureGroup, Marker, CircleMarker, Icon, LayerControl
from geopy.geocoders import Nominatim
from argparse import ArgumentParser


parser = ArgumentParser(description="Creating a map")
parser.add_argument('year', type=str, help='a year of the film production')
parser.add_argument('latitude', type=float, help='a geographic coordinate that specifies the north–south position')
parser.add_argument('longtitude', type=float, help='a geographic coordinate that specifies the east–west position')
parser.add_argument('path_to_dataset', type=str, help='Path to the file with data')
args = parser.parse_args()

input_year = args.year
input_latit = args.latitude
input_longit = args.longtitude
input_path_to_file = args.path_to_dataset


def read_file(path):
    with open(path, 'r') as file:
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


# def coordinates(films, year):
#     geolocator = Nominatim(user_agent="locationfind")
#     addresses_dictionary = {}
#     films_set = set(el[2] for el in films if year == el[1])
#     for address in list(films_set):
#         location = geolocator.geocode(address)
#         if location == None:
#             address1 = address.split(',')[1][1:] + ', '.join(address.split(',')[2:])
#             location1 = geolocator.geocode(address1)
#             if location1 == None:
#                 continue
#             else:
#                 if address1 not in addresses_dictionary:
#                     addresses_dictionary[address1] = [location1.latitude, location1.longitude]
#         else:
#             if address not in addresses_dictionary:
#                 addresses_dictionary[address] = [location.latitude, location.longitude]
#     return addresses_dictionary


# def write_csv(films, coords, year):
#     films_list = []
#     for film in films:
#         for key, value in coords.items():
#             if film[1] == year:
#                 under_film = []
#                 if key in film[2]:
#                     under_film.append(film[0])
#                     under_film.append(key)
#                     under_film.append(value[0])
#                     under_film.append(value[1])
#                     films_list.append(under_film)
#     my_df = DataFrame(films_list)
#     name = input('Please, name your file (with .csv extension) and wait a moment: ')
#     my_df.to_csv(name, index=False)
#     print('File is created..')
#     return name
# print(write_csv(read_file(input_path_to_file), coordinates(read_file(input_path_to_file), input_year), input_year))