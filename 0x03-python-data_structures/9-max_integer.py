#!/usr/bin/python3
def max_integer(my_list=[]):
    if bool(my_list) is False:
        return None
    max = 0
    for i in my_list:
        if i > max:
            max = i
    return max
