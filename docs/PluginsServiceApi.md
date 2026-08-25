# kubeapps_client.PluginsServiceApi

All URIs are relative to *http://127.0.0.1:8080/apis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plugins_service_get_configured_plugins**](PluginsServiceApi.md#plugins_service_get_configured_plugins) | **GET** /core/plugins/v1alpha1/configured-plugins | GetConfiguredPlugins returns a map of short and longnames for the configured plugins.

# **plugins_service_get_configured_plugins**
> V1alpha1GetConfiguredPluginsResponse plugins_service_get_configured_plugins()

GetConfiguredPlugins returns a map of short and longnames for the configured plugins.

### Example
```python
from __future__ import print_function
import time
import kubeapps_client
from kubeapps_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = kubeapps_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = kubeapps_client.PluginsServiceApi(kubeapps_client.ApiClient(configuration))

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

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

