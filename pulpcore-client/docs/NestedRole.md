# NestedRole

Serializer to add/remove object roles to/from users/groups.  This is used in conjunction with ``pulpcore.app.viewsets.base.RolesMixin`` and requires the underlying object to be passed as ``content_object`` in the context.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **list[str]** |  | [optional] [default to []]
**groups** | **list[str]** |  | [optional] [default to []]
**role** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


