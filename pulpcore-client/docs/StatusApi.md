# pulpcore.client.pulpcore.StatusApi

All URIs are relative to *http://pulp3-source-fedora35.pulpbox.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_read**](StatusApi.md#status_read) | **GET** /pulp/api/v3/status/ | Inspect status of Pulp


# **status_read**
> StatusResponse status_read()

Inspect status of Pulp

Returns status and app information about Pulp.  Information includes:  * version of pulpcore and loaded pulp plugins  * known workers  * known content apps  * database connection status  * redis connection status  * disk usage information

### Example

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


# Enter a context with an instance of the API client
with pulpcore.client.pulpcore.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulpcore.StatusApi(api_client)
    
    try:
        # Inspect status of Pulp
        api_response = api_instance.status_read()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusApi->status_read: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

