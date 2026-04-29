from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def bonjour():
    return{"text":"Bonjour"}