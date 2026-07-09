#!/usr/bin/python3
"""Module that divides element by element 2 lists."""


def list_division(my_list_1, my_list_2, list_length):
    """Divide my_list_1[i] by my_list_2[i] for each index up to list_length.

    Returns a new list of length list_length with the division results.
    Any element that can't be divided is set to 0, with a message
    printed explaining why (wrong type, division by 0, out of range).
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
