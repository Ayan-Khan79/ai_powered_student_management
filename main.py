import uvicorn
import os
from fastapi import FastAPI, HTTPException
from typing import List,Optional
from models import Student,Professor,Feedback
from database import students, professors
from nlp_utils import analyze_sentiment,smart_search

PORT = int(os.environ.get("PORT", 8000))
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT)

app = FastAPI(
    title="Student Management Api",
    description="A simple rest api using fast api",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message":"Welcome to student management Api"}
    
# Create a Student POST
@app.post("/students", response_model=Student)
def create_student(student:Student):
    students.append(student)
    return student

#Get all students list GET
@app.get("/students",response_model=List[Student])
def get_students():
    return students

# Create a Professor POST
@app.post("/professor", response_model=Professor)
def create_professor(prof:Professor):
    professors.append(prof)
    return prof

#Get all Professors list GET
@app.get("/professors",response_model=List[Professor])
def get_professors():
    return professors

#Get  Students by student id GET
@app.get("/students/{student_id}",response_model=Student)
def get_student(student_id:int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return students[student_id]


#Update a student detail PUT
@app.put("/students/{student_id}")
def update_student(student_id : int , student_det : Student):
     if student_id < 0 or student_id >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
     students[student_id] = student_det

     return {
        "message" : "Student updated successfully",
        "data" : student_det
    }

#Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id : int):
    if student_id < 0 or student_id  >= len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    del_student = students.pop(student_id)

    return {
        "message":"Student deleted successfully",
        "data": del_student
    }

@app.get("/search")
def search_student(name:str):
    result =[
        s for s in students
        if name.lower() in s.name.lower()
    ]
    if not result :
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    
    return {
        "count":len(result),
        "data":result
    }

# NLP Routes
@app.post("/analyze-feedback")
def analyze_feedback(feed:Feedback):
    result = analyze_sentiment(feed.text)
    return {
        "text": feed.text,
        "Result":result
    }

@app.get("/smart-search")
def search_students(query:str):
    results = smart_search(students,query)

    if not results:
        raise HTTPException(
            status_code=404,
            detail="No matching Student Found"
        )
    return {
        "Count" : len(results),
        'Students': results
    }
