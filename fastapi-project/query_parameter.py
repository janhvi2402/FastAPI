from fastapi import FastAPI

app=FastAPI()

all_customer=[
    {"id":101,"name":"Ravi","city":"Bengaluru","risk":"low"},
    {"id":102,"name":"Om","city":"mumbai","risk":"high"},
    {"id":103,"name":"Ranjan","city":"delhi","risk":"medium"},
    {"id":104,"name":"Ankita","city":"Bengaluru","risk":"low"},
    {"id":105,"name":"Himanshi","city":"Pune","risk":"medium"},
]

@app.get("/customer")
def get_customer(city:str, risk:str,limit:int=2):
    filter=[
        c for c in all_customer
        if c["city"]==city and c["risk"]==risk
    ]
    return {
        "city":city,
         "risk":risk,
         "count":len(filter),
         "resuts":filter #will print filtered       
    }