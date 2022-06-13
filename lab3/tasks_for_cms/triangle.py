'''lab3 task5'''

from math import sqrt
import point # pylint: disable=unused-import


class Triangle:
    '''A class to represent a triangle by its apexes.

    Attributes:
        address: str
            the address of the building
        classrooms: list
            list of all classrooms in the building

    >>> import point
    >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
    >>> triangle.is_triangle()
    True
    >>> triangle.perimeter()
    6.47213595499958
    >>> triangle.area()
    2.0
    '''
    def __init__(self, point1, point2, point3):
        '''Inits triangle with three points.'''
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    @staticmethod
    def vector(p_1, p_2):
        '''
        Method to count the side of triangle using the coordinates of its points.
        Returns float number.
        '''
        side = sqrt(((p_1[0]-p_2[0])**2)+((p_1[1]-p_2[1])**2))
        return side

    def sides(self):
        '''
        Method to gather all sides of triangle.
        Return three float numbers.
        '''
        side1 = self.vector((self.point1.x_cord, self.point1.y_cord),
            (self.point2.x_cord, self.point2.y_cord))
        side2 = self.vector((self.point3.x_cord, self.point3.y_cord),
            (self.point2.x_cord, self.point2.y_cord))
        side3 = self.vector((self.point1.x_cord, self.point1.y_cord),
            (self.point3.x_cord, self.point3.y_cord))
        return side1, side2, side3


    @staticmethod
    def checker(side1, side2, side3):
        '''
        Method to check if sum of two sides is bigger than third one.
        Returns True if bigger, and False if not
        '''
        if side1+side2>side3:
            return True
        else:
            return False

    def is_triangle(self):
        '''
        Method to check if the triangle with such points exists.
        Uses vector to count the sides and checker to check the sum of two ones.
        Returns True if triangle exists, and False if not.
        '''
        side1, side2, side3 = self.sides()
        boolean_list = []
        boolean_list.append(self.checker(side1, side2, side3))
        boolean_list.append(self.checker(side2, side3, side1))
        boolean_list.append(self.checker(side3, side1, side2))
        if False in boolean_list:
            return False
        else:
            return True

    def perimeter(self):
        '''
        Method to count the perimeter of triangle.
        Returns float number.
        '''
        side1, side2, side3 = self.sides()
        return side1+side2+side3

    def area(self):
        '''
        Method to count area of triangle by 3 sides.
        Returns float number.
        '''
        side1, side2, side3 = self.sides()
        per_tr = self.perimeter()/2
        area_formula = sqrt(per_tr*(per_tr-side1)*(per_tr-side2)*(per_tr-side3))
        return area_formula
