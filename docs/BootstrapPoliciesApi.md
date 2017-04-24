# pyacp.BootstrapPoliciesApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bootstrap_policies_add**](BootstrapPoliciesApi.md#bootstrap_policies_add) | **POST** /api/v1/bootstrappolicies | Create Bootsrap Policy
[**bootstrap_policies_get_all**](BootstrapPoliciesApi.md#bootstrap_policies_get_all) | **GET** /api/v1/bootstrappolicies | Get all Bootstrap Policies
[**bootstrap_policies_get_single_by_name**](BootstrapPoliciesApi.md#bootstrap_policies_get_single_by_name) | **GET** /api/v1/bootstrappolicies/{bspName} | Get Bootstrap Policy
[**remove_bootstrap_policy**](BootstrapPoliciesApi.md#remove_bootstrap_policy) | **DELETE** /api/v1/bootstrappolicies/{bspName} | Delete Bootstrap Policy
[**update_bootstrap_policy**](BootstrapPoliciesApi.md#update_bootstrap_policy) | **PUT** /api/v1/bootstrappolicies/{bspName} | Update Bootstrap Policy
[**upload_bootstrap_archive_file**](BootstrapPoliciesApi.md#upload_bootstrap_archive_file) | **PUT** /api/v1/bootstrappolicies/{bspName}/archive | Upload Bootstrap Policy archive


# **bootstrap_policies_add**
> bootstrap_policies_add(bootstrap_policy)

Create Bootsrap Policy

**Requires Platform version 6.7.0 or later.**   Adds a new Bootstrap Policy to the Platform. 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.BootstrapPoliciesApi()
bootstrap_policy = pyacp.ApprendaSOCWebRestAPIResourcesBootstrapPolicy() # ApprendaSOCWebRestAPIResourcesBootstrapPolicy | Required. Bootstrap Policy  to add to the system

try: 
    # Create Bootsrap Policy
    api_instance.bootstrap_policies_add(bootstrap_policy)
except ApiException as e:
    print("Exception when calling BootstrapPoliciesApi->bootstrap_policies_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bootstrap_policy** | [**ApprendaSOCWebRestAPIResourcesBootstrapPolicy**](ApprendaSOCWebRestAPIResourcesBootstrapPolicy.md)| Required. Bootstrap Policy  to add to the system | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bootstrap_policies_get_all**
> UnpagedResourceBaseBootstrapPolicy bootstrap_policies_get_all()

Get all Bootstrap Policies

**Requires Platform version 6.7.0 or later.**   Returns a list of all Bootstrap Policies on the Platform. 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.BootstrapPoliciesApi()

try: 
    # Get all Bootstrap Policies
    api_response = api_instance.bootstrap_policies_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootstrapPoliciesApi->bootstrap_policies_get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnpagedResourceBaseBootstrapPolicy**](UnpagedResourceBaseBootstrapPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bootstrap_policies_get_single_by_name**
> ApprendaSOCWebRestAPIResourcesBootstrapPolicy bootstrap_policies_get_single_by_name(bsp_name)

Get Bootstrap Policy

**Requires Platform version 6.7.0 or later.**   Returns a Bootstrap Policy. 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.BootstrapPoliciesApi()
bsp_name = 'bsp_name_example' # str | Required. Name of the Bootstrap Policy to retrieve

try: 
    # Get Bootstrap Policy
    api_response = api_instance.bootstrap_policies_get_single_by_name(bsp_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootstrapPoliciesApi->bootstrap_policies_get_single_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bsp_name** | **str**| Required. Name of the Bootstrap Policy to retrieve | 

### Return type

[**ApprendaSOCWebRestAPIResourcesBootstrapPolicy**](ApprendaSOCWebRestAPIResourcesBootstrapPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_bootstrap_policy**
> remove_bootstrap_policy(bsp_name)

Delete Bootstrap Policy

**Requires Platform version 6.7.0 or later.**   Deletes a Bootstrap Policy from the Platform.  

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.BootstrapPoliciesApi()
bsp_name = 'bsp_name_example' # str | Required. Name of the Bootstrap Policy to delete

try: 
    # Delete Bootstrap Policy
    api_instance.remove_bootstrap_policy(bsp_name)
except ApiException as e:
    print("Exception when calling BootstrapPoliciesApi->remove_bootstrap_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bsp_name** | **str**| Required. Name of the Bootstrap Policy to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bootstrap_policy**
> ApprendaSOCWebRestAPIResourcesBootstrapPolicy update_bootstrap_policy(bsp_name, bootstrap_policy)

Update Bootstrap Policy

**Requires Platform version 6.7.0 or later.**   Updates configuration settings for a Boostrap Policy. Making a request to this endpoint will update all fields for a Boostrap Policy. You should always pass all input values in the body of the request, because any value that is not provided will be updated to the default value. 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.BootstrapPoliciesApi()
bsp_name = 'bsp_name_example' # str | Required. Name of Boostrap Policy
bootstrap_policy = pyacp.ApprendaSOCWebRestAPIResourcesBootstrapPolicy() # ApprendaSOCWebRestAPIResourcesBootstrapPolicy | Required. Bootstrap Policy to add to the collection. All fields should be passed in the request

try: 
    # Update Bootstrap Policy
    api_response = api_instance.update_bootstrap_policy(bsp_name, bootstrap_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BootstrapPoliciesApi->update_bootstrap_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bsp_name** | **str**| Required. Name of Boostrap Policy | 
 **bootstrap_policy** | [**ApprendaSOCWebRestAPIResourcesBootstrapPolicy**](ApprendaSOCWebRestAPIResourcesBootstrapPolicy.md)| Required. Bootstrap Policy to add to the collection. All fields should be passed in the request | 

### Return type

[**ApprendaSOCWebRestAPIResourcesBootstrapPolicy**](ApprendaSOCWebRestAPIResourcesBootstrapPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_bootstrap_archive_file**
> upload_bootstrap_archive_file(bsp_name, file)

Upload Bootstrap Policy archive

**Requires Platform version 6.7.0 or later.**   Uploads an archive for a Bootstrap Policy. This will replace any archive already attached to the Bootstrap Policy.   Learn more about [Bootstrap Policy archive requirements](/current/bootstrap-policies). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.BootstrapPoliciesApi()
bsp_name = 'bsp_name_example' # str | Name of the Bootstrap Policy
file = '/path/to/file.txt' # file | Archive for the Bootstrap Policy

try: 
    # Upload Bootstrap Policy archive
    api_instance.upload_bootstrap_archive_file(bsp_name, file)
except ApiException as e:
    print("Exception when calling BootstrapPoliciesApi->upload_bootstrap_archive_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bsp_name** | **str**| Name of the Bootstrap Policy | 
 **file** | **file**| Archive for the Bootstrap Policy | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

