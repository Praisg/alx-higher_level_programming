#!/usr/bin/python3
'''retrieving element at specific index'''

def element_at(my_list, idx):
    if idx > (len(my_list) - 1) or idx < 0:
        return None
    return (my_list[idx])

