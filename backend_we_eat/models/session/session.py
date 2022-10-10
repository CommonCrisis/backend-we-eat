from pydantic import BaseModel


class Session(BaseModel):
    session_id: int
    users: list[str]
