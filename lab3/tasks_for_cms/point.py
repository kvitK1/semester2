'''a helper-module for lab3 task5'''


class Point:
    '''A class to represent a point for class Triangle.

    Attributes:
        x_point: int
            first value of the point
        y_point: int
            second value of the point

    '''
    def __init__(self, x_cord, y_cord):
        '''Inits Point with x_cord, y_cord.'''
        self.x_cord = x_cord
        self.y_cord = y_cord
