'''lab3 task2'''


class Markets:
    '''A class to represent a market.

    Attributes:
        name: str
            name of the market
        area: int
            area of the market (in m2)
        categories: list
            list of categories in the market

    '''
    def __init__(self, name, area, categories):
        '''Inits Markets with name, area, categories.'''
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self):
        '''Returns the attributes in one sentence."'''
        list_of_categories = ', '.join(self.categories)
        return f'Supermarket {self.name} has an area of {self.area}' +\
            f'm2 and has the following categories: {list_of_categories}.'

market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
