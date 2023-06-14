#!/usr/bin/python3

"""cotains a class MyInt that inherits from int"""


class MyInt(int):
    """A subclass int"""

    def __eq__(self, other):
        """sets the == """
        return int(self) != other

    def __ne__(self, other):
        """sets the != """
        return int(self) == other
