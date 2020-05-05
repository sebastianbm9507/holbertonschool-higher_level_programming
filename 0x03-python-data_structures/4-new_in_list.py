#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        # Variable to store the length of list 🛃 #
        len_list = len(my_list)
        # Variable to store the copy of list 🔴#
        copy_list = my_list.copy()
        # Checking the cases 🟢#
        if idx < 0 or idx >= len_list:
            return copy_list
        # Replacing the element ⚫️#
        copy_list[idx] = element
        # Return the copy of list ⚪️#
        return copy_list
