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


class PatchedPulpExporter(object):
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
        'name': 'str',
        'path': 'str',
        'repositories': 'list[str]',
        'last_export': 'str'
    }

    attribute_map = {
        'name': 'name',
        'path': 'path',
        'repositories': 'repositories',
        'last_export': 'last_export'
    }

    def __init__(self, name=None, path=None, repositories=None, last_export=None, local_vars_configuration=None):  # noqa: E501
        """PatchedPulpExporter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._path = None
        self._repositories = None
        self._last_export = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if repositories is not None:
            self.repositories = repositories
        self.last_export = last_export

    @property
    def name(self):
        """Gets the name of this PatchedPulpExporter.  # noqa: E501

        Unique name of the file system exporter.  # noqa: E501

        :return: The name of this PatchedPulpExporter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedPulpExporter.

        Unique name of the file system exporter.  # noqa: E501

        :param name: The name of this PatchedPulpExporter.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def path(self):
        """Gets the path of this PatchedPulpExporter.  # noqa: E501

        File system directory to store exported tar.gzs.  # noqa: E501

        :return: The path of this PatchedPulpExporter.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PatchedPulpExporter.

        File system directory to store exported tar.gzs.  # noqa: E501

        :param path: The path of this PatchedPulpExporter.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                path is not None and len(path) < 1):
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `1`")  # noqa: E501

        self._path = path

    @property
    def repositories(self):
        """Gets the repositories of this PatchedPulpExporter.  # noqa: E501


        :return: The repositories of this PatchedPulpExporter.  # noqa: E501
        :rtype: list[str]
        """
        return self._repositories

    @repositories.setter
    def repositories(self, repositories):
        """Sets the repositories of this PatchedPulpExporter.


        :param repositories: The repositories of this PatchedPulpExporter.  # noqa: E501
        :type: list[str]
        """

        self._repositories = repositories

    @property
    def last_export(self):
        """Gets the last_export of this PatchedPulpExporter.  # noqa: E501

        Last attempted export for this PulpExporter  # noqa: E501

        :return: The last_export of this PatchedPulpExporter.  # noqa: E501
        :rtype: str
        """
        return self._last_export

    @last_export.setter
    def last_export(self, last_export):
        """Sets the last_export of this PatchedPulpExporter.

        Last attempted export for this PulpExporter  # noqa: E501

        :param last_export: The last_export of this PatchedPulpExporter.  # noqa: E501
        :type: str
        """

        self._last_export = last_export

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
        if not isinstance(other, PatchedPulpExporter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedPulpExporter):
            return True

        return self.to_dict() != other.to_dict()
