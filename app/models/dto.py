from app.models.vo import (
    StudentIn,
    ProvinceIn,
    CityIn,
    CountyIn,
    SchoolIn,
    GradeIn,
    SemesterIn,
)
from pydantic import ConfigDict


class Student(StudentIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


class Province(ProvinceIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


class City(CityIn):
    model_config = ConfigDict(from_attributes=True)

    id: int


class County(CountyIn):
    model_config = ConfigDict(from_attributes=True)

    id: int

class School(SchoolIn):
    model_config = ConfigDict(from_attributes=True)

    id: int

class Grade(GradeIn):
    model_config = ConfigDict(from_attributes=True)

    id: int

class Semester(SemesterIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
