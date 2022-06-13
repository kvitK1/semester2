'''lab3 task4'''

import classroom # pylint: disable=unused-import


class AcademicBuilding:
    '''A class to represent an academic building with classrooms.

    Attributes:
        address: str
            the address of the building
        classrooms: list
            list of all classrooms in the building

    >>> import classroom
    >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
    >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
    >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
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
        self.address = address
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
