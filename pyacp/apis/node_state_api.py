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


class NodeStateApi(object):
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

    def get_node_state(self, role_name, node_name, **kwargs):
        """
        Get the state of a node
        Returns the state of the given node. A nodes state is releated to how healthy and active the node is in Platform activities.  Only valid for Windows and Linux nodes.   See more on [node states](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_node_state(role_name, node_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str role_name: (required)
        :param str node_name: Required. Name of the node (required)
        :return: NodeState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_node_state_with_http_info(role_name, node_name, **kwargs)
        else:
            (data) = self.get_node_state_with_http_info(role_name, node_name, **kwargs)
            return data

    def get_node_state_with_http_info(self, role_name, node_name, **kwargs):
        """
        Get the state of a node
        Returns the state of the given node. A nodes state is releated to how healthy and active the node is in Platform activities.  Only valid for Windows and Linux nodes.   See more on [node states](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_node_state_with_http_info(role_name, node_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str role_name: (required)
        :param str node_name: Required. Name of the node (required)
        :return: NodeState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role_name', 'node_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_node_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params) or (params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `get_node_state`")
        # verify the required parameter 'node_name' is set
        if ('node_name' not in params) or (params['node_name'] is None):
            raise ValueError("Missing the required parameter `node_name` when calling `get_node_state`")


        collection_formats = {}

        resource_path = '/api/v1/nodes/{roleName}/roleState'.replace('{format}', 'json')
        path_params = {}
        if 'role_name' in params:
            path_params['roleName'] = params['role_name']

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
                                        response_type='NodeState',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_node_state(self, node_name, node_state, role_name, **kwargs):
        """
        Update the state of a node
        Updates a server's state and initiates a state transition.   In the request body, send the state the server will be transitioned to and a reason the server is being transitioned. A server can be placed into the Online, Reserved, or Maintenance states and all state transitions will take affect imediately after a sucessfull request.   See more on [node states](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_node_state(node_name, node_state, role_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node_name: Required. Name of the node to transition (required)
        :param NodeState node_state: State to transition the node to (required)
        :param str role_name: (required)
        :return: NodeState
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_node_state_with_http_info(node_name, node_state, role_name, **kwargs)
        else:
            (data) = self.set_node_state_with_http_info(node_name, node_state, role_name, **kwargs)
            return data

    def set_node_state_with_http_info(self, node_name, node_state, role_name, **kwargs):
        """
        Update the state of a node
        Updates a server's state and initiates a state transition.   In the request body, send the state the server will be transitioned to and a reason the server is being transitioned. A server can be placed into the Online, Reserved, or Maintenance states and all state transitions will take affect imediately after a sucessfull request.   See more on [node states](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_node_state_with_http_info(node_name, node_state, role_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str node_name: Required. Name of the node to transition (required)
        :param NodeState node_state: State to transition the node to (required)
        :param str role_name: (required)
        :return: NodeState
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_name', 'node_state', 'role_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_node_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'node_name' is set
        if ('node_name' not in params) or (params['node_name'] is None):
            raise ValueError("Missing the required parameter `node_name` when calling `set_node_state`")
        # verify the required parameter 'node_state' is set
        if ('node_state' not in params) or (params['node_state'] is None):
            raise ValueError("Missing the required parameter `node_state` when calling `set_node_state`")
        # verify the required parameter 'role_name' is set
        if ('role_name' not in params) or (params['role_name'] is None):
            raise ValueError("Missing the required parameter `role_name` when calling `set_node_state`")


        collection_formats = {}

        resource_path = '/api/v1/nodes/{roleName}/roleState'.replace('{format}', 'json')
        path_params = {}
        if 'role_name' in params:
            path_params['roleName'] = params['role_name']

        query_params = {}
        if 'node_name' in params:
            query_params['nodeName'] = params['node_name']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'node_state' in params:
            body_params = params['node_state']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json', 'text/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='NodeState',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
