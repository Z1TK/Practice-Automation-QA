import pytest
from utils.api_utils import *

@pytest.mark.asyncio
async def test_get_products(async_client):
    result = await get_all_products(async_client)
    data = result.json()

    assert result.status_code == 200
    assert 'products' in data

@pytest.mark.asyncio
async def test_post_products(async_client):
    result = await post_all_products(async_client)
    data = result.json()

    assert data['responseCode'] == 405
    assert 'message' in data
    assert data['message'] == 'This request method is not supported.'


@pytest.mark.asyncio
@pytest.mark.parametrize('req_param', ['top', 'tshirt', 'jean'])
async def test_search_products(async_client, req_param):
    result = await post_search_product(async_client, req_param)
    data = result.json()

    if req_param == 'top':
        assert data['products'][0]['category']['category'] == 'Tops'
    elif req_param == 'jean':
        assert data['products'][0]['category']['category'] == 'Jeans'
    elif req_param == 'tshirt':
        assert data['products'][0]['category']['category'] == 'Tshirts'

    
