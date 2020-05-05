#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # Variable to store the length of list 🛃 #
    len_list = len(my_list)
    # checking if negative or greater than length list 🈂️#
    if idx < 0 or idx >= len_list:
        return my_list
    my_list[idx] = element
    return my_list
