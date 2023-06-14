#!/usr/bin/python3
"""Defines cl0as_Base_Geometry."""


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
