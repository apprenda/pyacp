# swagger_client.WorkloadsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_workloads_by_id**](WorkloadsApi.md#get_workloads_by_id) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads/{workloadId} | Get workload
[**get_workloads_for_components**](WorkloadsApi.md#get_workloads_for_components) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads | Get all workloads
[**post_workloads**](WorkloadsApi.md#post_workloads) | **POST** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads | Deploy workload
[**remove_workload**](WorkloadsApi.md#remove_workload) | **DELETE** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads/{workloadId} | Delete workload


# **get_workloads_by_id**
> Workload get_workloads_by_id(app_alias, version_alias, component_alias, workload_id)

Get workload

**Requires Platform version 6.7.0 or later.**   Returns a running application workload.   Learn more about [application workloads](/current/managing-apprenda-applications). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkloadsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component
workload_id = 'workload_id_example' # str | Required. Id of application workload

try: 
    # Get workload
    api_response = api_instance.get_workloads_by_id(app_alias, version_alias, component_alias, workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->get_workloads_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of application | 
 **version_alias** | **str**| Required. Alias of application version | 
 **component_alias** | **str**| Required. Alias of application component | 
 **workload_id** | **str**| Required. Id of application workload | 

### Return type

[**Workload**](Workload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workloads_for_components**
> UnpagedResourceBaseWorkload get_workloads_for_components(app_alias, version_alias, component_alias)

Get all workloads

**Requires Platform version 6.7.0 or later.**   Returns all running workloads of the application version component.   Learn more about [application workloads](/current/managing-apprenda-applications). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkloadsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component

try: 
    # Get all workloads
    api_response = api_instance.get_workloads_for_components(app_alias, version_alias, component_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WorkloadsApi->get_workloads_for_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of application | 
 **version_alias** | **str**| Required. Alias of application version | 
 **component_alias** | **str**| Required. Alias of application component | 

### Return type

[**UnpagedResourceBaseWorkload**](UnpagedResourceBaseWorkload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_workloads**
> post_workloads(app_alias, version_alias, component_alias, workload)

Deploy workload

**Requires Platform version 6.7.0 or later.**   Deploys a workload of the application component.   Learn more about deploying [application workloads](/current/managing-apprenda-applications). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkloadsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component
workload = swagger_client.WorkloadDeploymentRequest() # WorkloadDeploymentRequest | Required. Name of the node to deploy the workload to

try: 
    # Deploy workload
    api_instance.post_workloads(app_alias, version_alias, component_alias, workload)
except ApiException as e:
    print("Exception when calling WorkloadsApi->post_workloads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of application | 
 **version_alias** | **str**| Required. Alias of application version | 
 **component_alias** | **str**| Required. Alias of application component | 
 **workload** | [**WorkloadDeploymentRequest**](WorkloadDeploymentRequest.md)| Required. Name of the node to deploy the workload to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_workload**
> remove_workload(app_alias, version_alias, component_alias, workload_id)

Delete workload

**Requires Platform version 6.7.0 or later.**   Remove a specific workload from a node.    Learn more about [removing workloads](/current/managing-apprenda-applications). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkloadsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component
workload_id = 'workload_id_example' # str | Required. Alias of application workload

try: 
    # Delete workload
    api_instance.remove_workload(app_alias, version_alias, component_alias, workload_id)
except ApiException as e:
    print("Exception when calling WorkloadsApi->remove_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of application | 
 **version_alias** | **str**| Required. Alias of application version | 
 **component_alias** | **str**| Required. Alias of application component | 
 **workload_id** | **str**| Required. Alias of application workload | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

