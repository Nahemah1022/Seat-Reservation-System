from fastapi import APIRouter
from config.db import conn
from models.model import t_Student
from schemas import studentSchema
from typing import List

studentRouter = APIRouter()

@studentRouter.get("/users",response_model= List[studentSchema.dbStudent])
def getUsers():
    return conn.execute(t_Student.select()).fetchall()

@studentRouter.post("/users")
def createStudent(stu: studentSchema.dbStudent):
    print(stu)
    conn.execute(t_Student.insert().values(stu.dict()))
    return "success"