#!/usr/bin/python3
"""
2-square

That create class square to handle object
"""


class Square:
    """
    Class Square create square object
    """
    def __init__(self, size=0):
        """
        create an instance of object with these parameter
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
