#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """A square class with private size attribute and validation."""

    def __init__(self, size=0):
        """Initialize a square with given size.

        Args:
            size: The size of the square (default 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
