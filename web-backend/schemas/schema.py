import datetime
from pydantic import BaseModel

class Student(BaseModel):
    id: str
    name: str
    password: str

class Course(BaseModel):
    id: int
    date: datetime.date
    name: str
    classroom: int
    seats: int
    cols: int

class Seat(BaseModel):
    course_id: int
    course_date: datetime.date
    seat_id: int
    reserved_by: str