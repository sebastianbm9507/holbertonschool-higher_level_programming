#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # checking cases ✅
    if idx < 0 or idx >= len(my_list):
        return my_list
    # iterating the list 🔄
    for i in my_list:
        # found it 🆗
        if my_list[idx] == i:
            my_list.remove(i)
    return my_list
