'''lab3 task3'''


class Classroom:
    '''A class to represent a classroom.

    Attributes:
        number: str
            number of the class
        capacity: int
            number of people the class can contain
        equipment: list
            list of equipment in the class

    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_016.number
    '016'
    >>> classroom_016.capacity
    80
    >>> len(classroom_016.equipment)
    3
    >>> print(classroom_016)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    >>> classroom_007 = Classroom('007', 12, ['TV'])
    >>> classroom_016.is_larger(classroom_007)
    True
    >>> len(classroom_016.equipment_differences(classroom_007))
    3
    >>> classroom_016
    Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> [classroom_016]
    [Classroom('016', 80, ['PC', 'projector', 'mic'])]
    '''
    def __init__(self, number, capacity, equipment):
        '''Inits Markets with number, capacity, equipment.'''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        '''Returns the attributes in one sentence."'''
        list_of_equipment = ', '.join(self.equipment)
        return f'Classroom {self.number} has a capacity of {self.capacity} ' +\
            f'persons and has the following equipment: {list_of_equipment}.'

    def is_larger(self, other):
        '''
        Method to check if capacity of first classroom is larger than second one.
        Returns True if larger, and False of not.
        '''
        if self.capacity > other.capacity:
            return True
        else:
            return False

    def equipment_differences(self, other):
        '''
        Method to compare the equipment of first and second classrooms.
        Returns list of equipment, which is in first, but not in second.
        '''
        first_class = set(self.equipment)
        second_class = set(other.equipment)
        return list(first_class.difference(second_class))

    def __repr__(self):
        '''Represents the class and its attributes.'''
        sent = ''
        for eq_p in self.equipment:
            eq_p = "'" + eq_p + "', "
            sent += eq_p
        sent = sent[:-2]
        return f"{self.__class__.__name__}('{self.number}', {self.capacity}, [{sent}])"
