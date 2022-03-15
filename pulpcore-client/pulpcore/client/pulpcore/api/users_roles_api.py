# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulpcore.api_client import ApiClient
from pulpcore.client.pulpcore.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UsersRolesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, auth_user_href, user_role, **kwargs):  # noqa: E501
        """Create an user role  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(auth_user_href, user_role, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_user_href: (required)
        :param UserRole user_role: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UserRoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(auth_user_href, user_role, **kwargs)  # noqa: E501

    def create_with_http_info(self, auth_user_href, user_role, **kwargs):  # noqa: E501
        """Create an user role  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(auth_user_href, user_role, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_user_href: (required)
        :param UserRole user_role: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UserRoleResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'auth_user_href',
            'user_role'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_user_href' is set
        if self.api_client.client_side_validation and ('auth_user_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['auth_user_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auth_user_href` when calling `create`")  # noqa: E501
        # verify the required parameter 'user_role' is set
        if self.api_client.client_side_validation and ('user_role' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_role'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_role` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_user_href' in local_var_params:
            path_params['auth_user_href'] = local_var_params['auth_user_href']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_role' in local_var_params:
            body_params = local_var_params['user_role']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{auth_user_href}roles/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserRoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, auth_users_user_role_href, **kwargs):  # noqa: E501
        """Delete an user role  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(auth_users_user_role_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_users_user_role_href: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_with_http_info(auth_users_user_role_href, **kwargs)  # noqa: E501

    def delete_with_http_info(self, auth_users_user_role_href, **kwargs):  # noqa: E501
        """Delete an user role  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(auth_users_user_role_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_users_user_role_href: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'auth_users_user_role_href'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_users_user_role_href' is set
        if self.api_client.client_side_validation and ('auth_users_user_role_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['auth_users_user_role_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auth_users_user_role_href` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_users_user_role_href' in local_var_params:
            path_params['auth_users_user_role_href'] = local_var_params['auth_users_user_role_href']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{auth_users_user_role_href}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, auth_user_href, **kwargs):  # noqa: E501
        """List user roles  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(auth_user_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_user_href: (required)
        :param str content_object: content_object
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str ordering: Which field to use when ordering the results.
        :param str role:
        :param str role__contains:
        :param str role__icontains:
        :param list[str] role__in: Multiple values may be separated by commas.
        :param str role__startswith:
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatedUserRoleResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(auth_user_href, **kwargs)  # noqa: E501

    def list_with_http_info(self, auth_user_href, **kwargs):  # noqa: E501
        """List user roles  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(auth_user_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_user_href: (required)
        :param str content_object: content_object
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param str ordering: Which field to use when ordering the results.
        :param str role:
        :param str role__contains:
        :param str role__icontains:
        :param list[str] role__in: Multiple values may be separated by commas.
        :param str role__startswith:
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatedUserRoleResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'auth_user_href',
            'content_object',
            'limit',
            'offset',
            'ordering',
            'role',
            'role__contains',
            'role__icontains',
            'role__in',
            'role__startswith',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_user_href' is set
        if self.api_client.client_side_validation and ('auth_user_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['auth_user_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auth_user_href` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_user_href' in local_var_params:
            path_params['auth_user_href'] = local_var_params['auth_user_href']  # noqa: E501

        query_params = []
        if 'content_object' in local_var_params and local_var_params['content_object'] is not None:  # noqa: E501
            query_params.append(('content_object', local_var_params['content_object']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
        if 'role' in local_var_params and local_var_params['role'] is not None:  # noqa: E501
            query_params.append(('role', local_var_params['role']))  # noqa: E501
        if 'role__contains' in local_var_params and local_var_params['role__contains'] is not None:  # noqa: E501
            query_params.append(('role__contains', local_var_params['role__contains']))  # noqa: E501
        if 'role__icontains' in local_var_params and local_var_params['role__icontains'] is not None:  # noqa: E501
            query_params.append(('role__icontains', local_var_params['role__icontains']))  # noqa: E501
        if 'role__in' in local_var_params and local_var_params['role__in'] is not None:  # noqa: E501
            query_params.append(('role__in', local_var_params['role__in']))  # noqa: E501
            collection_formats['role__in'] = 'csv'  # noqa: E501
        if 'role__startswith' in local_var_params and local_var_params['role__startswith'] is not None:  # noqa: E501
            query_params.append(('role__startswith', local_var_params['role__startswith']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{auth_user_href}roles/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedUserRoleResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, auth_users_user_role_href, **kwargs):  # noqa: E501
        """Inspect an user role  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(auth_users_user_role_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_users_user_role_href: (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UserRoleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(auth_users_user_role_href, **kwargs)  # noqa: E501

    def read_with_http_info(self, auth_users_user_role_href, **kwargs):  # noqa: E501
        """Inspect an user role  # noqa: E501

        ViewSet for UserRole.  NOTE: This API endpoint is in \"tech preview\" and subject to change  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(auth_users_user_role_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str auth_users_user_role_href: (required)
        :param str fields: A list of fields to include in the response.
        :param str exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UserRoleResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'auth_users_user_role_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'auth_users_user_role_href' is set
        if self.api_client.client_side_validation and ('auth_users_user_role_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['auth_users_user_role_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `auth_users_user_role_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'auth_users_user_role_href' in local_var_params:
            path_params['auth_users_user_role_href'] = local_var_params['auth_users_user_role_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth']  # noqa: E501

        return self.api_client.call_api(
            '{auth_users_user_role_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserRoleResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
