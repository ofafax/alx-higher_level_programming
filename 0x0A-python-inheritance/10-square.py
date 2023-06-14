#!/usr/bin/python3

"""Defines a class Square with subclass Rectagle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a square"""

    def __init__(self, size):
        """Initialize new square """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
