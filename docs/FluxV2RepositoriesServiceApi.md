# swagger_client.FluxV2RepositoriesServiceApi

All URIs are relative to *{schema}://{url}:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flux_v2_repositories_service_add_package_repository**](FluxV2RepositoriesServiceApi.md#flux_v2_repositories_service_add_package_repository) | **POST** /apis/plugins/fluxv2/packages/v1alpha1/repositories | AddPackageRepository add an existing package repository to the set of ones already managed by the &#x27;fluxv2&#x27; plugin
[**flux_v2_repositories_service_delete_package_repository**](FluxV2RepositoriesServiceApi.md#flux_v2_repositories_service_delete_package_repository) | **DELETE** /apis/plugins/fluxv2/packages/v1alpha1/repositories/c/{packageRepoRef.context.cluster}/ns/{packageRepoRef.context.namespace}/{packageRepoRef.identifier} | 
[**flux_v2_repositories_service_get_package_repository_detail**](FluxV2RepositoriesServiceApi.md#flux_v2_repositories_service_get_package_repository_detail) | **GET** /apis/plugins/fluxv2/packages/v1alpha1/repositories/c/{packageRepoRef.context.cluster}/ns/{packageRepoRef.context.namespace}/{packageRepoRef.identifier} | 
[**flux_v2_repositories_service_get_package_repository_permissions**](FluxV2RepositoriesServiceApi.md#flux_v2_repositories_service_get_package_repository_permissions) | **GET** /apis/plugins/fluxv2/packages/v1alpha1/repositories/c/{context.cluster}/permissions | 
[**flux_v2_repositories_service_get_package_repository_summaries**](FluxV2RepositoriesServiceApi.md#flux_v2_repositories_service_get_package_repository_summaries) | **GET** /apis/plugins/fluxv2/packages/v1alpha1/repositories | 
[**flux_v2_repositories_service_update_package_repository**](FluxV2RepositoriesServiceApi.md#flux_v2_repositories_service_update_package_repository) | **PUT** /apis/plugins/fluxv2/packages/v1alpha1/repositories/c/{packageRepoRef.context.cluster}/ns/{packageRepoRef.context.namespace}/{packageRepoRef.identifier} | 

# **flux_v2_repositories_service_add_package_repository**
> V1alpha1AddPackageRepositoryResponse flux_v2_repositories_service_add_package_repository(body)

AddPackageRepository add an existing package repository to the set of ones already managed by the 'fluxv2' plugin

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FluxV2RepositoriesServiceApi()
body = swagger_client.V1alpha1AddPackageRepositoryRequest() # V1alpha1AddPackageRepositoryRequest | Request for AddPackageRepository

try:
    # AddPackageRepository add an existing package repository to the set of ones already managed by the 'fluxv2' plugin
    api_response = api_instance.flux_v2_repositories_service_add_package_repository(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FluxV2RepositoriesServiceApi->flux_v2_repositories_service_add_package_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1AddPackageRepositoryRequest**](V1alpha1AddPackageRepositoryRequest.md)| Request for AddPackageRepository | 

### Return type

[**V1alpha1AddPackageRepositoryResponse**](V1alpha1AddPackageRepositoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flux_v2_repositories_service_delete_package_repository**
> V1alpha1DeletePackageRepositoryResponse flux_v2_repositories_service_delete_package_repository(package_repo_ref_context_cluster, package_repo_ref_context_namespace, package_repo_ref_identifier, package_repo_ref_plugin_name=package_repo_ref_plugin_name, package_repo_ref_plugin_version=package_repo_ref_plugin_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FluxV2RepositoriesServiceApi()
package_repo_ref_context_cluster = 'package_repo_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
package_repo_ref_context_namespace = 'package_repo_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
package_repo_ref_identifier = 'package_repo_ref_identifier_example' # str | The fully qualified identifier for the repository (i.e. a unique name for the context).
package_repo_ref_plugin_name = 'package_repo_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`. (optional)
package_repo_ref_plugin_version = 'package_repo_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1 (optional)

try:
    api_response = api_instance.flux_v2_repositories_service_delete_package_repository(package_repo_ref_context_cluster, package_repo_ref_context_namespace, package_repo_ref_identifier, package_repo_ref_plugin_name=package_repo_ref_plugin_name, package_repo_ref_plugin_version=package_repo_ref_plugin_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FluxV2RepositoriesServiceApi->flux_v2_repositories_service_delete_package_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_repo_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **package_repo_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **package_repo_ref_identifier** | **str**| The fully qualified identifier for the repository (i.e. a unique name for the context). | 
 **package_repo_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | [optional] 
 **package_repo_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | [optional] 

### Return type

[**V1alpha1DeletePackageRepositoryResponse**](V1alpha1DeletePackageRepositoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flux_v2_repositories_service_get_package_repository_detail**
> V1alpha1GetPackageRepositoryDetailResponse flux_v2_repositories_service_get_package_repository_detail(package_repo_ref_context_cluster, package_repo_ref_context_namespace, package_repo_ref_identifier, package_repo_ref_plugin_name=package_repo_ref_plugin_name, package_repo_ref_plugin_version=package_repo_ref_plugin_version)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FluxV2RepositoriesServiceApi()
package_repo_ref_context_cluster = 'package_repo_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
package_repo_ref_context_namespace = 'package_repo_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
package_repo_ref_identifier = 'package_repo_ref_identifier_example' # str | The fully qualified identifier for the repository (i.e. a unique name for the context).
package_repo_ref_plugin_name = 'package_repo_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`. (optional)
package_repo_ref_plugin_version = 'package_repo_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1 (optional)

try:
    api_response = api_instance.flux_v2_repositories_service_get_package_repository_detail(package_repo_ref_context_cluster, package_repo_ref_context_namespace, package_repo_ref_identifier, package_repo_ref_plugin_name=package_repo_ref_plugin_name, package_repo_ref_plugin_version=package_repo_ref_plugin_version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FluxV2RepositoriesServiceApi->flux_v2_repositories_service_get_package_repository_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **package_repo_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **package_repo_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **package_repo_ref_identifier** | **str**| The fully qualified identifier for the repository (i.e. a unique name for the context). | 
 **package_repo_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | [optional] 
 **package_repo_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | [optional] 

### Return type

[**V1alpha1GetPackageRepositoryDetailResponse**](V1alpha1GetPackageRepositoryDetailResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flux_v2_repositories_service_get_package_repository_permissions**
> V1alpha1GetPackageRepositoryPermissionsResponse flux_v2_repositories_service_get_package_repository_permissions(context_cluster, context_namespace=context_namespace)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FluxV2RepositoriesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. (optional)

try:
    api_response = api_instance.flux_v2_repositories_service_get_package_repository_permissions(context_cluster, context_namespace=context_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FluxV2RepositoriesServiceApi->flux_v2_repositories_service_get_package_repository_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 

### Return type

[**V1alpha1GetPackageRepositoryPermissionsResponse**](V1alpha1GetPackageRepositoryPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flux_v2_repositories_service_get_package_repository_summaries**
> V1alpha1GetPackageRepositorySummariesResponse flux_v2_repositories_service_get_package_repository_summaries(context_cluster=context_cluster, context_namespace=context_namespace)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FluxV2RepositoriesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. (optional)
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. (optional)

try:
    api_response = api_instance.flux_v2_repositories_service_get_package_repository_summaries(context_cluster=context_cluster, context_namespace=context_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FluxV2RepositoriesServiceApi->flux_v2_repositories_service_get_package_repository_summaries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | [optional] 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 

### Return type

[**V1alpha1GetPackageRepositorySummariesResponse**](V1alpha1GetPackageRepositorySummariesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flux_v2_repositories_service_update_package_repository**
> V1alpha1UpdatePackageRepositoryResponse flux_v2_repositories_service_update_package_repository(body, package_repo_ref_context_cluster, package_repo_ref_context_namespace, package_repo_ref_identifier)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FluxV2RepositoriesServiceApi()
body = NULL # object | 
package_repo_ref_context_cluster = 'package_repo_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
package_repo_ref_context_namespace = 'package_repo_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
package_repo_ref_identifier = 'package_repo_ref_identifier_example' # str | The fully qualified identifier for the repository (i.e. a unique name for the context).

try:
    api_response = api_instance.flux_v2_repositories_service_update_package_repository(body, package_repo_ref_context_cluster, package_repo_ref_context_namespace, package_repo_ref_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FluxV2RepositoriesServiceApi->flux_v2_repositories_service_update_package_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 
 **package_repo_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **package_repo_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **package_repo_ref_identifier** | **str**| The fully qualified identifier for the repository (i.e. a unique name for the context). | 

### Return type

[**V1alpha1UpdatePackageRepositoryResponse**](V1alpha1UpdatePackageRepositoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

