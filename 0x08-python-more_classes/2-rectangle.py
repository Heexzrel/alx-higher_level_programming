#!/usr/bin/python3
"""
    Rectangle module
"""

class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Init Rectangle Class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
         return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return Rectangle Area """
        return self.__width * self.__height

    def perimeter(self):
        """  Return the perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)
