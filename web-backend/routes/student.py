from email import message
from fastapi import APIRouter, HTTPException,Depends
from sqlalchemy.orm import Session
from typing import List

from config.db import getDBSession
from models.model import t_Student
from schemas import studentSchema


studentRouter = APIRouter()

@studentRouter.get("/users",response_model= List[studentSchema.dbStudent],tags=["Student"])
def getAllStudent(conn:Session = Depends(getDBSession)):
    return conn.execute(t_Student.select()).fetchall()

@studentRouter.post("/users/register", response_model= studentSchema.Message,tags=["Student"])
def createStudent(stu: studentSchema.dbStudent,conn:Session = Depends(getDBSession)):
    # search id in db first
    dbStudentData =  conn.execute(t_Student.select().where(t_Student.c.id == stu.id)).first()
    if dbStudentData is not None:
        raise HTTPException(status_code= 400, detail= "ID already registered")
    else:
        conn.execute(t_Student.insert().values(stu.dict()))
        message = studentSchema.Message(message= "success", data= stu)
        return message

@studentRouter.post("/users/login", response_model= studentSchema.Message,tags=["Student"])
def loginStudent(user: studentSchema.StudnetLogin,conn:Session = Depends(getDBSession)):
    studentData =  conn.execute(t_Student.select().where(t_Student.c.id == user.id)).first()
    if studentData is None:
        raise HTTPException(status_code= 400, detail= "Invalid ID/Password")
    elif studentData.password == user.password:
        message = studentSchema.Message(message= "success", data= studentData)
        return message
    else:
        raise HTTPException(status_code= 400, detail= "Invalid ID/Password")