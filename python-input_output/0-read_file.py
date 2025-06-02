#!/usr/bin/python3
def read_file(filename=""):
    """reads a text to a file and  prints its contents to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
