from typing import Any

import allure
from httpx import AsyncClient, URL, Response, QueryParams
from httpx._types import RequestData, RequestFiles

from config import HTTPClientConfig
from clients.event_hooks import *

class AsyncBaseClient:

    def __init__(self, async_client: AsyncClient):
        self.async_client = async_client

    allure.step('Make get request to {url}')
    async def get(
            self, url: URL | str, 
            params: QueryParams | None = None
            ) -> Response:
        return await self.async_client.get(url, params=params)

    allure.step('Make POST request to {url}')
    async def post(
            self, 
            url: URL | str, 
            data: RequestData | None = None, 
            json: Any | None = None,
            files: RequestFiles | None = None
            ) -> Response:
        return await self.async_client.post(
            url, data=data, json=json, files=files
            )
    
    allure.step('Make PATCH request to {url}')
    async def patch(
            self,
            url: URL | str,
            json: Any | None = None
    ) -> Response:
        return await self.async_client.patch(
            url=url, json=json
        )
    
    allure.step('Make DELETE request to {url}')
    async def delete(
            self, 
            url: URL | str,
    ) -> Response:
        return await self.async_client.delete(url=url)
    
def get_async_http_client(config: HTTPClientConfig) -> AsyncClient:
    return AsyncClient(
        base_url=config.client_url,
        event_hooks={
            'request': [log_request_event_hook],
            'response': [log_respose_event_hook]
        }
    )