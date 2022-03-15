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

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmPackageGroupResponse(object):
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
        'id': 'str',
        'default': 'bool',
        'user_visible': 'bool',
        'display_order': 'int',
        'name': 'str',
        'description': 'str',
        'packages': 'object',
        'biarch_only': 'bool',
        'desc_by_lang': 'object',
        'name_by_lang': 'object',
        'digest': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'id': 'id',
        'default': 'default',
        'user_visible': 'user_visible',
        'display_order': 'display_order',
        'name': 'name',
        'description': 'description',
        'packages': 'packages',
        'biarch_only': 'biarch_only',
        'desc_by_lang': 'desc_by_lang',
        'name_by_lang': 'name_by_lang',
        'digest': 'digest'
    }

    def __init__(self, pulp_href=None, pulp_created=None, id=None, default=None, user_visible=None, display_order=None, name=None, description=None, packages=None, biarch_only=None, desc_by_lang=None, name_by_lang=None, digest=None, local_vars_configuration=None):  # noqa: E501
        """RpmPackageGroupResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._id = None
        self._default = None
        self._user_visible = None
        self._display_order = None
        self._name = None
        self._description = None
        self._packages = None
        self._biarch_only = None
        self._desc_by_lang = None
        self._name_by_lang = None
        self._digest = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        self.id = id
        if default is not None:
            self.default = default
        if user_visible is not None:
            self.user_visible = user_visible
        self.display_order = display_order
        self.name = name
        self.description = description
        self.packages = packages
        if biarch_only is not None:
            self.biarch_only = biarch_only
        self.desc_by_lang = desc_by_lang
        self.name_by_lang = name_by_lang
        self.digest = digest

    @property
    def pulp_href(self):
        """Gets the pulp_href of this RpmPackageGroupResponse.  # noqa: E501


        :return: The pulp_href of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this RpmPackageGroupResponse.


        :param pulp_href: The pulp_href of this RpmPackageGroupResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this RpmPackageGroupResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this RpmPackageGroupResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this RpmPackageGroupResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def id(self):
        """Gets the id of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup id.  # noqa: E501

        :return: The id of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RpmPackageGroupResponse.

        PackageGroup id.  # noqa: E501

        :param id: The id of this RpmPackageGroupResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def default(self):
        """Gets the default of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup default.  # noqa: E501

        :return: The default of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this RpmPackageGroupResponse.

        PackageGroup default.  # noqa: E501

        :param default: The default of this RpmPackageGroupResponse.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def user_visible(self):
        """Gets the user_visible of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup user visibility.  # noqa: E501

        :return: The user_visible of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._user_visible

    @user_visible.setter
    def user_visible(self, user_visible):
        """Sets the user_visible of this RpmPackageGroupResponse.

        PackageGroup user visibility.  # noqa: E501

        :param user_visible: The user_visible of this RpmPackageGroupResponse.  # noqa: E501
        :type: bool
        """

        self._user_visible = user_visible

    @property
    def display_order(self):
        """Gets the display_order of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup display order.  # noqa: E501

        :return: The display_order of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this RpmPackageGroupResponse.

        PackageGroup display order.  # noqa: E501

        :param display_order: The display_order of this RpmPackageGroupResponse.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def name(self):
        """Gets the name of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup name.  # noqa: E501

        :return: The name of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RpmPackageGroupResponse.

        PackageGroup name.  # noqa: E501

        :param name: The name of this RpmPackageGroupResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup description.  # noqa: E501

        :return: The description of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RpmPackageGroupResponse.

        PackageGroup description.  # noqa: E501

        :param description: The description of this RpmPackageGroupResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def packages(self):
        """Gets the packages of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup package list.  # noqa: E501

        :return: The packages of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: object
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this RpmPackageGroupResponse.

        PackageGroup package list.  # noqa: E501

        :param packages: The packages of this RpmPackageGroupResponse.  # noqa: E501
        :type: object
        """

        self._packages = packages

    @property
    def biarch_only(self):
        """Gets the biarch_only of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup biarch only.  # noqa: E501

        :return: The biarch_only of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._biarch_only

    @biarch_only.setter
    def biarch_only(self, biarch_only):
        """Sets the biarch_only of this RpmPackageGroupResponse.

        PackageGroup biarch only.  # noqa: E501

        :param biarch_only: The biarch_only of this RpmPackageGroupResponse.  # noqa: E501
        :type: bool
        """

        self._biarch_only = biarch_only

    @property
    def desc_by_lang(self):
        """Gets the desc_by_lang of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup description by language.  # noqa: E501

        :return: The desc_by_lang of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: object
        """
        return self._desc_by_lang

    @desc_by_lang.setter
    def desc_by_lang(self, desc_by_lang):
        """Sets the desc_by_lang of this RpmPackageGroupResponse.

        PackageGroup description by language.  # noqa: E501

        :param desc_by_lang: The desc_by_lang of this RpmPackageGroupResponse.  # noqa: E501
        :type: object
        """

        self._desc_by_lang = desc_by_lang

    @property
    def name_by_lang(self):
        """Gets the name_by_lang of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup name by language.  # noqa: E501

        :return: The name_by_lang of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: object
        """
        return self._name_by_lang

    @name_by_lang.setter
    def name_by_lang(self, name_by_lang):
        """Sets the name_by_lang of this RpmPackageGroupResponse.

        PackageGroup name by language.  # noqa: E501

        :param name_by_lang: The name_by_lang of this RpmPackageGroupResponse.  # noqa: E501
        :type: object
        """

        self._name_by_lang = name_by_lang

    @property
    def digest(self):
        """Gets the digest of this RpmPackageGroupResponse.  # noqa: E501

        PackageGroup digest.  # noqa: E501

        :return: The digest of this RpmPackageGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this RpmPackageGroupResponse.

        PackageGroup digest.  # noqa: E501

        :param digest: The digest of this RpmPackageGroupResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

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
        if not isinstance(other, RpmPackageGroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmPackageGroupResponse):
            return True

        return self.to_dict() != other.to_dict()
