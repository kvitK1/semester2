'''Lab2_task1'''

import json


def opening(path):
    '''
    A function to open a json file.
    Return a dictionary.
    >>> print(type(opening('kved.json')))
    <class 'dict'>
    '''
    with open(path) as file:
        json_data = json.load(file)
    return json_data


def parse_kved(class_code):
    '''
    A function to parse the json data and return new json.
    Return a dictionary.
    >>> print(len(parse_kved(classcode)))
    3
    '''
    data = opening('/Users/kvitoslava/2semestr/lab2/kved.json')
    gen_dict = {}
    dict1 = {}
    dict2 = {}
    dict3 = {}
    data_list = data.get('sections')[0]
    for h in range(len(data_list)):
        div_list = data_list[h].get('divisions')

        for i in range(len(div_list)):
            if div_list[i]['divisionCode'] == class_code[:2]:
                group_data = div_list[i]['groups']
                dict3 = {'name': data_list[h]['sectionName'], 'type': 'section',
                'num_children': len(data_list[h]['divisions'])}
                dict2 = {'name': div_list[i]['divisionName'], 'type': 'division',
                'num_children': len(div_list[i]['groups']), 'parent': dict3}

                for j in range(len(group_data)):
                    if group_data[j]['groupCode'] == class_code[:4]:
                        dict1 = {'name': group_data[j]['groupName'], 'type': 'group',
                        'num_children': len(group_data[j]['classes']), 'parent': dict2}
                        class_data = group_data[j]['classes']

                        for k in range(len(class_data)):
                            if class_data[k]['classCode'] == class_code:
                                gen_dict = {'name': class_data[k]['className'], 'type': 'class',
                                'parent': dict1}

    with open('kved_results.json', 'w') as file:
        json.dump(gen_dict, file, indent=2, ensure_ascii=False)
    return gen_dict
print(parse_kved('01.11'))