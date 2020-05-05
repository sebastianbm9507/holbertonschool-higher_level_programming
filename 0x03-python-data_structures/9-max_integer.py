#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        # Sorted list 🅰️
        my_list.sort()
        return my_list[-1]
