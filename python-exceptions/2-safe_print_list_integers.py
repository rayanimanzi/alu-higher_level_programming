#!/usr/bin/python3
"""Module that prints and counts integers from a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x integers of my_list on one line.

    Non-integer values are skipped silently. Returns the real
    number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count
