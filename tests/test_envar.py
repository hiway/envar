#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

from envar import envar, ImproperlyConfigured


class TestEnvar(unittest.TestCase):
    def test_missing_var_with_no_default(self):
        """
        If variable does not exist and no default is given,
        envar should raise an exception.
        """
        self.assertRaises(ImproperlyConfigured, envar, "TOWEL", str)

    # Integers
    def test_missing_int_with_default_int(self):
        self.assertEqual(envar('TOWEL', int, '42'), 42)

    def test_missing_int_with_default_float(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', int, '42.42')

    def test_missing_int_with_default_str(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', int, 'Forty Two')

    # Booleans
    def test_missing_bool_with_default_bool(self):
        self.assertEqual(envar('TOWEL', bool, 'True'), True)

    def test_missing_bool_with_default_str(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', bool, 'Forty Two')

    # Strings
    def test_missing_str_with_default_str(self):
        self.assertEqual(envar('TOWEL', str, 'here'), 'here')

    def test_missing_str_with_default_int(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', str, '42')

    def test_missing_str_with_default_bool(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', str, 'True')

    # Tuples
    def test_missing_tuple_with_default_tuple(self):
        self.assertEqual(envar('TOWEL', tuple, '("forty","two")'), ('forty', 'two'))

    def test_missing_tuple_with_default_tuple_without_parens(self):
        self.assertEqual(envar('TOWEL', tuple, '"forty","two"'), ('forty', 'two'))

if __name__ == '__main__':
    unittest.main()
