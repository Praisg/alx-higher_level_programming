#!/usr/bin/python3
"""Replace element  copied at specific position."""

def new_in_list(my_list, idx, element):
    
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    cop_y = [x for x in my_list]
    cop_y[idx] = element
    return (cop_y)

