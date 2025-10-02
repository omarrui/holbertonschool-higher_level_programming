#!/usr/bin/python3
"""Function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8).

    Args:
        filename: Name of the file to append to
        text: Text to append to the file

    Returns:
        Number of characters added
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
