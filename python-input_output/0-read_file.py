#!/usr/bin/python3
"""
read_file

This module contains a function that reads and prints a file's content.
"""

def read_file(filename=""):
    """Reads a text file and prints its contents to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
