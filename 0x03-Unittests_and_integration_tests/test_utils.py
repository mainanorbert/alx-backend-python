#!/usr/bin/env python3
"""a module that Parameterize a unit test"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
        ({}, ["a"], "'a'"),
        ({"a": 1}, ["a", "b"], "'b'")
        ])
    def test_access_nested_map_exception(self, data, path, err_message):
        """Parameterize a unit test"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(data, path)
        self.assertEqual(str(context.exception), f"KeyError({err_message})")


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""
    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, payload, mock_get):
        """mock test for json"""
        mock_res = Mock()
        mock_res.json.return_value = payload
        mock_res.return_value = mock_res
        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
