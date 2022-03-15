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

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.api.rpm_copy_api import RpmCopyApi  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException


class TestRpmCopyApi(unittest.TestCase):
    """RpmCopyApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_rpm.api.rpm_copy_api.RpmCopyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_content(self):
        """Test case for copy_content

        Copy content  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()