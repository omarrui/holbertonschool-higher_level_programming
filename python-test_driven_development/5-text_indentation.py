#!/usr/bin/python3
"""
Module that prints text with indentation.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'

    Args:
        text: string to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
