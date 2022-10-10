from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from httpx import AsyncClient

from backend_we_eat.models.food.intolerance import IntolernaceEnum
from backend_we_eat.utils import edamam

router = APIRouter()


@router.get('/recipies')
async def get_recipies(
    query: str,
    diet: list[IntolernaceEnum] = Query(None),
    httpx_client: AsyncClient = Depends(edamam.get_edamama_client),
):

    diet_params = [diet_param.value for diet_param in diet]
    response = await edamam.fetch_recipies(query=query, diets=diet_params, client=httpx_client)

    return response
