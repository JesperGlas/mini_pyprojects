#!/usr/bin/env python

"""
Testing for hello.py
"""

import unittest
from hello_world import hello

class TestHello(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(hello(), "Hello you!")

    def test_one_name(self):
        self.assertEqual(hello(["Jesper"]), "Hello Jesper!")

    def test_many_name(self):
        self.assertEqual(hello(["Kasper", "Jesper", "Jonathan"]), "Hello Kasper, Jesper, Jonathan!")

if __name__ == '__main__':
    unittest.main()