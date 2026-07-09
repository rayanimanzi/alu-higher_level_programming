#!/usr/bin/python3
"""Module that safely prints an integer."""


def safe_print_integer(value):
    """Print value as an integer using "{:d}".format().

    Returns True if value was printed successfully (it's an integer),
    otherwise returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
