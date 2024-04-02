from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(..., description='The user id')
    password: str = Field(..., description='The user password')
