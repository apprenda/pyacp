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


class Component(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, component_type=None, component_name=None, component_id=None, component_alias=None, version_alias=None, application_alias=None, version=None, workloads=None, href=None):
        """
        Component - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'component_type': 'str',
            'component_name': 'str',
            'component_id': 'str',
            'component_alias': 'str',
            'version_alias': 'str',
            'application_alias': 'str',
            'version': 'ApprendaUtilityRestAPICommonResourcesResourceBase',
            'workloads': 'ApprendaUtilityRestAPICommonResourcesResourceBase',
            'href': 'str'
        }

        self.attribute_map = {
            'component_type': 'componentType',
            'component_name': 'componentName',
            'component_id': 'componentId',
            'component_alias': 'componentAlias',
            'version_alias': 'versionAlias',
            'application_alias': 'applicationAlias',
            'version': 'version',
            'workloads': 'workloads',
            'href': 'href'
        }

        self._component_type = component_type
        self._component_name = component_name
        self._component_id = component_id
        self._component_alias = component_alias
        self._version_alias = version_alias
        self._application_alias = application_alias
        self._version = version
        self._workloads = workloads
        self._href = href

    @property
    def component_type(self):
        """
        Gets the component_type of this Component.

        :return: The component_type of this Component.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this Component.

        :param component_type: The component_type of this Component.
        :type: str
        """
        allowed_values = ["UserInterface", "Database", "WcfService", "LinuxService", "JavaWebApplication", "WindowsService"]
        if component_type not in allowed_values:
            raise ValueError(
                "Invalid value for `component_type` ({0}), must be one of {1}"
                .format(component_type, allowed_values)
            )

        self._component_type = component_type

    @property
    def component_name(self):
        """
        Gets the component_name of this Component.

        :return: The component_name of this Component.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """
        Sets the component_name of this Component.

        :param component_name: The component_name of this Component.
        :type: str
        """

        self._component_name = component_name

    @property
    def component_id(self):
        """
        Gets the component_id of this Component.

        :return: The component_id of this Component.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """
        Sets the component_id of this Component.

        :param component_id: The component_id of this Component.
        :type: str
        """

        self._component_id = component_id

    @property
    def component_alias(self):
        """
        Gets the component_alias of this Component.

        :return: The component_alias of this Component.
        :rtype: str
        """
        return self._component_alias

    @component_alias.setter
    def component_alias(self, component_alias):
        """
        Sets the component_alias of this Component.

        :param component_alias: The component_alias of this Component.
        :type: str
        """

        self._component_alias = component_alias

    @property
    def version_alias(self):
        """
        Gets the version_alias of this Component.

        :return: The version_alias of this Component.
        :rtype: str
        """
        return self._version_alias

    @version_alias.setter
    def version_alias(self, version_alias):
        """
        Sets the version_alias of this Component.

        :param version_alias: The version_alias of this Component.
        :type: str
        """

        self._version_alias = version_alias

    @property
    def application_alias(self):
        """
        Gets the application_alias of this Component.

        :return: The application_alias of this Component.
        :rtype: str
        """
        return self._application_alias

    @application_alias.setter
    def application_alias(self, application_alias):
        """
        Sets the application_alias of this Component.

        :param application_alias: The application_alias of this Component.
        :type: str
        """

        self._application_alias = application_alias

    @property
    def version(self):
        """
        Gets the version of this Component.

        :return: The version of this Component.
        :rtype: ApprendaUtilityRestAPICommonResourcesResourceBase
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this Component.

        :param version: The version of this Component.
        :type: ApprendaUtilityRestAPICommonResourcesResourceBase
        """

        self._version = version

    @property
    def workloads(self):
        """
        Gets the workloads of this Component.

        :return: The workloads of this Component.
        :rtype: ApprendaUtilityRestAPICommonResourcesResourceBase
        """
        return self._workloads

    @workloads.setter
    def workloads(self, workloads):
        """
        Sets the workloads of this Component.

        :param workloads: The workloads of this Component.
        :type: ApprendaUtilityRestAPICommonResourcesResourceBase
        """

        self._workloads = workloads

    @property
    def href(self):
        """
        Gets the href of this Component.

        :return: The href of this Component.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this Component.

        :param href: The href of this Component.
        :type: str
        """

        self._href = href

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
        if not isinstance(other, Component):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
