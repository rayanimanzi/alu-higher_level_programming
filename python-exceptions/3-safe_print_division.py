#!/usr/bin/python3
"""Module that divides 2 integers and prints the result."""


def safe_print_division(a, b):
    """Divide a by b, printing the result inside a finally block.

    Returns the result of the division, or None if it fails.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
