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


class PulpImportCheck(object):
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
        'path': 'str',
        'toc': 'str',
        'repo_mapping': 'str'
    }

    attribute_map = {
        'path': 'path',
        'toc': 'toc',
        'repo_mapping': 'repo_mapping'
    }

    def __init__(self, path=None, toc=None, repo_mapping=None, local_vars_configuration=None):  # noqa: E501
        """PulpImportCheck - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._toc = None
        self._repo_mapping = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if toc is not None:
            self.toc = toc
        if repo_mapping is not None:
            self.repo_mapping = repo_mapping

    @property
    def path(self):
        """Gets the path of this PulpImportCheck.  # noqa: E501

        Path to export-tar-gz that will be imported.  # noqa: E501

        :return: The path of this PulpImportCheck.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PulpImportCheck.

        Path to export-tar-gz that will be imported.  # noqa: E501

        :param path: The path of this PulpImportCheck.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def toc(self):
        """Gets the toc of this PulpImportCheck.  # noqa: E501

        Path to a table-of-contents file describing chunks to be validated, reassembled, and imported.  # noqa: E501

        :return: The toc of this PulpImportCheck.  # noqa: E501
        :rtype: str
        """
        return self._toc

    @toc.setter
    def toc(self, toc):
        """Sets the toc of this PulpImportCheck.

        Path to a table-of-contents file describing chunks to be validated, reassembled, and imported.  # noqa: E501

        :param toc: The toc of this PulpImportCheck.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                toc is not None and len(toc) < 1):
            raise ValueError("Invalid value for `toc`, length must be greater than or equal to `1`")  # noqa: E501

        self._toc = toc

    @property
    def repo_mapping(self):
        """Gets the repo_mapping of this PulpImportCheck.  # noqa: E501

        Mapping of repo names in an export file to the repo names in Pulp. For example, if the export has a repo named 'foo' and the repo to import content into was 'bar', the mapping would be \"{'foo': 'bar'}\".  # noqa: E501

        :return: The repo_mapping of this PulpImportCheck.  # noqa: E501
        :rtype: str
        """
        return self._repo_mapping

    @repo_mapping.setter
    def repo_mapping(self, repo_mapping):
        """Sets the repo_mapping of this PulpImportCheck.

        Mapping of repo names in an export file to the repo names in Pulp. For example, if the export has a repo named 'foo' and the repo to import content into was 'bar', the mapping would be \"{'foo': 'bar'}\".  # noqa: E501

        :param repo_mapping: The repo_mapping of this PulpImportCheck.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                repo_mapping is not None and len(repo_mapping) < 1):
            raise ValueError("Invalid value for `repo_mapping`, length must be greater than or equal to `1`")  # noqa: E501

        self._repo_mapping = repo_mapping

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
        if not isinstance(other, PulpImportCheck):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PulpImportCheck):
            return True

        return self.to_dict() != other.to_dict()
