#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Function that creates a pascal triangle
    Args:
        n ([int]): [size of the tringle]
    Returns:
        [list]: [pascal triangle]
    """
    lista = [1, 1]
    new = []
    fin = [[1], [1, 1]]
    if n <= 0:
        return new
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    else:
        for i in range(3, n + 1):
            new.append(1)
            for j in range(len(lista) - 1):
                new.append(lista[j] + lista[j + 1])
            new.append(1)
            fin.append(new)
            lista = new.copy()
            new = []
        return(fin)
