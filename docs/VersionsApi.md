# swagger_client.VersionsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_applications_app_alias_versions_get**](VersionsApi.md#api_v1_applications_app_alias_versions_get) | **GET** /api/v1/applications/{appAlias}/versions | Get an application
[**api_v1_applications_app_alias_versions_version_alias_get**](VersionsApi.md#api_v1_applications_app_alias_versions_version_alias_get) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias} | Get an application version


# **api_v1_applications_app_alias_versions_get**
> ApprendaRestAPICommonResourcesPagedResourceBaseVersion api_v1_applications_app_alias_versions_get(app_alias)

Get an application

**Requires Platform version 6.7.0 or later.**   Returns all versions of an application. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
app_alias = 'app_alias_example' # str | Required. Alias of the application

try: 
    # Get an application
    api_response = api_instance.api_v1_applications_app_alias_versions_get(app_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->api_v1_applications_app_alias_versions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of the application | 

### Return type

[**ApprendaRestAPICommonResourcesPagedResourceBaseVersion**](ApprendaRestAPICommonResourcesPagedResourceBaseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_applications_app_alias_versions_version_alias_get**
> Version api_v1_applications_app_alias_versions_version_alias_get(app_alias, version_alias)

Get an application version

**Requires Platform version 6.7.0 or later.**   Returns a version of an application. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
app_alias = 'app_alias_example' # str | Required. Alias of the application
version_alias = 'version_alias_example' # str | Required. Alias of version

try: 
    # Get an application version
    api_response = api_instance.api_v1_applications_app_alias_versions_version_alias_get(app_alias, version_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->api_v1_applications_app_alias_versions_version_alias_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of the application | 
 **version_alias** | **str**| Required. Alias of version | 

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

