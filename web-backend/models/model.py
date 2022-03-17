from datetime import datetime
from sqlalchemy import Table,Column, DATE
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

students = Table(
    "Student",
    meta,
    Column('id', String(100), primary_key=True),
    Column('name', String(100)),
    Column('password', String(100)),
)

courses = Table(
    "Course",
    meta,
    Column('id', Integer, primary_key=True),
    Column('date', DATE, nullable=False, default=datetime.now, primary_key=True),
    Column('name', String(100)),
    Column('classroom', Integer, default='0'),
    Column('seats', Integer, default='0'),
    Column('cols', Integer, default='0'),
)

seats = Table(
    "Seat",
    meta,
    Column('course_id', Integer, nullable=False, primary_key=True),
    Column('course_date', DATE, nullable=False, primary_key=True),
    Column('seat_id', Integer, nullable=False, primary_key=True),
    Column('reserved_by', String(100), nullable=False),
)

meta.create_all(engine)