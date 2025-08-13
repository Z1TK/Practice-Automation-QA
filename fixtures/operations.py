import pytest
from collections.abc import AsyncGenerator

from clients.operations_client import get_assync_operation_client, OperationsAsyncClient
from config import Settings
from schema.operations import OperationSchema

@pytest.fixture
def operation_client(settings: Settings) -> OperationsAsyncClient:
    return get_assync_operation_client(settings)

@pytest.fixture
async def function_operation(
    operation_client: OperationsAsyncClient
    ) -> AsyncGenerator[OperationSchema, None]:
    operation = await operation_client.create_operation()
    yield operation
    await operation_client.delete_operatopm_api(operation.id)