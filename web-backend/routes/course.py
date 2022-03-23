import datetime
from email import message
from msilib import schema
from fastapi import APIRouter, HTTPException
from pydantic import parse_obj_as
from typing import List
from sqlalchemy.sql import select

from models.model import t_Course, t_Seat,t_Student
from config.db import conn
from schemas import courseSchema,seatSchema

courseRouter = APIRouter()

@courseRouter.get("/course/getAllCourse",response_model= List[courseSchema.dbCourse],tags=["Course"])
def getAllCourse():
    return conn.execute(t_Course.select()).fetchall()

@courseRouter.get("/course/getCourse",response_model= courseSchema.SeatStatusMessage,tags=["Course"])
def getCourse(course_id: str, date: datetime.date):

    dbClassInfo = conn.execute(select(t_Course.c.cols,t_Course.c.seats).where(
        t_Course.c.id == course_id,
        t_Course.c.date == date
        )).first()

    if dbClassInfo is None:
        raise HTTPException(status_code= 400, detail= "Invalid Course")

    dbSeatInfo = conn.execute(select(t_Seat.c.seat_id,t_Seat.c.reserved_by,t_Student.c.name).where(
        t_Seat.c.course_id == course_id,
        t_Seat.c.course_date == date,
        t_Seat.c.reserved_by == t_Student.c.id
        ).order_by(t_Seat.c.seat_id)).all()

    reservedByDataClass = parse_obj_as(List[seatSchema.reserveName], dbSeatInfo)
    courseSeatDataClass = courseSchema.courseSeat(numberPerRow= dbClassInfo.cols, totalSeat=dbClassInfo.seats,seats=reservedByDataClass)
    message = courseSchema.SeatStatusMessage(message="sucess",data = courseSeatDataClass)
    return message


@courseRouter.post("/addCourse")
def addCourse(c: courseSchema.dbCourse):
    conn.execute(t_Course.insert().values(c.dict()))
    return "success"
