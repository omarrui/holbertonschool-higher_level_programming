#!/usr/bin/python3
"""Module containing BaseGeometry class with validation"""


class BaseGeometry:
    """BaseGeometry class with area and integer_validator methods"""
    
    def area(self):
        """Raises an exception - must be implemented by subclasses"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validates that value is a positive integer
        
        Args:
            name (str): Name of the value being validated
            value: Value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
