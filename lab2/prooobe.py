import json
from pprint import pprint
# path = '/Users/kvitoslava/2semestr/lab2/twitter1.json'
path = '/Users/kvitoslava/2semestr/lab2/twitter2.json'
with open(path, 'r') as file:
    data = json.load(file)


def json_flatten(info, return_data):
    if type(info) != list and type(info) != dict:
        return info
    elif type(info) == dict:
        print(list(info.keys()))
        user_input = input('Enter a key from list: ')
        if not user_input:
            exit()
        # if user_input == 'back':
        #     new = return_data[-2]
        #     return_data.pop(-1)
        #     return json_flatten(new, return_data)
        try:
            info1 = info[user_input]
            # return_data.append(info1)
        except KeyError:
            return json_flatten(info, return_data)
        return json_flatten(info1, return_data)

    elif type(info) == list:
        if len(info) == 1:
            user_input = 0
        else:
            user_input = input(f'enter a number from 0 to {len(info)-1}: ')
        if user_input == '':
            exit()
        # if user_input == 'back':
        #     new = return_data[-1]
        #     return_data.pop(-1)
        #     return json_flatten(info[new], return_data)
        try:
            info1 = info[int(user_input)]
            return_data.append(int(user_input))
        except IndexError:
            return json_flatten(info, return_data)
        return json_flatten(info1, return_data)

print(json_flatten(data, []))
