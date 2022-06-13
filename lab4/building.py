'''lab4 task1'''


class Building:
    '''A class to represent a building.
    
    Attributes:
        address: str
            address of the building
    
    >>> building1 = Building('Kozelnytska 2a')
    >>> building1.address
    'Kozelnytska 2a'

    '''
    def __init__(self, address):
        '''Inits Building with address.'''
        self.address = address


class House(Building):
    '''A class to represent a house.
    
    Attributes:
        address: str
            address of the building
        apartments: list
            list of all apartments in the house

    >>> house1 = House('Kozelnytska 2a', ['floor1', 'floor2', 'floor3'])
    >>> house1.address
    'Kozelnytska 2a'
    >>> house1.apartments
    ['floor1', 'floor2', 'floor3']

    '''
    def __init__(self, address, apartments):
        '''Inits House with address, apartments.'''
        super().__init__(address)
        self.apartments = apartments


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


class AcademicBuilding(Building):
    '''A class to represent an academic building with classrooms.

    Attributes:
        address: str
            the address of the building
        classrooms: list
            list of all classrooms in the building

    >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = Classroom('007', 12, ['TV'])
    >>> classroom_008 = Classroom('008', 25, ['PC', 'projector'])
    >>> classrooms = [classroom_016, classroom_007, classroom_008]
    >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
    >>> building.address
    'Kozelnytska st. 2a'
    >>> for room in building.classrooms:
    ...     print(room)
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
    Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
    >>> len(building.total_equipment())
    4
    >>> print(building)
    Kozelnytska st. 2a
    Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
    Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
    Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
    '''
    def __init__(self, address, classrooms):
        '''Inits AcademicBuilding with address, list of classrooms.'''
        super(AcademicBuilding, self).__init__(address)
        self.classrooms = classrooms

    def total_equipment(self):
        '''
        Method to show all kinds of equipmnet and number of their number.
        Returns list with tuples.
        '''
        list_of_equip = []
        equip = self.classrooms
        for eqp in equip:
            eqp = eqp.equipment
            for item in eqp:
                list_of_equip.append(item)
        set_equip = set()
        for eqp in list_of_equip:
            counter = list_of_equip.count(eqp)
            set_equip.add((eqp, counter))
        return list(set_equip)

    def __str__(self):
        '''Returns the information about the academic building,
           using the info about each classroom.'''
        sentence = f'{self.address}\n'
        for room in self.classrooms[:-1]:
            sentence += room.__str__() + '\n'
        sentence += self.classrooms[-1].__str__()
        return sentence
