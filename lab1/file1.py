from pandas import DataFrame


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
# print(read_file('/Users/kvitoslava/2semestr/lab1/short_location.list'))


def coordinates(films, year):
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="locationfind")
    addresses_dictionary = {}
    films_set = set(el[2] for el in films if year == el[1])
    for address in list(films_set):
        location = geolocator.geocode(address)
        if location == None:
            address1 = address.split(',')[1][1:] + ', '.join(address.split(',')[2:])
            location1 = geolocator.geocode(address1)
            if location1 == None:
                continue
            else:
                if address1 not in addresses_dictionary:
                    addresses_dictionary[address1] = [location1.latitude, location1.longitude]
        else:
            if address not in addresses_dictionary:
                addresses_dictionary[address] = [location.latitude, location.longitude]
    return addresses_dictionary
    # for key, value in addresses_dictionary.items():
    #     print(key, value)
# print(coordinates(read_file('/Users/kvitoslava/2semestr/lab1/short_location.list'), '2011'))

def write_csv(films, coords, year):
    films_list = []
    for film in films:
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
    my_df.to_csv('my_csv.csv', index=False)
    print('well done')
write_csv(read_file('short_location.list'), coordinates(read_file('short_location.list'), '2340'), '2340')