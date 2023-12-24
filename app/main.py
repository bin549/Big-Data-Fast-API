# api: getAreaList(provinceId) -> areaCode, cityName,
#      getProvinceList() -> provinceId, provinceName
#      getSchoolList(selectedCityId) -> schoolId, schoolName,
#      getSubjectList(schoolId) -> id, subject
#      getTermList() -> termId, name

# api: getClassList(selectedSchoolId, gradeId) -> classId, className
#      getStudentList(selectedClassId.value) -> studentId, name

# api: getTeacherList(school_id)

"""statistic: student"""
# api:
# statistic:
#   api1 -> 评价总数, 平均每学期收到评价数, 正面评价, 负面评价, 收到最多的评价前三, 班级平均数
#   api2 -> 评语统计柱状图


"""statistic: teacher"""
# api:
# statistic:
#   api1 -> 评价总数, 平均每学期收到评价数, 正面评价, 负面评价, 收到最多的评价前三, 班级平均数
#   api2 -> 评语统计柱状图
# count:
#   api1 -> teacher
#   api2 -> 评语统计柱状图

import logging
from contextlib import asynccontextmanager
from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.exception_handlers import http_exception_handler
from app.database import database
from app.logging_conf import configure_logging
from app.routers.area import router as area_router
from app.routers.entity import router as entity_router
from app.routers.timezone import router as timezone_router
from fastapi.middleware.cors import CORSMiddleware


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    configure_logging()
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.add_middleware(CorrelationIdMiddleware)

app.include_router(area_router, prefix='/api')
app.include_router(entity_router, prefix='/api')
app.include_router(timezone_router, prefix='/api')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request, exc):
    logger.error(f"HTTPException: {exc.status_code} {exc.detail}")
    return await http_exception_handler(request, exc)
