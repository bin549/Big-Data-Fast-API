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

)
from sqlalchemy import and_

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

