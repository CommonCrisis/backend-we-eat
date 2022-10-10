import os

import httpx


async def fetch_recipies(query: str, diets: list[str], client: httpx.AsyncClient) -> dict:
    app_id: str = os.getenv('EDAMAM_ID')
    app_key: str = os.getenv('EDAMAM_KEY')
    parameters = {'q': query, 'app_id': app_id, 'app_key': app_key, 'type': 'public'}

    additonal_params = {'health': diets}

    params_in = {**parameters, **additonal_params}

    response = await client.get(url='https://api.edamam.com/api/recipes/v2', params=params_in)

    return response.json()


async def get_edamama_client():
    client = httpx.AsyncClient()
    try:
        yield client
    finally:
        await client.aclose()
