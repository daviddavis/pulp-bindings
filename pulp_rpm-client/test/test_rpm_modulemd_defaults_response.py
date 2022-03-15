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

import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.models.rpm_modulemd_defaults_response import RpmModulemdDefaultsResponse  # noqa: E501
from pulpcore.client.pulp_rpm.rest import ApiException

class TestRpmModulemdDefaultsResponse(unittest.TestCase):
    """RpmModulemdDefaultsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RpmModulemdDefaultsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_rpm.models.rpm_modulemd_defaults_response.RpmModulemdDefaultsResponse()  # noqa: E501
        if include_optional :
            return RpmModulemdDefaultsResponse(
                pulp_href = '0', 
                pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                md5 = '0', 
                sha1 = '0', 
                sha224 = '0', 
                sha256 = '0', 
                sha384 = '0', 
                sha512 = '0', 
                artifact = '0', 
                module = '0', 
                stream = '0', 
                profiles = pulpcore.client.pulp_rpm.models.profiles.profiles()
            )
        else :
            return RpmModulemdDefaultsResponse(
                module = '0',
                stream = '0',
                profiles = pulpcore.client.pulp_rpm.models.profiles.profiles(),
        )

    def testRpmModulemdDefaultsResponse(self):
        """Test RpmModulemdDefaultsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
