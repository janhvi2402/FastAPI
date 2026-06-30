from fastapi import FastAPI

app=FastAPI()

customer_risk_profiles={
    101:{"name":"Ravi","risk":"low","score":0.12},
    102:{"name":"Preeti","risk":"medium","score":0.52},
    103:{"name":"Raj","risk":"high","score":0.93},
    104:{"name":"Aradhya","risk":"low","score":0.08},
}


#Path parameter
#our endpoint is customer, we are. not creating endpoit for each customer, we are jsut passing customer is
@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id: int):
    if customer_id not in customer_risk_profiles:
        return {"error":f"customer {customer_id} not found"}
    
    profile=customer_risk_profiles[customer_id]

    return {
        "customer_id":customer_id,
        "name":profile["name"],
        "risk_level":profile["risk"],
        "score":profile["score"]
    }

#we can also do same for different parameters
@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name: str, customer_id: int):
    return {
        "model": model_name,
        "customer_id":customer_id,
        "prediction":"high"
    }