from http import HTTPStatus

import allure
import pytest

from clients.operations_client import OperationsAsyncClient
from schema.operations import *
from tools.assertions.base import assert_status_code
from tools.assertions.operations import assert_operation, assert_create_operation
from tools.assertions.schema import validate_json_schema

@pytest.mark.operations
@pytest.mark.regression
class TestOperations:
    @allure.title('Get operations')
    async def test_get_operations(
        self,
        operation_client: OperationsAsyncClient
    ):
        response = await operation_client.get_operations_api()
        
        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(
            response.json(), 
            OperationsSchema.model_json_schema()
            )
        
    @allure.title('Get operation')
    async def test_get_operation(
        self,
        operation_client: OperationsAsyncClient,
        function_operation: OperationSchema
    ):
        response = await operation_client.get_operation_api(
            function_operation.id
        )
        operation = OperationSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_operation(operation, function_operation)

        validate_json_schema(response.json(), operation.model_json_schema())

    @allure.title('Create operation')
    async def test_create_operation(
        self,
        operation_client: OperationsAsyncClient
    ):
        request = CreateTransactionSchema()
        response = await operation_client.create_operation_api(request)
        operation = OperationSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.CREATED)
        assert_create_operation(operation, request)

        validate_json_schema(response.json(), operation.model_json_schema())

    @allure.title('Update operation')
    async def test_update_operation(
        self,
        operation_client: OperationsAsyncClient,
        function_operation: OperationSchema
    ):
        request = UpdateTransactionSchema()
        response = await operation_client.update_operation_api(
            function_operation.id,
            request
        )
        operation = OperationSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_operation(operation, request)

        validate_json_schema(response.json(), operation.model_json_schema())

    @allure.title('Delete operation')
    async def test_delete_operation(
        self,
        operation_client: OperationsAsyncClient,
        function_operation: OperationSchema
    ):
        response = await operation_client.delete_operatopm_api(function_operation.id)

        assert_status_code(response.status_code, HTTPStatus.OK)

        get_response = await operation_client.get_operation_api(function_operation.id)

        assert_status_code(get_response.status_code, HTTPStatus.NOT_FOUND)     
        