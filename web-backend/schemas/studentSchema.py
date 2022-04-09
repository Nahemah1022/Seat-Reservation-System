import datetime
from email import message
from pydantic import BaseModel

class dbStudent(BaseModel):
    id: str
    name: str
    password: str

class StudnetInfo(BaseModel):
    id: str
    name: str

class StudnetLogin(BaseModel):
    id: str
    password: str

class Message(BaseModel):
    message:str
    data: StudnetInfo