#!/usr/bin/python3
"""Define class MyList that inherits from list"""

class MyList(list):
    """Create my list inherits from list"""

    def __init__(self):
        """Init the object"""
        super().__init__()

    def print_sorted(self):
        """Print list as sorted"""
        print(sorted(self))
