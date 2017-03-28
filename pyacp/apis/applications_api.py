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


class ApplicationsApi(object):
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

    def apps_search_new(self, **kwargs):
        """
        Get all applications
        **Requires Platform version 6.7.0 or later.**   Returns all applications on the Plaform. By default Apprenda applications are not included. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_search_new(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Word to search for matching applications
        :param int page_number: The page of results to return. Defaults to 1, the first page
        :param int page_size: Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20
        :param str sort_order: Determines how results will be sorted. Allowed values: ascending, descending. Default: ascending
        :param str sort_by: Field name to use to sort results. Allowed values: ApplicationAlias
        :param bool include_apprenda_apps: Determines if Apprenda applications are returned in request. Default: false
        :param bool only_search_app_info: When true, limits request with a filter word provided to searching only the application name or application alias. When false, all application information and custom properties are searched. Default: True
        :return: ApprendaRestAPICommonResourcesPagedResourceBaseApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apps_search_new_with_http_info(**kwargs)
        else:
            (data) = self.apps_search_new_with_http_info(**kwargs)
            return data

    def apps_search_new_with_http_info(self, **kwargs):
        """
        Get all applications
        **Requires Platform version 6.7.0 or later.**   Returns all applications on the Plaform. By default Apprenda applications are not included. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apps_search_new_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Word to search for matching applications
        :param int page_number: The page of results to return. Defaults to 1, the first page
        :param int page_size: Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20
        :param str sort_order: Determines how results will be sorted. Allowed values: ascending, descending. Default: ascending
        :param str sort_by: Field name to use to sort results. Allowed values: ApplicationAlias
        :param bool include_apprenda_apps: Determines if Apprenda applications are returned in request. Default: false
        :param bool only_search_app_info: When true, limits request with a filter word provided to searching only the application name or application alias. When false, all application information and custom properties are searched. Default: True
        :return: ApprendaRestAPICommonResourcesPagedResourceBaseApplication
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'page_number', 'page_size', 'sort_order', 'sort_by', 'include_apprenda_apps', 'only_search_app_info']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apps_search_new" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/api/v1/applications'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'page_number' in params:
            query_params['pageNumber'] = params['page_number']
        if 'page_size' in params:
            query_params['pageSize'] = params['page_size']
        if 'sort_order' in params:
            query_params['sortOrder'] = params['sort_order']
        if 'sort_by' in params:
            query_params['sortBy'] = params['sort_by']
        if 'include_apprenda_apps' in params:
            query_params['includeApprendaApps'] = params['include_apprenda_apps']
        if 'only_search_app_info' in params:
            query_params['onlySearchAppInfo'] = params['only_search_app_info']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApprendaRestAPICommonResourcesPagedResourceBaseApplication',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_app_by_alias(self, app_alias, **kwargs):
        """
        Get application
        **Requires Platform version 6.7.0 or later.**   Returns information about an application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_by_alias(app_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of the application (required)
        :return: Application
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_app_by_alias_with_http_info(app_alias, **kwargs)
        else:
            (data) = self.get_app_by_alias_with_http_info(app_alias, **kwargs)
            return data

    def get_app_by_alias_with_http_info(self, app_alias, **kwargs):
        """
        Get application
        **Requires Platform version 6.7.0 or later.**   Returns information about an application. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_app_by_alias_with_http_info(app_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of the application (required)
        :return: Application
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
                    " to method get_app_by_alias" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `get_app_by_alias`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}'.replace('{format}', 'json')
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
                                        response_type='Application',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
