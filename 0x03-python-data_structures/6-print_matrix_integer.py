#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Going into row in matrix 🔁#
    for row in matrix:
        # assing value
        column = " ".join("{:d}".format(column) for column in row)
        print(column)
