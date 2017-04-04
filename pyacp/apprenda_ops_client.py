import requests
import json
import functools

import pyacp.api_client
from pyacp.apis.applications_api import ApplicationsApi
from pyacp.apis.custom_properties_api import CustomPropertiesApi
from pyacp.apis.hosts_api import HostsApi
from pyacp.apis.nodes_api import NodesApi
from pyacp import services

class ApprendaOpsClient:
    internalClient = None

    # how many applications to pull down per request
    apps_page_size = 20
    custom_properties_page_size = 20
    nodes_page_size = 500

    # Constructor for the client
    def __init__(self, host, username, password):
        self.internalClient = self.connect(self, host, username, password)

    @staticmethod
    def connect(self, host, username, password):
        # We need to create a session with the Apprenda Platform and store the authorization token for further use
        payload = '{"username": "' + username + '", "password": "' + password + '"}'
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.post(host + '/authentication/api/v1/sessions/soc', data=payload, headers=headers,
                                 verify=False)

        if response.status_code == 201:
            self.sessionToken = json.loads(response.content)['apprendaSessionToken']
            return pyacp.ApiClient(host + '/soc', "ApprendaSessionToken", self.sessionToken)
        elif response.status_code == 400:
            raise ConnectionError(
                'The provided credentials are not valid. Please provide the correct username/password')
        else:
            raise Exception('There was an issue connecting to the platform')

    """
    Worker function to begin retrieving results in a paged format.  This creates a generator, that returns an iterator
    """
    @staticmethod
    def get_paged_items_start(search_function, page_size):
        kwargs = {'page_size': page_size, 'page_number': 1}
        return search_function(**kwargs)

    """
    Worker function to continue retrieving results from a paged format.  
    Assumes the function takes page_size and page_number as params
    """
    @staticmethod
    def get_paged_items_next(search_function, page_size, url):
        page = services.DepagingService.extractPageNumberFromUrl(url)

        kwargs = {'page_size': page_size, 'page_number': str(page + 1)}
        return search_function(**kwargs)

    """
    Worker function to get depaged results when the search function is used for both first and next
    """
    def get_depager(self, search_function, page_size):
        function_arguments = [search_function, page_size]
        start_function = functools.partial(self.get_paged_items_start, *function_arguments)

        next_function = functools.partial(self.get_paged_items_next, *function_arguments)

        return services.DepagingService(start_function, next_function)

    """
    Get all applications currently hosted by the platform, or just one by alias
    """
    def get_applications(self, alias=None):
        api = ApplicationsApi(self.internalClient)
        if alias is None:
            api = ApplicationsApi(self.internalClient)
            depager = self.get_depager(api.apps_search_new, self.apps_page_size)
            return depager.next()
        else:
            response = api.api_v1_applications_app_alias_versions_get(alias).items
            if response.status_code == 404:
                raise KeyError('The application does not exist')
            elif response.status_code == 400:
                raise Exception('There was an error retrieving your application')
            else:

                return response

    """
    Get all custom properties, or one by name
    """
    def get_custom_properties(self, name=None):
        api = CustomPropertiesApi(self.internalClient)

        depager = self.get_depager(api.custom_properties_get_public, self.custom_properties_page_size)
        if name is None:
            return depager.next()
        else:
            for property in depager.next():
                if property.name == name:
                    return property

            raise KeyError('The custom property does not exist')

    def transition_node(self, node, newstate):
        if node is None or newstate is None:
            raise Exception('Please provide the name of the node to update and the new state')
        api = HostsApi(self.internalClient)
        response = api.api_v1_hosts_host_name_state_put(node, newstate)
        if response.status_code == 204:
            return True
        elif response.status_code == 404:
            raise KeyError(
                'The node provided was not found. Please ensure that the information passed is correct and try again.')
        else:
            raise Exception('Unknown error when setting the node state for: ' + node)

    def get_nodes(self, name=None):
        api = NodesApi(self.internalClient)

        if name is None:
            depager = self.get_depager(api.get_all_nodes, self.nodes_page_size)
            return depager.next()
        else:
            # a little funky here - the nodes controller takes an optional name, but swagger can't figure that out alone
            res = api.get_node_by_name(name)
            if res is None:
                raise KeyError("The node " + name + " was not found")
            return res
