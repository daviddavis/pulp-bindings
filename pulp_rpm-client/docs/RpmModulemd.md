# RpmModulemd

Modulemd serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact** | **str** | Artifact file representing the physical content | [optional] 
**relative_path** | **str** | Path where the artifact is located relative to distributions base_path | 
**file** | **file** | An uploaded file that may be turned into the artifact of the content unit. | [optional] 
**repository** | **str** | A URI of a repository the new content unit should be associated with. | [optional] 
**name** | **str** | Modulemd name. | 
**stream** | **str** | Stream name. | 
**version** | **str** | Modulemd version. | 
**static_context** | **bool** | Modulemd static-context flag. | [optional] 
**context** | **str** | Modulemd context. | 
**arch** | **str** | Modulemd architecture. | 
**artifacts** | [**object**](.md) | Modulemd artifacts. | 
**dependencies** | [**object**](.md) | Modulemd dependencies. | 
**packages** | **list[str]** | Modulemd artifacts&#39; packages. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


