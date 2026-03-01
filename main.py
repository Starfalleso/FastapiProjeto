from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello "}

@app.get("/hello")
async def greet():
    return {"message": "Hello"}


@app.get("/hello/{name}")
async def say_hello(name: str,age:Optional[int] = None):
    return {"message": f"Hello {name} and you are {age} years old"}

class Student(BaseModel):
    name: str
    age: int
    roll: int
@app.post("/create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }