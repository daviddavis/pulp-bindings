# Purge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished_before** | **datetime** | Purge tasks completed earlier than this timestamp. Format &#39;%Y-%m-%d[T%H:%M:%S]&#39; | [optional] 
**states** | [**list[StatesEnum]**](StatesEnum.md) | List of task-states to be purged. Only &#39;final&#39; states are allowed. | [optional] [default to ["completed"]]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


