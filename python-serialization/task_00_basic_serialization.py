#!/usr/bin/env python3
"""Basic serialization module."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save data to the specified file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load and deserialize data from the specified file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        Python Dictionary with the deserialized JSON data from the file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
