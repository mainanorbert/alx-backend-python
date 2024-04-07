#!/usr/bin/env python3
"""a module that Parameterize a unit test"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """class that implements Parameterize a unit test"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
        ])
    def test_access_nested_map(self, data, path, result):
        """testing_access_nested_map functin"""
        self.assertEqual(access_nested_map(data, path), result)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
        ])
    def test_access_nested_map(self, data, path, err_message):
        """Parameterize a unit test"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(data, path)
        self.assertEqual(str(context.exception), err_message)


if __name__ == "__main__":
    unittest.main()
