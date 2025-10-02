#!/usr/bin/python3
"""Function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return number of characters.

    Args:
        filename: Name of the file to write to
        text: Text to write to the file

    Returns:
        Number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
