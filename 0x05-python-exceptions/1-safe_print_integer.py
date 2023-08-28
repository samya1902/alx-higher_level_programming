#!/usr/bin/python3
def safe_print_integer(value):
    """print integer "{:d}".format()
    Args:
        value(int): integer to print
    Returns:
        true or false
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
