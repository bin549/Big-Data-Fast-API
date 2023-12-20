from app.models.vo import (
    StudentIn,
    ProvinceIn
)
from pydantic import ConfigDict


class Student(StudentIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


class Province(ProvinceIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
