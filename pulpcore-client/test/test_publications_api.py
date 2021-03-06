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
from pulpcore.client.pulpcore.api.publications_api import PublicationsApi  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException


class TestPublicationsApi(unittest.TestCase):
    """PublicationsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulpcore.api.publications_api.PublicationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list(self):
        """Test case for list

        List publications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
