#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # declare new matrix ✅
    new = []
    for i in (matrix):
        new.append([j**2 for j in i])
    return (new)
