#!/usr/bin/python3
"""Function that writes an Object to a text file using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file using JSON representation.

    Args:
        my_obj: Python object to save
        filename: Name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
