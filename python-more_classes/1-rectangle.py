#!/usr/bin/python3
"""define class rectangle"""


class Rectangle:

    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """"retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width"""
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
