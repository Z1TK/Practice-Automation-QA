import httpx
from dotenv import load_dotenv
import pytest
import os

load_dotenv()

@pytest.fixture
def async_client():
    with httpx.AsyncClient(base_url=f'{os.getenv("BASE_URL")}') as client:
        yield client