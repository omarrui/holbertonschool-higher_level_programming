#!/usr/bin/python3
"""Module for checking class membership including inheritance"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or inherited from it"""
    return isinstance(obj, a_class)
