#!/usr/bin/python3
def delete_at(my_list=None, idx=0):
    if my_list is None:
        my_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
