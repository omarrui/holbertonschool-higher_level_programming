#!/usr/bin/python3
"""
6 square

creates square class that handles objects
"""


class square:
    """
    square class to create objects
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        create an instance of object with these parameter
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        retruns priv ti acces it indirectly
        """
        return self.size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    @property
    def position(self):
        """
        returns a priv attribute to acces it indirectly
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        change value of a priv attribute indirectly
        """

        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        """
        That returns the current square area
        """
    def print(self):
        """
        prints the squaresith # ymbol and adds space to position
        """
        if self.size == 0:
            print()
            return
        for col in range(self.position[1]):
            print("")
        for i in range(self.size):
            for row in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
