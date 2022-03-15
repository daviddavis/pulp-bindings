# AccessPolicyResponse

Serializer for AccessPolicy.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**permissions_assignment** | **list[object]** | List of callables that define the new permissions to be created for new objects.This is deprecated. Use &#x60;creation_hooks&#x60; instead. | [optional] 
**creation_hooks** | **list[object]** | List of callables that may associate user roles for new objects. | [optional] 
**statements** | **list[object]** | List of policy statements defining the policy. | 
**viewset_name** | **str** | The name of ViewSet this AccessPolicy authorizes. | [optional] [readonly] 
**customized** | **bool** | True if the AccessPolicy has been user-modified. False otherwise. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


