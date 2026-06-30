from fastapi import FastAPI

app=FastAPI()

@app.get("/customer") #asking
def get_customer(customer_id: int):
    return {
        "customer_id":customer_id,
        "name":"Janhvi",
        "status":"active"
    }

#sending data to server, data-travels in request body not in url
#in get data travels in url

