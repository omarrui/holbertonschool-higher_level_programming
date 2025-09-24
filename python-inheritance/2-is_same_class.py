#!/usr/bin/python3
"""Module for checking exact class membership"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class (not inheritance)"""
    return type(obj) is a_class
