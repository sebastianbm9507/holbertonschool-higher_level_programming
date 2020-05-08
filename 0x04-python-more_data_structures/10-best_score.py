#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        hig = max(a_dictionary, key=a_dictionary.get)
        return hig
    else:
        return None

""" ✅
    to return the highest value of a key
    to ask the value -> dictonary[key] -> value
    hig = 0
    for i in dicionary:
        if dictionary[i] > hig:
            hig = dictionary[i]
    ✅
    to return the key that has the highest value:
        if a_dictionary:
        hig = 0
        kei = ''
        for i in a_dictionary:
            if a_dictionary[i] > hig:
                hig = a_dictionary[i]
                kei = i
            return i
    else:
        return None
"""
