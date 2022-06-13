'''lab3 task7'''

from location import Location
from random import randint


class Order:
    '''A class to represent the information about order.

    Attributes:
        orderId: int
            number of order
        user_name: str
            name of buyer
        location: Location
            info about location from Location class
        items: list(Item)
            list of information about goods
        vehicle: None

    >>> from location import Location
    >>> from item import Item
    >>> from random import randint
    >>> from order import Order
    >>> my_items = [Item('book',110), Item('chupachups',44)]
    >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    >>> my_order.location.city
    'Lviv'
    >>> for item in my_order.items:
    ...     print(item)
    You decided to buy book for 110 UAH.
    You decided to buy chupachups for 44 UAH.
    '''

    id_nums = []
    info = {}

    def __init__(self, user_name, city, postoffice, items):
        '''Inits Order with user_name, location (city, postoffice), items.'''
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.items = items
        self.location = Location(self.city, self.postoffice)
        self.vehicle = None
        while True:
            id_num = randint(1, 1000000000)
            if id_num in Order.id_nums:
                id_num = randint(1, 1000000000)
            else:
                Order.id_nums.append(id_num)
                break
        self.orderId = id_num
        Order.info[self.orderId] = [self.city, self.countPrice()]

    def calculateAmount(self):
        '''
        A method to calculate the total amount of all items in the order.
        Return int number.
        '''
        return len(self.items)

    def countPrice(self):
        '''
        Count the total price of the order.
        Return float.
        '''
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

    def assignVehicle(self, vehicle):
        '''
        Assign a vehicle for the order.
        '''
        self.vehicle = vehicle

    def __str__(self):
        '''Returns the number of order.'''
        return f'Your order number is {self.orderId}.'
