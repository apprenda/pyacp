import requests
import json

import sys

import pyacp.api_client
from pyacp.apis.applications_api import ApplicationsApi
from pyacp.apis.custom_properties_api import CustomPropertiesApi
from pyacp.apis.hosts_api import HostsApi

class ApprendaOpsClient():

    internalClient = None
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

    def getApplications(self, alias = None):
        api = ApplicationsApi(self.internalClient)
        kwargs = {'page_size':1000}
        if(alias is None):
            return api.apps_search_new(**kwargs).items
        else:
            return api.api_v1_applications_app_alias_versions_get(alias).items

    def getCustomProperties(self, id = None):
        kwargs = {'page_size': 1000}
        api = CustomPropertiesApi(self.internalClient)
        if(id is None):
            return api.custom_properties_get_public(**kwargs).items
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
            raise Exception('The node provided was not found. Please ensure that the information passed is correct and try again.')
        else:
            raise Exception('Unknown error when setting the node state for: '+ node)


    def getNodes(self, name = None):
        kwargs = {'page_size': 1000}
        api = HostsApi(self.internalClient)
        if(name is None):
            return
        else:
            return api.api_v1_hosts_host_name_state_get(name)






