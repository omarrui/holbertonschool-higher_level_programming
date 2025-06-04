#!/usr/bin/python3
"""
save_to_json_file

writes an object to text file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text dile
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
