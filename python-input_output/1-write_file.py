#!/usr/bin/python3
"""
1writefile

writingin a file
"""


def write_file(filename="", text=""):
    """writes a string into txt file and returns the number of ch written"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
