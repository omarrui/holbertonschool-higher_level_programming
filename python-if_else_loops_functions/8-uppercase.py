#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            upper_c = chr(ord(c) - 32)
        else:
            upper_c = c
        print("{}".format(upper_c), end="")
    print()
