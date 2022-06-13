'''lab3 task7'''


class Vehicle:
    '''A class to represent vehicles for delivery.

    Attributes:
        vehicleNo: int
            number of vehicle
        isAvailable: bool
            whether vehicle is available or not

    >>> from vehicle import Vehicle
    >>> auto = Vehicle(2)
    >>> auto.vehicleNo
    2
    '''

    def __init__(self, vehicleNo):
        '''Inits Vehicle with vehicleNo, isAvailable.'''
        self.vehicleNo = vehicleNo
        self.isAvailable = True

    def able_order(self):
        '''Makes vehicle not able for delivery.'''
        self.isAvailable = False
