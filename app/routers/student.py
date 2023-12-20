import sqlalchemy
from fastapi import APIRouter
import logging
from app.models.student import (
    Student,
    StudentIn,
)

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/student")
async def get_all_posts():
    logger.info("Getting all posts")
    return 11
