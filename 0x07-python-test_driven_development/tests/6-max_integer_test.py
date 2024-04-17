#!/usr/bin/python3
""" Unittest for max_integer([...]). """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Test suite for max_integer() """

    def test_empty_list(self):
        """ Validate outcome for empty list. """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(""), None)

    def test_single_element_list(self):
        """ Validate outcome for single element list. """
        self.assertEqual(max_integer([4]), 4)

    def test_max_at_beginning(self):
        """ Validate outcome for max at beginning of list. """
        self.assertEqual(max_integer([7, 3, 2, 0]), 7)

    def test_unsorted_list(self):
        """ Validate outcome for unsorted list. """
        self.assertEqual(max_integer([4, 5, 1, 3]), 5)

    def test_sorted_list(self):
        """ Validate outcome for sorted list. """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_neg_integers(self):
        """ Validate outcome for negative integer list. """
        self.assertEqual(max_integer([-4, -5, -1, -3]), -1)

    def test_float_values(self):
        """ Validate outcome for list of float values. """
        self.assertEqual(max_integer([4.4, 5.5, 1.1, 3.3]), 5.5)

    def test_neg_float_values(self):
        """ Validate outcome for list of negative float values. """
        self.assertEqual(max_integer([-4.5, -5.7, -1.2, -3.4]), -1.2)

    def test_float_int_values(self):
        """ Validate outcome for list of float and integer values. """
        self.assertEqual(max_integer([4.4, 5, 1.1, 3]), 5)

    def test_string_int_values(self):
        """ Validate outcome for list of string and integer values. """
        self.assertRaises(TypeError, max_integer, ['school', 5, 3, '7'])


if __name__ == '__main__':
    unittest.main()
