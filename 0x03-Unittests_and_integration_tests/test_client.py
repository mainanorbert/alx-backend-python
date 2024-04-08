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

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org: str) -> None:
        """Define a known payload for org"""
        mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/testorg/repos"
                }
        client = GithubOrgClient('testorg')
        self.assertEqual(client._public_repos_url, "https://api.github.com/orgs/testorg/repos")


if __name__ == "__main__":
    unittest.main()
