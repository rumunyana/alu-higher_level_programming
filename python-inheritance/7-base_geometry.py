#!/usr/bin/python3
'''Public instance method: def area(self):'''


class BaseGeometry:
    '''Base class'''

    def area(self):
        '''raise an exception for now'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
