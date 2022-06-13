'''lab3 task7'''


class Item:
    '''A class to represent the good, which the delivery has to deliver.

    Attributes:
        name: str
            name of the good
        price: float
            price of the good

    >>> from item import Item
    >>> item1 = Item('book',110)
    >>> print(item1)
    You decided to buy book for 110 UAH.
    '''

    def __init__(self, name, price):
        '''Inits Item with name, price.'''
        self.name = name
        self.price = price
    
    def __str__(self):
        '''Returns string with information about item of good.'''
        return f'You decided to buy {self.name} for {self.price} UAH.'
