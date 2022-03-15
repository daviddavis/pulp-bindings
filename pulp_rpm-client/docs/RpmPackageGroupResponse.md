# RpmPackageGroupResponse

PackageGroup serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**id** | **str** | PackageGroup id. | 
**default** | **bool** | PackageGroup default. | [optional] 
**user_visible** | **bool** | PackageGroup user visibility. | [optional] 
**display_order** | **int** | PackageGroup display order. | 
**name** | **str** | PackageGroup name. | 
**description** | **str** | PackageGroup description. | 
**packages** | [**object**](.md) | PackageGroup package list. | 
**biarch_only** | **bool** | PackageGroup biarch only. | [optional] 
**desc_by_lang** | [**object**](.md) | PackageGroup description by language. | 
**name_by_lang** | [**object**](.md) | PackageGroup name by language. | 
**digest** | **str** | PackageGroup digest. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


