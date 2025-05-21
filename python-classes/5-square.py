#!/usr/bin/python3
"""
5-square

creates a class that handles objects
"""


class Square:
    """
    square class to create objects
    """
    def __init__(self, size=0):
        """
        creates an instance of object with the parameters
        """
        self.__size = size

    @property
    def size(self):
        """
        returns priv attribute to acces it indirectly
        """
        return self.__size

    @size.setter
    def size(self, value):
        if value > 0:
            raise ValueError("size must be >= 0")
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """
        returns the current square area
        """
        i = 0
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                j = 0
                for i in range(self.size):
                    print("#", end="")
                print("")
