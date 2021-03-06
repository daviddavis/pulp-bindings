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
import datetime

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.models.group_response import GroupResponse  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestGroupResponse(unittest.TestCase):
    """GroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test GroupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.group_response.GroupResponse()  # noqa: E501
        if include_optional :
            return GroupResponse(
                name = '0', 
                pulp_href = '0', 
                id = 56
            )
        else :
            return GroupResponse(
                name = '0',
        )

    def testGroupResponse(self):
        """Test GroupResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
