#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements my list inheres list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
