#!/usr/bin/python3
"""
square 3

creates a class that hanfles rectangles
"""


class Rectangle:
    """
    rectancle class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if not value < 0:
            raise ValueError("width must be >= 0")
        return self.width

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.height

    def area(self):
        """
        returns the area
        """
        return (self.height * self.width)

    def perimeter(self):
        if self.heigth == 0 or self.width == 0:
            return 0
        return (self.height * self.width) * 2

    def str(self):
        if self.height == 0 or self.height == 0:
            return ""
        row = "#" * self.width
        return "{}".format(row + "\n") * (self.height - 1) + row
