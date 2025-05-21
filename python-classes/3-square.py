#!/usr/bin/python3
"""
4-square

creates class square to handle objects
"""


class Square:
    """
    Class Square creates square objects
    """
    def __init__(self, size=0):
        """
        creates an instance of object with these parameter
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        returns the current square area
        """
        return self.__size ** 2
