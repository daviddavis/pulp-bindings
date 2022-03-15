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
from pulpcore.client.pulpcore.models.paginated_group_response_list import PaginatedGroupResponseList  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException

class TestPaginatedGroupResponseList(unittest.TestCase):
    """PaginatedGroupResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedGroupResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulpcore.models.paginated_group_response_list.PaginatedGroupResponseList()  # noqa: E501
        if include_optional :
            return PaginatedGroupResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulpcore.models.group_response.GroupResponse(
                        name = '0', 
                        pulp_href = '0', 
                        id = 56, )
                    ]
            )
        else :
            return PaginatedGroupResponseList(
        )

    def testPaginatedGroupResponseList(self):
        """Test PaginatedGroupResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
