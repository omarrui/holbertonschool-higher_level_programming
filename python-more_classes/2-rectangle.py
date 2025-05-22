#!/usr/bin/python3
"""
rectangle 2

creating a class that defines objects
"""


class Rectangle:
    """
    a rectangle class that defines objects
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieve the attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        assign anew value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrive teh attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set new vlaue
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        retrun the area
        """
        return (self.height * self.width)

    def perimeter(self):
        """
        return the primiter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2
