#!/usr/bin/python3
"""Module that prints all integers of a list, one per line."""


def print_list_integer(my_list=[]):
    """Print every integer in my_list, one per line."""
    for number in my_list:
        print("{:d}".format(number))
