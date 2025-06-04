#!/usr/bin/bash/python3
"""
load_from_json_file


this module contains a
load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    anfunction that creates an object from
      a json file"""
    with open(filename, "r") as file:
        return json.load(file)
