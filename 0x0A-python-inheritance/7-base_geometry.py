#!/usr/bin/python3
"""contains class BaseGeometry"""


class BaseGeometry:
    """define basegeometry"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks that the value of an integer is greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
