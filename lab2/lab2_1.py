import json
with open('twitter1.json', 'r') as file:
    # file_r = file.read()
    data = json.load(file)
print(list(data.keys()))
while True:
    input_key = input("Enter a key: ")
    if not input_key:
        break
    if type(data) == list:
        input_key = int(input_key)
    data = data[input_key]
    if type(data) == list:
        print(f'Number of elements in list: {len(data)}')
    elif type(data) == dict:
        print(f'Dict keys are:\n{list(data.keys())}')
    else:
        print(f'Value is:\n{data}')
        break

