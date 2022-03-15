# RpmModulemdResponse

Modulemd serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**md5** | **str** | The MD5 checksum if available. | [optional] [readonly] 
**sha1** | **str** | The SHA-1 checksum if available. | [optional] [readonly] 
**sha224** | **str** | The SHA-224 checksum if available. | [optional] [readonly] 
**sha256** | **str** | The SHA-256 checksum if available. | [optional] [readonly] 
**sha384** | **str** | The SHA-384 checksum if available. | [optional] [readonly] 
**sha512** | **str** | The SHA-512 checksum if available. | [optional] [readonly] 
**artifact** | **str** | Artifact file representing the physical content | [optional] 
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


