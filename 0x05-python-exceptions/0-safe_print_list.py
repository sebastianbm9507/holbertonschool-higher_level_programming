#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for index, value in enumerate(my_list):
            if index < x:
                print("{:d}".format(my_list[index]), end="")
                counter += 1
        print()
        return counter
    except IndexError as error:
        print(erro)

""" ✅
 Another solution :
 try:
        for item in range(0, x):
            print("{}".format(my_list[item]), end="")
            num += 1
    except IndexError:
"""
