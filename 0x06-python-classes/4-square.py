#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a quare."""

    def __init__(self, size=0):
        
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size =integer")
        elif value < 0:
            raise ValueError("size>= 0")
        self.__size = value

    def area(self):
 """Return area."""
        return (self.__size * self.__size)

