#!/usr/bin/python3
"""Defines a func that Write_file."""


def write_file(filename="", text=""):
    """Write a string to a.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
