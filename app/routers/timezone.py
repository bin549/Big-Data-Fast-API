import sqlalchemy
from sqlalchemy import (
    desc,
    cast,
    Integer
)
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
    coin_table,
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/semester/list")
async def list_semester():
    logger.info("Getting all semesters")
    query = semester_table.select().order_by(desc(cast(semester_table.c.id, Integer)))
    logger.debug(query)
    semesters = [{'termId': semester['id'], 'name': semester['name']} for semester in await database.fetch_all(query)]
    return semesters


@router.get("/coin/list")
async def list_subject(school_id: int):
    logger.info("Getting all coins")
    query = coin_table.select(coin_table.c.school_id == school_id)
    logger.debug(query)
    coins = [{'id': coin['id'], 'name': coin['name']} for coin in await database.fetch_all(query)]
    return coins


@router.get("/subject/list")
async def list_subject(school_id: int):
    logger.info("Getting all subject")
    query = subject_table.select(subject_table.c.school_id == school_id)
    logger.debug(query)
    subjects = [{'id': subject['id'], 'subject': subject['name']} for subject in await database.fetch_all(query)]
    return subjects
