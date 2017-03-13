# swagger_client.ApplicationsApi

All URIs are relative to *http://apps.apprenda.myhost/soc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_applications_app_alias_versions_get**](ApplicationsApi.md#api_v1_applications_app_alias_versions_get) | **GET** /api/v1/applications/{appAlias}/versions | Get an application
[**api_v1_applications_app_alias_versions_version_alias_get**](ApplicationsApi.md#api_v1_applications_app_alias_versions_version_alias_get) | **GET** /api/v1/applications/{appAlias}/versions/{versionAlias} | Get an application version
[**apps_search_new**](ApplicationsApi.md#apps_search_new) | **GET** /api/v1/applications | Get all applications
[**get_app_by_alias**](ApplicationsApi.md#get_app_by_alias) | **GET** /api/v1/applications/{appAlias} | Get application


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
api_instance = swagger_client.ApplicationsApi()
app_alias = 'app_alias_example' # str | Required. Alias of the application

try: 
    # Get an application
    api_response = api_instance.api_v1_applications_app_alias_versions_get(app_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->api_v1_applications_app_alias_versions_get: %s\n" % e)
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
api_instance = swagger_client.ApplicationsApi()
app_alias = 'app_alias_example' # str | Required. Alias of the application
version_alias = 'version_alias_example' # str | Required. Alias of version

try: 
    # Get an application version
    api_response = api_instance.api_v1_applications_app_alias_versions_version_alias_get(app_alias, version_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->api_v1_applications_app_alias_versions_version_alias_get: %s\n" % e)
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

# **apps_search_new**
> ApprendaRestAPICommonResourcesPagedResourceBaseApplication apps_search_new(filter=filter, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, include_apprenda_apps=include_apprenda_apps, only_search_app_info=only_search_app_info)

Get all applications

**Requires Platform version 6.7.0 or later.**   Returns all applications on the Plaform. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
filter = 'filter_example' # str | Word to search for matching applications (optional)
page_number = 56 # int | The page of results to return. Defaults to 1, the first page (optional)
page_size = 56 # int | Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20 (optional)
sort_order = 'sort_order_example' # str | Determines how results will be sorted. Allowed values: ascending, descending. Default: ascending (optional)
sort_by = 'sort_by_example' # str | Field name to use to sort results. Allowed values: ApplicationAlias (optional)
include_apprenda_apps = true # bool | Determines if Apprenda applications are returned in request. Default: True (optional)
only_search_app_info = true # bool | When true, limits request with a filter word provided to searching only the application name or application alias. When false, all application information and custom properties are searched. Default: True (optional)

try: 
    # Get all applications
    api_response = api_instance.apps_search_new(filter=filter, page_number=page_number, page_size=page_size, sort_order=sort_order, sort_by=sort_by, include_apprenda_apps=include_apprenda_apps, only_search_app_info=only_search_app_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->apps_search_new: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Word to search for matching applications | [optional] 
 **page_number** | **int**| The page of results to return. Defaults to 1, the first page | [optional] 
 **page_size** | **int**| Number of results to return in a single request. All results will be grouped into pages of this size. Default: 20 | [optional] 
 **sort_order** | **str**| Determines how results will be sorted. Allowed values: ascending, descending. Default: ascending | [optional] 
 **sort_by** | **str**| Field name to use to sort results. Allowed values: ApplicationAlias | [optional] 
 **include_apprenda_apps** | **bool**| Determines if Apprenda applications are returned in request. Default: True | [optional] 
 **only_search_app_info** | **bool**| When true, limits request with a filter word provided to searching only the application name or application alias. When false, all application information and custom properties are searched. Default: True | [optional] 

### Return type

[**ApprendaRestAPICommonResourcesPagedResourceBaseApplication**](ApprendaRestAPICommonResourcesPagedResourceBaseApplication.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_by_alias**
> Application get_app_by_alias(app_alias)

Get application

**Requires Platform version 6.7.0 or later.**   Returns information about an application. 

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationsApi()
app_alias = 'app_alias_example' # str | Required. Alias of the application

try: 
    # Get application
    api_response = api_instance.get_app_by_alias(app_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationsApi->get_app_by_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_alias** | **str**| Required. Alias of the application | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

