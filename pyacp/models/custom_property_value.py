# coding: utf-8

"""
    Platform Operations Rest API

    The Platform Operations REST API can be leveraged to customize the Platform Operator experience of managing infrastructure and applications for the Apprenda Platform. This allows some of the functionality of the Platform's System Operations Center (SOC) to be accomplished through a variety of means such as custom-built UX or command-line interfaces.   For more information about the abilities of Platform Operators, see our documentation on the [SOC](/current/SOC).   ##Authentication   Before making a request, you must be authenticated. Learn how to [get authenticated](/restapi/platformops/v1/authentication).   ##Making a Request   ###Prerequisites   * Installed Platform of version 6.5.1 or later (Note that most endpoints are only available in version 6.7.0 and later)    * Authentication token   * If SOC authorization is enabled on your Platform, you must be assigned as an active Platform Operator   ###Request URL   All requests must use **https**.   The URL for every request you make is the Cloud URI of your Platform followed by \"/soc\" and the path structure of the endpoint. For example, if your Cloud URI is apps.apprenda.harp and you want to get the Add-ons for your Platform, the request URI will be **apps.apprenda.harp/soc/api/v1/addons**.   For more information, see our documentation on [using API resources](/restapi/platformops/v1/using-resources) and [finding your Cloud URI](/current/clouduri).   ###Request Headers   Your authenication token must be passed in the header of all requests using the key **ApprendaSessionToken** (not case sensitive).  

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CustomPropertyValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, custom_property=None, values=None, allowed_values=None, default_values=None, allows_multiple_values=None, allows_custom_values=None):
        """
        CustomPropertyValue - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'custom_property': 'ApprendaRestAPICommonResourcesResourceBase',
            'values': 'list[str]',
            'allowed_values': 'list[str]',
            'default_values': 'list[str]',
            'allows_multiple_values': 'bool',
            'allows_custom_values': 'bool'
        }

        self.attribute_map = {
            'custom_property': 'customProperty',
            'values': 'values',
            'allowed_values': 'allowedValues',
            'default_values': 'defaultValues',
            'allows_multiple_values': 'allowsMultipleValues',
            'allows_custom_values': 'allowsCustomValues'
        }

        self._custom_property = custom_property
        self._values = values
        self._allowed_values = allowed_values
        self._default_values = default_values
        self._allows_multiple_values = allows_multiple_values
        self._allows_custom_values = allows_custom_values

    @property
    def custom_property(self):
        """
        Gets the custom_property of this CustomPropertyValue.

        :return: The custom_property of this CustomPropertyValue.
        :rtype: ApprendaRestAPICommonResourcesResourceBase
        """
        return self._custom_property

    @custom_property.setter
    def custom_property(self, custom_property):
        """
        Sets the custom_property of this CustomPropertyValue.

        :param custom_property: The custom_property of this CustomPropertyValue.
        :type: ApprendaRestAPICommonResourcesResourceBase
        """

        self._custom_property = custom_property

    @property
    def values(self):
        """
        Gets the values of this CustomPropertyValue.

        :return: The values of this CustomPropertyValue.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this CustomPropertyValue.

        :param values: The values of this CustomPropertyValue.
        :type: list[str]
        """

        self._values = values

    @property
    def allowed_values(self):
        """
        Gets the allowed_values of this CustomPropertyValue.

        :return: The allowed_values of this CustomPropertyValue.
        :rtype: list[str]
        """
        return self._allowed_values

    @allowed_values.setter
    def allowed_values(self, allowed_values):
        """
        Sets the allowed_values of this CustomPropertyValue.

        :param allowed_values: The allowed_values of this CustomPropertyValue.
        :type: list[str]
        """

        self._allowed_values = allowed_values

    @property
    def default_values(self):
        """
        Gets the default_values of this CustomPropertyValue.

        :return: The default_values of this CustomPropertyValue.
        :rtype: list[str]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """
        Sets the default_values of this CustomPropertyValue.

        :param default_values: The default_values of this CustomPropertyValue.
        :type: list[str]
        """

        self._default_values = default_values

    @property
    def allows_multiple_values(self):
        """
        Gets the allows_multiple_values of this CustomPropertyValue.

        :return: The allows_multiple_values of this CustomPropertyValue.
        :rtype: bool
        """
        return self._allows_multiple_values

    @allows_multiple_values.setter
    def allows_multiple_values(self, allows_multiple_values):
        """
        Sets the allows_multiple_values of this CustomPropertyValue.

        :param allows_multiple_values: The allows_multiple_values of this CustomPropertyValue.
        :type: bool
        """

        self._allows_multiple_values = allows_multiple_values

    @property
    def allows_custom_values(self):
        """
        Gets the allows_custom_values of this CustomPropertyValue.

        :return: The allows_custom_values of this CustomPropertyValue.
        :rtype: bool
        """
        return self._allows_custom_values

    @allows_custom_values.setter
    def allows_custom_values(self, allows_custom_values):
        """
        Sets the allows_custom_values of this CustomPropertyValue.

        :param allows_custom_values: The allows_custom_values of this CustomPropertyValue.
        :type: bool
        """

        self._allows_custom_values = allows_custom_values

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, CustomPropertyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other