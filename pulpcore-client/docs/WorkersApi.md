# pulpcore.client.pulpcore.WorkersApi

All URIs are relative to *http://pulp3-source-fedora35.pulpbox.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](WorkersApi.md#list) | **GET** /pulp/api/v3/workers/ | List workers
[**read**](WorkersApi.md#read) | **GET** {worker_href} | Inspect a worker


# **list**
> PaginatedWorkerResponseList list(last_heartbeat=last_heartbeat, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__range=last_heartbeat__range, limit=limit, missing=missing, name=name, name__contains=name__contains, name__icontains=name__icontains, name__in=name__in, name__startswith=name__startswith, offset=offset, online=online, ordering=ordering, fields=fields, exclude_fields=exclude_fields)

List workers

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp3-source-fedora35.pulpbox.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.WorkersApi(api_client)
    last_heartbeat = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 formatted dates are supported (optional)
last_heartbeat__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is greater than value (optional)
last_heartbeat__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is greater than or equal to value (optional)
last_heartbeat__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is less than value (optional)
last_heartbeat__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is less than or equal to value (optional)
last_heartbeat__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where last_heartbeat is between two comma separated values (optional)
limit = 56 # int | Number of results to return per page. (optional)
missing = True # bool |  (optional)
name = 'name_example' # str |  (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
online = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List workers
        api_response = api_instance.list(last_heartbeat=last_heartbeat, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__range=last_heartbeat__range, limit=limit, missing=missing, name=name, name__contains=name__contains, name__icontains=name__icontains, name__in=name__in, name__startswith=name__startswith, offset=offset, online=online, ordering=ordering, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp3-source-fedora35.pulpbox.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.WorkersApi(api_client)
    last_heartbeat = '2013-10-20T19:20:30+01:00' # datetime | ISO 8601 formatted dates are supported (optional)
last_heartbeat__gt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is greater than value (optional)
last_heartbeat__gte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is greater than or equal to value (optional)
last_heartbeat__lt = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is less than value (optional)
last_heartbeat__lte = '2013-10-20T19:20:30+01:00' # datetime | Filter results where last_heartbeat is less than or equal to value (optional)
last_heartbeat__range = ['2013-10-20T19:20:30+01:00'] # list[datetime] | Filter results where last_heartbeat is between two comma separated values (optional)
limit = 56 # int | Number of results to return per page. (optional)
missing = True # bool |  (optional)
name = 'name_example' # str |  (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
online = True # bool |  (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List workers
        api_response = api_instance.list(last_heartbeat=last_heartbeat, last_heartbeat__gt=last_heartbeat__gt, last_heartbeat__gte=last_heartbeat__gte, last_heartbeat__lt=last_heartbeat__lt, last_heartbeat__lte=last_heartbeat__lte, last_heartbeat__range=last_heartbeat__range, limit=limit, missing=missing, name=name, name__contains=name__contains, name__icontains=name__icontains, name__in=name__in, name__startswith=name__startswith, offset=offset, online=online, ordering=ordering, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_heartbeat** | **datetime**| ISO 8601 formatted dates are supported | [optional] 
 **last_heartbeat__gt** | **datetime**| Filter results where last_heartbeat is greater than value | [optional] 
 **last_heartbeat__gte** | **datetime**| Filter results where last_heartbeat is greater than or equal to value | [optional] 
 **last_heartbeat__lt** | **datetime**| Filter results where last_heartbeat is less than value | [optional] 
 **last_heartbeat__lte** | **datetime**| Filter results where last_heartbeat is less than or equal to value | [optional] 
 **last_heartbeat__range** | [**list[datetime]**](datetime.md)| Filter results where last_heartbeat is between two comma separated values | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **missing** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__icontains** | **str**| Filter results where name contains value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__startswith** | **str**| Filter results where name starts with value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **online** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedWorkerResponseList**](PaginatedWorkerResponseList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> WorkerResponse read(worker_href, fields=fields, exclude_fields=exclude_fields)

Inspect a worker

A customized named ModelViewSet that knows how to register itself with the Pulp API router.  This viewset is discoverable by its name. \"Normal\" Django Models and Master/Detail models are supported by the ``register_with`` method.  Attributes:     lookup_field (str): The name of the field by which an object should be looked up, in         addition to any parent lookups if this ViewSet is nested. Defaults to 'pk'     endpoint_name (str): The name of the final path segment that should identify the ViewSet's         collection endpoint.     nest_prefix (str): Optional prefix under which this ViewSet should be nested. This must         correspond to the \"parent_prefix\" of a router with rest_framework_nested.NestedMixin.         None indicates this ViewSet should not be nested.     parent_lookup_kwargs (dict): Optional mapping of key names that would appear in self.kwargs         to django model filter expressions that can be used with the corresponding value from         self.kwargs, used only by a nested ViewSet to filter based on the parent object's         identity.     schema (DefaultSchema): The schema class to use by default in a viewset.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp3-source-fedora35.pulpbox.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.WorkersApi(api_client)
    worker_href = 'worker_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a worker
        api_response = api_instance.read(worker_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->read: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp3-source-fedora35.pulpbox.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulpcore.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulpcore.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.WorkersApi(api_client)
    worker_href = 'worker_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a worker
        api_response = api_instance.read(worker_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkersApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worker_href** | **str**|  | 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**WorkerResponse**](WorkerResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

