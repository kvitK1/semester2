'''lab4 task3'''


class Furniture:
    '''A class to represent furniture.
    
    Attributes:
        style: str
            style of furniture
        assign: str
            where is the place for furniture

    >>> furniture1 = Furniture("empire", "bedroom")
    >>> furniture1.style
    'empire'
    >>> print(furniture1)
    <furniture style is empire>

    '''
    def __init__(self, style, assign):
        '''Inits Furniture with style, assign.'''
        self.style = style
        self.assign = assign

    def __str__(self):
        '''String with information about furniture.'''
        return f'<furniture style is {self.style}>'

    def __eq__(self, other):
        '''Method to deal with identical objects.'''
        return self.style == other.style and self.assign == other.assign


class Chair(Furniture):
    '''A class to represent a chair.
    
    Attributes:
        style: str
            style of furniture
        assign: str
            where is the place for furniture
        tipe: str
            type of animal

    >>> chair1 = Chair("empire", "bedroom", "armchair")
    >>> chair1.tipe
    'armchair'
    >>> print(chair1)
    <This armchair furniture style is empire>

    '''
    def __init__(self, style, assign, tipe):
        '''Inits Chair with style, assign, tipe.'''
        super().__init__(style, assign)
        self.tipe = tipe
    
    def __str__(self):
        '''String with info about chair.'''
        return f'<This {self.tipe} furniture style is {self.style}>'
    
    def get_assign(self):
        '''Return the assign of chair.'''
        return self.assign
