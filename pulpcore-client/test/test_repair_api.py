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
from pulpcore.client.pulpcore.api.repair_api import RepairApi  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException


class TestRepairApi(unittest.TestCase):
    """RepairApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulpcore.api.repair_api.RepairApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post(self):
        """Test case for post

        Repair Artifact Storage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
