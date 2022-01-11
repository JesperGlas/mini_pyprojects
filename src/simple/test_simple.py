import unittest

from simple import first_recurring, anagram, first_and_last, kth_largest, balanced_para

class TestSimple(unittest.TestCase):

    def test_first_recurring(self):
        self.assertEqual(first_recurring(['A', 'B', 'C', 'D', 'A']), 'A')
        self.assertEqual(first_recurring(['A', 'B', 'C', 'B','A']), 'B')
        self.assertEqual(first_recurring(['A', 'B', 'C', 'D', 'E']), None)

    def test_anagram(self):
        self.assertTrue(anagram('danger', 'garden'))
        self.assertTrue(anagram('helloworld', 'hdelllroow'))
        self.assertTrue(anagram('a', 'a'))
        self.assertTrue(anagram('abc', 'cba'))
        self.assertFalse(anagram('helloworld', 'hdellrooow'))
        self.assertFalse(anagram('a', ''))

    def test_first_and_last(self):
        self.assertEqual(first_and_last([2, 4, 5, 5, 5, 5, 5, 7, 9, 9], 5), (2, 6))
        self.assertEqual(first_and_last([1, 2, 3, 4, 5, 2, 4], 9), (-1, -1))

    def test_kth_largest(self):
        self.assertEqual(kth_largest([4, 2, 9, 7, 5, 6, 7, 1, 3], 4), 6)
        self.assertEqual(kth_largest([4, 2, 9, 7, 5, 6, 7, 1, 3], 4, unique=True), 5)
        self.assertEqual(kth_largest([4, 6, 5, 7], 5), 4)
        self.assertEqual(kth_largest([1, 2, 3, 4, 5, 5, 5], 3), 5)
        self.assertEqual(kth_largest([1, 2, 3, 4, 5, 5, 5], 3, unique=True), 3)

    def test_balanced_para(self):
        self.assertEqual(balanced_para(1), ['()'])
        self.assertEqual(balanced_para(2), ['(())', '()()'])
        self.assertCountEqual(balanced_para(3), ['((()))', '()()()', '(())()', '()(())', '(()())'])

if __name__ == '__main__':
    unittest.main()