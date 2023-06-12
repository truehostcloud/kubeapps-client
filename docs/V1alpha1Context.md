# V1alpha1Context

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** | A cluster name can be provided to target a specific cluster if multiple clusters are configured, otherwise all clusters will be assumed. | [optional] 
**namespace** | **str** | A namespace must be provided if the context of the operation is for a resource or resources in a particular namespace. For requests to list items, not including a namespace here implies that the context for the request is everything the requesting user can read, though the result can be filtered by any filtering options of the request. Plugins may choose to return Unimplemented for some queries for which we do not yet have a need. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

