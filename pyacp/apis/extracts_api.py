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


class ExtractsApi(object):
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

    def logs_export(self, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.logs_export(format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: Designates the desired formatting of the log entry extract stream (required)
        :param str search: Search term filter to apply to log entries.
        :param datetime begin: Timestamp of the oldest log entry to consider for extract.
        :param datetime end: Timestamp of the newest log entry to consider for extract.
        :param str version_alias: Version Alias of a specific application version to extract logs from.
        :param str app_alias: Application Alias of a specific application to extract logs from.
        :param bool include_platform: Should platform sourced logs be included in extract.
        :param bool include_guest_apps: Should guest application sourced logs be included in extract.
        :param float rows: Number of rows per page to return in paged output
        :param float page: How many pages of rows should be skipped
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.logs_export_with_http_info(format, **kwargs)
        else:
            (data) = self.logs_export_with_http_info(format, **kwargs)
            return data

    def logs_export_with_http_info(self, format, **kwargs):
        """
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.logs_export_with_http_info(format, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str format: Designates the desired formatting of the log entry extract stream (required)
        :param str search: Search term filter to apply to log entries.
        :param datetime begin: Timestamp of the oldest log entry to consider for extract.
        :param datetime end: Timestamp of the newest log entry to consider for extract.
        :param str version_alias: Version Alias of a specific application version to extract logs from.
        :param str app_alias: Application Alias of a specific application to extract logs from.
        :param bool include_platform: Should platform sourced logs be included in extract.
        :param bool include_guest_apps: Should guest application sourced logs be included in extract.
        :param float rows: Number of rows per page to return in paged output
        :param float page: How many pages of rows should be skipped
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['format', 'search', 'begin', 'end', 'version_alias', 'app_alias', 'include_platform', 'include_guest_apps', 'rows', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logs_export" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'format' is set
        if ('format' not in params) or (params['format'] is None):
            raise ValueError("Missing the required parameter `format` when calling `logs_export`")


        collection_formats = {}

        resource_path = '/api/v1/logs/extract.{format}'.replace('{format}', 'json')
        path_params = {}
        if 'format' in params:
            path_params['format'] = params['format']

        query_params = {}
        if 'search' in params:
            query_params['search'] = params['search']
        if 'begin' in params:
            query_params['begin'] = params['begin']
        if 'end' in params:
            query_params['end'] = params['end']
        if 'version_alias' in params:
            query_params['versionAlias'] = params['version_alias']
        if 'app_alias' in params:
            query_params['appAlias'] = params['app_alias']
        if 'include_platform' in params:
            query_params['includePlatform'] = params['include_platform']
        if 'include_guest_apps' in params:
            query_params['includeGuestApps'] = params['include_guest_apps']
        if 'rows' in params:
            query_params['rows'] = params['rows']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/csv', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='file',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
