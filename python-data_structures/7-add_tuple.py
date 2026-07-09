#!/usr/bin/python3
"""Module that adds 2 tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Return a tuple that is the element-wise sum of two tuples.

    Missing elements (if a tuple has fewer than 2 items) are
    treated as 0. Only the first 2 elements of each tuple are used.
    """
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a1 + b1, a2 + b2)
