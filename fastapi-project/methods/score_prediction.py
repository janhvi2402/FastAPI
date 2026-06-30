from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()
class About(BaseModel):
    name: str
    study_hours: float
    prev_gpa: float
    sleep_hours: int

@app.get("/customer")
def get_student(student_id: int):
    return {
        "name" : "Siya",
        "age" : 21
    }

@app.post("/predict")
def details(student: About):
    if student.study_hours>5 and student.sleep_hours>7:
        decision="pass"
    else:
        decision="fail"

    return {
        "student_name": student.name,
        "decision":decision
    }
