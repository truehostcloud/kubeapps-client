# kubeapps_client.PackagesServiceApi

All URIs are relative to *http://127.0.0.1:8080/apis*

Method | HTTP request | Description
------------- | ------------- | -------------
[**packages_service_create_installed_package**](PackagesServiceApi.md#packages_service_create_installed_package) | **POST** /core/packages/v1alpha1/installedpackages | 
[**packages_service_delete_installed_package**](PackagesServiceApi.md#packages_service_delete_installed_package) | **DELETE** /core/packages/v1alpha1/installedpackages/plugin/{installedPackageRef.plugin.name}/{installedPackageRef.plugin.version}/c/{installedPackageRef.context.cluster}/ns/{installedPackageRef.context.namespace}/{installedPackageRef.identifier} | 
[**packages_service_get_available_package_detail**](PackagesServiceApi.md#packages_service_get_available_package_detail) | **GET** /core/packages/v1alpha1/availablepackages/plugin/{availablePackageRef.plugin.name}/{availablePackageRef.plugin.version}/c/{availablePackageRef.context.cluster}/ns/{availablePackageRef.context.namespace}/{availablePackageRef.identifier} | 
[**packages_service_get_available_package_metadatas**](PackagesServiceApi.md#packages_service_get_available_package_metadatas) | **GET** /core/packages/v1alpha1/availablepackages/plugin/{availablePackageRef.plugin.name}/{availablePackageRef.plugin.version}/c/{availablePackageRef.context.cluster}/ns/{availablePackageRef.context.namespace}/{availablePackageRef.identifier}/metadata | 
[**packages_service_get_available_package_summaries**](PackagesServiceApi.md#packages_service_get_available_package_summaries) | **GET** /core/packages/v1alpha1/availablepackages | 
[**packages_service_get_available_package_versions**](PackagesServiceApi.md#packages_service_get_available_package_versions) | **GET** /core/packages/v1alpha1/availablepackages/plugin/{availablePackageRef.plugin.name}/{availablePackageRef.plugin.version}/c/{availablePackageRef.context.cluster}/ns/{availablePackageRef.context.namespace}/{availablePackageRef.identifier}/versions | 
[**packages_service_get_installed_package_detail**](PackagesServiceApi.md#packages_service_get_installed_package_detail) | **GET** /core/packages/v1alpha1/installedpackages/plugin/{installedPackageRef.plugin.name}/{installedPackageRef.plugin.version}/c/{installedPackageRef.context.cluster}/ns/{installedPackageRef.context.namespace}/{installedPackageRef.identifier} | 
[**packages_service_get_installed_package_resource_refs**](PackagesServiceApi.md#packages_service_get_installed_package_resource_refs) | **GET** /core/packages/v1alpha1/installedpackages/plugin/{installedPackageRef.plugin.name}/{installedPackageRef.plugin.version}/c/{installedPackageRef.context.cluster}/ns/{installedPackageRef.context.namespace}/{installedPackageRef.identifier}/resourcerefs | 
[**packages_service_get_installed_package_summaries**](PackagesServiceApi.md#packages_service_get_installed_package_summaries) | **GET** /core/packages/v1alpha1/installedpackages | 
[**packages_service_update_installed_package**](PackagesServiceApi.md#packages_service_update_installed_package) | **PUT** /core/packages/v1alpha1/installedpackages/plugin/{installedPackageRef.plugin.name}/{installedPackageRef.plugin.version}/c/{installedPackageRef.context.cluster}/ns/{installedPackageRef.context.namespace}/{installedPackageRef.identifier} | 

# **packages_service_create_installed_package**
> V1alpha1CreateInstalledPackageResponse packages_service_create_installed_package(body)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
body = kubeapps_client.V1alpha1CreateInstalledPackageRequest() # V1alpha1CreateInstalledPackageRequest | Request for CreateInstalledPackage

try:
    api_response = api_instance.packages_service_create_installed_package(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_create_installed_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1CreateInstalledPackageRequest**](V1alpha1CreateInstalledPackageRequest.md)| Request for CreateInstalledPackage | 

### Return type

[**V1alpha1CreateInstalledPackageResponse**](V1alpha1CreateInstalledPackageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_delete_installed_package**
> V1alpha1DeleteInstalledPackageResponse packages_service_delete_installed_package(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
installed_package_ref_plugin_name = 'installed_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
installed_package_ref_plugin_version = 'installed_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
installed_package_ref_context_cluster = 'installed_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
installed_package_ref_context_namespace = 'installed_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
installed_package_ref_identifier = 'installed_package_ref_identifier_example' # str | The fully qualified identifier for the installed package (ie. a unique name for the context).

try:
    api_response = api_instance.packages_service_delete_installed_package(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_delete_installed_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installed_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **installed_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **installed_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **installed_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **installed_package_ref_identifier** | **str**| The fully qualified identifier for the installed package (ie. a unique name for the context). | 

### Return type

[**V1alpha1DeleteInstalledPackageResponse**](V1alpha1DeleteInstalledPackageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_available_package_detail**
> V1alpha1GetAvailablePackageDetailResponse packages_service_get_available_package_detail(available_package_ref_plugin_name, available_package_ref_plugin_version, available_package_ref_context_cluster, available_package_ref_context_namespace, available_package_ref_identifier, pkg_version=pkg_version)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
available_package_ref_plugin_name = 'available_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
available_package_ref_plugin_version = 'available_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
available_package_ref_context_cluster = 'available_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
available_package_ref_context_namespace = 'available_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
available_package_ref_identifier = 'available_package_ref_identifier_example' # str | Available package identifier  The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \"apache\" chart that is available globally, the names would need to encode that to be unique (ie. \"repoA:apache\" and \"repoB:apache\").
pkg_version = 'pkg_version_example' # str | Optional specific version (or version reference) to request. By default the latest version (or latest version matching the reference) will be returned. (optional)

try:
    api_response = api_instance.packages_service_get_available_package_detail(available_package_ref_plugin_name, available_package_ref_plugin_version, available_package_ref_context_cluster, available_package_ref_context_namespace, available_package_ref_identifier, pkg_version=pkg_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_available_package_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **available_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **available_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **available_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **available_package_ref_identifier** | **str**| Available package identifier  The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \&quot;apache\&quot; chart that is available globally, the names would need to encode that to be unique (ie. \&quot;repoA:apache\&quot; and \&quot;repoB:apache\&quot;). | 
 **pkg_version** | **str**| Optional specific version (or version reference) to request. By default the latest version (or latest version matching the reference) will be returned. | [optional] 

### Return type

[**V1alpha1GetAvailablePackageDetailResponse**](V1alpha1GetAvailablePackageDetailResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_available_package_metadatas**
> V1alpha1GetAvailablePackageMetadatasResponse packages_service_get_available_package_metadatas(available_package_ref_plugin_name, available_package_ref_plugin_version, available_package_ref_context_cluster, available_package_ref_context_namespace, available_package_ref_identifier, pkg_version=pkg_version)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
available_package_ref_plugin_name = 'available_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
available_package_ref_plugin_version = 'available_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
available_package_ref_context_cluster = 'available_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
available_package_ref_context_namespace = 'available_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
available_package_ref_identifier = 'available_package_ref_identifier_example' # str | Available package identifier  The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \"apache\" chart that is available globally, the names would need to encode that to be unique (ie. \"repoA:apache\" and \"repoB:apache\").
pkg_version = 'pkg_version_example' # str | Package Version  Version reference for which metadata is requested. (optional)

try:
    api_response = api_instance.packages_service_get_available_package_metadatas(available_package_ref_plugin_name, available_package_ref_plugin_version, available_package_ref_context_cluster, available_package_ref_context_namespace, available_package_ref_identifier, pkg_version=pkg_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_available_package_metadatas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **available_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **available_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **available_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **available_package_ref_identifier** | **str**| Available package identifier  The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \&quot;apache\&quot; chart that is available globally, the names would need to encode that to be unique (ie. \&quot;repoA:apache\&quot; and \&quot;repoB:apache\&quot;). | 
 **pkg_version** | **str**| Package Version  Version reference for which metadata is requested. | [optional] 

### Return type

[**V1alpha1GetAvailablePackageMetadatasResponse**](V1alpha1GetAvailablePackageMetadatasResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_available_package_summaries**
> V1alpha1GetAvailablePackageSummariesResponse packages_service_get_available_package_summaries(context_cluster=context_cluster, context_namespace=context_namespace, filter_options_query=filter_options_query, filter_options_categories=filter_options_categories, filter_options_repositories=filter_options_repositories, filter_options_pkg_version=filter_options_pkg_version, filter_options_app_version=filter_options_app_version, pagination_options_page_token=pagination_options_page_token, pagination_options_page_size=pagination_options_page_size)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. (optional)
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. (optional)
filter_options_query = 'filter_options_query_example' # str | Text query  Text query for the request (optional)
filter_options_categories = ['filter_options_categories_example'] # list[str] | Categories  Collection of categories for the request (optional)
filter_options_repositories = ['filter_options_repositories_example'] # list[str] | Repositories  Collection of repositories where the packages belong to (optional)
filter_options_pkg_version = 'filter_options_pkg_version_example' # str | Package version  Package version for the request (optional)
filter_options_app_version = 'filter_options_app_version_example' # str | App version  Packaged app version for the request (optional)
pagination_options_page_token = 'pagination_options_page_token_example' # str | Page token  The client uses this field to request a specific page of the list results. (optional)
pagination_options_page_size = 56 # int | Page size  Clients use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page. If the page_size is 0, the server will decide the number of results to be returned. (optional)

try:
    api_response = api_instance.packages_service_get_available_package_summaries(context_cluster=context_cluster, context_namespace=context_namespace, filter_options_query=filter_options_query, filter_options_categories=filter_options_categories, filter_options_repositories=filter_options_repositories, filter_options_pkg_version=filter_options_pkg_version, filter_options_app_version=filter_options_app_version, pagination_options_page_token=pagination_options_page_token, pagination_options_page_size=pagination_options_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_available_package_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | [optional] 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 
 **filter_options_query** | **str**| Text query  Text query for the request | [optional] 
 **filter_options_categories** | [**list[str]**](str.md)| Categories  Collection of categories for the request | [optional] 
 **filter_options_repositories** | [**list[str]**](str.md)| Repositories  Collection of repositories where the packages belong to | [optional] 
 **filter_options_pkg_version** | **str**| Package version  Package version for the request | [optional] 
 **filter_options_app_version** | **str**| App version  Packaged app version for the request | [optional] 
 **pagination_options_page_token** | **str**| Page token  The client uses this field to request a specific page of the list results. | [optional] 
 **pagination_options_page_size** | **int**| Page size  Clients use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page. If the page_size is 0, the server will decide the number of results to be returned. | [optional] 

### Return type

[**V1alpha1GetAvailablePackageSummariesResponse**](V1alpha1GetAvailablePackageSummariesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_available_package_versions**
> V1alpha1GetAvailablePackageVersionsResponse packages_service_get_available_package_versions(available_package_ref_plugin_name, available_package_ref_plugin_version, available_package_ref_context_cluster, available_package_ref_context_namespace, available_package_ref_identifier, pkg_version=pkg_version)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
available_package_ref_plugin_name = 'available_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
available_package_ref_plugin_version = 'available_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
available_package_ref_context_cluster = 'available_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
available_package_ref_context_namespace = 'available_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
available_package_ref_identifier = 'available_package_ref_identifier_example' # str | Available package identifier  The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \"apache\" chart that is available globally, the names would need to encode that to be unique (ie. \"repoA:apache\" and \"repoB:apache\").
pkg_version = 'pkg_version_example' # str | Optional version reference for which full version history is required.  By default a summary of versions is returned as outlined in the response. Plugins can choose not to implement this and provide the summary only, it is provided for completeness only. (optional)

try:
    api_response = api_instance.packages_service_get_available_package_versions(available_package_ref_plugin_name, available_package_ref_plugin_version, available_package_ref_context_cluster, available_package_ref_context_namespace, available_package_ref_identifier, pkg_version=pkg_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_available_package_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **available_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **available_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **available_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **available_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **available_package_ref_identifier** | **str**| Available package identifier  The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \&quot;apache\&quot; chart that is available globally, the names would need to encode that to be unique (ie. \&quot;repoA:apache\&quot; and \&quot;repoB:apache\&quot;). | 
 **pkg_version** | **str**| Optional version reference for which full version history is required.  By default a summary of versions is returned as outlined in the response. Plugins can choose not to implement this and provide the summary only, it is provided for completeness only. | [optional] 

### Return type

[**V1alpha1GetAvailablePackageVersionsResponse**](V1alpha1GetAvailablePackageVersionsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_installed_package_detail**
> V1alpha1GetInstalledPackageDetailResponse packages_service_get_installed_package_detail(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
installed_package_ref_plugin_name = 'installed_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
installed_package_ref_plugin_version = 'installed_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
installed_package_ref_context_cluster = 'installed_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
installed_package_ref_context_namespace = 'installed_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
installed_package_ref_identifier = 'installed_package_ref_identifier_example' # str | The fully qualified identifier for the installed package (ie. a unique name for the context).

try:
    api_response = api_instance.packages_service_get_installed_package_detail(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_installed_package_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installed_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **installed_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **installed_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **installed_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **installed_package_ref_identifier** | **str**| The fully qualified identifier for the installed package (ie. a unique name for the context). | 

### Return type

[**V1alpha1GetInstalledPackageDetailResponse**](V1alpha1GetInstalledPackageDetailResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_installed_package_resource_refs**
> V1alpha1GetInstalledPackageResourceRefsResponse packages_service_get_installed_package_resource_refs(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
installed_package_ref_plugin_name = 'installed_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
installed_package_ref_plugin_version = 'installed_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
installed_package_ref_context_cluster = 'installed_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
installed_package_ref_context_namespace = 'installed_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
installed_package_ref_identifier = 'installed_package_ref_identifier_example' # str | The fully qualified identifier for the installed package (ie. a unique name for the context).

try:
    api_response = api_instance.packages_service_get_installed_package_resource_refs(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_installed_package_resource_refs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installed_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **installed_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **installed_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **installed_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **installed_package_ref_identifier** | **str**| The fully qualified identifier for the installed package (ie. a unique name for the context). | 

### Return type

[**V1alpha1GetInstalledPackageResourceRefsResponse**](V1alpha1GetInstalledPackageResourceRefsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_get_installed_package_summaries**
> V1alpha1GetInstalledPackageSummariesResponse packages_service_get_installed_package_summaries(context_cluster=context_cluster, context_namespace=context_namespace, pagination_options_page_token=pagination_options_page_token, pagination_options_page_size=pagination_options_page_size)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. (optional)
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. (optional)
pagination_options_page_token = 'pagination_options_page_token_example' # str | Page token  The client uses this field to request a specific page of the list results. (optional)
pagination_options_page_size = 56 # int | Page size  Clients use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page. If the page_size is 0, the server will decide the number of results to be returned. (optional)

try:
    api_response = api_instance.packages_service_get_installed_package_summaries(context_cluster=context_cluster, context_namespace=context_namespace, pagination_options_page_token=pagination_options_page_token, pagination_options_page_size=pagination_options_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_get_installed_package_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | [optional] 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 
 **pagination_options_page_token** | **str**| Page token  The client uses this field to request a specific page of the list results. | [optional] 
 **pagination_options_page_size** | **int**| Page size  Clients use this field to specify the maximum number of results to be returned by the server. The server may further constrain the maximum number of results returned in a single page. If the page_size is 0, the server will decide the number of results to be returned. | [optional] 

### Return type

[**V1alpha1GetInstalledPackageSummariesResponse**](V1alpha1GetInstalledPackageSummariesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **packages_service_update_installed_package**
> V1alpha1UpdateInstalledPackageResponse packages_service_update_installed_package(body, installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)



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
api_instance = kubeapps_client.PackagesServiceApi(kubeapps_client.ApiClient(configuration))
body = kubeapps_client.V1alpha1PackagesServiceUpdateInstalledPackageBody() # V1alpha1PackagesServiceUpdateInstalledPackageBody | 
installed_package_ref_plugin_name = 'installed_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
installed_package_ref_plugin_version = 'installed_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
installed_package_ref_context_cluster = 'installed_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
installed_package_ref_context_namespace = 'installed_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
installed_package_ref_identifier = 'installed_package_ref_identifier_example' # str | The fully qualified identifier for the installed package (ie. a unique name for the context).

try:
    api_response = api_instance.packages_service_update_installed_package(body, installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PackagesServiceApi->packages_service_update_installed_package: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1PackagesServiceUpdateInstalledPackageBody**](V1alpha1PackagesServiceUpdateInstalledPackageBody.md)|  | 
 **installed_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **installed_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **installed_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **installed_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **installed_package_ref_identifier** | **str**| The fully qualified identifier for the installed package (ie. a unique name for the context). | 

### Return type

[**V1alpha1UpdateInstalledPackageResponse**](V1alpha1UpdateInstalledPackageResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

