'''
Tests for seach algorithms
'''

import unittest
from sorting_algorithms import insertion_sort

UNSORTED10 = [2, 65, 8, 43, 12, 4, 4, 90, 192, 82]
SORTED10 = [2, 4, 4, 8, 12, 43, 65, 82, 90, 192]

class TestSorting(unittest.TestCase):

    def TestLinearSort(self):
        self.assertEqual(
            linear_sort(UNSORTED10),
            SORTED10
        )

if __name__ == '__main__':
    unittest.main()