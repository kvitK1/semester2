'''a module to navigate through json'''

import json


def main():
    '''
    Main function.
    '''
    path = input('Enter the path to your json-file: ')
    try:
        with open(path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        quit('No such file or directory! Try again..')
    print(json_flatten(data, [data]))


def json_flatten(info, return_data):
    '''
    The function to navigate through json-file.
    '''
    if type(info) != list and type(info) != dict:
        return info

        # print(info)
        # user_input = input('Want to return or end? ')
        # if user_input == 'return':
        #     return_data.pop(-1)
        #     info1 = return_data[-1]
        #     return json_flatten(info1, return_data)

    if len(info) == 1:
        return info
    elif type(info) == dict:
        print(list(info.keys()))
        user_input = input('Enter a key from list: ')
        if user_input == 'back':
            return_data.pop(-1)
            if len(return_data) != 0:
                info1 = return_data[-1]
                return json_flatten(info1, return_data)
            else:
                return_data = [info]
                return json_flatten(info, return_data)
        if not user_input:
            exit()
        try:
            info1 = info[user_input]
            return_data.append(info1)
        except KeyError:
            return json_flatten(info, return_data)
        return json_flatten(info1, return_data)

    elif type(info) == list:
        if len(info) == 1:
            user_input = 0
        else:
            print(info)
            user_input = input(f'enter a number from 0 to {len(info)-1}: ')
        if user_input == '':
            exit()
        if user_input == 'back':
            return_data.pop(-1)
            if len(return_data) != 0:
                info1 = return_data[-1]
                return json_flatten(info1, return_data)
            else:
                return_data = [info]
                return json_flatten(info, return_data)
        try:
            info1 = info[int(user_input)]
        except IndexError:
            return json_flatten(info, return_data)
        return json_flatten(info1, return_data)


if __name__ == '__main__':
    main()
