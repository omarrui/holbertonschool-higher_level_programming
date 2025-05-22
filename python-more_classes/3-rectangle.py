#!/usr/bin/python3
"""
3-rectangle

creates a class that defines a rectangle
"""


class Rectangle:
    """
    class rectangle to define a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns the attribut
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        assigns new value at attribut
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the attribut
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        assigns new value at attribut
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        that displays the area of rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """
        that displays the perimeter of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        row = "#" * self.width
        return "{}".format(row + "\n") * (self.height - 1) + row
