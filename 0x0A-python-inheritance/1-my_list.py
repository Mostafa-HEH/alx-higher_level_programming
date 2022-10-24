#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements my list inheres list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        for i in range(0, len(self)):
            if not isinstance(self[i], int):
                break
        print(sorted(self))
