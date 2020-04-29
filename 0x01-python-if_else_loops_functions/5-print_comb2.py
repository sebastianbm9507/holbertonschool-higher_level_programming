#!/usr/bin/python3
for number in range(0, 100):
    if number <= 9:
        unit = number / 10
        print("0{}".format(number), end=", ")
    else:
        if number != 99:
            print("{}".format(number), end=", ")
        else:
            print(number)
