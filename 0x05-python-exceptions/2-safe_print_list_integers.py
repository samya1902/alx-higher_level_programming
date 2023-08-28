#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers
    Args:
        my_list(list): list
        x(int): nb of elements to print
    Retruns:
        nbr of elements to print
    """
    a = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            a += 1
        except (ValueError, TypeError):
            continue
        print("")
    return (a)
