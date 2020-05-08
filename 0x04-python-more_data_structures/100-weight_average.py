#!/usr/bin/python3
def weight_average(my_list=[]):
    add = 0
    div = 0
    if my_list:
        for i in my_list:
            add += i[1] * i[0]
            div += i[1]
        return add/div
    else:
        return 0
