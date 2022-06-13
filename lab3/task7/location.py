'''lab3 task7'''


class Location:
    '''A class to represent the location, where the delivery has to deliver.

    Attributes:
        city: str
            name of the good
        postoffice: int
            price of the good

    >>> from location import Location
    >>> user1 = Location('Kolomyia', 3)
    >>> user1.city
    'Kolomyia'
    '''

    def __init__(self, city, postoffice):
        '''Inits Location with city, postoffice.'''
        self.city = city
        self.postoffice = postoffice
