#!/usr/bin/python3
"""Module containing Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    
    def __init__(self, size):
        """Initialize Square with validated size
        
        Args:
            size (int): Size of square sides (must be positive integer)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
