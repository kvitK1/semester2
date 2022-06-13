'''lab4 task4'''

from math import sqrt


class Point:
    '''A class to represent a point with two coordinates.

    Attributes:
        x: int
            x coordinate of point
        y: int
            y coordinate of point

    >>> point1 = Point(17, 2)
    >>> print(point1)
    Point in two-dimensional space with coordinates (17, 2)
    '''
    def __init__(self, x, y):
        '''Inits Point with x and y.'''
        self.x = x
        self.y = y

    def __str__(self):
        '''String to show the information about the point.'''
        return f'Point in two-dimensional space with coordinates ({self.x}, {self.y})'

    def vector_length(self):
        '''Method to find the length of vector.'''
        return round(sqrt(self.x**2+self.y**2), 2)

    def __repr__(self):
        '''Some info about Point.'''
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        '''Deals with equality of 2d points.'''
        return self.x == other.x and self.y == other.y


class Point3D(Point):
    '''A class to represent a point with three coordinates.

    Attributes:
        x: int
            x coordinate of point
        y: int
            y coordinate of point
        z: int
            z coordinate of point

    >>> point1 = Point(17, 2)
    >>> point2 = Point3D(17, 4, 2)
    >>> print(point2)
    Point in three-dimensional space with coordinates (17, 4, 2)
    >>> print(Point(3, 4).vector_length())
    5.0
    >>> print([point1, point2])
    [Point(x=17, y=2), Point(x=17, y=4, z=2)]

    '''
    def __init__(self, x, y, z=0):
        '''Inits Point3D with x, y and z.'''
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        '''String with information about the point.'''
        return  f'Point in three-dimensional space with coordinates ({self.x}, {self.y}, {self.z})'

    def vector_length(self):
        '''Method to find the length of vector.'''
        return round(sqrt(self.x**2+self.y**2+self.z**2), 2)

    def __eq__(self, other):
        '''Deals with equality of 3d point and 2d point.'''
        return self.x == other.x and self.y == other.y and self.z == 0

    def __repr__(self):
        '''Some info about Point.'''
        return f'Point(x={self.x}, y={self.y}, z={self.z})'
