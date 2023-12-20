import sqlalchemy
from fastapi import APIRouter
import logging
from app.models.vo import (
    StudentIn,
)

from app.models.dto import (
    Student,
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/student/list")
async def list():
    logger.info("Getting all posts")
    return 11
