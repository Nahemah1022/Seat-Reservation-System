from fastapi import APIRouter
from config.db import conn
from models.model import students
from schemas.schema import Student

studentRouter = APIRouter()

@studentRouter.get("/users")
def getUsers():
    return conn.execute(students.select()).fetchall()

@studentRouter.post("/users")
def createStudent(stu: Student):
    print(stu)
    user = {
        "id":stu.id,
        "name":stu.name,
        "password":stu.password
    }
    conn.execute(students.insert().values(user))
    return "success"