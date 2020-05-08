#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # convert keys into a list
    for kei in list(a_dictionary):
        # check if value exist in dictionary
        if value in a_dictionary[kei]:
            del a_dictionary[kei]
    return a_dictionary
    """
    to move into keys in a dictionary
    have to use list(dictionary)
    list of keys = list(dictionary)
    """
