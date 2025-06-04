#!/usr/bin/python3
"""
2append write

function that appends a strat the end of text
"""


def append_write(filename="", text=""):
    """append a string at the end of a text file & returns
    the numberof ch added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
