#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print("Original list:", my_list)

new_list = copy_list(my_list)

print("Original after copy:", my_list)
print("New list:", new_list)
print("Are they equal?", new_list == my_list)
print("Are they the same object?", new_list is my_list)

# Test with None
print("Copy of None:", copy_list(None))
