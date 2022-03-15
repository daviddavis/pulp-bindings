# StatusResponse

Serializer for the status information of the app
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versions** | [**list[VersionResponse]**](VersionResponse.md) | Version information of Pulp components | 
**online_workers** | [**list[WorkerResponse]**](WorkerResponse.md) | List of online workers known to the application. An online worker is actively heartbeating and can respond to new work | 
**online_content_apps** | [**list[ContentAppStatusResponse]**](ContentAppStatusResponse.md) | List of online content apps known to the application. An online content app is actively heartbeating and can serve data to clients | 
**database_connection** | [**DatabaseConnectionResponse**](DatabaseConnectionResponse.md) | Database connection information | 
**redis_connection** | [**RedisConnectionResponse**](RedisConnectionResponse.md) | Redis connection information | [optional] 
**storage** | [**StorageResponse**](StorageResponse.md) | Storage information | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


