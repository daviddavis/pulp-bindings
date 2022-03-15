# AccessPolicy

Serializer for AccessPolicy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions_assignment** | **list[object]** | List of callables that define the new permissions to be created for new objects.This is deprecated. Use &#x60;creation_hooks&#x60; instead. | [optional] 
**creation_hooks** | **list[object]** | List of callables that may associate user roles for new objects. | [optional] 
**statements** | **list[object]** | List of policy statements defining the policy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


