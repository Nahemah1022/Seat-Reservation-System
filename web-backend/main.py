from typing import Optional
from routes.student import studentRouter
from routes.course import courseRouter
from routes.seat import seatRouter
from fastapi import FastAPI

app = FastAPI()
app.include_router(studentRouter)
app.include_router(courseRouter)
app.include_router(seatRouter)

@app.get("/")
def read():
    return {"Hello": "World"}
