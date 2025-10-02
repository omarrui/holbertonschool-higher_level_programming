#!/usr/bin/env python3
"""Custom object serialization using pickle."""
import pickle


class CustomObject:
    """A custom class with serialization methods."""

    def __init__(self, name, age, is_student):
        """Initialize CustomObject.
    
        Args:
            name: A string
            age: An integer
            is_student: A boolean
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file.

        Args:
            filename: The filename to save to
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a file.

        Args:
            filename: The filename to load from

        Returns:
            An instance of CustomObject or None if failed
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
