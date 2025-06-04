#!/usr/bin/bash/python3
"""
6 load from json file


write a function htat creates an object
"""


import json


def load_from_json_file(filename):
    """
    anfunction that creates an object from
      a json file"""
    with open(filename, "r") as file:
        return json.load(file)
