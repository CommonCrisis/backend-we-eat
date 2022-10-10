from pydantic import BaseModel

from backend_we_eat.models.food import intolerance


class User(BaseModel):
    user_id: int
    user_name: str
    intolerances: list[intolerance.Intolerance] = []
    favourite_food: list[str] = []
