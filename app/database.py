import databases
import sqlalchemy

from app.config import config

metadata = sqlalchemy.MetaData()

student_table = sqlalchemy.Table(
    "student",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String)
)


engine = sqlalchemy.create_engine(
    config.DATABASE_URL
)

metadata.create_all(engine)
database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
