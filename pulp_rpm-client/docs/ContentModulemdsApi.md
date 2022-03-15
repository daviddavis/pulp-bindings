# pulpcore.client.pulp_rpm.ContentModulemdsApi

All URIs are relative to *http://pulp3-source-fedora35.pulpbox.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentModulemdsApi.md#create) | **POST** /pulp/api/v3/content/rpm/modulemds/ | Create a modulemd
[**list**](ContentModulemdsApi.md#list) | **GET** /pulp/api/v3/content/rpm/modulemds/ | List modulemds
[**read**](ContentModulemdsApi.md#read) | **GET** {rpm_modulemd_href} | Inspect a modulemd


# **create**
> AsyncOperationResponse create(relative_path, name, stream, version, context, arch, artifacts, dependencies, artifact=artifact, file=file, repository=repository, static_context=static_context, packages=packages)

Create a modulemd

Trigger an asynchronous task to create content,optionally create new repository version.

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
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    relative_path = 'relative_path_example' # str | Path where the artifact is located relative to distributions base_path
name = 'name_example' # str | Modulemd name.
stream = 'stream_example' # str | Stream name.
version = 'version_example' # str | Modulemd version.
context = 'context_example' # str | Modulemd context.
arch = 'arch_example' # str | Modulemd architecture.
artifacts = None # object | Modulemd artifacts.
dependencies = None # object | Modulemd dependencies.
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that may be turned into the artifact of the content unit. (optional)
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
static_context = True # bool | Modulemd static-context flag. (optional)
packages = 'packages_example' # list[str] | Modulemd artifacts' packages. (optional)

    try:
        # Create a modulemd
        api_response = api_instance.create(relative_path, name, stream, version, context, arch, artifacts, dependencies, artifact=artifact, file=file, repository=repository, static_context=static_context, packages=packages)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdsApi->create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    relative_path = 'relative_path_example' # str | Path where the artifact is located relative to distributions base_path
name = 'name_example' # str | Modulemd name.
stream = 'stream_example' # str | Stream name.
version = 'version_example' # str | Modulemd version.
context = 'context_example' # str | Modulemd context.
arch = 'arch_example' # str | Modulemd architecture.
artifacts = None # object | Modulemd artifacts.
dependencies = None # object | Modulemd dependencies.
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that may be turned into the artifact of the content unit. (optional)
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)
static_context = True # bool | Modulemd static-context flag. (optional)
packages = 'packages_example' # list[str] | Modulemd artifacts' packages. (optional)

    try:
        # Create a modulemd
        api_response = api_instance.create(relative_path, name, stream, version, context, arch, artifacts, dependencies, artifact=artifact, file=file, repository=repository, static_context=static_context, packages=packages)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relative_path** | **str**| Path where the artifact is located relative to distributions base_path | 
 **name** | **str**| Modulemd name. | 
 **stream** | **str**| Stream name. | 
 **version** | **str**| Modulemd version. | 
 **context** | **str**| Modulemd context. | 
 **arch** | **str**| Modulemd architecture. | 
 **artifacts** | [**object**](object.md)| Modulemd artifacts. | 
 **dependencies** | [**object**](object.md)| Modulemd dependencies. | 
 **artifact** | **str**| Artifact file representing the physical content | [optional] 
 **file** | **file**| An uploaded file that may be turned into the artifact of the content unit. | [optional] 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 
 **static_context** | **bool**| Modulemd static-context flag. | [optional] 
 **packages** | [**list[str]**](str.md)| Modulemd artifacts&#39; packages. | [optional] 

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

# **list**
> PaginatedrpmModulemdResponseList list(limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, fields=fields, exclude_fields=exclude_fields)

List modulemds

ViewSet for Modulemd.

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
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
sha256 = 'sha256_example' # str |  (optional)
stream = 'stream_example' # str | Filter results where stream matches value (optional)
stream__in = ['stream__in_example'] # list[str] | Filter results where stream is in a comma-separated list of values (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List modulemds
        api_response = api_instance.list(limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdsApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
sha256 = 'sha256_example' # str |  (optional)
stream = 'stream_example' # str | Filter results where stream matches value (optional)
stream__in = ['stream__in_example'] # list[str] | Filter results where stream is in a comma-separated list of values (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List modulemds
        api_response = api_instance.list(limit=limit, name=name, name__in=name__in, offset=offset, ordering=ordering, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, stream=stream, stream__in=stream__in, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdsApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **sha256** | **str**|  | [optional] 
 **stream** | **str**| Filter results where stream matches value | [optional] 
 **stream__in** | [**list[str]**](str.md)| Filter results where stream is in a comma-separated list of values | [optional] 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedrpmModulemdResponseList**](PaginatedrpmModulemdResponseList.md)

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
> RpmModulemdResponse read(rpm_modulemd_href, fields=fields, exclude_fields=exclude_fields)

Inspect a modulemd

ViewSet for Modulemd.

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
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    rpm_modulemd_href = 'rpm_modulemd_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a modulemd
        api_response = api_instance.read(rpm_modulemd_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdsApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentModulemdsApi(api_client)
    rpm_modulemd_href = 'rpm_modulemd_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a modulemd
        api_response = api_instance.read(rpm_modulemd_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentModulemdsApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_modulemd_href** | **str**|  | 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**RpmModulemdResponse**](RpmModulemdResponse.md)

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

