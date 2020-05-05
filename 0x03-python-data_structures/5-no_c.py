#!/usr/bin/python3
def no_c(my_string):
    # Variable to store the new str 🛃 #
    str = ""
    # iterating into mystring 🔰 #
    for i in my_string:
        if i not in 'cC':
            str += i
    return str
