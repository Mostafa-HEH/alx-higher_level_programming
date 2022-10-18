#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """This class run tests on alist with max integer function
    """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 7, 99, 20]), 99)
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())
        self.assertEqual(max_integer(['a', 'd', 's']), 's')
        self.assertRaises(TypeError, max_integer, 'a', 'd', 2)
        self.assertRaises(TypeError, max_integer, 5)
        self.assertEqual(max_integer('Mostafa'), 't')
        self.assertEqual(max_integer((20, 3)), 20)
