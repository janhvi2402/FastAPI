from fastapi import FastAPI
from pydantic import BaseModel,Field

class LoanApp(BaseModel): #no comma
    name:str
    age: int=Field(ge=0, le=100) #ge,le,gt,lt
    income: float=Field(ge=1000, le=10000000)
    loan_amount: float
    employeement_years: int

app=FastAPI()

@app.post("/predict")
def predict_loan(application: LoanApp):
    #model logic
    approved=(
        application.income>30000 and
        application.employeement_years>2 and
        application.age>21
    )
    return {
        "applicant name":  application.name,
        "loan_amount": application.loan_amount,
        "decision":"approved" if approved else "rejected",
        "reviewed income":application.income
    }

#always send and return data in json