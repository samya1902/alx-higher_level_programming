#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    try:
        reslt = fct(*args)
        return (reslt)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
