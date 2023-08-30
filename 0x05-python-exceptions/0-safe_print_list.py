#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """prints x elements of a list.

    Args:
        my_list (list): list
        x (int): nbr of elements

    Returns:
        nbr of elements printed
    """
    a = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            a += 1
        except IndexError:
            break
    print("")
    return (a)
