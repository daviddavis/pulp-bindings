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


class GroupRoleResponse(object):
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
        'role': 'str',
        'content_object': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'role': 'role',
        'content_object': 'content_object'
    }

    def __init__(self, pulp_href=None, pulp_created=None, role=None, content_object=None, local_vars_configuration=None):  # noqa: E501
        """GroupRoleResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._role = None
        self._content_object = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.role = role
        self.content_object = content_object

    @property
    def pulp_href(self):
        """Gets the pulp_href of this GroupRoleResponse.  # noqa: E501


        :return: The pulp_href of this GroupRoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this GroupRoleResponse.


        :param pulp_href: The pulp_href of this GroupRoleResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this GroupRoleResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this GroupRoleResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this GroupRoleResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this GroupRoleResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def role(self):
        """Gets the role of this GroupRoleResponse.  # noqa: E501


        :return: The role of this GroupRoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this GroupRoleResponse.


        :param role: The role of this GroupRoleResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def content_object(self):
        """Gets the content_object of this GroupRoleResponse.  # noqa: E501

        Optional pulp_href of the object the permissions are to be asserted on.  # noqa: E501

        :return: The content_object of this GroupRoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_object

    @content_object.setter
    def content_object(self, content_object):
        """Sets the content_object of this GroupRoleResponse.

        Optional pulp_href of the object the permissions are to be asserted on.  # noqa: E501

        :param content_object: The content_object of this GroupRoleResponse.  # noqa: E501
        :type: str
        """

        self._content_object = content_object

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
        if not isinstance(other, GroupRoleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupRoleResponse):
            return True

        return self.to_dict() != other.to_dict()
