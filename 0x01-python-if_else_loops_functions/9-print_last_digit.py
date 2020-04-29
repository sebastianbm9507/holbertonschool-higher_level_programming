#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        sign = number * -1
        last_ = sign % 10
    else:
        last_ = number % 10

    print("{}".format(last_), end="")
    return last_
