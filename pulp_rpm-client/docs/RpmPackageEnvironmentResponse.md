# RpmPackageEnvironmentResponse

PackageEnvironment serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**id** | **str** | Environment id. | 
**name** | **str** | Environment name. | 
**description** | **str** | Environment description. | 
**display_order** | **int** | Environment display order. | 
**group_ids** | [**object**](.md) | Environment group list. | 
**option_ids** | [**object**](.md) | Environment option ids | 
**desc_by_lang** | [**object**](.md) | Environment description by language. | 
**name_by_lang** | [**object**](.md) | Environment name by language. | 
**digest** | **str** | Environment digest. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


