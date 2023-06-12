# swagger_client.ResourcesServiceApi

All URIs are relative to *{schema}://{url}:{port}*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resources_service_can_i**](ResourcesServiceApi.md#resources_service_can_i) | **POST** /apis/plugins/resources/v1alpha1/c/{context.cluster}/can-i | 
[**resources_service_check_namespace_exists**](ResourcesServiceApi.md#resources_service_check_namespace_exists) | **GET** /apis/plugins/resources/v1alpha1/c/{context.cluster}/ns/{context.namespace} | 
[**resources_service_create_namespace**](ResourcesServiceApi.md#resources_service_create_namespace) | **POST** /apis/plugins/resources/v1alpha1/c/{context.cluster}/ns | 
[**resources_service_create_secret**](ResourcesServiceApi.md#resources_service_create_secret) | **POST** /apis/plugins/resources/v1alpha1/c/{context.cluster}/ns/{context.namespace}/secrets | 
[**resources_service_get_namespace_names**](ResourcesServiceApi.md#resources_service_get_namespace_names) | **GET** /apis/plugins/resources/v1alpha1/c/{cluster}/namespacenames | 
[**resources_service_get_resources**](ResourcesServiceApi.md#resources_service_get_resources) | **GET** /apis/plugins/resources/v1alpha1/{installedPackageRef.plugin.name}/{installedPackageRef.plugin.version}/c/{installedPackageRef.context.cluster}/ns/{installedPackageRef.context.namespace}/{installedPackageRef.identifier} | 
[**resources_service_get_secret_names**](ResourcesServiceApi.md#resources_service_get_secret_names) | **GET** /apis/plugins/resources/v1alpha1/c/{context.cluster}/ns/{context.namespace}/secretnames | 
[**resources_service_get_service_account_names**](ResourcesServiceApi.md#resources_service_get_service_account_names) | **GET** /apis/plugins/resources/v1alpha1/c/{context.cluster}/ns/{context.namespace}/serviceaccountnames | 

# **resources_service_can_i**
> V1alpha1CanIResponse resources_service_can_i(context_cluster, context_namespace=context_namespace, group=group, resource=resource, verb=verb)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. (optional)
group = 'group_example' # str | Group API Group of the Resource.  \"*\" means all. +optional (optional)
resource = 'resource_example' # str | Resource is one of the existing resource types.  \"*\" means all. +optional (optional)
verb = 'verb_example' # str | Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \"*\" means all. +optional (optional)

try:
    api_response = api_instance.resources_service_can_i(context_cluster, context_namespace=context_namespace, group=group, resource=resource, verb=verb)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_can_i: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 
 **group** | **str**| Group API Group of the Resource.  \&quot;*\&quot; means all. +optional | [optional] 
 **resource** | **str**| Resource is one of the existing resource types.  \&quot;*\&quot; means all. +optional | [optional] 
 **verb** | **str**| Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy.  \&quot;*\&quot; means all. +optional | [optional] 

### Return type

[**V1alpha1CanIResponse**](V1alpha1CanIResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_check_namespace_exists**
> V1alpha1CheckNamespaceExistsResponse resources_service_check_namespace_exists(context_cluster, context_namespace)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.

try:
    api_response = api_instance.resources_service_check_namespace_exists(context_cluster, context_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_check_namespace_exists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 

### Return type

[**V1alpha1CheckNamespaceExistsResponse**](V1alpha1CheckNamespaceExistsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_create_namespace**
> V1alpha1CreateNamespaceResponse resources_service_create_namespace(context_cluster, context_namespace=context_namespace)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. (optional)

try:
    api_response = api_instance.resources_service_create_namespace(context_cluster, context_namespace=context_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_create_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 

### Return type

[**V1alpha1CreateNamespaceResponse**](V1alpha1CreateNamespaceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_create_secret**
> V1alpha1CreateSecretResponse resources_service_create_secret(context_cluster, context_namespace, type=type, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
type = 'SECRET_TYPE_OPAQUE_UNSPECIFIED' # str | Type  The type of the secret. Valid values are defined by the Type enumeration. (optional) (default to SECRET_TYPE_OPAQUE_UNSPECIFIED)
name = 'name_example' # str | Name  The name of the secret. (optional)

try:
    api_response = api_instance.resources_service_create_secret(context_cluster, context_namespace, type=type, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_create_secret: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **type** | **str**| Type  The type of the secret. Valid values are defined by the Type enumeration. | [optional] [default to SECRET_TYPE_OPAQUE_UNSPECIFIED]
 **name** | **str**| Name  The name of the secret. | [optional] 

### Return type

[**V1alpha1CreateSecretResponse**](V1alpha1CreateSecretResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_get_namespace_names**
> V1alpha1GetNamespaceNamesResponse resources_service_get_namespace_names(cluster)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
cluster = 'cluster_example' # str | Cluster  The context for which the namespace names are being fetched.  The service will attempt to list namespaces across the cluster, first with the users credential, then with a configured service account if available.

try:
    api_response = api_instance.resources_service_get_namespace_names(cluster)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_get_namespace_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | **str**| Cluster  The context for which the namespace names are being fetched.  The service will attempt to list namespaces across the cluster, first with the users credential, then with a configured service account if available. | 

### Return type

[**V1alpha1GetNamespaceNamesResponse**](V1alpha1GetNamespaceNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_get_resources**
> StreamResultOfV1alpha1GetResourcesResponse resources_service_get_resources(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier, watch=watch)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
installed_package_ref_plugin_name = 'installed_package_ref_plugin_name_example' # str | Plugin name  The name of the plugin, such as `fluxv2.packages` or `kapp_controller.packages`.
installed_package_ref_plugin_version = 'installed_package_ref_plugin_version_example' # str | Plugin version  The version of the plugin, such as v1alpha1
installed_package_ref_context_cluster = 'installed_package_ref_context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
installed_package_ref_context_namespace = 'installed_package_ref_context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.
installed_package_ref_identifier = 'installed_package_ref_identifier_example' # str | The fully qualified identifier for the installed package (ie. a unique name for the context).
watch = true # bool | Watch  When true, this will cause the stream to remain open with updated resources being sent as events are received from the Kubernetes API server. (optional)

try:
    api_response = api_instance.resources_service_get_resources(installed_package_ref_plugin_name, installed_package_ref_plugin_version, installed_package_ref_context_cluster, installed_package_ref_context_namespace, installed_package_ref_identifier, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_get_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installed_package_ref_plugin_name** | **str**| Plugin name  The name of the plugin, such as &#x60;fluxv2.packages&#x60; or &#x60;kapp_controller.packages&#x60;. | 
 **installed_package_ref_plugin_version** | **str**| Plugin version  The version of the plugin, such as v1alpha1 | 
 **installed_package_ref_context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **installed_package_ref_context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 
 **installed_package_ref_identifier** | **str**| The fully qualified identifier for the installed package (ie. a unique name for the context). | 
 **watch** | **bool**| Watch  When true, this will cause the stream to remain open with updated resources being sent as events are received from the Kubernetes API server. | [optional] 

### Return type

[**StreamResultOfV1alpha1GetResourcesResponse**](StreamResultOfV1alpha1GetResourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_get_secret_names**
> V1alpha1GetSecretNamesResponse resources_service_get_secret_names(context_cluster, context_namespace)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.

try:
    api_response = api_instance.resources_service_get_secret_names(context_cluster, context_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_get_secret_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 

### Return type

[**V1alpha1GetSecretNamesResponse**](V1alpha1GetSecretNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resources_service_get_service_account_names**
> V1alpha1GetServiceAccountNamesResponse resources_service_get_service_account_names(context_cluster, context_namespace)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ResourcesServiceApi()
context_cluster = 'context_cluster_example' # str | Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed.
context_namespace = 'context_namespace_example' # str | Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need.

try:
    api_response = api_instance.resources_service_get_service_account_names(context_cluster, context_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResourcesServiceApi->resources_service_get_service_account_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **context_cluster** | **str**| Cluster  A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | 
 **context_namespace** | **str**| Namespace  A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | 

### Return type

[**V1alpha1GetServiceAccountNamesResponse**](V1alpha1GetServiceAccountNamesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

