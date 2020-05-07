#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Copy of list ✅
    copy_list = my_list.copy()
    idx = 0
    for i in copy_list:
        if i == search:
            # replace the element 🔁
            copy_list[idx] = replace
        idx += 1
    return copy_list
