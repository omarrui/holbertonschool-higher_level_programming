#!/usr/bin/python3
"""
basic_serialization

this module contains 2 functions
to serialize and deserialize
"""
import json


def serialize_nd_save_to_file(data, filename):
    """
    Serialize data to a JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)
    pass


def load_from_file_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    pass
