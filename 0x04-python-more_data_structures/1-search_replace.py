#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Copy of list ✅
    copy_list = my_list.copy()
    for i in copy_list:
        if i == search:
            # replace the element 🔁
            copy_list[i] = replace
    return copy_list
