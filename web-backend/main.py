from typing import Optional
from routes.student import studentRouter
from routes.course import courseRouter
from routes.seat import seatRouter
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(studentRouter)
app.include_router(courseRouter)
app.include_router(seatRouter)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read():
    return {"Hello": "World"}
