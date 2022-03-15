# PulpImportCheck

Check validity of provided import-options.  Provides the ability to check that an import is 'sane' without having to actually create an importer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** | Path to export-tar-gz that will be imported. | [optional] 
**toc** | **str** | Path to a table-of-contents file describing chunks to be validated, reassembled, and imported. | [optional] 
**repo_mapping** | **str** | Mapping of repo names in an export file to the repo names in Pulp. For example, if the export has a repo named &#39;foo&#39; and the repo to import content into was &#39;bar&#39;, the mapping would be \&quot;{&#39;foo&#39;: &#39;bar&#39;}\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


