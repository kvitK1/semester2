'''lab4 task2'''


class Animal:
    '''A class to represent an animal.
    
    Attributes:
        phylum: str
            type of animal
        clas: str
            class of animal

    >>> animal1 = Animal("chordata", "mammalia")
    >>> animal1.phylum
    'chordata'
    >>> print(animal1)
    <animal class is mammalia>

    '''
    def __init__(self, phylum, clas):
        '''Inits Animal with phylum, clas.'''
        self.phylum = phylum
        self.clas = clas

    def __str__(self):
        '''Return a string with information about animal class.'''
        return f'<animal class is {self.clas}>'
    
    def __eq__(self, other):
        '''Method to deal with identical objects.'''
        return self.phylum == other.phylum and self.clas == other.clas


class Cat(Animal):
    '''A class to represent a cat.
    
    Attributes:
        phylum: str
            type of animal
        clas: str
            class of animal
        genus: str
            kind of animal

    >>> cat1 = Cat("chordata", "mammalia", "felis")
    >>> cat1.sound()
    'Meow'
    >>> print(cat1)
    <This felis animal class is mammalia>

    '''
    def __init__(self, phylum, clas, genus):
        '''Inits Cat with phylum, clas, genus.'''
        super().__init__(phylum, clas)
        self.genus = genus
    
    def sound(self):
        '''Function to return "meow", like cat.'''
        return 'Meow'

    def __str__(self):
        '''String with info about cat.'''
        return f'<This {self.genus} animal class is {self.clas}>'

# import doctest
# print(doctest.testmod())
