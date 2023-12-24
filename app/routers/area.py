from fastapi import APIRouter, HTTPException
import logging
from app.models.vo import (
    ProvinceIn,
    CityIn,
    CountyIn,
)

from app.models.dto import (
    Province,
    City,
    County,
)
from app.database import (
    database,
    province_table,
    city_table,
    county_table,
)
router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/province/list")
async def list_provinces():
    logger.info("Getting all posts")
    query = province_table.select()
    logger.debug(query)
    provinces = [{'provinceId': province['id'], 'provinceName': province['name']} for province in await database.fetch_all(query)]
    return provinces

@router.get("/city/list")
async def list_cities(province_id: int):
    logger.info("Getting all citys")
    query = city_table.select(city_table.c.province_id == province_id)
    logger.debug(query)
    cities = [{'areaCode': city['id'], 'cityName': city['name']} for city in await database.fetch_all(query)]
    return cities


@router.get("/county/list")
async def list_counties(city_id: int):
    logger.info("Getting all counties")
    query = county_table.select(county_table.c.city_id == city_id)
    logger.debug(query)
    counties = await database.fetch_all(query)
    return counties
