import httpx
from dotenv import load_dotenv
import pytest_asyncio
import os

load_dotenv()

@pytest_asyncio.fixture
async def async_client():
    async with httpx.AsyncClient(base_url=f'{os.getenv("BASE_URL")}') as client:
        yield client