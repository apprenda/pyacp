# pyacp.HostsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_hosts_host_name_is_transitioning_get**](HostsApi.md#api_v1_hosts_host_name_is_transitioning_get) | **GET** /api/v1/hosts/{HostName}/isTransitioning | Check server transition
[**api_v1_hosts_host_name_state_get**](HostsApi.md#api_v1_hosts_host_name_state_get) | **GET** /api/v1/hosts/{HostName}/state | Get server state
[**api_v1_hosts_host_name_state_put**](HostsApi.md#api_v1_hosts_host_name_state_put) | **PUT** /api/v1/hosts/{HostName}/state | Update server state


# **api_v1_hosts_host_name_is_transitioning_get**
> InlineResponse2001 api_v1_hosts_host_name_is_transitioning_get(host_name)

Check server transition

**Requires Platform version 6.5.1 or later**   Returns true if a sever is transitioning between states or false if the server is not transitioning   Learn more about [server states transitions](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.HostsApi()
host_name = 'host_name_example' # str | Host name of the server

try: 
    # Check server transition
    api_response = api_instance.api_v1_hosts_host_name_is_transitioning_get(host_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->api_v1_hosts_host_name_is_transitioning_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| Host name of the server | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_hosts_host_name_state_get**
> InlineResponse200 api_v1_hosts_host_name_state_get(host_name)

Get server state

**Requires Platform version 6.5.1 or later**   Returns the current state of the server and a reason the server has been placed into a state.   Learn more about [server states transitions](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.HostsApi()
host_name = 'host_name_example' # str | Host name of the server

try: 
    # Get server state
    api_response = api_instance.api_v1_hosts_host_name_state_get(host_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostsApi->api_v1_hosts_host_name_state_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| Host name of the server | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_hosts_host_name_state_put**
> api_v1_hosts_host_name_state_put(host_name, node_state)

Update server state

**Requires Platform version 6.5.1 or later**   Updates a server's state and initiates a state transition.   In the request body, send the state the server will be transitioned to and a reason the server is being transitioned. A server can be placed into the Online, Reserved, or Maintenance states and all state transitions will take affect imediately after a sucessfull request.    Learn more about [server states transitions](/current/Managing-Apprenda-Infrastructure#maintenancereserved). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.HostsApi()
host_name = 'host_name_example' # str | Host name of the server
node_state = pyacp.NodeState() # NodeState | State the server should be transitioned to.

try: 
    # Update server state
    api_instance.api_v1_hosts_host_name_state_put(host_name, node_state)
except ApiException as e:
    print("Exception when calling HostsApi->api_v1_hosts_host_name_state_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name** | **str**| Host name of the server | 
 **node_state** | [**NodeState**](NodeState.md)| State the server should be transitioned to. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

