import datetime
from fastapi import APIRouter
from config.db import conn
from models.model import t_Course
from schemas.schema import Course

courseRouter = APIRouter()

@courseRouter.get("/getAllCourse")
def getAllCourse():
    return conn.execute(t_Course.select()).fetchall()

@courseRouter.post("/getCourse")
def getCourse(course_id: str, date: datetime.date):
    print(course_id, date)
    result = conn.execute(t_Course.select().where(t_Course.c.id == course_id and t_Course.c.date == date)).first()
    print(result)
    return result


@courseRouter.post("/addCourse")
def addCourse(c: Course):
    print(c)
    course = {
        "date":c.date,
        "name":c.name,
        "classroom":c.classroom,
        "seats":c.seats,
        "cols":c.cols,
    }
    return conn.execute(Course.values(course))
