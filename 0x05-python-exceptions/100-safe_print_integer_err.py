#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err_:
        print("Exception: {}".format(err_), file=sys.stderr)
        return False
    return True
