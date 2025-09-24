#!/usr/bin/python3
"""Module containing full Rectangle class with area calculation"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with area calculation and string representation"""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle

        Returns:
            int: Area (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle

        Returns:
            str: Format "[Rectangle] width/height"
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
