#!/usr/bin/python3
"""class My_Int that inherits_from_int."""


class MyInt(int):
    """My_Int clas_body"""

    def __eq__(self, value):
        """Override == with !=."""
        return self.real != value

    def __ne__(self, value):
        """Override !="""
        return self.real == value
