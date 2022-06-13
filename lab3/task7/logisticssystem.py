'''lab3 task7'''

from order import Order
from vehicle import Vehicle
from item import Item

class LogisticsSystem:
    '''A class to represent the system of the delivery.

    Attributes:
        orders: list
            list of orders
        vehicles: list
            list of vehicles

    >>> from order import Order
    >>> from vehicle import Vehicle
    >>> from item import Item
    >>> from logisticssystem import LogisticsSystem
    >>> vehicles = [Vehicle(1), Vehicle(2)]
    >>> logSystem = LogisticsSystem(vehicles)
    >>> my_items = [Item('book',110), Item('chupachups',44)]
    >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    >>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    >>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    >>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    >>> logSystem.placeOrder(my_order)
    >>> logSystem.placeOrder(my_order2)
    >>> logSystem.placeOrder(my_order3)
    There is no available vehicle to deliver an order.
    >>> logSystem.trackOrder(my_order3.orderId)
    No such order.
    >>> logSystem.trackOrder(-77643993)
    No such order.
    '''

    def __init__(self, vehicles):
        '''Inits LogisticSystem with orders, vehicles.'''
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        '''Confirms or refuses creating the order.'''
        self.orders.append(order)
        veh = self.assigning_vehicles()
        if veh is not None:
            order.assignVehicle(self.vehicles[veh])
        else:
            print('There is no available vehicle to deliver an order.')

    def assigning_vehicles(self):
        '''Assigns vehicles to orders.'''
        for vehicle in self.vehicles:
            if vehicle.isAvailable is True:
                inx = self.vehicles.index(vehicle)
                self.vehicles[inx].able_order()
                return inx
        return None

    def trackOrder(self, orderId):
        '''Tracks the order if it is approved or shows the message if not.'''
        bol = False
        for order in self.orders:
            if order.orderId == orderId and order.vehicle is not None:
                bol = True

        if bol:
            print(f'Your order #{orderId} is sent to {Order.info[orderId][0]}. \
Total price: {Order.info[orderId][1]} UAH.')
        else:
            print('No such order.')


