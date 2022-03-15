# RpmRpmRepository

Serializer for Rpm Repositories.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_labels** | [**object**](.md) |  | [optional] 
**name** | **str** | A unique name for this repository. | 
**description** | **str** | An optional description. | [optional] 
**retain_repo_versions** | **int** | Retain X versions of the repository. Default is null which retains all versions. This is provided as a tech preview in Pulp 3 and may change in the future. | [optional] 
**remote** | **str** | An optional remote to use by default when syncing. | [optional] 
**autopublish** | **bool** | Whether to automatically create publications for new repository versions, and update any distributions pointing to this repository. | [optional] [default to False]
**metadata_signing_service** | **str** | A reference to an associated signing service. | [optional] 
**retain_package_versions** | **int** | The number of versions of each package to keep in the repository; older versions will be purged. The default is &#39;0&#39;, which will disable this feature and keep all versions of each package. | [optional] 
**metadata_checksum_type** | [**MetadataChecksumTypeEnum**](MetadataChecksumTypeEnum.md) | The checksum type for metadata. | [optional] 
**package_checksum_type** | [**PackageChecksumTypeEnum**](PackageChecksumTypeEnum.md) | The checksum type for packages. | [optional] 
**gpgcheck** | **int** | An option specifying whether a client should perform a GPG signature check on packages. | [optional] [default to 0]
**repo_gpgcheck** | **int** | An option specifying whether a client should perform a GPG signature check on the repodata. | [optional] [default to 0]
**sqlite_metadata** | **bool** | An option specifying whether Pulp should generate SQLite metadata. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


