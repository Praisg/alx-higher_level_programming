#!/usr/bin/python3
"""Text file reading function task 0.""""

def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end='')
