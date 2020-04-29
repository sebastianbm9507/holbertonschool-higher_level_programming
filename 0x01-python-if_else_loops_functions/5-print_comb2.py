#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        # 02d formats an integer (d) to a field of minimum width 2 (2) #
        # with zero-padding on the left (leading 0):#
        print("{:02d}".format(number))
    else:
        print("{:02d}, ".format(number), end="")
