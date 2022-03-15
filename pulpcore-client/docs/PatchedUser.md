# PatchedUser

Serializer for User.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [optional] 
**password** | **str** | Users password. Set to &#x60;&#x60;null&#x60;&#x60; to disable password authentication. | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email address | [optional] 
**is_staff** | **bool** | Designates whether the user can log into this admin site. | [optional] [default to False]
**is_active** | **bool** | Designates whether this user should be treated as active. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


