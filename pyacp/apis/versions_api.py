# coding: utf-8

"""
    Platform Operations Rest API

    The Platform Operations REST API can be leveraged to customize the Platform Operator experience of managing infrastructure and applications for the Apprenda Platform. This allows some of the functionality of the Platform's System Operations Center (SOC) to be accomplished through a variety of means such as custom-built UX or command-line interfaces.   For more information about the abilities of Platform Operators, see our documentation on the [SOC](/current/SOC).   ##Authentication   Before making a request, you must be authenticated. Learn how to [get authenticated](/restapi/platformops/v1/authentication).   ##Making a Request   ###Prerequisites   * Installed Platform of version 6.5.1 or later (Note that most endpoints are only available in version 6.7.0 and later)    * Authentication token   * If SOC authorization is enabled on your Platform, you must be assigned as an active Platform Operator   ###Request URL   All requests must use **https**.   The URL for every request you make is the Cloud URI of your Platform followed by \"/soc\" and the path structure of the endpoint. For example, if your Cloud URI is apps.apprenda.harp and you want to get the Add-ons for your Platform, the request URI will be **apps.apprenda.harp/soc/api/v1/addons**.   For more information, see our documentation on [using API resources](/restapi/platformops/v1/using-resources) and [finding your Cloud URI](/current/clouduri).   ###Request Headers   Your authenication token must be passed in the header of all requests using the key **ApprendaSessionToken** (not case sensitive).  

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class VersionsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def api_v1_applications_app_alias_versions_get(self, app_alias, **kwargs):
        """
        Get an application
        **Requires Platform version 6.7.0 or later.**   Returns all versions of an application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_applications_app_alias_versions_get(app_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of the application (required)
        :return: ApprendaRestAPICommonResourcesPagedResourceBaseVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.api_v1_applications_app_alias_versions_get_with_http_info(app_alias, **kwargs)
        else:
            (data) = self.api_v1_applications_app_alias_versions_get_with_http_info(app_alias, **kwargs)
            return data

    def api_v1_applications_app_alias_versions_get_with_http_info(self, app_alias, **kwargs):
        """
        Get an application
        **Requires Platform version 6.7.0 or later.**   Returns all versions of an application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_applications_app_alias_versions_get_with_http_info(app_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of the application (required)
        :return: ApprendaRestAPICommonResourcesPagedResourceBaseVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_alias']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_applications_app_alias_versions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `api_v1_applications_app_alias_versions_get`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}/versions'.replace('{format}', 'json')
        path_params = {}
        if 'app_alias' in params:
            path_params['appAlias'] = params['app_alias']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApprendaRestAPICommonResourcesPagedResourceBaseVersion',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def api_v1_applications_app_alias_versions_version_alias_get(self, app_alias, version_alias, **kwargs):
        """
        Get an application version
        **Requires Platform version 6.7.0 or later.**   Returns a version of an application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_applications_app_alias_versions_version_alias_get(app_alias, version_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of the application (required)
        :param str version_alias: Required. Alias of version (required)
        :return: Version
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.api_v1_applications_app_alias_versions_version_alias_get_with_http_info(app_alias, version_alias, **kwargs)
        else:
            (data) = self.api_v1_applications_app_alias_versions_version_alias_get_with_http_info(app_alias, version_alias, **kwargs)
            return data

    def api_v1_applications_app_alias_versions_version_alias_get_with_http_info(self, app_alias, version_alias, **kwargs):
        """
        Get an application version
        **Requires Platform version 6.7.0 or later.**   Returns a version of an application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.api_v1_applications_app_alias_versions_version_alias_get_with_http_info(app_alias, version_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of the application (required)
        :param str version_alias: Required. Alias of version (required)
        :return: Version
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_alias', 'version_alias']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_applications_app_alias_versions_version_alias_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `api_v1_applications_app_alias_versions_version_alias_get`")
        # verify the required parameter 'version_alias' is set
        if ('version_alias' not in params) or (params['version_alias'] is None):
            raise ValueError("Missing the required parameter `version_alias` when calling `api_v1_applications_app_alias_versions_version_alias_get`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}/versions/{versionAlias}'.replace('{format}', 'json')
        path_params = {}
        if 'app_alias' in params:
            path_params['appAlias'] = params['app_alias']
        if 'version_alias' in params:
            path_params['versionAlias'] = params['version_alias']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Version',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
