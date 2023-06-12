# V1alpha1ReconciliationOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | The interval with which the package is checked for reconciliation (in time+unit) | [optional] 
**suspend** | **bool** | Whether reconciliation should be suspended until otherwise enabled. This can be utilized to e.g. temporarily ignore chart changes, and prevent a Helm release from getting upgraded | [optional] 
**service_account_name** | **str** | A name for a service account in the same namespace which should be used to perform the reconciliation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

