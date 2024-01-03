import databases
import sqlalchemy

from app.config import config

metadata = sqlalchemy.MetaData()

student_table = sqlalchemy.Table(
    "t_student",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("sex", sqlalchemy.String),
    sqlalchemy.Column("class_id", sqlalchemy.ForeignKey("t_classes.id"), nullable=False)
)


province_table = sqlalchemy.Table(
    "t_province",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


city_table = sqlalchemy.Table(
    "t_city",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("province_id", sqlalchemy.ForeignKey("t_province.id"), nullable=False)
)


county_table = sqlalchemy.Table(
    "t_county",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("city_id", sqlalchemy.ForeignKey("t_city.id"), nullable=False)
)

school_table = sqlalchemy.Table(
    "t_school",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("county_id", sqlalchemy.ForeignKey("t_county.id"), nullable=False)
)

grade_table = sqlalchemy.Table(
    "t_grade",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)

classes_table = sqlalchemy.Table(
    "t_classes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("cid", sqlalchemy.Integer),
    sqlalchemy.Column("grade_id", sqlalchemy.ForeignKey("t_grade.id"), nullable=False),
    sqlalchemy.Column("school_id", sqlalchemy.ForeignKey("t_school.id"), nullable=False)
)

teacher_table = sqlalchemy.Table(
    "t_teacher",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("school_id", sqlalchemy.ForeignKey("t_school.id"), nullable=False)
)

teacher_table = sqlalchemy.Table(
    "t_teach",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("teacher_id", sqlalchemy.ForeignKey("t_teacher.id"), nullable=False),
    sqlalchemy.Column("class_id", sqlalchemy.ForeignKey("t_classes.id"), nullable=False)
)

semester_table = sqlalchemy.Table(
    "t_semester",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

student_evaluation_table = sqlalchemy.Table(
    "t_student_evaluation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("content", sqlalchemy.String),
    sqlalchemy.Column("score", sqlalchemy.Integer),
    sqlalchemy.Column("subject", sqlalchemy.String),
    sqlalchemy.Column("week", sqlalchemy.Integer),
    sqlalchemy.Column("student_id", sqlalchemy.ForeignKey("t_student.id"), nullable=False),
    sqlalchemy.Column("teacher_id", sqlalchemy.ForeignKey("t_teacher.id"), nullable=False),
    sqlalchemy.Column("term_id", sqlalchemy.ForeignKey("t_semester.id"), nullable=False)
)


teacher_evaluation_table = sqlalchemy.Table(
    "t_teacher_evaluation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


subject_table = sqlalchemy.Table(
    "t_subject",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("weights", sqlalchemy.Integer),
    sqlalchemy.Column("school_id", sqlalchemy.ForeignKey("t_school.id"), nullable=False)
)



engine = sqlalchemy.create_engine(
    config.DATABASE_URL
)

# metadata.drop_all(engine)
metadata.create_all(engine)
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
