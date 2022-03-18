import datetime
from pydantic import BaseModel

class dbSeat(BaseModel):
    course_id: int
    course_date: datetime.date
    seat_id: int
    reserved_by: str