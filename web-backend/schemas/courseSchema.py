import datetime
from email import message
from pydantic import BaseModel
from typing import List,Union
from schemas.seatSchema import reserveName

class dbCourse(BaseModel):
    id: str
    date: datetime.date
    name: str
    classroom: str
    seats: int
    cols: int

class courseSeat(BaseModel):
    numberPerRow:int
    totalSeat:int
    seats:List[reserveName]

class showAllCourse(BaseModel):
    id:str
    name:str
    classroom:str
    date:List[datetime.date]

class SeatStatusMessage(BaseModel):
    message: str
    data:Union[courseSeat,List[showAllCourse]]