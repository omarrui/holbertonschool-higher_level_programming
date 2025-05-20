#!/usr/bin/python3
"""
represent a square

defining the square
"""


class Square:
    """
    the square Class creates square objects
    """
    def __init__(self, size=0):
        """
        create an instance of object with these parameters
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size > 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        returns the sauare area
        """
        return self.__size ** 2
