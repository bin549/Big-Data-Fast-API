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
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/semester/list")
async def list_semester():
    logger.info("Getting all semesters")
    query = semester_table.select()
    logger.debug(query)
    schools = await database.fetch_all(query)
    return schools
