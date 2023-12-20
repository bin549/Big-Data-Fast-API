from pydantic import BaseModel


class StudentIn(BaseModel):
    name: str


class ProvinceIn(BaseModel):
    name: str
