import datetime
from pydantic import BaseModel

class dbCourse(BaseModel):
    id: str
    date: datetime.date
    name: str
    classroom: str
    seats: int
    cols: int
