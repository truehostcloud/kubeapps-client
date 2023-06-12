# V1alpha1GetAvailablePackageVersionsResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_app_versions** | [**list[V1alpha1PackageAppVersion]**](V1alpha1PackageAppVersion.md) | By default (when version_query is empty or ignored) the response should contain an ordered summary of versions including the most recent three patch versions of the most recent three minor versions of the most recent three major versions when available, something like: [   { pkg_version: \&quot;10.3.19\&quot;, app_version: \&quot;2.16.8\&quot; },   { pkg_version: \&quot;10.3.18\&quot;, app_version: \&quot;2.16.8\&quot; },   { pkg_version: \&quot;10.3.17\&quot;, app_version: \&quot;2.16.7\&quot; },   { pkg_version: \&quot;10.2.6\&quot;, app_version: \&quot;2.15.3\&quot; },   { pkg_version: \&quot;10.2.5\&quot;, app_version: \&quot;2.15.2\&quot; },   { pkg_version: \&quot;10.2.4\&quot;, app_version: \&quot;2.15.2\&quot; },   { pkg_version: \&quot;10.1.8\&quot;, app_version: \&quot;2.13.5\&quot; },   { pkg_version: \&quot;10.1.7\&quot;, app_version: \&quot;2.13.5\&quot; },   { pkg_version: \&quot;10.1.6\&quot;, app_version: \&quot;2.13.5\&quot; },   { pkg_version: \&quot;9.5.4\&quot;, app_version: \&quot;2.8.9\&quot; },   ...   { pkg_version: \&quot;8.2.5\&quot;, app_version: \&quot;1.19.5\&quot; },   ... ] If a version_query is present and the plugin chooses to support it, the full history of versions matching the version query should be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

