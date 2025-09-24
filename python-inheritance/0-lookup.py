#!/usr/bin/python3
"""built-in Python function that returns a list of all attributes"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return dir(obj)
