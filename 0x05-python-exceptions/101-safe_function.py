#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return_value = fct(args[0], args[1])
        return return_value
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return None
