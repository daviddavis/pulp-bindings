# RpmModulemdDefaults

ModulemdDefaults serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | 
**file** | **file** | An uploaded file that may be turned into the artifact of the content unit. | [optional] 
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**module** | **str** | Modulemd name. | 
**stream** | **str** | Modulemd default stream. | 
**profiles** | [**object**](.md) | Default profiles for modulemd streams. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


