#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements my list inheres list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        new_list = self[:]
        new_list.sort()
        print("{}".format(new_list))
