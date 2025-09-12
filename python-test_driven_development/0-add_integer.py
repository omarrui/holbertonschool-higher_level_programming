#!/usr/bin/python3
"""
Module that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: first integer or float
        b: second integer or float (default 98)

    Returns:
        The addition of a and b as integer

    Raises:
        TypeError: if a or b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    if a == float('inf') or a == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if b == float('inf') or b == float('-inf'):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
