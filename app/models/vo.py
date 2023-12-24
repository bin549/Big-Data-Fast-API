from pydantic import BaseModel


class StudentIn(BaseModel):
    name: str


class ProvinceIn(BaseModel):
    name: str


class CityIn(BaseModel):
    name: str


class CountyIn(BaseModel):
    name: str


class SchoolIn(BaseModel):
    name: str


class GradeIn(BaseModel):
    name: str

class SemesterIn(BaseModel):
    name: str
