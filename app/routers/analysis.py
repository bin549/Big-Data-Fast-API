from fastapi import APIRouter, HTTPException
import logging
from app.models.vo import (
    ProvinceIn,
)

from app.models.dto import (
    Province,
    City,
    County,
)
from app.database import (
    database,
    student_evaluation_table,
    student_table,
    teacher_table,

)
from sqlalchemy import (
    and_, func)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/student_evaluation/list")
async def list_student_evaluation(student_id: str, subject_ids: str, term_ids: str):
    logger.info("Getting all posts")
    query = student_evaluation_table.select().where(
        and_(
            student_evaluation_table.c.student_id == student_id,
            student_evaluation_table.c.subject_id.in_(
                [int(subject_ids_str) for subject_ids_str in subject_ids.split(",")]),
            student_evaluation_table.c.term_id.in_(term_ids.split(",")),
        )
    )
    logger.debug(query)
    student_evaluations = await database.fetch_all(query)
    return student_evaluations


@router.get("/student_evaluation/list_week")
async def list_student_evaluation_week(student_id: str):
    logger.info("Getting all posts")
    query = student_evaluation_table.select().where(
        and_(
            student_evaluation_table.c.student_id == student_id,
        )
    )
    logger.debug(query)
    student_evaluations = await database.fetch_all(query)
    return student_evaluations


@router.get("/student_evaluation/list_class")
async def list_student_evaluation_week(class_id: str, term_id: str):
    logger.info("Getting list_class")
    query = student_table.select().where(student_table.c.class_id == class_id)
    student_query = await database.fetch_all(query)
    student_ids = [student.id for student in student_query]
    query = student_evaluation_table.select().where(and_(
        student_evaluation_table.c.student_id.in_(student_ids),
        student_evaluation_table.c.term_id == term_id
    ))
    student_evaluations = await database.fetch_all(query)
    return student_evaluations


@router.get("/student_evaluation/list_teacher")
async def list_student_evaluation(teacher_id: str, subject_ids: str, term_ids: str):
    logger.info("Getting all posts")
    query = student_evaluation_table.select().where(
        and_(
            student_evaluation_table.c.teacher_id == teacher_id,
            student_evaluation_table.c.subject_id.in_(
                [int(subject_ids_str) for subject_ids_str in subject_ids.split(",")]),
            student_evaluation_table.c.term_id.in_(term_ids.split(",")),
        )
    )
    logger.debug(query)
    student_evaluations = await database.fetch_all(query)
    return student_evaluations


@router.get("/student_evaluation/list_school")
async def list_student_evaluation(school_id: int, subject_ids: str, term_ids: str):
    logger.info("Getting all posts")
    query = teacher_table.select().where(teacher_table.c.school_id == school_id)
    teacher_query = await database.fetch_all(query)
    teacher_maps = {teacher.id: teacher.name for teacher in teacher_query}
    query = student_evaluation_table.select().where(
        and_(
            student_evaluation_table.c.subject_id.in_(
                [int(subject_ids_str) for subject_ids_str in subject_ids.split(",")]),
            student_evaluation_table.c.term_id.in_(term_ids.split(",")),
        )
    ).group_by(student_evaluation_table.c.teacher_id).with_only_columns(
        student_evaluation_table.c.teacher_id,
        func.count().label('count')
    )
    results = await database.fetch_all(query)
    xData = []
    yData = []
    for row in results:
        if row['teacher_id'] in teacher_maps.keys():
            teacher_id = row['teacher_id']
            count = row['count']
            xData.append(teacher_maps[teacher_id])
            yData.append(count)
    if len(xData) == 0:
        return []
    sorted_data = sorted(zip(xData, yData), key=lambda x: x[1], reverse=False)
    sorted_names, sorted_numbers = zip(*sorted_data)
    return [sorted_names, sorted_numbers]
