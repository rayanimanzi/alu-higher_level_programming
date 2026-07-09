#!/usr/bin/python3
"""Module that replaces all occurrences of an element by another."""


def search_replace(my_list, search, replace):
    """Return a new list with every occurrence of search replaced."""
    return [replace if item == search else item for item in my_list]o

