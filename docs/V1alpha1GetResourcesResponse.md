# V1alpha1GetResourcesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_ref** | [**V1alpha1ResourceRef**](V1alpha1ResourceRef.md) |  | [optional] 
**manifest** | **str** | The current manifest of the requested resource.  Initially the JSON manifest will be returned a json-encoded string, enabling the existing Kubeapps UI to replace its current direct api-server getting and watching of resources, but we may in the future pull out further structured metadata into this message as needed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

