# UpdatePackageRepositoryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_repo_ref** | [**AReferenceUniquelyIdentifyingThePackageRepositoryBeingUpdatedTheOnlyRequiredField**](AReferenceUniquelyIdentifyingThePackageRepositoryBeingUpdatedTheOnlyRequiredField.md) |  | [optional] 
**url** | **str** | URL identifying the package repository location. | [optional] 
**description** | **str** | A user-provided description. | [optional] 
**interval** | **str** |  | [optional] 
**tls_config** | [**V1alpha1PackageRepositoryTlsConfig**](V1alpha1PackageRepositoryTlsConfig.md) |  | [optional] 
**auth** | [**V1alpha1PackageRepositoryAuth**](V1alpha1PackageRepositoryAuth.md) |  | [optional] 
**custom_detail** | [**ProtobufAny**](ProtobufAny.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

