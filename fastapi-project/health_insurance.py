from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Optional

app=FastAPI()

class Insurance(BaseModel):
    name:str
    insurance_id: int
    age: int
    income: float=Field(ge=1000,le=1000000)
    city:str

all_customer=[
    {"id":101,"name":"Ravi","age":21,"income":25000,"city":"Bengaluru"},
    {"id":102,"name":"Radha","age":51,"income":250000,"city":"Delhi"},
    {"id":103,"name":"Hari","age":27,"income":50000,"city":"Mumbai"},
    {"id":104,"name":"Sunidhi","age":34,"income":254000,"city":"Bengaluru"},
    {"id":105,"name":"Anaya","age":18,"income":25000,"city":"Bhopal"}
]


#query
@app.get("/customer")
def get_customer(city:str,income:float):
    filter=[]
    for c in all_customer:
        if c["city"]==city and c["income"]==income:
            filter.append(c)
    return {
        "resuts":filter,
        "city":city
    }

# def get_customer(city: Optional[str] = None, income: Optional[float] = None):
#     if city is None and income is None:
#         return all_customer

#     filtered = []
#     for c in all_customer:
#         if (city is None or c["city"] == city) and \
#            (income is None or c["income"] == income):
#             filtered.append(c)

#     return filtered