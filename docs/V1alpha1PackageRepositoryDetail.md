# V1alpha1PackageRepositoryDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_repo_ref** | [**V1alpha1PackageRepositoryReference**](V1alpha1PackageRepositoryReference.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** | A user-provided description. | [optional] 
**namespace_scoped** | **bool** | Whether this repository is global or namespace-scoped. | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** | A URL identifying the package repository location. | [optional] 
**interval** | **str** |  | [optional] 
**tls_config** | [**V1alpha1PackageRepositoryTlsConfig**](V1alpha1PackageRepositoryTlsConfig.md) |  | [optional] 
**auth** | [**V1alpha1PackageRepositoryAuth**](V1alpha1PackageRepositoryAuth.md) |  | [optional] 
**custom_detail** | [**ProtobufAny**](ProtobufAny.md) |  | [optional] 
**status** | [**V1alpha1PackageRepositoryStatus**](V1alpha1PackageRepositoryStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

