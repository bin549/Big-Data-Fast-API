import databases
import sqlalchemy

from app.config import config

metadata = sqlalchemy.MetaData()

student_table = sqlalchemy.Table(
    "t_student",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


province_table = sqlalchemy.Table(
    "t_province",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


city_table = sqlalchemy.Table(
    "t_city",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


school_table = sqlalchemy.Table(
    "t_school",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

classes_table = sqlalchemy.Table(
    "t_classes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


student_evaluation_table = sqlalchemy.Table(
    "t_student_evaluation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

teacher_table = sqlalchemy.Table(
    "t_teacher",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

teacher_evaluation_table = sqlalchemy.Table(
    "t_teacher_evaluation",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)

semester_evaluation_table = sqlalchemy.Table(
    "t_semester",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


engine = sqlalchemy.create_engine(
    config.DATABASE_URL
)

metadata.create_all(engine)
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
