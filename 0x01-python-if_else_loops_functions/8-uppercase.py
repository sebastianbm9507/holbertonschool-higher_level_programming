#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(c) >= 97 and ord(c) <= 122:
            chr = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")
