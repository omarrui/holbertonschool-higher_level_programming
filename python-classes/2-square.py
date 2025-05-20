#!/usr/bin/python3
"""

represent a square


"""


class Square:
    """
    the square Class creates square objects
    """
    def __innit__(self, size=0):
        """
        creating an instance of object withthese parameters
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size > 0:
            raise ValueError("size must be >= 0")
