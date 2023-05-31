#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent  square."""

    def __init__(self, size=0):
      
        if not isinstance(size, int):
            raise TypeError("size =integer")
        elif size < 0:
            raise ValueError("size  >= 0")
        self.__size = size

    def area(self):
        """Return area."""
        return (self.__size * self.__size)


