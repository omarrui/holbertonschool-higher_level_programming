#!/usr/bin/python3
"""Function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout.

    Args:
        filename: Name of the file to read (default empty string)
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
