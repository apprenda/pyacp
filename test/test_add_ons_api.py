# coding: utf-8

"""
    Platform Operations Rest API

    The Platform Operations REST API can be leveraged to customize the Platform Operator experience of managing infrastructure and applications for the Apprenda Platform. This allows some of the functionality of the Platform's System Operations Center (SOC) to be accomplished through a variety of means such as custom-built UX or command-line interfaces.   For more information about the abilities of Platform Operators, see our documentation on the [SOC](/current/SOC).   ##Authentication   Before making a request, you must be authenticated. Learn how to [get authenticated](/restapi/platformops/v1/authentication).   ##Making a Request   ###Prerequisites   * Installed Platform of version 6.5.1 or later (Note that most endpoints are only available in version 6.7.0 and later)    * Authentication token   * If SOC authorization is enabled on your Platform, you must be assigned as an active Platform Operator   ###Request URL   All requests must use **https**.   The URL for every request you make is the Cloud URI of your Platform followed by \"/soc\" and the path structure of the endpoint. For example, if your Cloud URI is apps.apprenda.harp and you want to get the Add-ons for your Platform, the request URI will be **apps.apprenda.harp/soc/api/v1/addons**.   For more information, see our documentation on [using API resources](/restapi/platformops/v1/using-resources) and [finding your Cloud URI](/current/clouduri).   ###Request Headers   Your authenication token must be passed in the header of all requests using the key **ApprendaSessionToken** (not case sensitive).  

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import pyacp
from pyacp.rest import ApiException
from pyacp.apis.add_ons_api import AddOnsApi


class TestAddOnsApi(unittest.TestCase):
    """ AddOnsApi unit test stubs """

    def setUp(self):
        self.api = pyacp.apis.add_ons_api.AddOnsApi()

    def tearDown(self):
        pass

    def test_add_add_on(self):
        """
        Test case for add_add_on

        Create Add-On
        """
        pass

    def test_add_on_get(self):
        """
        Test case for add_on_get

        Get all Add-Ons
        """
        pass

    def test_add_on_get_by_name(self):
        """
        Test case for add_on_get_by_name

        Get Add-On
        """
        pass

    def test_remove_add_on(self):
        """
        Test case for remove_add_on

        Delete Add-On
        """
        pass


if __name__ == '__main__':
    unittest.main()
