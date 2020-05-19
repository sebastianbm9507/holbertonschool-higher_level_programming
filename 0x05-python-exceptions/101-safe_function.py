#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException as err_:
        print("Exception: {}".format(err_), file=sys.stderr)
        return None
