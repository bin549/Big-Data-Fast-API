import sqlalchemy
from fastapi import APIRouter
import logging

from app.models.vo import (
    SemesterIn,
)

from app.models.dto import (
    Semester,
)
from app.database import (
    database,
    semester_table,
    subject_table,
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/semester/list")
async def list_semester():
    logger.info("Getting all semesters")
    query = semester_table.select()
    logger.debug(query)
    semesters = [{'termId': semester['id'], 'name': semester['name']} for semester in await database.fetch_all(query)]
    return semesters


@router.get("/subject/list")
async def list_subject(school_id: int):
    logger.info("Getting all subject")
    query = subject_table.select(subject_table.c.school_id == school_id)
    logger.debug(query)
    subjects = [{'id': subject['id'], 'subject': subject['name']} for subject in await database.fetch_all(query)]
    return subjects
