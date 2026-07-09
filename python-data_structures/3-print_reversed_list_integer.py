#!/usr/bin/python3
"""Module that prints all integers of a list in reverse order."""


def print_reversed_list_integer(my_list=[]):
    """Print every integer in my_list in reverse order, one per line."""
    idx = len(my_list) - 1
    while idx >= 0:
        print("{:d}".format(my_list[idx]))
        idx -= 1
