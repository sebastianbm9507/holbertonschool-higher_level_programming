#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    elements_printed = 0
    try:
        for item in range(x):
            print("{:d}".format(my_list[item]), end="")
            elements_printed += 1
    except (ValueError, TypeError):
        pass
    print()
    return elements_printed
