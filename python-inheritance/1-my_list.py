#!/usr/bin/python3
"""Module containing MyList class"""


class MyList(list):
    """A class that inherits from list with additional functionality"""
    
    def print_sorted(self):
        """Prints the list in sorted order (ascending) without modifying original"""
        print(sorted(self))
