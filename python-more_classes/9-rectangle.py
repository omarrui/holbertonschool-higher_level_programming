#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """A rectangle class with square creation method."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with given width and height.

        Args:
            width: The width of the rectangle (default 0)
            height: The height of the rectangle (default 0)
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value: The new width value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value: The new height value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle (2 * (width + height))
            Returns 0 if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation using print_symbol.

        Returns:
            String representation, empty string if width or height is 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result = []
        for i in range(self.__height):
            result.append(str(self.print_symbol) * self.__width)
        return "\n".join(result)

    def __repr__(self):
        """Return string representation to recreate the rectangle.

        Returns:
            String that can be used with eval() to create a new instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area.

        Args:
            rect_1: First rectangle to compare
            rect_2: Second rectangle to compare

        Returns:
            The rectangle with the bigger area, or rect_1 if equal

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance as a square.

        Args:
            size: The size of the square (default 0)

        Returns:
            A new Rectangle instance with width == height == size
        """
        return cls(size, size)
