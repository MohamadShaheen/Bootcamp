from pydantic import BaseModel


class Student(BaseModel):
    name: str
    id: str
    age: int
    classes: list
