# pulpcore.client.pulp_rpm.RpmCompsApi

All URIs are relative to *http://pulp3-source-fedora35.pulpbox.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rpm_comps_upload**](RpmCompsApi.md#rpm_comps_upload) | **POST** /pulp/api/v3/rpm/comps/ | Upload comps.xml


# **rpm_comps_upload**
> AsyncOperationResponse rpm_comps_upload(file, repository=repository, replace=replace)

Upload comps.xml

Trigger an asynchronous task to upload a comps.xml file.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp3-source-fedora35.pulpbox.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.RpmCompsApi(api_client)
    file = '/path/to/file' # file | Full path of a comps.xml file that may be parsed into comps.xml Content units.
repository = 'repository_example' # str | URI of an RPM repository the comps.xml content units should be associated to. (optional)
replace = True # bool | If true, incoming comps.xml replaces existing comps-related ContentUnits in the specified repository. (optional)

    try:
        # Upload comps.xml
        api_response = api_instance.rpm_comps_upload(file, repository=repository, replace=replace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RpmCompsApi->rpm_comps_upload: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://pulp3-source-fedora35.pulpbox.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://pulp3-source-fedora35.pulpbox.example.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.RpmCompsApi(api_client)
    file = '/path/to/file' # file | Full path of a comps.xml file that may be parsed into comps.xml Content units.
repository = 'repository_example' # str | URI of an RPM repository the comps.xml content units should be associated to. (optional)
replace = True # bool | If true, incoming comps.xml replaces existing comps-related ContentUnits in the specified repository. (optional)

    try:
        # Upload comps.xml
        api_response = api_instance.rpm_comps_upload(file, repository=repository, replace=replace)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RpmCompsApi->rpm_comps_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Full path of a comps.xml file that may be parsed into comps.xml Content units. | 
 **repository** | **str**| URI of an RPM repository the comps.xml content units should be associated to. | [optional] 
 **replace** | **bool**| If true, incoming comps.xml replaces existing comps-related ContentUnits in the specified repository. | [optional] 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

