# RpmDistributionTreeResponse

DistributionTree serializer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pulp_href** | **str** |  | [optional] [readonly] 
**header_version** | **str** | Header Version. | 
**release_name** | **str** | Release name. | 
**release_short** | **str** | Release short name. | 
**release_version** | **str** | Release version. | 
**release_is_layered** | **bool** | Typically False for an operating system, True otherwise. | 
**base_product_name** | **str** | Base Product name. | 
**base_product_short** | **str** | Base Product short name. | 
**base_product_version** | **str** | Base Product version. | 
**arch** | **str** | Tree architecturerch. | 
**build_timestamp** | **float** | Tree build time timestamp. | 
**instimage** | **str** | Relative path to Anaconda instimage. | 
**mainimage** | **str** | Relative path to Anaconda stage2 image. | 
**discnum** | **int** | Disc number. | 
**totaldiscs** | **int** | Number of discs in media set. | 
**addons** | [**list[AddonResponse]**](AddonResponse.md) |  | 
**checksums** | [**list[ChecksumResponse]**](ChecksumResponse.md) |  | 
**images** | [**list[ImageResponse]**](ImageResponse.md) |  | 
**variants** | [**list[VariantResponse]**](VariantResponse.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


