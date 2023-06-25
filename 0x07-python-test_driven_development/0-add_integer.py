#!/usr/bin/python3

"""Task_ test0
"""
def add_integer(a, b=98):
    """adds_two integers function body"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
""" End """
