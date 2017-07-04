# VolumeCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autosize_enabled** | **bool** |  | [optional] 
**autosize_increment** | **int** |  | [optional] 
**max_autosize** | **int** |  | [optional] 
**active_policy_name** | **str** |  | [optional] 
**percentage_snapshot_reserve** | **int** |  | [optional] 
**compression_enabled** | **bool** |  | [optional] 
**inline_compression** | **bool** |  | [optional] 
**caching_policy** | **str** |  | [optional] 
**name** | **str** | The internal name of the volume | [optional] 
**size_total** | **int** | The total size of the volume,  in bytes. If creating, the size of the volume. | [optional] 
**aggregate_name** | **str** | If applicable, the aggregate to place the volume in (NetApp only). If not provided, will use the one with the most free space. | [optional] 
**junction_path** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

