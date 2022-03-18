from fastapi import APIRouter
from config.db import conn
from models.model import t_Student
from schemas.schema import Student
from typing import List

studentRouter = APIRouter()

@studentRouter.get("/users",response_model= List[Student])
def getUsers():
    return conn.execute(t_Student.select()).fetchall()

@studentRouter.post("/users")
def createStudent(stu: Student):
    print(stu)
    conn.execute(t_Student.insert().values(stu.dict()))
    return "success"