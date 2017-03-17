import requests
import json
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
        if(alias is None):
            return api.apps_search_new()
        else:
            return api.api_v1_applications_app_alias_versions_get(alias)

    def getCustomProperties(self, id = None):
        api = CustomPropertiesApi(self.internalClient)
        if(id is None):
            return api.custom_properties_get_public()
        else:
            return api.custom_properties_get_single_public(id)

    def getNodes(self, name = None):
        api = HostsApi(self.internalClient)
        return api.api_v1_hosts_host_name_state_get(name)






