# swagger_client.CloudsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clouds_get_by_id_p_ublic**](CloudsApi.md#clouds_get_by_id_p_ublic) | **GET** /api/v1/clouds/{id} | Get cloud
[**clouds_get_public**](CloudsApi.md#clouds_get_public) | **GET** /api/v1/clouds | Get clouds


# **clouds_get_by_id_p_ublic**
> Cloud clouds_get_by_id_p_ublic(id)

Get cloud

**Requires Platform version 6.7.0 or later.**   Retrieve a cloud by its ID. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudsApi()
id = 56 # int | 

try: 
    # Get cloud
    api_response = api_instance.clouds_get_by_id_p_ublic(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudsApi->clouds_get_by_id_p_ublic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Cloud**](Cloud.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clouds_get_public**
> list[UnpagedResourceBaseCloud] clouds_get_public()

Get clouds

**Requires Platform version 6.7.0 or later.**   Retrieve all clouds in the Platform. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CloudsApi()

try: 
    # Get clouds
    api_response = api_instance.clouds_get_public()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudsApi->clouds_get_public: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UnpagedResourceBaseCloud]**](UnpagedResourceBaseCloud.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

