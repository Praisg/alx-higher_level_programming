#!/usr/bin/python3
"""Defines class Student."""


class Student:
    """ Student class's body."""

    def __init__(self, first_name, last_name, age):
        """Initialit propontructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
