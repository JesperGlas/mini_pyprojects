#!/usr/bin/env python
'''
Tests for seach algorithms
'''

import unittest
from sorting_algorithms import insertion_sort, merge_sort

EMPTY = []

UNSORTED10 = [2, 65, 8, 43, 12, 4, 4, 90, 192, 82]
SORTED10 = [2, 4, 4, 8, 12, 43, 65, 82, 90, 192]

class TestSorting(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertEqual(
            insertion_sort(UNSORTED10),
            SORTED10
        )

        self.assertEqual(
            insertion_sort(EMPTY),
            EMPTY
        )

        self.assertEqual(
            insertion_sort(SORTED10),
            SORTED10
        )

    def test_merge_sort(self):
        self.assertEqual(
            merge_sort(UNSORTED10),
            SORTED10
        )

        self.assertEqual(
            merge_sort(EMPTY),
            EMPTY
        )

        self.assertEqual(
            merge_sort(SORTED10),
            SORTED10
        )
        

if __name__ == '__main__':
    unittest.main()