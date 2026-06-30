from fastapi import FastAPI

from pydantic import BaseModel

app=FastAPI()
class LoanApplication(BaseModel): #client will send data in these format
    age: int
    income: float
    loan_amount: float
    empoyeement_years:int

@app.post("/predict")
def predict_loan(application: LoanApplication):
    #pretend this model
    if application.income>50000 and application.empoyeement_years>2:
        decision="approved"
    else:
        decision="rejected"
    return { 
        "application_age": application.age,
        "decision":decision
    }


 #path parameters
@app.get("/customer/{cutomer_id}") #{}part of url not fixed
def get_customer(customer_id: int):
    return {
        "customer_id": customer_id
    }
