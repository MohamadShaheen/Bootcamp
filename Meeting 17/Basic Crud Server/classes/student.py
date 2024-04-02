from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str = Field(..., description='The name of the student')
    id: str = Field(..., description='The id of the student')
    age: int = Field(..., description='The age of the student')
    classes: list = Field(..., description='The classes of the student')
