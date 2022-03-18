from fastapi import APIRouter
from config.db import conn
from models.model import t_Student
from schemas.schema import Student

studentRouter = APIRouter()

@studentRouter.get("/users")
def getUsers():
    return conn.execute(t_Student.select()).fetchall()

@studentRouter.post("/users")
def createStudent(stu: Student):
    print(stu)
    user = {
        "id":stu.id,
        "name":stu.name,
        "password":stu.password
    }
    conn.execute(t_Student.insert().values(user))
    return "success"