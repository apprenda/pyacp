# swagger_client.AddOnsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_add_on**](AddOnsApi.md#add_add_on) | **POST** /api/v1/addons | Create Add-On
[**add_on_get**](AddOnsApi.md#add_on_get) | **GET** /api/v1/addons | Get all Add-Ons
[**add_on_get_by_name**](AddOnsApi.md#add_on_get_by_name) | **GET** /api/v1/addons/{addonAlias} | Get Add-On
[**remove_add_on**](AddOnsApi.md#remove_add_on) | **DELETE** /api/v1/addons/{addonAlias} | Delete Add-On
[**upload_addon_archive_file**](AddOnsApi.md#upload_addon_archive_file) | **PUT** /api/v1/addons/{addonAlias}/archive | Upload Add-On archive


# **add_add_on**
> AddOn add_add_on(addon)

Create Add-On

**Requires Platform version 6.7.0 or later.**   Create a new Add-On for the Platform. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddOnsApi()
addon = swagger_client.AddOnCreationRequest() # AddOnCreationRequest | Required. Add-On to add to the collection

try: 
    # Create Add-On
    api_response = api_instance.add_add_on(addon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->add_add_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon** | [**AddOnCreationRequest**](AddOnCreationRequest.md)| Required. Add-On to add to the collection | 

### Return type

[**AddOn**](AddOn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_on_get**
> list[UnpagedResourceBaseAddOn] add_on_get()

Get all Add-Ons

**Requires Platform version 6.7.0 or later.**   Returns a list of all Add-Ons for the Platform. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddOnsApi()

try: 
    # Get all Add-Ons
    api_response = api_instance.add_on_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->add_on_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UnpagedResourceBaseAddOn]**](UnpagedResourceBaseAddOn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_on_get_by_name**
> AddOn add_on_get_by_name(addon_alias)

Get Add-On

**Requires Platform version 6.7.0 or later.**   Returns the given Add-On.  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddOnsApi()
addon_alias = 'addon_alias_example' # str | Required. Alias of the Add-On to retrieve

try: 
    # Get Add-On
    api_response = api_instance.add_on_get_by_name(addon_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddOnsApi->add_on_get_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_alias** | **str**| Required. Alias of the Add-On to retrieve | 

### Return type

[**AddOn**](AddOn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_add_on**
> remove_add_on(addon_alias)

Delete Add-On

**Requires Platform verison 6.7.0 or later.**   Deletes the given Add-On from the Platform. Note that you can't delete an Add-On if there are provisioned instances belonging to one or more Development Teams.   Learn more about [removing an Add-On from your Platform](/current/addons#delete). 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddOnsApi()
addon_alias = 'addon_alias_example' # str | Required. Alias of the Add-On to delete

try: 
    # Delete Add-On
    api_instance.remove_add_on(addon_alias)
except ApiException as e:
    print("Exception when calling AddOnsApi->remove_add_on: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_alias** | **str**| Required. Alias of the Add-On to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_addon_archive_file**
> upload_addon_archive_file(addon_alias, file)

Upload Add-On archive

**Requires Platform version 6.7.0 or later.**   Uploads an Add-On archive to the Platform. This will replace any binaries attached to the Add-On with the new upload.  

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AddOnsApi()
addon_alias = 'addon_alias_example' # str | Required. Alias of the Add-On to update
file = '/path/to/file.txt' # file | Archive for the Add-on

try: 
    # Upload Add-On archive
    api_instance.upload_addon_archive_file(addon_alias, file)
except ApiException as e:
    print("Exception when calling AddOnsApi->upload_addon_archive_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addon_alias** | **str**| Required. Alias of the Add-On to update | 
 **file** | **file**| Archive for the Add-on | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

