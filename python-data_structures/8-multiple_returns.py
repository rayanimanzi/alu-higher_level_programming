#!/usr/bin/python3
"""Module that returns the length and first character of a string."""


def multiple_returns(sentence):
    """Return a tuple: (length of sentence, first character).

    If sentence is empty, the first character is None.
    """
    first_character = sentence[0] if len(sentence) > 0 else None
    return (len(sentence), first_character)
