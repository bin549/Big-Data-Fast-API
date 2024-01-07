import sqlalchemy
from fastapi import APIRouter
import logging

from app.models.vo import (
    SchoolIn,
    GradeIn,
    StudentIn,
)

from app.models.dto import (
    School,
    Grade,
    Student,
)
from app.database import (
    database,
    school_table,
    grade_table,
    classes_table,
    student_table,
    teacher_table,
)
from app.routers.area import (
    list_counties,
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/school/list")
async def list_schools(county_id: int):
    logger.info("Getting all schools")
    query = school_table.select(school_table.c.county_id == county_id)
    logger.debug(query)
    schools = await database.fetch_all(query)
    return schools


@router.get("/school/list_city")
async def list_schools_city(city_id: int):
    logger.info("Getting all schools")
    counties_query = await list_counties(city_id)
    county_ids = [county.id for county in counties_query]
    query = school_table.select().where(school_table.c.county_id.in_(county_ids))
    logger.debug(query)
    schools = [{'schoolId': school['id'], 'schoolName': school['name']} for school in await database.fetch_all(query)]
    return schools


@router.get("/grade/list")
async def list_grades():
    logger.info("Getting all grades")
    query = grade_table.select()
    logger.debug(query)
    schools = await database.fetch_all(query)
    return schools


@router.get("/classes/list")
async def list_classes(school_id: int, grade_id: int):
    logger.info("Getting all classes")
    query = classes_table.select().where(
        (classes_table.c.school_id == school_id) & (classes_table.c.grade_id == grade_id)
    )
    logger.debug(query)
    cls = [{'classId': cls['id'], 'className': cls['name']} for cls in await database.fetch_all(query)]
    return cls


@router.get("/student/list")
async def list(class_id: str):
    logger.info("Getting all students")
    query = student_table.select(student_table.c.class_id == class_id)
    logger.debug(query)
    students = await database.fetch_all(query)
    return students


@router.get("/teacher/list")
async def list(school_id: int):
    logger.info("Getting all teachers")
    print(school_id)
    query = teacher_table.select(teacher_table.c.school_id == school_id)
    logger.debug(query)
    teachers = [{'teacherId': teacher['id'], 'teacherName': teacher['name']} for teacher in await database.fetch_all(query)]
    return teachers
