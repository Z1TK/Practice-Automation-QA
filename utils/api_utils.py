from httpx import AsyncClient

async def get_all_products(client: AsyncClient):
    response = await client.get('/productsList')
    response.raise_for_status()
    return response

async def post_all_products(client: AsyncClient):
    response = await client.post('/productsList')
    return response

async def post_search_product(client: AsyncClient,  req_param):
    response = await client.post(
        '/searchProduct',
        data={'search_product': req_param}
        )
    return response