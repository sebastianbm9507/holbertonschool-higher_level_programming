#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # create the copy of a_dictionary
    newdic = dict(a_dictionary)
    for dic, value in a_dictionary.items():
        newdic[dic] = value * 2
    return newdic
