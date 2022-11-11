#!/usr/bin/python3
"""define class rectangle"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """"return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width instance"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """define height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign height"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """" prints area of the rectangle"""
        A = self.__height * self.__width
        return A

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            p = 2 * (self.__height + self.__width)
            return p

    def __str__(self):
        """return rectangle using # sign"""
        if self.__width == 0 or self.__height == 0:
            return ''
        else:
            rectangle = ''
            for h in range(self.__height):
                for w in range(self.__width):
                    rectangle = rectangle + str(self.print_symbol)

                rectangle = rectangle + '\n'
            return rectangle[:-1]

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to create new instance using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints deletion message"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
