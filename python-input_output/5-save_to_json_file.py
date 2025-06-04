#!/usr/bin/python3
"""
5save to json

writes an object to text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text dile
    """
    with open(filename, "w") as f:
        return json.dump(my_obj)
