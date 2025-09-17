#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """A square class with private size attribute."""
    
    def __init__(self, size):
        """Initialize a square with given size.
        
        Args:
            size: The size of the square
        """
        self.__size = size

