import datetime
from pydantic import BaseModel

class dbSeat(BaseModel):
    course_id: str
    course_date: datetime.date
    seat_id: int
    reserved_by: str

class reserveName(BaseModel):
    seat_id: int
    reserved_by: str
    name:str