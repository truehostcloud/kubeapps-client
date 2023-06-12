# swagger_client.PluginsServiceApi

All URIs are relative to *{schema}://{url}:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugins_service_get_configured_plugins**](PluginsServiceApi.md#plugins_service_get_configured_plugins) | **GET** /apis/core/plugins/v1alpha1/configured-plugins | GetConfiguredPlugins returns a map of short and longnames for the configured plugins.

# **plugins_service_get_configured_plugins**
> V1alpha1GetConfiguredPluginsResponse plugins_service_get_configured_plugins()

GetConfiguredPlugins returns a map of short and longnames for the configured plugins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PluginsServiceApi()

try:
    # GetConfiguredPlugins returns a map of short and longnames for the configured plugins.
    api_response = api_instance.plugins_service_get_configured_plugins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PluginsServiceApi->plugins_service_get_configured_plugins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1alpha1GetConfiguredPluginsResponse**](V1alpha1GetConfiguredPluginsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

