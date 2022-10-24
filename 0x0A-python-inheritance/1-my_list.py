#!/usr/bin/python3
"""Define class MyList that inherits from list"""


class MyList(list):
    """Create my list inherits from list"""

    def print_sorted(self):
        """Print list as sorted"""
        print(sorted(self))
