#!/usr/bin/python3
"""Module containing BaseGeometry class with area method"""


class BaseGeometry:
    """BaseGeometry class with unimplemented area method"""

    def area(self):
        """Raises an exception - must be implemented by subclasses"""
        raise Exception("area() is not implemented")
