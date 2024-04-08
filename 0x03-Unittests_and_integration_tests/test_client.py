#!/usr/bin/env python3
"""module for Parameterize and patch as decorators"""

from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Parameterize and patch as decorators"""
    @parameterized.expand([
        ('google',),
        ('abc',),
        ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mocked_func: MagicMock) -> None:
        """testing GithubOrgClient respons"""
        client = GithubOrgClient(org_name)
        client.arg()
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}')


if __name__ == "__main__":
    unittest.main()
