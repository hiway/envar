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
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', str)

    def test_env_var_available_with_no_default(self):
        os.environ['LEWOT'] = '42'
        self.assertEqual(envar('LEWOT', int), 42)

    def test_env_var_available_with_default(self):
        os.environ['LEWOT'] = '42'
        self.assertEqual(envar('LEWOT', int, '24'), 42)

    def test_env_var_available_with_default_verbose(self):
        os.environ['LEWOT'] = '42'
        self.assertEqual(envar('LEWOT', int, '24', verbose=True), 42)
        #todo: check for warning

    # Integers
    def test_missing_int_with_default_int(self):
        self.assertEqual(envar('TOWEL', int, '42'), 42)

    def test_missing_int_with_default_float(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', int, '42.42')

    def test_missing_int_with_default_str(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', int, 'Forty Two')

    def test_missing_int_with_default_bool(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', int, 'True')

    # Booleans
    def test_missing_bool_with_default_bool(self):
        self.assertEqual(envar('TOWEL', bool, 'True'), True)

    def test_missing_bool_with_default_str(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', bool, 'Forty Two')

    def test_missing_bool_with_default_int(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', bool, '42')

    def test_missing_bool_with_default_float(self):
        self.assertRaises(ImproperlyConfigured, envar, 'TOWEL', bool, '42.42')

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
