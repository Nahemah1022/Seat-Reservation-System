import datetime
from dataclasses import dataclass
from fastapi import APIRouter
from config.db import conn
from models.model import t_Seat
from schemas import seatSchema 

seatRouter = APIRouter()

@seatRouter.post("/book")
def bookSeat(course_id : str, course_date : datetime.date, seat_id : int, reserved_by : str):
    # asume that the request is always valid.
    # we don't handle the situation that the user trys to book the reserved seat.
    # if the seat is reserved or unclickable, the user won't access this route.
    conn.execute(t_Seat.insert().values(
        {
            "course_id" : course_id,
            "course_date" : course_date,
            "seat_id" : seat_id,
            "reserved_by" : reserved_by
        }
    ))
    return "success"

@seatRouter.post("/cancel")
def cancelBookedSeat(course_id : str, course_date : datetime.date, seat_id : int, reserved_by : str):
    conn.execute(t_Seat.delete().where(
        t_Seat.c.course_id == course_id,
        t_Seat.c.course_date == course_date,
        t_Seat.c.seat_id == seat_id,
        t_Seat.c.reserved_by == reserved_by
        ))
    return "success"