#!/usr/bin/python3
import sys

#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as err:
        print("Exception:", err, file=stderr)
