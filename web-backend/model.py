from sqlalchemy import Column, Date, ForeignKey, ForeignKeyConstraint, String, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Course(Base):
    __tablename__ = 'Course'

    id = Column(String(10), primary_key=True, nullable=False)
    date = Column(Date, primary_key=True, nullable=False, server_default=text("(curdate())"))
    name = Column(String(100), server_default=text("''"))
    classroom = Column(INTEGER, server_default=text("'0'"))
    seats = Column(INTEGER, server_default=text("'0'"))
    cols = Column(INTEGER, server_default=text("'0'"))


class Student(Base):
    __tablename__ = 'Student'

    id = Column(String(100), primary_key=True)
    name = Column(String(100), server_default=text("''"))
    password = Column(String(100), server_default=text("''"))


class Seat(Base):
    __tablename__ = 'Seat'
    __table_args__ = (
        ForeignKeyConstraint(['course_id', 'course_date'], ['Course.id', 'Course.date'], ondelete='CASCADE', onupdate='CASCADE'),
    )

    course_id = Column(String(10), primary_key=True, nullable=False)
    course_date = Column(Date, primary_key=True, nullable=False)
    seat_id = Column(INTEGER, primary_key=True, nullable=False)
    reserved_by = Column(ForeignKey('Student.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)

    course = relationship('Course')
    Student = relationship('Student')