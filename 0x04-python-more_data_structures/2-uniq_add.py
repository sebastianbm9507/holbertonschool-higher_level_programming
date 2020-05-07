#!/usr/bin/python3
def uniq_add(my_list=[]):
    # new list
    new_list = []
    for element in my_list:
        # checking element not exist in list 🔄
        if element not in new_list:
            new_list.append(element)
    result = 0
    # adding each element in list into result 🔴
    for item in new_list:
        result += item
    return result
