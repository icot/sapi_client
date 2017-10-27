# sapi_client.SapiApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_export**](SapiApi.md#delete_export) | **DELETE** /v3/{subsystem}/export/{policy} | 
[**delete_export_rule**](SapiApi.md#delete_export_rule) | **DELETE** /v3/{subsystem}/export/{policy}/rule/{rule} | 
[**delete_locks**](SapiApi.md#delete_locks) | **DELETE** /v3/{subsystem}/volumes/{volume_name}/locks/{host} | 
[**delete_snapshots**](SapiApi.md#delete_snapshots) | **DELETE** /v3/{subsystem}/volumes/{volume_name}/snapshots/{snapshot_name} | 
[**delete_volume**](SapiApi.md#delete_volume) | **DELETE** /v3/{subsystem}/volumes/{volume_name} | 
[**get_all_exports**](SapiApi.md#get_all_exports) | **GET** /v3/{subsystem}/export | 
[**get_all_locks**](SapiApi.md#get_all_locks) | **GET** /v3/{subsystem}/volumes/{volume_name}/locks | 
[**get_all_snapshots**](SapiApi.md#get_all_snapshots) | **GET** /v3/{subsystem}/volumes/{volume_name}/snapshots | 
[**get_export**](SapiApi.md#get_export) | **GET** /v3/{subsystem}/export/{policy} | 
[**get_snapshots**](SapiApi.md#get_snapshots) | **GET** /v3/{subsystem}/volumes/{volume_name}/snapshots/{snapshot_name} | 
[**get_volume**](SapiApi.md#get_volume) | **GET** /v3/{subsystem}/volumes/{volume_name} | 
[**get_volumes**](SapiApi.md#get_volumes) | **GET** /v3/{subsystem}/volumes | 
[**patch_volume**](SapiApi.md#patch_volume) | **PATCH** /v3/{subsystem}/volumes/{volume_name} | 
[**post_export**](SapiApi.md#post_export) | **POST** /v3/{subsystem}/export/{policy} | 
[**post_snapshots**](SapiApi.md#post_snapshots) | **POST** /v3/{subsystem}/volumes/{volume_name}/snapshots/{snapshot_name} | 
[**post_volume**](SapiApi.md#post_volume) | **POST** /v3/{subsystem}/volumes/{volume_name} | 
[**put_export_rule**](SapiApi.md#put_export_rule) | **PUT** /v3/{subsystem}/export/{policy}/rule/{rule} | 
[**put_locks**](SapiApi.md#put_locks) | **PUT** /v3/{subsystem}/volumes/{volume_name}/locks/{host} | 


# **delete_export**
> delete_export(policy, subsystem)



Delete the entire policy

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
policy = 'policy_example' # str | The policy to operate on
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.delete_export(policy, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->delete_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy to operate on | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_export_rule**
> delete_export_rule(rule, policy, subsystem)



Delete rule from policy

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
rule = 'rule_example' # str | The policy rule to operate on
policy = 'policy_example' # str | The policy to operate on
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.delete_export_rule(rule, policy, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->delete_export_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The policy rule to operate on | 
 **policy** | **str**| The policy to operate on | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_locks**
> delete_locks(host, volume_name, subsystem)



Force the lock for the host

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
host = 'host_example' # str | the host holding the lock in question
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.delete_locks(host, volume_name, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->delete_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| the host holding the lock in question | 
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshots**
> delete_snapshots(snapshot_name, volume_name, subsystem)



Delete the snapshot

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
snapshot_name = 'snapshot_name_example' # str | The snapshot name
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.delete_snapshots(snapshot_name, volume_name, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->delete_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_name** | **str**| The snapshot name | 
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume**
> delete_volume(volume_name, subsystem)



Restrict the volume named *volume_name* but do not actually delete it

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.delete_volume(volume_name, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->delete_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_exports**
> list[ExportPolicy] get_all_exports(subsystem, x_fields=x_fields)



Get all ACLs present on the back-end

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_all_exports(subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_all_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[ExportPolicy]**](ExportPolicy.md)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_locks**
> list[Lock] get_all_locks(volume_name, subsystem, x_fields=x_fields)



Get the host locking the volume, if any

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_all_locks(volume_name, subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_all_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[Lock]**](Lock.md)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_snapshots**
> list[Snapshot] get_all_snapshots(volume_name, subsystem, x_fields=x_fields)



### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.SapiApi()
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_all_snapshots(volume_name, subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_all_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[Snapshot]**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export**
> ExportPolicy get_export(policy, subsystem, x_fields=x_fields)



Display the rules of a given policy

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
policy = 'policy_example' # str | The policy to operate on
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_export(policy, subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy to operate on | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ExportPolicy**](ExportPolicy.md)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshots**
> Snapshot get_snapshots(snapshot_name, volume_name, subsystem, x_fields=x_fields)



Get the current information for a given snapshot

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.SapiApi()
snapshot_name = 'snapshot_name_example' # str | The snapshot name
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_snapshots(snapshot_name, volume_name, subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_name** | **str**| The snapshot name | 
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume**
> VolumeRead get_volume(volume_name, subsystem, x_fields=x_fields)



Get a specific volume by name

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_volume(volume_name, subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VolumeRead**](VolumeRead.md)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volumes**
> list[VolumeRead] get_volumes(subsystem, x_fields=x_fields)



Get a list of all volumes

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.get_volumes(subsystem, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->get_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subsystem** | **str**| The subsystem to run the command on. | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**list[VolumeRead]**](VolumeRead.md)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_volume**
> patch_volume(volume_name, subsystem, payload)



Partially update volume_name

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
payload = sapi_client.VolumeWrite() # VolumeWrite | 

try: 
    api_instance.patch_volume(volume_name, subsystem, payload)
except ApiException as e:
    print("Exception when calling SapiApi->patch_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **payload** | [**VolumeWrite**](VolumeWrite.md)|  | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_export**
> post_export(policy, subsystem, payload)



Grant hosts matching a given pattern access to the given volume

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
policy = 'policy_example' # str | The policy to operate on
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
payload = sapi_client.PolicyRule() # PolicyRule | 

try: 
    api_instance.post_export(policy, subsystem, payload)
except ApiException as e:
    print("Exception when calling SapiApi->post_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**| The policy to operate on | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **payload** | [**PolicyRule**](PolicyRule.md)|  | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_snapshots**
> post_snapshots(snapshot_name, volume_name, subsystem, payload)



Create a new snapshot of *volume_name* under *snapshot_name*

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.SapiApi()
snapshot_name = 'snapshot_name_example' # str | The snapshot name
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
payload = sapi_client.SnapshotPut() # SnapshotPut | 

try: 
    api_instance.post_snapshots(snapshot_name, volume_name, subsystem, payload)
except ApiException as e:
    print("Exception when calling SapiApi->post_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_name** | **str**| The snapshot name | 
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **payload** | [**SnapshotPut**](SnapshotPut.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_volume**
> VolumeRead post_volume(volume_name, subsystem, payload, x_fields=x_fields)



Create a new volume with the given details.  If `from_snapshot` is a snapshot and `volume_name` already refers to an existing volume, roll back that volume to that snapshot. If `from_snapshot` is a snapshot, `from_volume` is an existing volume and `volume_name` doesn't already exist, create a clone of `from_volume` named `volume_name`, in the state at `from_snapshot`.

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.
payload = sapi_client.OptionalFromSnapshot() # OptionalFromSnapshot | 
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

try: 
    api_response = api_instance.post_volume(volume_name, subsystem, payload, x_fields=x_fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SapiApi->post_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 
 **payload** | [**OptionalFromSnapshot**](OptionalFromSnapshot.md)|  | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**VolumeRead**](VolumeRead.md)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_export_rule**
> put_export_rule(rule, policy, subsystem)



Grant hosts matching a given pattern access

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
rule = 'rule_example' # str | The policy rule to operate on
policy = 'policy_example' # str | The policy to operate on
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.put_export_rule(rule, policy, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->put_export_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | **str**| The policy rule to operate on | 
 **policy** | **str**| The policy to operate on | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_locks**
> put_locks(host, volume_name, subsystem)



Lock the volume with host holding the lock

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: sso
configuration = sapi_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = sapi_client.SapiApi(sapi_client.ApiClient(configuration))
host = 'host_example' # str | the host holding the lock in question
volume_name = 'volume_name_example' # str | The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path.
subsystem = 'subsystem_example' # str | The subsystem to run the command on.

try: 
    api_instance.put_locks(host, volume_name, subsystem)
except ApiException as e:
    print("Exception when calling SapiApi->put_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| the host holding the lock in question | 
 **volume_name** | **str**| The name of the volume. Must not contain leading /. On NetApp back-ends, this may either be the name of a volume, or node_name:/junction/path. | 
 **subsystem** | **str**| The subsystem to run the command on. | 

### Return type

void (empty response body)

### Authorization

[sso](../README.md#sso)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

