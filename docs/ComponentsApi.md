# swagger_client.ComponentsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**components_get**](ComponentsApi.md#components_get) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias}/components | Get all application components
[**components_get_by_alias**](ComponentsApi.md#components_get_by_alias) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias} | Get an application component
[**get_workloads_by_id**](ComponentsApi.md#get_workloads_by_id) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads/{workloadId} | Get workload
[**get_workloads_for_components**](ComponentsApi.md#get_workloads_for_components) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads | Get all workloads
[**post_workloads**](ComponentsApi.md#post_workloads) | **POST** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads | Deploy workload
[**remove_workload**](ComponentsApi.md#remove_workload) | **DELETE** /api/v1/applications/{appAlias}/versions/{versionAlias}/components/{componentAlias}/workloads/{workloadId} | Delete workload


# **components_get**
> list[UnpagedResourceBaseComponent] components_get(app_alias, version_alias)

Get all application components

**Requires Platform version 6.7.0 or later.**   Returns all components of an application version.  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version

try: 
    # Get all application components
    api_response = api_instance.components_get(app_alias, version_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->components_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of application | 
 **version_alias** | **str**| Required. Alias of application version | 

### Return type

[**list[UnpagedResourceBaseComponent]**](UnpagedResourceBaseComponent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **components_get_by_alias**
> Component components_get_by_alias(app_alias, version_alias, component_alias)

Get an application component

**Requires Platform version 6.7.0 or later.**   Returns a componet for an application version. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component

try: 
    # Get an application component
    api_response = api_instance.components_get_by_alias(app_alias, version_alias, component_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->components_get_by_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of application | 
 **version_alias** | **str**| Required. Alias of application version | 
 **component_alias** | **str**| Required. Alias of application component | 

### Return type

[**Component**](Component.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.ComponentsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component
workload_id = 'workload_id_example' # str | Required. Id of application workload

try: 
    # Get workload
    api_response = api_instance.get_workloads_by_id(app_alias, version_alias, component_alias, workload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_workloads_by_id: %s\n" % e)
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
api_instance = swagger_client.ComponentsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component

try: 
    # Get all workloads
    api_response = api_instance.get_workloads_for_components(app_alias, version_alias, component_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_workloads_for_components: %s\n" % e)
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
api_instance = swagger_client.ComponentsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component
workload = swagger_client.WorkloadDeploymentRequest() # WorkloadDeploymentRequest | Required. Name of the node to deploy the workload to

try: 
    # Deploy workload
    api_instance.post_workloads(app_alias, version_alias, component_alias, workload)
except ApiException as e:
    print("Exception when calling ComponentsApi->post_workloads: %s\n" % e)
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
api_instance = swagger_client.ComponentsApi()
app_alias = 'app_alias_example' # str | Required. Alias of application
version_alias = 'version_alias_example' # str | Required. Alias of application version
component_alias = 'component_alias_example' # str | Required. Alias of application component
workload_id = 'workload_id_example' # str | Required. Alias of application workload

try: 
    # Delete workload
    api_instance.remove_workload(app_alias, version_alias, component_alias, workload_id)
except ApiException as e:
    print("Exception when calling ComponentsApi->remove_workload: %s\n" % e)
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

