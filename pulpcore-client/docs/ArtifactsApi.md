# pulpcore.client.pulpcore.ArtifactsApi

All URIs are relative to *http://pulp3-source-fedora35.pulpbox.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ArtifactsApi.md#create) | **POST** /pulp/api/v3/artifacts/ | Create an artifact
[**delete**](ArtifactsApi.md#delete) | **DELETE** {artifact_href} | Delete an artifact
[**list**](ArtifactsApi.md#list) | **GET** /pulp/api/v3/artifacts/ | List artifacts
[**read**](ArtifactsApi.md#read) | **GET** {artifact_href} | Inspect an artifact


# **create**
> ArtifactResponse create(file, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)

Create an artifact

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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    file = '/path/to/file' # file | The stored file.
size = 56 # int | The size of the file in bytes. (optional)
md5 = 'md5_example' # str | The MD5 checksum of the file if available. (optional)
sha1 = 'sha1_example' # str | The SHA-1 checksum of the file if available. (optional)
sha224 = 'sha224_example' # str | The SHA-224 checksum of the file if available. (optional)
sha256 = 'sha256_example' # str | The SHA-256 checksum of the file if available. (optional)
sha384 = 'sha384_example' # str | The SHA-384 checksum of the file if available. (optional)
sha512 = 'sha512_example' # str | The SHA-512 checksum of the file if available. (optional)

    try:
        # Create an artifact
        api_response = api_instance.create(file, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->create: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    file = '/path/to/file' # file | The stored file.
size = 56 # int | The size of the file in bytes. (optional)
md5 = 'md5_example' # str | The MD5 checksum of the file if available. (optional)
sha1 = 'sha1_example' # str | The SHA-1 checksum of the file if available. (optional)
sha224 = 'sha224_example' # str | The SHA-224 checksum of the file if available. (optional)
sha256 = 'sha256_example' # str | The SHA-256 checksum of the file if available. (optional)
sha384 = 'sha384_example' # str | The SHA-384 checksum of the file if available. (optional)
sha512 = 'sha512_example' # str | The SHA-512 checksum of the file if available. (optional)

    try:
        # Create an artifact
        api_response = api_instance.create(file, size=size, md5=md5, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The stored file. | 
 **size** | **int**| The size of the file in bytes. | [optional] 
 **md5** | **str**| The MD5 checksum of the file if available. | [optional] 
 **sha1** | **str**| The SHA-1 checksum of the file if available. | [optional] 
 **sha224** | **str**| The SHA-224 checksum of the file if available. | [optional] 
 **sha256** | **str**| The SHA-256 checksum of the file if available. | [optional] 
 **sha384** | **str**| The SHA-384 checksum of the file if available. | [optional] 
 **sha512** | **str**| The SHA-512 checksum of the file if available. | [optional] 

### Return type

[**ArtifactResponse**](ArtifactResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(artifact_href)

Delete an artifact

Remove Artifact only if it is not associated with any Content.

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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 

    try:
        # Delete an artifact
        api_instance.delete(artifact_href)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->delete: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 

    try:
        # Delete an artifact
        api_instance.delete(artifact_href)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatedArtifactResponseList list(limit=limit, md5=md5, offset=offset, ordering=ordering, repository_version=repository_version, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, fields=fields, exclude_fields=exclude_fields)

List artifacts

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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
md5 = 'md5_example' # str | Filter results where md5 matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
sha1 = 'sha1_example' # str | Filter results where sha1 matches value (optional)
sha224 = 'sha224_example' # str | Filter results where sha224 matches value (optional)
sha256 = 'sha256_example' # str | Filter results where sha256 matches value (optional)
sha384 = 'sha384_example' # str | Filter results where sha384 matches value (optional)
sha512 = 'sha512_example' # str | Filter results where sha512 matches value (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List artifacts
        api_response = api_instance.list(limit=limit, md5=md5, offset=offset, ordering=ordering, repository_version=repository_version, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
md5 = 'md5_example' # str | Filter results where md5 matches value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
sha1 = 'sha1_example' # str | Filter results where sha1 matches value (optional)
sha224 = 'sha224_example' # str | Filter results where sha224 matches value (optional)
sha256 = 'sha256_example' # str | Filter results where sha256 matches value (optional)
sha384 = 'sha384_example' # str | Filter results where sha384 matches value (optional)
sha512 = 'sha512_example' # str | Filter results where sha512 matches value (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List artifacts
        api_response = api_instance.list(limit=limit, md5=md5, offset=offset, ordering=ordering, repository_version=repository_version, sha1=sha1, sha224=sha224, sha256=sha256, sha384=sha384, sha512=sha512, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **md5** | **str**| Filter results where md5 matches value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **sha1** | **str**| Filter results where sha1 matches value | [optional] 
 **sha224** | **str**| Filter results where sha224 matches value | [optional] 
 **sha256** | **str**| Filter results where sha256 matches value | [optional] 
 **sha384** | **str**| Filter results where sha384 matches value | [optional] 
 **sha512** | **str**| Filter results where sha512 matches value | [optional] 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedArtifactResponseList**](PaginatedArtifactResponseList.md)

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
> ArtifactResponse read(artifact_href, fields=fields, exclude_fields=exclude_fields)

Inspect an artifact

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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an artifact
        api_response = api_instance.read(artifact_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulpcore.ArtifactsApi(api_client)
    artifact_href = 'artifact_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect an artifact
        api_response = api_instance.read(artifact_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtifactsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **artifact_href** | **str**|  | 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**ArtifactResponse**](ArtifactResponse.md)

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

