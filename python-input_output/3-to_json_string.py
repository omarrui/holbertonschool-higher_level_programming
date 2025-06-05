#!/bin/bash/python3
"""
to_json_string

to json string
"""
import json


def to_json_string(my_obj):
    """
    returns the json representation of a string
    """
    return json.dumps(my_obj)
