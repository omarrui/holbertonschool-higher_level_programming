#!/usr/bin/python3
"""Module containing Square class with custom string representation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class with custom string representation"""
    
    def __init__(self, size):
        """Initialize Square with validated size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def __str__(self):
        """Return string representation of the square
        
        Returns:
            str: Format "[Square] size/size"
        """
        return f"[Square] {self.__size}/{self.__size}"
