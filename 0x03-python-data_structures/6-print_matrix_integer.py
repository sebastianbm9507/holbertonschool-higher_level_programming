#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Into row in matrix 🔄#
    for row in matrix:
        # Into val in row 🔄#
        for val in row:
            print("{:d} ".format(val), end="")
        print()
