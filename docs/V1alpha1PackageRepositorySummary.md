# V1alpha1PackageRepositorySummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_repo_ref** | [**V1alpha1PackageRepositoryReference**](V1alpha1PackageRepositoryReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | A user-provided description. | [optional] 
**namespace_scoped** | **bool** | Whether this repository is global or namespace-scoped. | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** | URL identifying the package repository location. | [optional] 
**status** | [**V1alpha1PackageRepositoryStatus**](V1alpha1PackageRepositoryStatus.md) |  | [optional] 
**requires_auth** | **bool** | existence of any authentication parameters for connecting to a repository. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

