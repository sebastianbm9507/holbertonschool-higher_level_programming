#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # create new tuple ✅
    tuple_rslt = []
    # convert tuples into list 🆗
    list_a = list(tuple_a) + [0, 0]
    list_b = list(tuple_b) + [0, 0]
    # append to the tuple 🔄
    tuple_rslt.append(list_a[0] + list_b[0])
    tuple_rslt.append(list_a[1] + list_b[1])
    # conver to tuple 🔰
    tuple_rslt = tuple(tuple_rslt)

    return tuple_rslt
