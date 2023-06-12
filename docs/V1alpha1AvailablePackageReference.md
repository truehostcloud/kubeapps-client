# V1alpha1AvailablePackageReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**V1alpha1Context**](V1alpha1Context.md) |  | [optional] 
**identifier** | **str** | The fully qualified identifier for the available package (ie. a unique name for the context). For some packaging systems (particularly those where an available package is backed by a CR) this will just be the name, but for others such as those where an available package is not backed by a CR (eg. standard helm) it may be necessary to include the repository in the name or even the repo namespace to ensure this is unique. For example two helm repositories can define an \&quot;apache\&quot; chart that is available globally, the names would need to encode that to be unique (ie. \&quot;repoA:apache\&quot; and \&quot;repoB:apache\&quot;). | [optional] 
**plugin** | [**V1alpha1Plugin**](V1alpha1Plugin.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

