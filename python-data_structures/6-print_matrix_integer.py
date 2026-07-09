#!/usr/bin/python3
"""Module that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, one row per line."""
    for row in matrix:
        values = []
        for number in row:
            values.append("{:d}".format(number))
        print(" ".join(values))
