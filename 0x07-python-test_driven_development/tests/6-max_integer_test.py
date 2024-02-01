#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        n = [1, 2, 3, 4]
        self.assertEqual(max_integer(n), 4)
    def test_variable_type(self):
        n = [1, 2, 3, 4]
        for element in n:
            with self.subTest(element=element):
                self.assertIsInstance(element, int)
    def test_if_list_is_empty(self):
        n = []
        self.assertFalse(n)
    def test_negative(self):
        n = [-1, -5, -3, -2]
        self.assertEqual(max_integer(n), -1)
    def test_float(self):
        n = [0.1 , 0.2, 2.4, 2.2]
        self.assertEqual(max_integer(n), 2.4)
