# V1alpha1CreateInstalledPackageRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_package_ref** | [**V1alpha1AvailablePackageReference**](V1alpha1AvailablePackageReference.md) |  | [optional] 
**target_context** | [**V1alpha1Context**](V1alpha1Context.md) |  | [optional] 
**name** | **str** |  | [optional] 
**pkg_version_reference** | [**V1alpha1VersionReference**](V1alpha1VersionReference.md) |  | [optional] 
**values** | **str** | An optional serialized values string to be included when templating a package in the format expected by the plugin. Included when the backend format doesn&#x27;t use secrets or configmaps for values or supports both. These values are layered on top of any values refs above, when relevant. | [optional] 
**reconciliation_options** | [**V1alpha1ReconciliationOptions**](V1alpha1ReconciliationOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

