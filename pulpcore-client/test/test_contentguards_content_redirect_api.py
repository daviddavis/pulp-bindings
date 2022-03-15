# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.api.contentguards_content_redirect_api import ContentguardsContentRedirectApi  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException


class TestContentguardsContentRedirectApi(unittest.TestCase):
    """ContentguardsContentRedirectApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulpcore.api.contentguards_content_redirect_api.ContentguardsContentRedirectApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create a content redirect content guard  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a content redirect content guard  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List content redirect content guards  # noqa: E501
        """
        pass

    def test_partial_update(self):
        """Test case for partial_update

        Update a content redirect content guard  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a content redirect content guard  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update a content redirect content guard  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
