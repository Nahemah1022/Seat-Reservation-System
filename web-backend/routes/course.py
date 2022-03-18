import datetime
from fastapi import APIRouter
from config.db import conn
from models.model import courses
from schemas.schema import Course

courseRouter = APIRouter()

@courseRouter.get("/getAllCourse")
def getAllCourse():
    # return data format
    return conn.execute(courses.select()).fetchall()

@courseRouter.post("/getCourse")
def getCourse(course_id: int, date: datetime.date):
    print(course_id, date)
    result = conn.execute(courses.select().where(courses.c.id == course_id and courses.c.date == date)).first()
    print(result)
    # TODO: JOIN seat information
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
    return conn.execute(courses.insert().values(course))
