#!/usr/bin/python3
"""Create a square """


class Square:
    '''
    Create a square
        Has a private Instance att: size
    '''

    def __init__(self, size=0):
        ''' init size '''
        self.__size = size

    @property
    def size(self):
        "returns the size att"
        return self.__size

    @size.setter
    def size(self, size):
        '''asign the size to the size att'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
