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
from pulpcore.client.pulpcore.api.importers_pulp_api import ImportersPulpApi  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException


class TestImportersPulpApi(unittest.TestCase):
    """ImportersPulpApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulpcore.api.importers_pulp_api.ImportersPulpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create a pulp importer  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a pulp importer  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List pulp importers  # noqa: E501
        """
        pass

    def test_partial_update(self):
        """Test case for partial_update

        Update a pulp importer  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a pulp importer  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update a pulp importer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
