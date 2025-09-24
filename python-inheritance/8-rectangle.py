#!/usr/bin/python3
"""Module containing Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height

        Args:
            width (int): Width of rectangle (must be positive integer)
            height (int): Height of rectangle (must be positive integer)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
