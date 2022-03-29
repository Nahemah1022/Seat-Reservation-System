import datetime
from secrets import token_urlsafe
from fastapi import APIRouter, Depends, HTTPException
from pydantic import parse_obj_as
from typing import List
from sqlalchemy.sql import select
from sqlalchemy.orm import Session

from models.model import t_Course, t_Seat,t_Student
from config.db import getDBSession
from schemas import courseSchema,seatSchema

courseRouter = APIRouter()

@courseRouter.get("/course/getAllCourse", response_model= courseSchema.SeatStatusMessage, tags=["Course"])
def getAllCourse(conn:Session = Depends(getDBSession)):
    allCourseId = conn.execute(select(t_Course.c.id)).unique().all()
    print(allCourseId)
    returnCourseList = []
    for id in allCourseId:
        allCourseInfo = conn.execute(select(t_Course.c.id, t_Course.c.date, t_Course.c.name, t_Course.c.classroom).where(
            t_Course.c.id == id[0]
        ).order_by(t_Course.c.date)).all()

        firstCourseInfo = allCourseInfo[0]
        # print(firstCourseInfo)
        # print(firstCourseInfo, allCourseInfo)
        dateList = []
        for course in allCourseInfo:
            dateList.append(course[1])

        firstCourseInfo = {
            'id':firstCourseInfo[0],
            'name':firstCourseInfo[2],
            'classroom':firstCourseInfo[3],
            'date':dateList
        }
        firstCourseInfo = parse_obj_as(courseSchema.showAllCourse, firstCourseInfo)

        returnCourseList.append(firstCourseInfo)
    returnCourseList = parse_obj_as(List[courseSchema.showAllCourse], returnCourseList)
    message = courseSchema.SeatStatusMessage(message="sucess",data = returnCourseList)


    return message


@courseRouter.get("/course/getCourse",response_model= courseSchema.SeatStatusMessage,tags=["Course"])
def getCourse(course_id: str, date: datetime.date,conn:Session = Depends(getDBSession)):

    dbClassInfo = conn.execute(select(t_Course.c.cols,t_Course.c.seats).where(
        t_Course.c.id == course_id,
        t_Course.c.date == date
        )).first()

    if dbClassInfo is None:
        raise HTTPException(status_code= 400, detail= "Invalid Course")

    dbSeatInfo = conn.execute(select(t_Seat.c.seat_id,t_Seat.c.reserved_by,t_Student.c.name).where(
        t_Seat.c.course_id == course_id,
        t_Seat.c.course_date == date,
        t_Seat.c.reserved_by == t_Student.c.id
        ).order_by(t_Seat.c.seat_id)).all()

    reservedByDataClass = parse_obj_as(List[seatSchema.reserveName], dbSeatInfo)
    courseSeatDataClass = courseSchema.courseSeat(numberPerRow= dbClassInfo.cols, totalSeat=dbClassInfo.seats,seats=reservedByDataClass)
    message = courseSchema.SeatStatusMessage(message="sucess",data = courseSeatDataClass)
    return message


@courseRouter.post("/addCourse")
def addCourse(c: courseSchema.dbCourse,conn:Session = Depends(getDBSession)):
    conn.execute(t_Course.insert().values(c.dict()))
    return "success"