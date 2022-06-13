"lab1.task1"
from re import findall

# address = input()
address = '91.124.230.205/30'

def validate_ip_address(ip_check: str):
    '''Return a message of error if the ip-address is not correct.
    >>> print(validate_ip_address('172.20g.0.0/14'))
    Error
    >>> print(validate_ip_address('91.124.230.205/30'))
    None
    '''
    if ip_check.count('.') != 3:
        return "Error"
    elif '/' in ip_check:
        inx = ip_check.find('/')
        ip_address = ip_check[:inx]
        if ip_address.count('.') == 3:
            ip_list = ip_address.split('.')
            for elem in ip_list:
                if not elem.isdigit() is True:
                    return "Error"
                elif int(elem) not in range(256):
                    return "Error"
        else:
            return "Error"
        if ip_check[-1] != '/':
            mask = ip_check[inx+1:]
            if not mask.isdigit() is True:
                return "Error"
            elif int(mask) not in range(33):
                return "Error"
        else:
            return "Missing prefix"
    else:
        return "Missing prefix"
print(validate_ip_address(address))


def if_true_func(var):
    '''
    Return True if ip is correct and False if not.
    >>> print(if_true_func(validate_ip_address('172.20g.0.0/14')))
    False
    >>> print(if_true_func(validate_ip_address('91.124.230.205/30')))
    True
    '''
    check = True
    if type(var) == str:
        check = False
    return check


def get_ip_from_raw_address(raw_address: str) -> str:
    '''
    Return an ip-address from the initial raw address.
    >>> print(get_ip_from_raw_address('91.124.230.205/30'))
    91.124.230.205
    >>> print(get_ip_from_raw_address('text'))
    None
    '''
    if if_true_func(validate_ip_address(raw_address)):
        slash_ind = raw_address.find("/")
        ip_add = raw_address[:slash_ind]
        return ip_add
print(get_ip_from_raw_address(address))


def ip_into_binary(ip_a: str) -> str:
    '''
    Return a binary form of ip-address.
    >>> print(ip_into_binary('91.124.230.205/30'))
    10110110.11111000.11100110.11001101
    >>> print(ip_into_binary('215.17.125.177'))
    None
    '''
    if if_true_func(validate_ip_address(ip_a)):
        ip_a = get_ip_from_raw_address(address)
        ip_a = [int(elem) for elem in ip_a.split(".")]
        ip_list = []
        for element in ip_a:
            bin_num = bin(element).replace('0b', '')
            while len(bin_num) != 8:
                bin_num += '0'
            ip_list.append(bin_num)
        ip_num = ".".join(ip_list)
        return ip_num
print(ip_into_binary(address))


def get_network_address_from_raw_address(raw_address: str) -> str:
    '''
    Return a network address from raw address.
    >>> print(get_network_address_from_raw_address('67.38.173.245/20'))
    67.38.160.0
    >>> print(get_network_address_from_raw_address('91.124.230.205/30'))
    91.124.230.204
    '''
    if if_true_func(validate_ip_address(raw_address)):
        slash_ind = raw_address.find("/")
        ip_list = [int(elem) for elem in raw_address[:slash_ind].split(".")]
        mask_num = int(raw_address[slash_ind+1:])
        mask_bin = findall('.'*8, "1"*mask_num + "0"*(32-mask_num))
        mask_lst = [int(elem, 2) for elem in mask_bin]
        address_lst = []
        for i in range(len(mask_lst)):
            number = ip_list[i]&mask_lst[i]
            address_lst.append(str(number))
        web_address = ".".join(address_lst)
        return web_address
print(get_network_address_from_raw_address(address))


def get_binary_mask_from_raw_address(raw_address: str) -> str:
    '''
    Return a mask in a binary form.
    >>> print(get_binary_mask_from_raw_address('67.38.173.245/20'))
    11111111.11111111.11110000.00000000
    >>> print(get_binary_mask_from_raw_address('Text'))
    None
    '''
    if if_true_func(validate_ip_address(raw_address)):
        slash_ind = raw_address.find("/")
        mask_num = int(raw_address[slash_ind+1:])
        mask_bin = findall('.'*8, "1"*mask_num + "0"*(32-mask_num))
        mask = '.'.join(mask_bin)
        return mask
print(get_binary_mask_from_raw_address(address))


def get_broadcast_address_from_raw_address(raw_address: str) -> str:
    '''
    Return a brodcast address from a raw address.
    >>> print(get_broadcast_address_from_raw_address('215.017.125.177/28'))
    215.17.125.191
    >>> print(get_broadcast_address_from_raw_address('91.124.230.205/30'))
    91.124.230.207
    '''
    if if_true_func(validate_ip_address(raw_address)):
        slash_ind = raw_address.find("/")
        ip_list = [int(elem) for elem in raw_address[:slash_ind].split(".")]
        mask_num = int(raw_address[slash_ind+1:])
        mask_bin = findall('.'*8, "0"*mask_num + "1"*(32-mask_num))
        mask_lst = [int(elem, 2) for elem in mask_bin]
        broadcast_list = []
        for i in range(len(mask_lst)):
            number = ip_list[i]|mask_lst[i]
            broadcast_list.append(str(number))
        broadcast_address = '.'.join(broadcast_list)
        return broadcast_address
print(get_broadcast_address_from_raw_address(address))


def get_first_usable_ip_address_from_raw_address(raw_address: str) -> str:
    '''
    Return a first usable ip-address from raw address.
    >>> print(get_first_usable_ip_address_from_raw_address('215.017.17'))
    None
    >>> print(get_first_usable_ip_address_from_raw_address('error'))
    None
    '''
    if if_true_func(validate_ip_address(raw_address)):
        network_address = get_network_address_from_raw_address(raw_address)
        address_list = [int(elem) for elem in network_address.split('.')]
        address_list[-1] += 1
        first_address = '.'.join([str(elem) for elem in address_list])
        return first_address
print(get_first_usable_ip_address_from_raw_address(address))


def get_penultimate_usable_ip_address_from_raw_address(raw_address: str) -> str:
    '''
    Return a penultimate usable ip-address from raw address.
    >>> print(get_penultimate_usable_ip_address_from_raw_address('215.017.125.177/28'))
    215.17.125.190
    >>> print(get_penultimate_usable_ip_address_from_raw_address('error'))
    None
    '''
    if if_true_func(validate_ip_address(raw_address)):
        broad_address = get_broadcast_address_from_raw_address(raw_address)
        address_list = [int(elem) for elem in broad_address.split('.')]
        address_list[-1] -= 1
        last_address = '.'.join([str(elem) for elem in address_list])
        return last_address
print(get_penultimate_usable_ip_address_from_raw_address(address))


def get_number_of_usable_hosts_from_raw_address(raw_address: str) -> int:
    '''
    Return a number of usable hosts from raw address.
    >>> print(get_number_of_usable_hosts_from_raw_address('172.20.0.0/14'))
    262142
    >>> print(get_number_of_usable_hosts_from_raw_address('172.20.0.0/'))
    None
    '''
    if if_true_func(validate_ip_address(raw_address)):
        slash_ind = raw_address.find("/")
        mask = 32 - int(raw_address[slash_ind+1:])
        hosts = 2**mask - 2
        return hosts
print(get_number_of_usable_hosts_from_raw_address(address))


def get_ip_class_from_raw_address(raw_address: str) -> str:
    '''
    Return a number of ip-class of the raw address.
    >>> print(get_ip_class_from_raw_address('215.017.125.177/28'))
    C
    >>> print(get_ip_class_from_raw_address('91.124.230.205/30'))
    A
    '''
    if if_true_func(validate_ip_address(raw_address)):
        ip_list = [int(e) for e in \
        get_ip_from_raw_address(raw_address).split('.')]
        clas = {'A': [1, 126], 'B': [128, 191], 'C': [192, 223],
        'D': [224, 239], 'E': [240, 247]}
        classes_list = list(clas.values())
        clas_key = list(clas.keys())
        for i in range(len(classes_list)):
            if ip_list[0] in range(classes_list[i][0], classes_list[i][1]+1):
                return clas_key[i]
print(get_ip_class_from_raw_address(address))


def check_private_ip_address_from_raw_address(raw_address: str) -> bool:
    '''
    Return True if ip is private and False if not.
    >>> print(check_private_ip_address_from_raw_address('91.124.230.205/30'))
    False
    >>> print(check_private_ip_address_from_raw_address('192.168.0.0/16'))
    True
    '''
    if if_true_func(validate_ip_address(raw_address)):
        ip_list = [int(elem) for elem in \
        get_ip_from_raw_address(raw_address).split('.')]
        if ip_list[0] == 10:
            return True
        elif ip_list[0] == 172 and ip_list[1] in range(16, 32):
            return True
        elif ip_list[0] == 192 and ip_list[1] == 168:
            return True
        else:
            return False
print(check_private_ip_address_from_raw_address(address))

import doctest
print(doctest.testmod())
