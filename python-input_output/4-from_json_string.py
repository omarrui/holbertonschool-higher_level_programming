#!/usr/bin/python3
"""Function that returns an object from a JSON string."""
import json


def from_json_string(my_str):
    """Return an object (Python data structure) from a JSON string.

    Args:
        my_str: JSON string to convert to Python object

    Returns:
        Python object represented by the JSON string
    """
    return json.loads(my_str)
