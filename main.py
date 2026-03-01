# Import necessary libraries
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# Initialize FastAPI application
app = FastAPI()


# GET endpoint - Root path
@app.get("/")
async def root():
    """Simple greeting endpoint"""
    return {"message": "Hello "}

# GET endpoint - Simple greeting
@app.get("/hello")
async def greet():
    """Returns a hello message"""
    return {"message": "Hello"}


# GET endpoint - Personalized greeting with optional age parameter
@app.get("/hello/{name}")
async def say_hello(name: str, age: Optional[int] = None):
    """
    Greet a person by name and optionally show their age
    
    Parameters:
    - name: Person's name (required)
    - age: Person's age (optional)
    """
    return {"message": f"Hello {name} and you are {age} years old"}

# Data model for a Student
class Student(BaseModel):
    """Student data model with name, age, and roll number"""
    name: str
    age: int
    roll: int

# POST endpoint - Create a new student
@app.post("/create_student")
def create_student(student: Student):
    """
    Create a new student record
    
    Parameters:
    - student: Student object with name, age, and roll number
    
    Returns: The created student data
    """
    return {
        "name": student.name,
        "age": student.age,
        "roll": student.roll
    }