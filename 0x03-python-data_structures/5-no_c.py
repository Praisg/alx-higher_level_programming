#!/usr/bin/python3
def no_c(my_string):
   #data  = [x for x in my_string if x != 'c' and x != 'C']
    #return ("".join(data))
  new_string = ""
for char in my_string:
        if char != "c" and char != "C":
            new_string += char
        return new_string
