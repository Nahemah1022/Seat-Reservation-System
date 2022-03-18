import datetime
from pydantic import BaseModel

class dbStudent(BaseModel):
    id: str
    name: str
    password: str