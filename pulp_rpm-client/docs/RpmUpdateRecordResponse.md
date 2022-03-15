# RpmUpdateRecordResponse

A Serializer for UpdateRecord.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**pulp_created** | **datetime** | Timestamp of creation. | [optional] [readonly] 
**id** | **str** | Update id (short update name, e.g. RHEA-2013:1777) | [optional] [readonly] 
**updated_date** | **str** | Date when the update was updated (e.g. &#39;2013-12-02 00:00:00&#39;) | [optional] [readonly] 
**description** | **str** | Update description | [optional] [readonly] 
**issued_date** | **str** | Date when the update was issued (e.g. &#39;2013-12-02 00:00:00&#39;) | [optional] [readonly] 
**fromstr** | **str** | Source of the update (e.g. security@redhat.com) | [optional] [readonly] 
**status** | **str** | Update status (&#39;final&#39;, ...) | [optional] [readonly] 
**title** | **str** | Update name | [optional] [readonly] 
**summary** | **str** | Short summary | [optional] [readonly] 
**version** | **str** | Update version (probably always an integer number) | [optional] [readonly] 
**type** | **str** | Update type (&#39;enhancement&#39;, &#39;bugfix&#39;, ...) | [optional] [readonly] 
**severity** | **str** | Severity | [optional] [readonly] 
**solution** | **str** | Solution | [optional] [readonly] 
**release** | **str** | Update release | [optional] [readonly] 
**rights** | **str** | Copyrights | [optional] [readonly] 
**pushcount** | **str** | Push count | [optional] [readonly] 
**pkglist** | [**list[RpmUpdateCollectionResponse]**](RpmUpdateCollectionResponse.md) | List of packages | [optional] [readonly] 
**references** | **list[object]** | List of references | [optional] [readonly] 
**reboot_suggested** | **bool** | Reboot suggested | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


