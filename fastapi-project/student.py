from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app=FastAPI()

student={
    "S01":{"name":"Janhvi","marks":98,"gragde":"A+"},
    "S02":{"name":"Siya","marks":78,"gragde":"B"},
    "S02":{"name":"Anirudh","marks":87,"gragde":"A"}
}

class MarksSubmission(BaseModel):
    student_id:str
    marks:int
    subject:str
#error handling
@app.get("/student/{student_id}")
def get_student(student_id:str):
    if student_id not in student:
        raise HTTPException(
            status_code=404,
            detail=f"Student with ID {student_id} does not exist"
        )

    return student[student_id]

@app.post("/submit-marks")
def submit_marks(submission:MarksSubmission):
    if submission.student_id not in student:
        raise HTTPException(
            status_code=404,
            detail=f"STudent with ID {submission.student_id} does not exist"
        )
    if submission.marks <0 or submission.marks>100:
        raise HTTPException(
            status_code=400,
            detail="Marks must be between 0 and 100"
        )
    if submission.subject.strip()=="": #strip removes whitespaces
        raise HTTPException(
            status_code=400,
            detail="Subject cannot be empty"
        )
    
    student[submission.student_id]["marks"]= submission.marks
    return {
        "message":"Marks submitted successfully",
        "student":student[submission.student_id]["name"],
        "subject":submission.subject,
        "marks":submission.marks
    }