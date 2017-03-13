# pyacp.CustomPropertiesApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_property**](CustomPropertiesApi.md#add_custom_property) | **POST** /api/v1/customproperties | Add a new Custom Property
[**custom_properties_get_public**](CustomPropertiesApi.md#custom_properties_get_public) | **GET** /api/v1/customproperties | Get all Custom Properties
[**custom_properties_get_single_public**](CustomPropertiesApi.md#custom_properties_get_single_public) | **GET** /api/v1/customproperties/{id} | Get Custom Property
[**custom_properties_remove**](CustomPropertiesApi.md#custom_properties_remove) | **DELETE** /api/v1/customproperties/{id} | Delete a Custom Property
[**update_custom_property**](CustomPropertiesApi.md#update_custom_property) | **PUT** /api/v1/customproperties/{id} | Update a Custom Property


# **add_custom_property**
> CustomProperty add_custom_property(custom_property)

Add a new Custom Property

**Requires Platform version 6.7.0 or later.**   Adds a new Custom Property to the Platform.   Learn more about [Custom Properties](/current/custom-properties). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.CustomPropertiesApi()
custom_property = pyacp.CustomProperty() # CustomProperty | Required. Custom Property to add

try: 
    # Add a new Custom Property
    api_response = api_instance.add_custom_property(custom_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomPropertiesApi->add_custom_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_property** | [**CustomProperty**](CustomProperty.md)| Required. Custom Property to add | 

### Return type

[**CustomProperty**](CustomProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_properties_get_public**
> PagedResourceBaseCustomProperty custom_properties_get_public(type=type, page_size=page_size, page_number=page_number)

Get all Custom Properties

**Requires Platform version 6.7.0 or later.**   Returns all Custom Properties available on the Platform.   Learn more about [Custom Properties](/current/custom-properties). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.CustomPropertiesApi()
type = ['type_example'] # list[str] | A comma-separated list of applicability options to filter on. (optional)
page_size = 56 # int | Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20 (optional)
page_number = 56 # int | The page of results to return. Defaults to 1, the first page (optional)

try: 
    # Get all Custom Properties
    api_response = api_instance.custom_properties_get_public(type=type, page_size=page_size, page_number=page_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomPropertiesApi->custom_properties_get_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[str]**](str.md)| A comma-separated list of applicability options to filter on. | [optional] 
 **page_size** | **int**| Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20 | [optional] 
 **page_number** | **int**| The page of results to return. Defaults to 1, the first page | [optional] 

### Return type

[**PagedResourceBaseCustomProperty**](PagedResourceBaseCustomProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_properties_get_single_public**
> CustomProperty custom_properties_get_single_public(id)

Get Custom Property

**Requires Platform version 6.7.0 or later.**   Returns a Custom Property.   Learn more about [Custom Properties](/current/custom-properties). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.CustomPropertiesApi()
id = 56 # int | Required. Id of the Custom Property

try: 
    # Get Custom Property
    api_response = api_instance.custom_properties_get_single_public(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomPropertiesApi->custom_properties_get_single_public: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Required. Id of the Custom Property | 

### Return type

[**CustomProperty**](CustomProperty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_properties_remove**
> custom_properties_remove(id)

Delete a Custom Property

**Requires Platform version 6.7.0 or later.**   Deletes a Custom Property from the Platform. A Custom Property can't be deleted if it is referenced by any [Application Deployment Policy](/current/app-deployment-policies). Before deleting, make sure the Custom Property is not being referenced by an Application Deployment Policy.   Learn more about [managing Custom Properties](/current/custom-properties#managing). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.CustomPropertiesApi()
id = 56 # int | 

try: 
    # Delete a Custom Property
    api_instance.custom_properties_remove(id)
except ApiException as e:
    print("Exception when calling CustomPropertiesApi->custom_properties_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_property**
> update_custom_property(id, custom_property)

Update a Custom Property

**Requires Platform version 6.7.0 or later.**   Updates a Custom Property. If a Custom Property is referenced by an active [Application Deployment Policy](/current/app-deployment-policies), it can't be edited. Before making changes, you must set any referncing Application Deployment Policies to \"Inactive\" or remove the Custom Property from the policy all together.   Additionally, making a request to this endpoint will update all fields for a Custom Property. You should always pass all input values in the body of the request, because any value that is not provided will be updated to the default value.    Learn more about [managing Custom Properties](/current/custom-properties#managing). 

### Example 
```python
from __future__ import print_statement
import time
import pyacp
from pyacp.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pyacp.CustomPropertiesApi()
id = 56 # int | Required. Id of the Custom Property
custom_property = pyacp.CustomPropertyUpdate() # CustomPropertyUpdate | Custom Property to update

try: 
    # Update a Custom Property
    api_instance.update_custom_property(id, custom_property)
except ApiException as e:
    print("Exception when calling CustomPropertiesApi->update_custom_property: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Required. Id of the Custom Property | 
 **custom_property** | [**CustomPropertyUpdate**](CustomPropertyUpdate.md)| Custom Property to update | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

