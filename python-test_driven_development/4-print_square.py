#!/usr/bin/python3
"""
Module that prints a square.
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size: size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
