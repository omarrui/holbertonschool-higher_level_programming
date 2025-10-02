#!/usr/bin/python3
"""Function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create an Object from a JSON file.

    Args:
        filename: Name of the JSON file to read from

    Returns:
        Python object from the JSON file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
