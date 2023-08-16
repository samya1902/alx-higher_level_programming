#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    ls_key = list(new_dir.keys())
    for i in ls_key:
        new_dir[i] *= 2

    return (new_dir)
