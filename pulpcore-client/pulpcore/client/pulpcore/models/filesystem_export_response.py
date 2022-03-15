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


class FilesystemExportResponse(object):
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
        'pulp_href': 'str',
        'pulp_created': 'datetime',
        'task': 'str',
        'exported_resources': 'list[str]',
        'params': 'object'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'task': 'task',
        'exported_resources': 'exported_resources',
        'params': 'params'
    }

    def __init__(self, pulp_href=None, pulp_created=None, task=None, exported_resources=None, params=None, local_vars_configuration=None):  # noqa: E501
        """FilesystemExportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._task = None
        self._exported_resources = None
        self._params = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.task = task
        if exported_resources is not None:
            self.exported_resources = exported_resources
        if params is not None:
            self.params = params

    @property
    def pulp_href(self):
        """Gets the pulp_href of this FilesystemExportResponse.  # noqa: E501


        :return: The pulp_href of this FilesystemExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this FilesystemExportResponse.


        :param pulp_href: The pulp_href of this FilesystemExportResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this FilesystemExportResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this FilesystemExportResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this FilesystemExportResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this FilesystemExportResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def task(self):
        """Gets the task of this FilesystemExportResponse.  # noqa: E501

        A URI of the task that ran the Export.  # noqa: E501

        :return: The task of this FilesystemExportResponse.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this FilesystemExportResponse.

        A URI of the task that ran the Export.  # noqa: E501

        :param task: The task of this FilesystemExportResponse.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def exported_resources(self):
        """Gets the exported_resources of this FilesystemExportResponse.  # noqa: E501

        Resources that were exported.  # noqa: E501

        :return: The exported_resources of this FilesystemExportResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._exported_resources

    @exported_resources.setter
    def exported_resources(self, exported_resources):
        """Sets the exported_resources of this FilesystemExportResponse.

        Resources that were exported.  # noqa: E501

        :param exported_resources: The exported_resources of this FilesystemExportResponse.  # noqa: E501
        :type: list[str]
        """

        self._exported_resources = exported_resources

    @property
    def params(self):
        """Gets the params of this FilesystemExportResponse.  # noqa: E501

        Any additional parameters that were used to create the export.  # noqa: E501

        :return: The params of this FilesystemExportResponse.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this FilesystemExportResponse.

        Any additional parameters that were used to create the export.  # noqa: E501

        :param params: The params of this FilesystemExportResponse.  # noqa: E501
        :type: object
        """

        self._params = params

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
        if not isinstance(other, FilesystemExportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilesystemExportResponse):
            return True

        return self.to_dict() != other.to_dict()
