#!/usr/bin/python3
"""Module that returns a new dictionary with all values multiplied by 2."""


def multiply_by_2(a_dictionary):
    """Return a new dictionary with every value doubled."""
    new_dictionary = {}
    for key, value in a_dictionary.items():
        new_dictionary[key] = value * 2
    return new_dictionary
