#!/usr/bin/python3
"""
Module that creates a read_lines function
"""


def read_lines(filename="", nb_lines=0):
    """[summary]

    Args:
        filename (str, optional): [description]. Defaults to "".
        nb_lines (int, optional): [description]. Defaults to 0.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        n_lines = 0
        for lines in file:
            n_lines += 1

        file.seek(0)
        if nb_lines <= 0 or nb_lines >= n_lines:
            file_data = file.read()
            print(file_data, end="")
        else:
            for line in range(nb_lines):
                file_data = file.readline()
                print(file_data, end='')
