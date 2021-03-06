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


class ProgressReportResponse(object):
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
        'message': 'str',
        'code': 'str',
        'state': 'str',
        'total': 'int',
        'done': 'int',
        'suffix': 'str'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'state': 'state',
        'total': 'total',
        'done': 'done',
        'suffix': 'suffix'
    }

    def __init__(self, message=None, code=None, state=None, total=None, done=None, suffix=None, local_vars_configuration=None):  # noqa: E501
        """ProgressReportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._code = None
        self._state = None
        self._total = None
        self._done = None
        self._suffix = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if state is not None:
            self.state = state
        if total is not None:
            self.total = total
        if done is not None:
            self.done = done
        self.suffix = suffix

    @property
    def message(self):
        """Gets the message of this ProgressReportResponse.  # noqa: E501

        The message shown to the user for the progress report.  # noqa: E501

        :return: The message of this ProgressReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ProgressReportResponse.

        The message shown to the user for the progress report.  # noqa: E501

        :param message: The message of this ProgressReportResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """Gets the code of this ProgressReportResponse.  # noqa: E501

        Identifies the type of progress report'.  # noqa: E501

        :return: The code of this ProgressReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ProgressReportResponse.

        Identifies the type of progress report'.  # noqa: E501

        :param code: The code of this ProgressReportResponse.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def state(self):
        """Gets the state of this ProgressReportResponse.  # noqa: E501

        The current state of the progress report. The possible values are: 'waiting', 'skipped', 'running', 'completed', 'failed', 'canceled' and 'canceling'. The default is 'waiting'.  # noqa: E501

        :return: The state of this ProgressReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProgressReportResponse.

        The current state of the progress report. The possible values are: 'waiting', 'skipped', 'running', 'completed', 'failed', 'canceled' and 'canceling'. The default is 'waiting'.  # noqa: E501

        :param state: The state of this ProgressReportResponse.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def total(self):
        """Gets the total of this ProgressReportResponse.  # noqa: E501

        The total count of items.  # noqa: E501

        :return: The total of this ProgressReportResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProgressReportResponse.

        The total count of items.  # noqa: E501

        :param total: The total of this ProgressReportResponse.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def done(self):
        """Gets the done of this ProgressReportResponse.  # noqa: E501

        The count of items already processed. Defaults to 0.  # noqa: E501

        :return: The done of this ProgressReportResponse.  # noqa: E501
        :rtype: int
        """
        return self._done

    @done.setter
    def done(self, done):
        """Sets the done of this ProgressReportResponse.

        The count of items already processed. Defaults to 0.  # noqa: E501

        :param done: The done of this ProgressReportResponse.  # noqa: E501
        :type: int
        """

        self._done = done

    @property
    def suffix(self):
        """Gets the suffix of this ProgressReportResponse.  # noqa: E501

        The suffix to be shown with the progress report.  # noqa: E501

        :return: The suffix of this ProgressReportResponse.  # noqa: E501
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """Sets the suffix of this ProgressReportResponse.

        The suffix to be shown with the progress report.  # noqa: E501

        :param suffix: The suffix of this ProgressReportResponse.  # noqa: E501
        :type: str
        """

        self._suffix = suffix

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
        if not isinstance(other, ProgressReportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProgressReportResponse):
            return True

        return self.to_dict() != other.to_dict()
