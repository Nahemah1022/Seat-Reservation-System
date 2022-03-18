from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, MetaData, String, Table, text
from sqlalchemy.dialects.mysql import INTEGER
from config.db import meta, engine

t_Course = Table(
    'Course', meta,
    Column('id', String(10), primary_key=True, nullable=False),
    Column('date', Date, primary_key=True, nullable=False, server_default=text("(curdate())")),
    Column('name', String(100), server_default=text("''")),
    Column('classroom', String(100), server_default=text("''")),
    Column('seats', INTEGER, server_default=text("'0'")),
    Column('cols', INTEGER, server_default=text("'0'"))
)

t_Student = Table(
    'Student', meta,
    Column('id', String(100), primary_key=True),
    Column('name', String(100), server_default=text("''")),
    Column('password', String(100), server_default=text("''"))
)

t_Seat = Table(
    'Seat', meta,
    Column('course_id', String(10), primary_key=True, nullable=False),
    Column('course_date', Date, primary_key=True, nullable=False),
    Column('seat_id', INTEGER, primary_key=True, nullable=False),
    Column('reserved_by', ForeignKey('Student.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
    ForeignKeyConstraint(['course_id', 'course_date'], ['Course.id', 'Course.date'], ondelete='CASCADE', onupdate='CASCADE')
)

meta.create_all(engine)