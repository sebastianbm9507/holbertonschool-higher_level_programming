#!/usr/bin/python3
def magic_string(x=[0]):
    x[0] = x[0] + 1
    return ((("Holberton" + ", ") * x[0])[:-2])
