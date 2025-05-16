#!/usr/bin/python3
"""
add_integer.py

This module defines a function that adds two integers or floats.
Floats are cast to integers before addition.
"""

import math

def add_integer(a, b=98):
    """
    Adds two integers or floats (which are cast to ints).
    
    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.
    
    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b are not int or float.
        ValueError: If a or b are NaN or infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and (math.isnan(a) or math.isinf(a)):
        raise ValueError("cannot convert float NaN or infinity to integer")
    if isinstance(b, float) and (math.isnan(b) or math.isinf(b)):
        raise ValueError("cannot convert float NaN or infinity to integer")

    return int(a) + int(b)
