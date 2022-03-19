import datetime
from dataclasses import dataclass
from fastapi import APIRouter
from config.db import conn
from models.model import t_Seat
from schemas import seatSchema 

seatRouter = APIRouter()

@seatRouter.post("/book")
def bookSeat(s: seatSchema.dbSeat):
    # asume that the request is always valid.
    # we don't handle the situation that the user trys to book the reserved seat.
    # if the seat is reserved or unclickable, the user won't access this route.
    conn.execute(t_Seat.insert().values(s.dict()))
    return "success"

@seatRouter.post("/cancel")
def cancelBookedSeat(s: seatSchema.dbSeat):
    print(s)
    conn.execute(t_Seat.delete().where(
        t_Seat.c.reserved_by == s.reserved_by,
        t_Seat.c.seat_id == s.seat_id
        ))
    return "success"