#!/usr/bin/python3
"""Defines ends a string."""


def append_write(filename="", text=""):
    """Appends a stringha UTF8 text file.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
