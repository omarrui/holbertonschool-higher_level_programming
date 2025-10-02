#!/usr/bin/python3
"""Function that returns the dictionary description of an object for JSON."""


def class_to_json(obj):
    """Return dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class

    Returns:
        Dictionary with all serializable attributes of the object
    """
    return obj.__dict__
