#!/usr/bin/python3
"""Function that returns the JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string).

    Args:
        my_obj: Python object to convert to JSON

    Returns:
        JSON string representation of the object
    """
    return json.dumps(my_obj)
