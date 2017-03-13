# swagger_client.RegistryApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registry_delete**](RegistryApi.md#registry_delete) | **DELETE** /api/v1/registry/{name} | Delete Registry Setting
[**registry_get**](RegistryApi.md#registry_get) | **GET** /api/v1/registry | Get all Registry Settings
[**registry_get_by_name**](RegistryApi.md#registry_get_by_name) | **GET** /api/v1/registry/{name} | Get Registry Setting
[**registry_post_new**](RegistryApi.md#registry_post_new) | **POST** /api/v1/registry | Create new Registry Setting
[**registry_put**](RegistryApi.md#registry_put) | **PUT** /api/v1/registry/{name} | Update Registry Setting


# **registry_delete**
> registry_delete(name)

Delete Registry Setting

**Requires Platform verison 6.7.0 or later.**   Removes a Registry Setting from the Platform. Before removing a setting, you should know how it will affect the Platform.    Learn more about [Platform Registry Settings](/current-managing-registry). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegistryApi()
name = 'name_example' # str | Required. Name of setting

try: 
    # Delete Registry Setting
    api_instance.registry_delete(name)
except ApiException as e:
    print("Exception when calling RegistryApi->registry_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of setting | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_get**
> list[PagedResourceBaseRegistrySetting] registry_get(page_size=page_size, page_number=page_number, search_term=search_term)

Get all Registry Settings

**Requires Platform version 6.7.0 or later.**   Returns all Platform Registry Settings. Learn more about [Platform Registry Settings](/current/managing-registry). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegistryApi()
page_size = 56 # int | Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20 (optional)
page_number = 56 # int | The page of results to return. Defaults to 1, the first page (optional)
search_term = 'search_term_example' # str | Word to use to search for matching settings (optional)

try: 
    # Get all Registry Settings
    api_response = api_instance.registry_get(page_size=page_size, page_number=page_number, search_term=search_term)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->registry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20 | [optional] 
 **page_number** | **int**| The page of results to return. Defaults to 1, the first page | [optional] 
 **search_term** | **str**| Word to use to search for matching settings | [optional] 

### Return type

[**list[PagedResourceBaseRegistrySetting]**](PagedResourceBaseRegistrySetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_get_by_name**
> RegistrySetting registry_get_by_name(name)

Get Registry Setting

**Required Platform version 6.7.0 or later.**   Returns a Registry Setting.   Learn more about [Platform Registry Settings](/current/managing-registry). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegistryApi()
name = 'name_example' # str | Required. Name of the setting

try: 
    # Get Registry Setting
    api_response = api_instance.registry_get_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->registry_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the setting | 

### Return type

[**RegistrySetting**](RegistrySetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_post_new**
> str registry_post_new(setting)

Create new Registry Setting

**Required Platform version 6.7.0 or later.**   Creates a new Platform Registry Setting. This endpoint should be used if you want to add a registry setting that has not already be added to the Platform.   All available settings are described on the [Platform Registry Setting page](/current/managing-registry). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegistryApi()
setting = swagger_client.RegistrySetting() # RegistrySetting | Required. Registry Setting to add

try: 
    # Create new Registry Setting
    api_response = api_instance.registry_post_new(setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->registry_post_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting** | [**RegistrySetting**](RegistrySetting.md)| Required. Registry Setting to add | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registry_put**
> RegistrySetting registry_put(name, setting)

Update Registry Setting

**Required Platform version 6.7.0 or later.**   Updates the Registry Setting. Making a request to this endpoint will update all fields for a setting. You should always pass all input values in the body of the request, because any value that is not provided will be updated to the default value.   All available settings are described on the [Platform Registry Setting page](/current/managing-registry). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RegistryApi()
name = 'name_example' # str | Required. Name of the setting
setting = swagger_client.RegistrySetting() # RegistrySetting | Required. Regirty Setting to update

try: 
    # Update Registry Setting
    api_response = api_instance.registry_put(name, setting)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegistryApi->registry_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Required. Name of the setting | 
 **setting** | [**RegistrySetting**](RegistrySetting.md)| Required. Regirty Setting to update | 

### Return type

[**RegistrySetting**](RegistrySetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

