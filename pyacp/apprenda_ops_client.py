import requests
import json

import sys

import pyacp.api_client
from pyacp.apis.applications_api import ApplicationsApi
from pyacp.apis.custom_properties_api import CustomPropertiesApi
from pyacp.apis.hosts_api import HostsApi
from pyacp import services

class ApprendaOpsClient():

    internalClient = None

    #how many applications to pull down per request
    apps_page_size = 20

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
        return self.get_apps_worker(None, self.apps_page_size)

    def get_apps_nextPage(self, url):
        return self.get_apps_worker(url, self.apps_page_size)

    def get_apps_worker(self, url, pageSize):
        if url is None:
            kwargs = {'page_size': pageSize, 'page_number': 1}
        else:
            page_string = url.split("pagenumber=")
            split = page_string[-1]
            ended = split.split("&")

            pageString = ended[0]
            page = int(pageString)

            kwargs = {'page_size' : pageSize, 'page_number': str(page + 1)}
        api = ApplicationsApi(self.internalClient)
        return api.apps_search_new(**kwargs)

    def getApplications(self, alias = None):
        api = ApplicationsApi(self.internalClient)
        if(alias is None):
            depage = services.DepagingService(self.get_apps_start, self.get_apps_nextPage)
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






