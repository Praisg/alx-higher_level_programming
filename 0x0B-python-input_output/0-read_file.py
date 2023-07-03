#!/usr/bin/python3
"""Text file reading function task 0.""""

def read_file(filename=""):
"""Print file to standarrd output"""
    with open(filename, encoding="utf8") as file:
            print(file.read(), end="")
