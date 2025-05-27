#!/usr/bin/python3
"""
list 1

list
"""


class MyList(list):
    """
    class that calls lists
    """
    def print_sorted(self):
        """
        prints the sorted lists
        """
        print(sorted(self))
