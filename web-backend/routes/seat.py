from fastapi import APIRouter
from config.db import conn
from models.model import t_Seat
from schemas.schema import Seat

seatRouter = APIRouter()

@seatRouter.post("/book")
def bookSeat(studentId: str, seatId: int):
    print(studentId, seatId)
    return "success"

@seatRouter.post("/cancel")
def cancelBookedSeat(studentId: str, seatId: int):
    print(studentId, seatId)
    return "success"