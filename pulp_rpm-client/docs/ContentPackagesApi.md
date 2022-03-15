# pulpcore.client.pulp_rpm.ContentPackagesApi

All URIs are relative to *http://pulp3-source-fedora35.pulpbox.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ContentPackagesApi.md#create) | **POST** /pulp/api/v3/content/rpm/packages/ | Create a package
[**list**](ContentPackagesApi.md#list) | **GET** /pulp/api/v3/content/rpm/packages/ | List packages
[**read**](ContentPackagesApi.md#read) | **GET** {rpm_package_href} | Inspect a package


# **create**
> AsyncOperationResponse create(relative_path, artifact=artifact, file=file, repository=repository)

Create a package

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
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    relative_path = 'relative_path_example' # str | Path where the artifact is located relative to distributions base_path
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that may be turned into the artifact of the content unit. (optional)
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)

    try:
        # Create a package
        api_response = api_instance.create(relative_path, artifact=artifact, file=file, repository=repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentPackagesApi->create: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    relative_path = 'relative_path_example' # str | Path where the artifact is located relative to distributions base_path
artifact = 'artifact_example' # str | Artifact file representing the physical content (optional)
file = '/path/to/file' # file | An uploaded file that may be turned into the artifact of the content unit. (optional)
repository = 'repository_example' # str | A URI of a repository the new content unit should be associated with. (optional)

    try:
        # Create a package
        api_response = api_instance.create(relative_path, artifact=artifact, file=file, repository=repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentPackagesApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relative_path** | **str**| Path where the artifact is located relative to distributions base_path | 
 **artifact** | **str**| Artifact file representing the physical content | [optional] 
 **file** | **file**| An uploaded file that may be turned into the artifact of the content unit. | [optional] 
 **repository** | **str**| A URI of a repository the new content unit should be associated with. | [optional] 

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
> PaginatedrpmPackageResponseList list(arch=arch, arch__in=arch__in, arch__ne=arch__ne, checksum_type=checksum_type, checksum_type__in=checksum_type__in, checksum_type__ne=checksum_type__ne, epoch=epoch, epoch__in=epoch__in, epoch__ne=epoch__ne, limit=limit, name=name, name__in=name__in, name__ne=name__ne, offset=offset, ordering=ordering, pkg_id=pkg_id, pkg_id__in=pkg_id__in, release=release, release__in=release__in, release__ne=release__ne, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, version=version, version__in=version__in, version__ne=version__ne, fields=fields, exclude_fields=exclude_fields)

List packages

A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.

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
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    arch = 'arch_example' # str | Filter results where arch matches value (optional)
arch__in = ['arch__in_example'] # list[str] | Filter results where arch is in a comma-separated list of values (optional)
arch__ne = 'arch__ne_example' # str | Filter results where arch not equal to value (optional)
checksum_type = 'checksum_type_example' # str | Filter results where checksum_type matches value (optional)
checksum_type__in = ['checksum_type__in_example'] # list[str] | Filter results where checksum_type is in a comma-separated list of values (optional)
checksum_type__ne = 'checksum_type__ne_example' # str | Filter results where checksum_type not equal to value (optional)
epoch = 'epoch_example' # str | Filter results where epoch matches value (optional)
epoch__in = ['epoch__in_example'] # list[str] | Filter results where epoch is in a comma-separated list of values (optional)
epoch__ne = 'epoch__ne_example' # str | Filter results where epoch not equal to value (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__ne = 'name__ne_example' # str | Filter results where name not equal to value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
pkg_id = 'pkg_id_example' # str | Filter results where pkgId matches value (optional)
pkg_id__in = ['pkg_id__in_example'] # list[str] | Filter results where pkgId is in a comma-separated list of values (optional)
release = 'release_example' # str | Filter results where release matches value (optional)
release__in = ['release__in_example'] # list[str] | Filter results where release is in a comma-separated list of values (optional)
release__ne = 'release__ne_example' # str | Filter results where release not equal to value (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
sha256 = 'sha256_example' # str |  (optional)
version = 'version_example' # str | Filter results where version matches value (optional)
version__in = ['version__in_example'] # list[str] | Filter results where version is in a comma-separated list of values (optional)
version__ne = 'version__ne_example' # str | Filter results where version not equal to value (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List packages
        api_response = api_instance.list(arch=arch, arch__in=arch__in, arch__ne=arch__ne, checksum_type=checksum_type, checksum_type__in=checksum_type__in, checksum_type__ne=checksum_type__ne, epoch=epoch, epoch__in=epoch__in, epoch__ne=epoch__ne, limit=limit, name=name, name__in=name__in, name__ne=name__ne, offset=offset, ordering=ordering, pkg_id=pkg_id, pkg_id__in=pkg_id__in, release=release, release__in=release__in, release__ne=release__ne, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, version=version, version__in=version__in, version__ne=version__ne, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentPackagesApi->list: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    arch = 'arch_example' # str | Filter results where arch matches value (optional)
arch__in = ['arch__in_example'] # list[str] | Filter results where arch is in a comma-separated list of values (optional)
arch__ne = 'arch__ne_example' # str | Filter results where arch not equal to value (optional)
checksum_type = 'checksum_type_example' # str | Filter results where checksum_type matches value (optional)
checksum_type__in = ['checksum_type__in_example'] # list[str] | Filter results where checksum_type is in a comma-separated list of values (optional)
checksum_type__ne = 'checksum_type__ne_example' # str | Filter results where checksum_type not equal to value (optional)
epoch = 'epoch_example' # str | Filter results where epoch matches value (optional)
epoch__in = ['epoch__in_example'] # list[str] | Filter results where epoch is in a comma-separated list of values (optional)
epoch__ne = 'epoch__ne_example' # str | Filter results where epoch not equal to value (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__ne = 'name__ne_example' # str | Filter results where name not equal to value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
pkg_id = 'pkg_id_example' # str | Filter results where pkgId matches value (optional)
pkg_id__in = ['pkg_id__in_example'] # list[str] | Filter results where pkgId is in a comma-separated list of values (optional)
release = 'release_example' # str | Filter results where release matches value (optional)
release__in = ['release__in_example'] # list[str] | Filter results where release is in a comma-separated list of values (optional)
release__ne = 'release__ne_example' # str | Filter results where release not equal to value (optional)
repository_version = 'repository_version_example' # str | Repository Version referenced by HREF (optional)
repository_version_added = 'repository_version_added_example' # str | Repository Version referenced by HREF (optional)
repository_version_removed = 'repository_version_removed_example' # str | Repository Version referenced by HREF (optional)
sha256 = 'sha256_example' # str |  (optional)
version = 'version_example' # str | Filter results where version matches value (optional)
version__in = ['version__in_example'] # list[str] | Filter results where version is in a comma-separated list of values (optional)
version__ne = 'version__ne_example' # str | Filter results where version not equal to value (optional)
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # List packages
        api_response = api_instance.list(arch=arch, arch__in=arch__in, arch__ne=arch__ne, checksum_type=checksum_type, checksum_type__in=checksum_type__in, checksum_type__ne=checksum_type__ne, epoch=epoch, epoch__in=epoch__in, epoch__ne=epoch__ne, limit=limit, name=name, name__in=name__in, name__ne=name__ne, offset=offset, ordering=ordering, pkg_id=pkg_id, pkg_id__in=pkg_id__in, release=release, release__in=release__in, release__ne=release__ne, repository_version=repository_version, repository_version_added=repository_version_added, repository_version_removed=repository_version_removed, sha256=sha256, version=version, version__in=version__in, version__ne=version__ne, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentPackagesApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arch** | **str**| Filter results where arch matches value | [optional] 
 **arch__in** | [**list[str]**](str.md)| Filter results where arch is in a comma-separated list of values | [optional] 
 **arch__ne** | **str**| Filter results where arch not equal to value | [optional] 
 **checksum_type** | **str**| Filter results where checksum_type matches value | [optional] 
 **checksum_type__in** | [**list[str]**](str.md)| Filter results where checksum_type is in a comma-separated list of values | [optional] 
 **checksum_type__ne** | **str**| Filter results where checksum_type not equal to value | [optional] 
 **epoch** | **str**| Filter results where epoch matches value | [optional] 
 **epoch__in** | [**list[str]**](str.md)| Filter results where epoch is in a comma-separated list of values | [optional] 
 **epoch__ne** | **str**| Filter results where epoch not equal to value | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__ne** | **str**| Filter results where name not equal to value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **pkg_id** | **str**| Filter results where pkgId matches value | [optional] 
 **pkg_id__in** | [**list[str]**](str.md)| Filter results where pkgId is in a comma-separated list of values | [optional] 
 **release** | **str**| Filter results where release matches value | [optional] 
 **release__in** | [**list[str]**](str.md)| Filter results where release is in a comma-separated list of values | [optional] 
 **release__ne** | **str**| Filter results where release not equal to value | [optional] 
 **repository_version** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_added** | **str**| Repository Version referenced by HREF | [optional] 
 **repository_version_removed** | **str**| Repository Version referenced by HREF | [optional] 
 **sha256** | **str**|  | [optional] 
 **version** | **str**| Filter results where version matches value | [optional] 
 **version__in** | [**list[str]**](str.md)| Filter results where version is in a comma-separated list of values | [optional] 
 **version__ne** | **str**| Filter results where version not equal to value | [optional] 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatedrpmPackageResponseList**](PaginatedrpmPackageResponseList.md)

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
> RpmPackageResponse read(rpm_package_href, fields=fields, exclude_fields=exclude_fields)

Inspect a package

A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/rpm/packages/  Also specify queryset and serializer for Package.

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
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    rpm_package_href = 'rpm_package_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a package
        api_response = api_instance.read(rpm_package_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentPackagesApi->read: %s\n" % e)
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
    api_instance = pulpcore.client.pulp_rpm.ContentPackagesApi(api_client)
    rpm_package_href = 'rpm_package_href_example' # str | 
fields = 'fields_example' # str | A list of fields to include in the response. (optional)
exclude_fields = 'exclude_fields_example' # str | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a package
        api_response = api_instance.read(rpm_package_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContentPackagesApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpm_package_href** | **str**|  | 
 **fields** | **str**| A list of fields to include in the response. | [optional] 
 **exclude_fields** | **str**| A list of fields to exclude from the response. | [optional] 

### Return type

[**RpmPackageResponse**](RpmPackageResponse.md)

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

