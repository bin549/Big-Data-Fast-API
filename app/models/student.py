from pydantic import BaseModel, ConfigDict


class StudentIn(BaseModel):
    name: str


class Student(StudentIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
