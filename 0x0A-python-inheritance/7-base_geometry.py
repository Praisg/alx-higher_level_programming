#!/usr/bin/python3
"""Defines Base_Geometry of class."""


class BaseGeometry:
    """Class_body."""

    def area(self):
        """Not_get_implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter format.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
