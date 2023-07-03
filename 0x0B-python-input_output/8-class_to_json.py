#!/usr/bin/python3
""" class-to-JSON module."""


def class_to_json(obj):
    """Return the dicon of json."""
    return obj.__dict__
