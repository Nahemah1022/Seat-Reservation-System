import datetime
from fastapi import APIRouter
from config.db import conn
from models.model import t_Course, t_Seat
from schemas import courseSchema 

courseRouter = APIRouter()

@courseRouter.get("/getAllCourse")
def getAllCourse():
    return conn.execute(t_Course.select()).fetchall()

@courseRouter.get("/getCourse")
def getCourse(course_id: str, date: datetime.date):
    print(course_id, date)

    classInfo = conn.execute(t_Course.select().where(
        t_Course.c.id == course_id,
        t_Course.c.date == date
        )).first()

    seatInfo = conn.execute(t_Seat.select().where(
        t_Seat.c.course_id == course_id,
        t_Seat.c.course_date == date
        )).all()

    print(classInfo, seatInfo)
    return {'classInfo' : classInfo, 'seatInfo' : seatInfo}


@courseRouter.post("/addCourse")
def addCourse(c: courseSchema.dbCourse):
    conn.execute(t_Course.insert().values(c.dict()))
    return "success"
