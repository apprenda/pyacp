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


class WorkloadsApi(object):
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

    def get_workloads_by_id(self, app_alias, version_alias, component_alias, workload_id, **kwargs):
        """
        Get workload
        **Requires Platform version 6.7.0 or later.**   Returns a running application workload.   Learn more about [application workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workloads_by_id(app_alias, version_alias, component_alias, workload_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :param str workload_id: Required. Id of application workload (required)
        :return: Workload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_workloads_by_id_with_http_info(app_alias, version_alias, component_alias, workload_id, **kwargs)
        else:
            (data) = self.get_workloads_by_id_with_http_info(app_alias, version_alias, component_alias, workload_id, **kwargs)
            return data

    def get_workloads_by_id_with_http_info(self, app_alias, version_alias, component_alias, workload_id, **kwargs):
        """
        Get workload
        **Requires Platform version 6.7.0 or later.**   Returns a running application workload.   Learn more about [application workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workloads_by_id_with_http_info(app_alias, version_alias, component_alias, workload_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :param str workload_id: Required. Id of application workload (required)
        :return: Workload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_alias', 'version_alias', 'component_alias', 'workload_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workloads_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `get_workloads_by_id`")
        # verify the required parameter 'version_alias' is set
        if ('version_alias' not in params) or (params['version_alias'] is None):
            raise ValueError("Missing the required parameter `version_alias` when calling `get_workloads_by_id`")
        # verify the required parameter 'component_alias' is set
        if ('component_alias' not in params) or (params['component_alias'] is None):
            raise ValueError("Missing the required parameter `component_alias` when calling `get_workloads_by_id`")
        # verify the required parameter 'workload_id' is set
        if ('workload_id' not in params) or (params['workload_id'] is None):
            raise ValueError("Missing the required parameter `workload_id` when calling `get_workloads_by_id`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads/{workloadId}'.replace('{format}', 'json')
        path_params = {}
        if 'app_alias' in params:
            path_params['appAlias'] = params['app_alias']
        if 'version_alias' in params:
            path_params['versionAlias'] = params['version_alias']
        if 'component_alias' in params:
            path_params['componentAlias'] = params['component_alias']
        if 'workload_id' in params:
            path_params['workloadId'] = params['workload_id']

        query_params = {}

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
                                        response_type='Workload',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_workloads_for_components(self, app_alias, version_alias, component_alias, **kwargs):
        """
        Get all workloads
        **Requires Platform version 6.7.0 or later.**   Returns all running workloads of the application version component.   Learn more about [application workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workloads_for_components(app_alias, version_alias, component_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :return: UnpagedResourceBaseWorkload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_workloads_for_components_with_http_info(app_alias, version_alias, component_alias, **kwargs)
        else:
            (data) = self.get_workloads_for_components_with_http_info(app_alias, version_alias, component_alias, **kwargs)
            return data

    def get_workloads_for_components_with_http_info(self, app_alias, version_alias, component_alias, **kwargs):
        """
        Get all workloads
        **Requires Platform version 6.7.0 or later.**   Returns all running workloads of the application version component.   Learn more about [application workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workloads_for_components_with_http_info(app_alias, version_alias, component_alias, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :return: UnpagedResourceBaseWorkload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_alias', 'version_alias', 'component_alias']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workloads_for_components" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `get_workloads_for_components`")
        # verify the required parameter 'version_alias' is set
        if ('version_alias' not in params) or (params['version_alias'] is None):
            raise ValueError("Missing the required parameter `version_alias` when calling `get_workloads_for_components`")
        # verify the required parameter 'component_alias' is set
        if ('component_alias' not in params) or (params['component_alias'] is None):
            raise ValueError("Missing the required parameter `component_alias` when calling `get_workloads_for_components`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads'.replace('{format}', 'json')
        path_params = {}
        if 'app_alias' in params:
            path_params['appAlias'] = params['app_alias']
        if 'version_alias' in params:
            path_params['versionAlias'] = params['version_alias']
        if 'component_alias' in params:
            path_params['componentAlias'] = params['component_alias']

        query_params = {}

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
                                        response_type='UnpagedResourceBaseWorkload',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_workloads_on_node(self, node_name, **kwargs):
        """
        Get all workloads on a node
        Returns all workloads currently running on the node.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workloads_on_node(node_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node_name: Required. Name of the node (required)
        :return: UnpagedResourceBaseWorkload
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_workloads_on_node_with_http_info(node_name, **kwargs)
        else:
            (data) = self.get_workloads_on_node_with_http_info(node_name, **kwargs)
            return data

    def get_workloads_on_node_with_http_info(self, node_name, **kwargs):
        """
        Get all workloads on a node
        Returns all workloads currently running on the node.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_workloads_on_node_with_http_info(node_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node_name: Required. Name of the node (required)
        :return: UnpagedResourceBaseWorkload
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_workloads_on_node" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_name' is set
        if ('node_name' not in params) or (params['node_name'] is None):
            raise ValueError("Missing the required parameter `node_name` when calling `get_workloads_on_node`")


        collection_formats = {}

        resource_path = '/api/v1/nodes/workloads'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'node_name' in params:
            query_params['nodeName'] = params['node_name']

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
                                        response_type='UnpagedResourceBaseWorkload',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def post_workloads(self, app_alias, version_alias, component_alias, workload, **kwargs):
        """
        Deploy workload
        **Requires Platform version 6.7.0 or later.**   Deploys a workload of the application component.   Learn more about deploying [application workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workloads(app_alias, version_alias, component_alias, workload, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :param WorkloadDeploymentRequest workload: Required. Name of the node to deploy the workload to (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.post_workloads_with_http_info(app_alias, version_alias, component_alias, workload, **kwargs)
        else:
            (data) = self.post_workloads_with_http_info(app_alias, version_alias, component_alias, workload, **kwargs)
            return data

    def post_workloads_with_http_info(self, app_alias, version_alias, component_alias, workload, **kwargs):
        """
        Deploy workload
        **Requires Platform version 6.7.0 or later.**   Deploys a workload of the application component.   Learn more about deploying [application workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.post_workloads_with_http_info(app_alias, version_alias, component_alias, workload, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :param WorkloadDeploymentRequest workload: Required. Name of the node to deploy the workload to (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_alias', 'version_alias', 'component_alias', 'workload']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_workloads" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `post_workloads`")
        # verify the required parameter 'version_alias' is set
        if ('version_alias' not in params) or (params['version_alias'] is None):
            raise ValueError("Missing the required parameter `version_alias` when calling `post_workloads`")
        # verify the required parameter 'component_alias' is set
        if ('component_alias' not in params) or (params['component_alias'] is None):
            raise ValueError("Missing the required parameter `component_alias` when calling `post_workloads`")
        # verify the required parameter 'workload' is set
        if ('workload' not in params) or (params['workload'] is None):
            raise ValueError("Missing the required parameter `workload` when calling `post_workloads`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads'.replace('{format}', 'json')
        path_params = {}
        if 'app_alias' in params:
            path_params['appAlias'] = params['app_alias']
        if 'version_alias' in params:
            path_params['versionAlias'] = params['version_alias']
        if 'component_alias' in params:
            path_params['componentAlias'] = params['component_alias']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'workload' in params:
            body_params = params['workload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def remove_workload(self, app_alias, version_alias, component_alias, workload_id, **kwargs):
        """
        Delete workload
        **Requires Platform version 6.7.0 or later.**   Remove a specific workload from a node.    Learn more about [removing workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_workload(app_alias, version_alias, component_alias, workload_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :param str workload_id: Required. Alias of application workload (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_workload_with_http_info(app_alias, version_alias, component_alias, workload_id, **kwargs)
        else:
            (data) = self.remove_workload_with_http_info(app_alias, version_alias, component_alias, workload_id, **kwargs)
            return data

    def remove_workload_with_http_info(self, app_alias, version_alias, component_alias, workload_id, **kwargs):
        """
        Delete workload
        **Requires Platform version 6.7.0 or later.**   Remove a specific workload from a node.    Learn more about [removing workloads](/current/managing-apprenda-applications). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_workload_with_http_info(app_alias, version_alias, component_alias, workload_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str app_alias: Required. Alias of application (required)
        :param str version_alias: Required. Alias of application version (required)
        :param str component_alias: Required. Alias of application component (required)
        :param str workload_id: Required. Alias of application workload (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_alias', 'version_alias', 'component_alias', 'workload_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_workload" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_alias' is set
        if ('app_alias' not in params) or (params['app_alias'] is None):
            raise ValueError("Missing the required parameter `app_alias` when calling `remove_workload`")
        # verify the required parameter 'version_alias' is set
        if ('version_alias' not in params) or (params['version_alias'] is None):
            raise ValueError("Missing the required parameter `version_alias` when calling `remove_workload`")
        # verify the required parameter 'component_alias' is set
        if ('component_alias' not in params) or (params['component_alias'] is None):
            raise ValueError("Missing the required parameter `component_alias` when calling `remove_workload`")
        # verify the required parameter 'workload_id' is set
        if ('workload_id' not in params) or (params['workload_id'] is None):
            raise ValueError("Missing the required parameter `workload_id` when calling `remove_workload`")


        collection_formats = {}

        resource_path = '/api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads/{workloadId}'.replace('{format}', 'json')
        path_params = {}
        if 'app_alias' in params:
            path_params['appAlias'] = params['app_alias']
        if 'version_alias' in params:
            path_params['versionAlias'] = params['version_alias']
        if 'component_alias' in params:
            path_params['componentAlias'] = params['component_alias']
        if 'workload_id' in params:
            path_params['workloadId'] = params['workload_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
