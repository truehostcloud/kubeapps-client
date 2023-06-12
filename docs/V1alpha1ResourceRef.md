# V1alpha1ResourceRef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The APIVersion directly from the resource has the group and version, eg. \&quot;apps/v1\&quot; or just the version for core resources. | [optional] 
**kind** | **str** | The Kind directly from the templated manifest. Together with the APIVersion this forms the GroupVersionKind. | [optional] 
**name** | **str** | The name of the specific resource in the context of the installed package. | [optional] 
**namespace** | **str** | The namespace of the specific resource in the context of the installed package. In most cases this will be identical to the namespace of the installed package. Exceptions will be non-namespaced resources and packages that install resources in other namespaces for special reasons. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

