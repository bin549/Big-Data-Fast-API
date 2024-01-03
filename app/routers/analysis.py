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

)
from sqlalchemy import and_

router = APIRouter()

logger = logging.getLogger(__name__)


@router.get("/student_evaluation/list")
async def list_student_evaluation(student_id: str, term_id: str):
    logger.info("Getting all posts")
    query = student_evaluation_table.select(
        and_(
            student_evaluation_table.c.student_id == student_id,
            student_evaluation_table.c.term_id == term_id,
        )
    )
    logger.debug(query)
    student_evaluations = await database.fetch_all(query)
    return student_evaluations
