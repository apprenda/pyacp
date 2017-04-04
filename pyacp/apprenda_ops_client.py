import requests
import json

import functools

import pyacp.api_client
from pyacp.apis.applications_api import ApplicationsApi
from pyacp.apis.custom_properties_api import CustomPropertiesApi
from pyacp.apis.hosts_api import HostsApi
from pyacp import services

class ApprendaOpsClient():

    internalClient = None

    #how many applications to pull down per request
    apps_page_size = 20
    custom_properties_page_size = 20

    # Constructor for the client
    def __init__(self, host, username, password):
        self.internalClient = self.connect(self,host,username,password)

    @staticmethod
    def connect(self, host, username, password):
        # We need to create a session with the Apprenda Platform and store the authorization token for further use
        payload = '{"username": "'+ username +'", "password": "'+ password + '"}'
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.post(host+'/authentication/api/v1/sessions/soc', data=payload, headers=headers, verify=False)

        if (response.status_code == 201):
            self.sessionToken = json.loads(response.content)['apprendaSessionToken']
            return pyacp.ApiClient(host+'/soc',"ApprendaSessionToken",self.sessionToken)
        elif (response.status_code == 400):
            raise ConnectionError('The provided credentials are not valid. Please provide the correct username/password')
        else:
            raise Exception('There was an issue connecting to the platform')

    def get_apps_start(self):
        api = ApplicationsApi(self.internalClient)
        return self.get_paged_items_start(api.apps_search_new, self.apps_page_size)

    def get_apps_nextPage(self, url):
        api = ApplicationsApi(self.internalClient)
        return self.get_paged_items_next(url, api.apps_search_new, self.apps_page_size)

    """
    Worker function to begin retrieving results in a paged format.  This creates a generator, that returns an iterator
    """
    def get_paged_items_start(self, searchFunc, pageSize):
        kwargs = {'page_size': pageSize, 'page_number': 1}
        return searchFunc(**kwargs)

    """
    Worker function to continue retrieving results from a paged format.  Assumes the function takes page_size and page_number as params
    """
    def get_paged_items_next(self, searchFunc, pageSize, url):
        page = services.DepagingService.extractPageNumberFromUrl(url)

        kwargs = {'page_size': pageSize, 'page_number': str(page + 1)}
        return searchFunc(**kwargs)

    """
    Worker function to get depaged results when the search function is used for both first and next
    """
    def get_depager(self, searchFunc, pageSize):
        startArg = [searchFunc, pageSize]
        start = functools.partial(self.get_paged_items_start, *startArg)

        next = functools.partial(self.get_paged_items_next, *startArg)

        return services.DepagingService(start, next)

    """
    Get all applications currently hosted by the platform, or just one by alias
    """
    def getApplications(self, alias = None):
        api = ApplicationsApi(self.internalClient)
        if(alias is None):
            api = ApplicationsApi(self.internalClient)
            depage = self.get_depager(api.apps_search_new, self.apps_page_size)
            return depage.next()
        else:
            response = api.api_v1_applications_app_alias_versions_get(alias).items
            if response.status_code == 404:
                raise KeyError('The application does not exist')
            elif response.status_code == 400:
                raise Exception('There was an error retrieving your application')
            else:

                return response


    def getCustomProperties(self, name = None):
        kwargs = {'page_size': 1000}
        api = CustomPropertiesApi(self.internalClient)
        if(name is None):
            return api.custom_properties_get_public(**kwargs).items
        else:
            response = api.custom_properties_get_public(**kwargs).items
            id = None
            for property in response:
                if property.name == name:
                    id = property.id
            if id is None:
                raise KeyError('The custom property does not exist')
            else:
                return api.custom_properties_get_single_public(id)

    def transitionNode(self, node, newstate):
        if(node is None or newstate is None):
            raise Exception('Please provide the name of the node to update and the new state')
        api = HostsApi(self.internalClient)
        response = api.api_v1_hosts_host_name_state_put(node, newstate)
        if (response.status_code==204):
            return True
        elif (response.status_code==404):
            raise KeyError('The node provided was not found. Please ensure that the information passed is correct and try again.')
        else:
            raise Exception('Unknown error when setting the node state for: '+ node)


    def getNodes(self, name = None):
        kwargs = {'page_size': 1000}
        api = HostsApi(self.internalClient)
        if(name is None):
            return
        else:
            return api.api_v1_hosts_host_name_state_get(name)






