import datetime
from dataclasses import dataclass
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from pydantic import parse_obj_as
from typing import List

from config.db import getDBSession
from models.model import t_Seat, t_Course, t_Student
from schemas import seatSchema, courseSchema

seatRouter = APIRouter()

@seatRouter.post("/seat/book", tags= ["Seat"])
def bookSeat(seat: seatSchema.dbSeat ,conn:Session = Depends(getDBSession)):
    # is the reserved_by id exist?
    user = conn.execute(t_Student.select().where(
        t_Student.c.id == seat.reserved_by
    )).first()
    if user == None:
        raise HTTPException(status_code = 400, detail = "Invalid User")

    # is the course exist?
    targetCourse = conn.execute(t_Course.select().where(
        t_Course.c.id == seat.course_id,
        t_Course.c.date == seat.course_date,
    )).first()
    if targetCourse == None: 
        raise HTTPException(status_code = 400, detail = "Invalid Course")

    # is the seat valid (0 ~ # of seat - 1)?
    if seat.seat_id < 0 or seat.seat_id >= targetCourse.seats:
        raise HTTPException(status_code = 400, detail = "Invalid Seat")

    # can't reserve multiple seats by the same one.
    record = conn.execute(t_Seat.select().where(
        t_Seat.c.course_id == seat.course_id,
        t_Seat.c.course_date == seat.course_date,
        t_Seat.c.reserved_by == seat.reserved_by,
    )).first()
    if record : 
        raise HTTPException(status_code = 400, detail = "Invalid Reservation")

    sameSeat = conn.execute(t_Seat.select().where(
        t_Seat.c.seat_id == seat.seat_id
    )).first()
    if sameSeat :
        raise HTTPException(status_code = 400, detail = "Invalid Reservation")

    conn.execute(t_Seat.insert().values(
        {
            "course_id" : seat.course_id,
            "course_date" : seat.course_date,
            "seat_id" : seat.seat_id,
            "reserved_by" : seat.reserved_by
        }
    ))
    return seatSchema.Message(message = "success")

@seatRouter.post("/seat/cancel", tags= ["Seat"])
def cancelBookedSeat(seat: seatSchema.dbSeat, conn:Session = Depends(getDBSession)):
    record = conn.execute(t_Seat.select().where(
        t_Seat.c.course_id == seat.course_id,
        t_Seat.c.course_date == seat.course_date,
        t_Seat.c.seat_id == seat.seat_id,
        t_Seat.c.reserved_by == seat.reserved_by
    )).first()
    if record == None:
        raise HTTPException(status_code = 400, detail = "Invalid Seat")

    conn.execute(t_Seat.delete().where(
        t_Seat.c.course_id == seat.course_id,
        t_Seat.c.course_date == seat.course_date,
        t_Seat.c.seat_id == seat.seat_id,
        t_Seat.c.reserved_by == seat.reserved_by
    ))
    return seatSchema.Message(message = "success")