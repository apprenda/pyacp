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


class ResourceAllocationReport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allocated_cpu=None, allocated_memory=None, allocated_storage=None):
        """
        ResourceAllocationReport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allocated_cpu': 'float',
            'allocated_memory': 'float',
            'allocated_storage': 'float'
        }

        self.attribute_map = {
            'allocated_cpu': 'allocatedCpu',
            'allocated_memory': 'allocatedMemory',
            'allocated_storage': 'allocatedStorage'
        }

        self._allocated_cpu = allocated_cpu
        self._allocated_memory = allocated_memory
        self._allocated_storage = allocated_storage

    @property
    def allocated_cpu(self):
        """
        Gets the allocated_cpu of this ResourceAllocationReport.

        :return: The allocated_cpu of this ResourceAllocationReport.
        :rtype: float
        """
        return self._allocated_cpu

    @allocated_cpu.setter
    def allocated_cpu(self, allocated_cpu):
        """
        Sets the allocated_cpu of this ResourceAllocationReport.

        :param allocated_cpu: The allocated_cpu of this ResourceAllocationReport.
        :type: float
        """

        self._allocated_cpu = allocated_cpu

    @property
    def allocated_memory(self):
        """
        Gets the allocated_memory of this ResourceAllocationReport.

        :return: The allocated_memory of this ResourceAllocationReport.
        :rtype: float
        """
        return self._allocated_memory

    @allocated_memory.setter
    def allocated_memory(self, allocated_memory):
        """
        Sets the allocated_memory of this ResourceAllocationReport.

        :param allocated_memory: The allocated_memory of this ResourceAllocationReport.
        :type: float
        """

        self._allocated_memory = allocated_memory

    @property
    def allocated_storage(self):
        """
        Gets the allocated_storage of this ResourceAllocationReport.

        :return: The allocated_storage of this ResourceAllocationReport.
        :rtype: float
        """
        return self._allocated_storage

    @allocated_storage.setter
    def allocated_storage(self, allocated_storage):
        """
        Sets the allocated_storage of this ResourceAllocationReport.

        :param allocated_storage: The allocated_storage of this ResourceAllocationReport.
        :type: float
        """

        self._allocated_storage = allocated_storage

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
        if not isinstance(other, ResourceAllocationReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
