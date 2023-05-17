#!/usr/bin/python3
'''retrn max int of a list'''
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    my_list.sort(reverse=True)
    big = my_list[0]
    return big

