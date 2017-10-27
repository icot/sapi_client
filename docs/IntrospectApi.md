# sapi_client.IntrospectApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_am_ia**](IntrospectApi.md#get_am_ia) | **GET** /conf/roles/{role}/am_i_a | 
[**get_role_egroups**](IntrospectApi.md#get_role_egroups) | **GET** /conf/roles/{role}/egroups | 
[**get_roles**](IntrospectApi.md#get_roles) | **GET** /conf/roles | 
[**get_subsystems**](IntrospectApi.md#get_subsystems) | **GET** /conf/subsystems | 
[**get_user_roles**](IntrospectApi.md#get_user_roles) | **GET** /conf/me/roles | 


# **get_am_ia**
> get_am_ia(role)



Returns True if the user is the given role, False otherwise

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.IntrospectApi()
role = 'role_example' # str | The name of a role, one of USER, ADMIN, UBER_ADMIN.

try: 
    api_instance.get_am_ia(role)
except ApiException as e:
    print("Exception when calling IntrospectApi->get_am_ia: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of a role, one of USER, ADMIN, UBER_ADMIN. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_egroups**
> get_role_egroups(role)



Get a list of all egroups for a given role

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.IntrospectApi()
role = 'role_example' # str | The name of a role, one of USER, ADMIN, UBER_ADMIN.

try: 
    api_instance.get_role_egroups(role)
except ApiException as e:
    print("Exception when calling IntrospectApi->get_role_egroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**| The name of a role, one of USER, ADMIN, UBER_ADMIN. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> get_roles()



Get a list of all available roles

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.IntrospectApi()

try: 
    api_instance.get_roles()
except ApiException as e:
    print("Exception when calling IntrospectApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subsystems**
> get_subsystems()



Get a list of all available subsystems

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.IntrospectApi()

try: 
    api_instance.get_subsystems()
except ApiException as e:
    print("Exception when calling IntrospectApi->get_subsystems: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> get_user_roles()



List the roles of the current user

### Example 
```python
from __future__ import print_function
import time
import sapi_client
from sapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = sapi_client.IntrospectApi()

try: 
    api_instance.get_user_roles()
except ApiException as e:
    print("Exception when calling IntrospectApi->get_user_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

