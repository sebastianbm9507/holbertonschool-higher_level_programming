#!/usr/bin/python3
def element_at(my_list, idx):
    # Variable to store the length of list 🛃 #
    len_list = len(my_list)
    # checking if negative or greater than length list 🈂️#
    if idx < 0 or idx > len_list:
        return None
    # Returning element at idx 🆗#
    return my_list[idx]
