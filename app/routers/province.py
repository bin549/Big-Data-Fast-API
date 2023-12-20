from fastapi import APIRouter, HTTPException
import logging
from app.models.vo import (
    ProvinceIn,
)

from app.models.dto import (
    Province,
)
from app.database import (
    database,
    province_table,
)
router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/province/list", response_model=list[Province])
async def list():
    logger.info("Getting all posts")
    query = province_table.select()
    logger.debug(query)
    provinces = await database.fetch_all(query)
    return provinces
