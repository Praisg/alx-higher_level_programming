#!/usr/bin/python3
"""Text file reading function.""""

def read_file(filename=""):
"""Print file to standarrd output"""
    with open(filename, encoding="utf8") as file:
            print(file.read(), end="")
