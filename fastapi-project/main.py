from fastapi import FastAPI

app=FastAPI() #creating my application

@app.get("/") #decorator meaning-if get request to url "/", run the below function
def home():
    return {"message":"my first API is working"}

#app is your FastAPI application, which contains your API.

@app.get("/about")
def about():
    return {"project":"loan risk model","version":"1.0"}