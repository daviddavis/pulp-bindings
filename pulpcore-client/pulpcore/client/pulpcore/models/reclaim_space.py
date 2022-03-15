# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class ReclaimSpace(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'repo_hrefs': 'list[object]',
        'repo_versions_keeplist': 'list[str]'
    }

    attribute_map = {
        'repo_hrefs': 'repo_hrefs',
        'repo_versions_keeplist': 'repo_versions_keeplist'
    }

    def __init__(self, repo_hrefs=None, repo_versions_keeplist=None, local_vars_configuration=None):  # noqa: E501
        """ReclaimSpace - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._repo_hrefs = None
        self._repo_versions_keeplist = None
        self.discriminator = None

        self.repo_hrefs = repo_hrefs
        if repo_versions_keeplist is not None:
            self.repo_versions_keeplist = repo_versions_keeplist

    @property
    def repo_hrefs(self):
        """Gets the repo_hrefs of this ReclaimSpace.  # noqa: E501

        Will reclaim space for the specified list of repos.  # noqa: E501

        :return: The repo_hrefs of this ReclaimSpace.  # noqa: E501
        :rtype: list[object]
        """
        return self._repo_hrefs

    @repo_hrefs.setter
    def repo_hrefs(self, repo_hrefs):
        """Sets the repo_hrefs of this ReclaimSpace.

        Will reclaim space for the specified list of repos.  # noqa: E501

        :param repo_hrefs: The repo_hrefs of this ReclaimSpace.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and repo_hrefs is None:  # noqa: E501
            raise ValueError("Invalid value for `repo_hrefs`, must not be `None`")  # noqa: E501

        self._repo_hrefs = repo_hrefs

    @property
    def repo_versions_keeplist(self):
        """Gets the repo_versions_keeplist of this ReclaimSpace.  # noqa: E501

        Will exclude repo versions from space reclaim.  # noqa: E501

        :return: The repo_versions_keeplist of this ReclaimSpace.  # noqa: E501
        :rtype: list[str]
        """
        return self._repo_versions_keeplist

    @repo_versions_keeplist.setter
    def repo_versions_keeplist(self, repo_versions_keeplist):
        """Sets the repo_versions_keeplist of this ReclaimSpace.

        Will exclude repo versions from space reclaim.  # noqa: E501

        :param repo_versions_keeplist: The repo_versions_keeplist of this ReclaimSpace.  # noqa: E501
        :type: list[str]
        """

        self._repo_versions_keeplist = repo_versions_keeplist

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReclaimSpace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReclaimSpace):
            return True

        return self.to_dict() != other.to_dict()
