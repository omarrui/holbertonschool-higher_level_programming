#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list1 = my_list[:]
    if idx < 0 and idx >= len(my_list):
        return list1
    list1[idx] = element
    return list1
