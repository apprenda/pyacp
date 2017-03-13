# pyacp.DeploymentPoliciesApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_deploymentpolicies_get**](DeploymentPoliciesApi.md#api_v1_deploymentpolicies_get) | **GET** /api/v1/deploymentpolicies | Get all Deployment Policies
[**api_v1_deploymentpolicies_id_delete**](DeploymentPoliciesApi.md#api_v1_deploymentpolicies_id_delete) | **DELETE** /api/v1/deploymentpolicies/{id} | Delete Deployment Policy
[**api_v1_deploymentpolicies_id_get**](DeploymentPoliciesApi.md#api_v1_deploymentpolicies_id_get) | **GET** /api/v1/deploymentpolicies/{id} | Get Deployment Policy
[**api_v1_deploymentpolicies_id_put**](DeploymentPoliciesApi.md#api_v1_deploymentpolicies_id_put) | **PUT** /api/v1/deploymentpolicies/{id} | Update deployment Policy
[**api_v1_deploymentpolicies_post**](DeploymentPoliciesApi.md#api_v1_deploymentpolicies_post) | **POST** /api/v1/deploymentpolicies | Create Deployment Policy


# **api_v1_deploymentpolicies_get**
> UnpagedResourceBaseDeploymentPolicy api_v1_deploymentpolicies_get()

Get all Deployment Policies

**Required Platform version 6.7.0 or later.**   Returns all Deployment Policies on the Platform. 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.DeploymentPoliciesApi()

try: 
    # Get all Deployment Policies
    api_response = api_instance.api_v1_deploymentpolicies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentPoliciesApi->api_v1_deploymentpolicies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnpagedResourceBaseDeploymentPolicy**](UnpagedResourceBaseDeploymentPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_deploymentpolicies_id_delete**
> api_v1_deploymentpolicies_id_delete(id)

Delete Deployment Policy

**Required Platform version 6.7.0 or later.**   Deletes a Deployment Policy. Learn more about [Application Deployment Policies](/current/app-deployment-policies). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.DeploymentPoliciesApi()
id = 56 # int | Required. Platform assigned id of Deployment Policy

try: 
    # Delete Deployment Policy
    api_instance.api_v1_deploymentpolicies_id_delete(id)
except ApiException as e:
    print("Exception when calling DeploymentPoliciesApi->api_v1_deploymentpolicies_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Required. Platform assigned id of Deployment Policy | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_deploymentpolicies_id_get**
> DeploymentPolicy api_v1_deploymentpolicies_id_get(id)

Get Deployment Policy

**Required Platform version 6.7.0 or later.**   Returns a Deployment Policy. Learn more about [Application Deployment Policies](/current/app-deployment-policies). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.DeploymentPoliciesApi()
id = 56 # int | Platform assigned id of Deployment Policy

try: 
    # Get Deployment Policy
    api_response = api_instance.api_v1_deploymentpolicies_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentPoliciesApi->api_v1_deploymentpolicies_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Platform assigned id of Deployment Policy | 

### Return type

[**DeploymentPolicy**](DeploymentPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_deploymentpolicies_id_put**
> api_v1_deploymentpolicies_id_put(id, deployment_policy)

Update deployment Policy

**Required Platform version 6.7.0 or later.**   Updates a Deployment Policy. Updates made to Deployment Policies will affect all furture deployments that match the policy. Currently deployed workloads will not be affected.    Additionally, making a request to this endpoint will update all fields for an Application Deployment Policy. You should always pass all input values in the body of the request, because any value that is not provided will be updated to the default value.    Learn more about [Application Deployment Policies](/current/app-deployment-policies). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.DeploymentPoliciesApi()
id = 56 # int | Required. Platform assigned id of Deployment Policy
deployment_policy = pyacp.DeploymentPolicy() # DeploymentPolicy | Required. Deployment Policy to update

try: 
    # Update deployment Policy
    api_instance.api_v1_deploymentpolicies_id_put(id, deployment_policy)
except ApiException as e:
    print("Exception when calling DeploymentPoliciesApi->api_v1_deploymentpolicies_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Required. Platform assigned id of Deployment Policy | 
 **deployment_policy** | [**DeploymentPolicy**](DeploymentPolicy.md)| Required. Deployment Policy to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_deploymentpolicies_post**
> DeploymentPolicy api_v1_deploymentpolicies_post(deployment_policy)

Create Deployment Policy

**Required Platform version 6.7.0 or later.**   Creates a new Deployment Policy on the Platform.    Learn more about [Application Deployment Policies](/current/app-deployment-policies). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.DeploymentPoliciesApi()
deployment_policy = pyacp.DeploymentPolicy() # DeploymentPolicy | Required. Deployment Policy to add

try: 
    # Create Deployment Policy
    api_response = api_instance.api_v1_deploymentpolicies_post(deployment_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeploymentPoliciesApi->api_v1_deploymentpolicies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_policy** | [**DeploymentPolicy**](DeploymentPolicy.md)| Required. Deployment Policy to add | 

### Return type

[**DeploymentPolicy**](DeploymentPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

