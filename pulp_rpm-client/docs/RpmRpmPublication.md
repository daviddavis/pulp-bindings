# RpmRpmPublication

A Serializer for RpmPublication.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_version** | **str** |  | [optional] 
**repository** | **str** | A URI of the repository to be published. | [optional] 
**metadata_checksum_type** | [**MetadataChecksumTypeEnum**](MetadataChecksumTypeEnum.md) | The checksum type for metadata. | [optional] 
**package_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | The checksum type for packages. | [optional] 
**gpgcheck** | **int** | An option specifying whether a client should perform a GPG signature check on packages. | [optional] [default to 0]
**repo_gpgcheck** | **int** | An option specifying whether a client should perform a GPG signature check on the repodata. | [optional] [default to 0]
**sqlite_metadata** | **bool** | An option specifying whether Pulp should generate SQLite metadata. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


