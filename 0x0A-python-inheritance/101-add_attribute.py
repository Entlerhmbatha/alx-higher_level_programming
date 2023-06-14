#!/usr/bin/python3
"""Define a func attr."""


def add_attribute(obj, att, value):
    """Add a new_attr
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
