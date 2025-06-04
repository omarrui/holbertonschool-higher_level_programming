#!/usr/bin/python3
"""
4 from json string

from json string to object
"""


import json


def from_json_string(my_str):
    """
    return the json string
    """
    return json.loads(my_str)
