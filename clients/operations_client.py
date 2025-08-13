import allure
from httpx import Response

from clients.base_client import AsyncBaseClient, get_async_http_client
from schema.operations import CreateTransactionSchema, UpdateTransactionSchema, OperationSchema
from config import Settings
from tools.routes import ApiRoutes

class OperationsAsyncClient(AsyncBaseClient):

    @allure.step('Get list of operations')
    async def get_operations_api(self) -> Response:
        return await self.get(ApiRoutes.OPERATIONS)
    
    @allure.step('Get operation by id {operation_id}')
    async def get_operation_api(self, operation_id: int) -> Response:
        return await self.get(f'{ApiRoutes.OPERATIONS}/{operation_id}')
    
    @allure.step('Create operation')
    async def create_operation_api(self, operation: CreateTransactionSchema) -> Response:
        return await self.post(
            ApiRoutes.OPERATIONS,
            json=operation.model_dump(mode='json', by_alias=True)
        )
    
    @allure.step('Update operation by id {operation_id}')
    async def update_operation_api(
        self, 
        operation_id: int,
        operation: UpdateTransactionSchema
        ) -> Response:
        return await self.patch(
            f'{ApiRoutes.OPERATIONS}/{operation_id}',
            operation.model_dump(mode='json', exclude_none=True, by_alias=True)
        )
    
    @allure.step('Delete operation by id {operation_id}')
    async def delete_operatopm_api(self, operation_id: int) -> Response:
        return await self.delete(
            f'{ApiRoutes.OPERATIONS}/{operation_id}',
        )
    
    async def create_operation(self) -> OperationSchema:

        request = CreateTransactionSchema()

        response = await self.create_operation_api(request)

        return OperationSchema.model_validate_json(response.text)


def get_assync_operation_client(settings: Settings) -> OperationsAsyncClient:
    return OperationsAsyncClient(
        async_client=get_async_http_client(settings.fake_bank_http_client)
        )