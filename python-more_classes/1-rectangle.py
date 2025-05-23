#!/usr/bin/python3
"""
recangle 1

creates a class that defines reclangles
"""


class Rectangle:
    """
    a recangle class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrives the width
        """
        return self.__width

    @property
    def height(self):
        """
        retrives the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        retrives width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        retrives the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
