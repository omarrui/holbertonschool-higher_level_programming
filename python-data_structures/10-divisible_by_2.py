#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in my_list:
        if i % 2 == 0:   # divisible
            new_list.append(True)
        else:            # not divisible
            new_list.append(False)
    return new_list
