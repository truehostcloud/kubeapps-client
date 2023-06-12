# V1alpha1AvailablePackageDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_package_ref** | [**V1alpha1AvailablePackageReference**](V1alpha1AvailablePackageReference.md) |  | [optional] 
**name** | **str** | The name of the available package | [optional] 
**version** | [**V1alpha1PackageAppVersion**](V1alpha1PackageAppVersion.md) |  | [optional] 
**repo_url** | **str** |  | [optional] 
**home_url** | **str** |  | [optional] 
**icon_url** | **str** | A url for an icon. | [optional] 
**display_name** | **str** | A name as displayed to users | [optional] 
**short_description** | **str** | A short description of the app provided by the package | [optional] 
**long_description** | **str** | A longer description of the package, a few sentences. | [optional] 
**readme** | **str** | A longer README with potentially pages of formatted Markdown. | [optional] 
**default_values** | **str** | An example of default values used during package templating that can serve as documentation or a starting point for user customization. | [optional] 
**additional_default_values** | **dict(str, str)** | A package may contain additional default value files for specific scenarios, such as values_production.yaml or values_dev.yaml | [optional] 
**values_schema** | **str** |  | [optional] 
**source_urls** | **list[str]** |  | [optional] 
**maintainers** | [**list[V1alpha1Maintainer]**](V1alpha1Maintainer.md) | List of Maintainer | [optional] 
**categories** | **list[str]** | A user-facing list of category names useful for creating richer user interfaces. Plugins can choose not to implement this | [optional] 
**custom_detail** | [**ProtobufAny**](ProtobufAny.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

