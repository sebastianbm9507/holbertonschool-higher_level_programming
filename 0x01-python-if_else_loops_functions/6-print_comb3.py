#!/usr/bin/python3
for i in range(0, 100):
    first_digit = int(i / 10)
    second_digit = i % 10
    if first_digit < second_digit:
        if i == 89:
            print("{:d}".format(i))
        else:
            print("{:02d}".format(i), end=", ")
