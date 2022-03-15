# RpmModulemdDefaultsResponse

ModulemdDefaults serializer.
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
**module** | **str** | Modulemd name. | 
**stream** | **str** | Modulemd default stream. | 
**profiles** | [**object**](.md) | Default profiles for modulemd streams. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


