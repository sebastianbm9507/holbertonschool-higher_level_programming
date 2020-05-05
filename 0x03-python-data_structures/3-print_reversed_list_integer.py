#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Variable to store the length of list 🛃 #
    len_list = len(my_list)
    # reversing the list ⏮#
    my_list.reverse()
    # Variable to stored the reversed list 🔁 #
    reversed_list = my_list
    # Iterating in the list 🔄#
    for i in range(len_list):
        print("{:d}".format(reversed_list[i]))
